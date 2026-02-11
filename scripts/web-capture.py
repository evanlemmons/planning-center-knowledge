#!/usr/bin/env python3
"""
Capture web pages as markdown for the PM Assistant knowledge base.

Usage:
  python scripts/web-capture.py "https://example.com/article"
  python scripts/web-capture.py "https://example.com/article" --output knowledge/research/
  python scripts/web-capture.py "https://example.com/docs" --depth 2
  python scripts/web-capture.py "https://example.com/article" --light  (trafilatura only, no browser)

Dependencies: crawl4ai, trafilatura
Install:  pip install -r scripts/requirements.txt

Note: For sites requiring login or interactive navigation (clicking tabs, filling forms),
consider adding Playwright MCP (microsoft/playwright-mcp) as an MCP server instead.
Playwright drives a live browser and can handle interactive pages that Crawl4AI cannot.
"""

import argparse
import asyncio
import os
import re
import sys
from datetime import datetime
from urllib.parse import urlparse, urljoin


def sanitize_filename(title: str) -> str:
    """Convert a title to a safe, descriptive filename."""
    name = re.sub(r'[^\w\s-]', '', title.strip()).strip()
    name = re.sub(r'[\s_]+', '-', name).lower()
    return name[:80] if name else 'untitled'


def add_metadata_header(content: str, url: str, title: str) -> str:
    """Add source metadata to the top of captured markdown."""
    date = datetime.now().strftime('%Y-%m-%d')
    header = f"<!-- Source: {url} | Captured: {date} -->\n"
    header += f"# {title}\n\n"
    return header + content


async def capture_with_crawl4ai(url: str, depth: int = 0) -> list[dict]:
    """Capture pages using Crawl4AI (handles JavaScript-rendered content)."""
    try:
        from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
    except ImportError:
        print("Error: crawl4ai not installed. Run: pip install crawl4ai", file=sys.stderr)
        sys.exit(1)

    results = []
    visited = set()

    browser_config = BrowserConfig(headless=True)
    crawl_config = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        await _crawl_recursive(crawler, crawl_config, url, depth, visited, results)

    return results


async def _crawl_recursive(crawler, config, url: str, depth: int,
                           visited: set, results: list):
    """Recursively crawl pages up to the specified depth."""
    if url in visited:
        return
    visited.add(url)

    print(f"  Crawling: {url}")
    try:
        result = await crawler.arun(url=url, config=config)
    except Exception as e:
        print(f"  Error crawling {url}: {e}", file=sys.stderr)
        return

    if not result.success:
        print(f"  Failed: {url} - {getattr(result, 'error_message', 'unknown error')}", file=sys.stderr)
        return

    title = getattr(result, 'title', '') or urlparse(url).path.split('/')[-1] or 'Untitled'
    markdown = result.markdown or ''

    results.append({
        'url': url,
        'title': title,
        'markdown': markdown,
    })

    # Follow internal links if depth > 0
    if depth > 0 and hasattr(result, 'links') and result.links:
        base_domain = urlparse(url).netloc
        internal_links = []
        for link_info in result.links.get('internal', []):
            link = link_info if isinstance(link_info, str) else link_info.get('href', '')
            full_url = urljoin(url, link)
            if urlparse(full_url).netloc == base_domain and full_url not in visited:
                internal_links.append(full_url)

        for link in internal_links[:20]:  # Cap at 20 links per page
            await _crawl_recursive(crawler, config, link, depth - 1, visited, results)


def capture_with_trafilatura(url: str) -> list[dict]:
    """Capture a single page using trafilatura (lightweight, no browser needed)."""
    try:
        import trafilatura
    except ImportError:
        print("Error: trafilatura not installed. Run: pip install trafilatura", file=sys.stderr)
        sys.exit(1)

    print(f"  Fetching: {url}")
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        print(f"  Failed to fetch: {url}", file=sys.stderr)
        return []

    # Extract as markdown
    content = trafilatura.extract(
        downloaded,
        output_format='markdown',
        include_links=True,
        include_tables=True,
    )

    if not content:
        print(f"  No content extracted from: {url}", file=sys.stderr)
        return []

    # Try to get title from metadata
    metadata = trafilatura.extract_metadata(downloaded)
    title = metadata.title if metadata and metadata.title else urlparse(url).path.split('/')[-1] or 'Untitled'

    return [{
        'url': url,
        'title': title,
        'markdown': content,
    }]


def save_results(results: list[dict], output_dir: str):
    """Save captured pages as markdown files."""
    os.makedirs(output_dir, exist_ok=True)

    for page in results:
        filename = sanitize_filename(page['title']) + '.md'
        filepath = os.path.join(output_dir, filename)

        # Avoid overwriting - append number if file exists
        counter = 1
        while os.path.exists(filepath):
            filename = f"{sanitize_filename(page['title'])}-{counter}.md"
            filepath = os.path.join(output_dir, filename)
            counter += 1

        content = add_metadata_header(page['markdown'], page['url'], page['title'])

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Saved: {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description='Capture web pages as markdown for the Planning Center knowledge base.'
    )
    parser.add_argument('url', help='URL to capture')
    parser.add_argument(
        '--output', '-o',
        default='raw/',
        help='Output directory (default: raw/)'
    )
    parser.add_argument(
        '--depth', '-d',
        type=int, default=0,
        help='Recursion depth for following links (default: 0, single page only)'
    )
    parser.add_argument(
        '--light',
        action='store_true',
        help='Use trafilatura only (no browser, faster but no JS rendering)'
    )

    args = parser.parse_args()

    # Resolve output path relative to project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, args.output) if not os.path.isabs(args.output) else args.output

    print(f"Capturing: {args.url}")
    print(f"Output:    {output_dir}")
    print(f"Depth:     {args.depth}")
    print(f"Engine:    {'trafilatura (light)' if args.light else 'crawl4ai'}")
    print()

    if args.light:
        results = capture_with_trafilatura(args.url)
    else:
        results = asyncio.run(capture_with_crawl4ai(args.url, depth=args.depth))

    if not results:
        print("\nNo pages captured.", file=sys.stderr)
        sys.exit(1)

    save_results(results, output_dir)
    print(f"\nDone. Captured {len(results)} page(s).")


if __name__ == '__main__':
    main()
