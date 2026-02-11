#!/usr/bin/env python3
"""
AI-powered content updater for the Planning Center knowledge base.

Called by the content-update GitHub Action when new blog/changelog entries
are detected. Fetches full content, calls Claude API to generate updates,
and writes changes for the workflow to commit as a PR.

Usage:
  python scripts/update-content.py --entries '<JSON>'

The JSON should be an array of objects:
  [{"feed": "blog"|"changelog", "title": "...", "link": "...", "date": "..."}]
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic not installed. Run: pip install anthropic", file=sys.stderr)
    sys.exit(1)

try:
    import trafilatura
except ImportError:
    print("Error: trafilatura not installed. Run: pip install trafilatura", file=sys.stderr)
    sys.exit(1)


REPO_ROOT = Path(__file__).parent.parent

SYSTEM_PROMPT = """You are a knowledge base maintainer for Planning Center, a church management software company.

Your job is to update markdown knowledge files when new blog posts or changelog entries are published.

Rules:
1. Match the existing style, tone, and formatting of each file exactly.
2. For blog-recent.md: Add entries under the correct month heading. Create new month headings if needed. Each entry follows the pattern: `- **Title** (Mon DD) — One-sentence summary.`
3. For changelog-recent.md: Add entries under the correct product section heading. Each entry follows the pattern: `- **Feature name** (Mon YYYY) — Brief description` or just `- Feature description (Mon YYYY)`.
4. For product files (products/*.md): Only update if the new content describes a significant new feature or capability change. Add to the relevant section. Do NOT rewrite the whole file.
5. Keep entries concise — one to two sentences max per entry.
6. Do not add personal opinions, speculation, or editorial commentary.
7. Do not remove existing content unless it is factually superseded by the new information.
8. Update the "Last Updated" date at the top of any file you modify.
9. Return ONLY valid JSON — no markdown code fences, no commentary outside the JSON.
"""


def fetch_content(url: str) -> str:
    """Fetch and extract the main text content from a URL."""
    print(f"  Fetching: {url}")
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        print(f"  Warning: Could not fetch {url}", file=sys.stderr)
        return ""

    content = trafilatura.extract(
        downloaded,
        output_format="text",
        include_links=False,
        include_tables=True,
    )
    return content or ""


def read_file(path: Path) -> str:
    """Read a file relative to the repo root."""
    full_path = REPO_ROOT / path
    if full_path.exists():
        return full_path.read_text(encoding="utf-8")
    return ""


def write_file(path: Path, content: str):
    """Write a file relative to the repo root."""
    full_path = REPO_ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8")
    print(f"  Updated: {path}")


def identify_relevant_product(title: str, content: str) -> str | None:
    """Guess which product file might be relevant based on title/content keywords."""
    product_keywords = {
        "people": "products/people.md",
        "services": "products/services.md",
        "check-ins": "products/check-ins.md",
        "check-in": "products/check-ins.md",
        "giving": "products/giving.md",
        "groups": "products/groups.md",
        "calendar": "products/calendar.md",
        "registrations": "products/registrations.md",
        "publishing": "products/publishing.md",
        "church center": "products/church-center.md",
        "music stand": "products/music-stand.md",
        "home": "products/home.md",
        "accounts": "products/accounts.md",
    }

    text = (title + " " + content[:500]).lower()
    for keyword, path in product_keywords.items():
        if keyword in text:
            return path
    return None


def call_claude(entries: list[dict], fetched_content: dict[str, str]) -> dict:
    """Call Claude API to generate file updates."""
    client = anthropic.Anthropic()
    today = datetime.now().strftime("%Y-%m-%d")

    # Build the user prompt with current file states and new content
    blog_current = read_file(Path("blog-recent.md"))
    changelog_current = read_file(Path("changelog-recent.md"))

    # Identify potentially relevant product files
    product_files = {}
    for entry in entries:
        content = fetched_content.get(entry["link"], "")
        product_path = identify_relevant_product(entry["title"], content)
        if product_path and product_path not in product_files:
            product_files[product_path] = read_file(Path(product_path))

    user_prompt = f"""Today's date: {today}

## New entries to process

"""
    for entry in entries:
        content = fetched_content.get(entry["link"], "(could not fetch content)")
        user_prompt += f"""### [{entry['feed'].upper()}] {entry['title']}
- Date: {entry['date']}
- URL: {entry['link']}
- Content:
{content[:3000]}

"""

    user_prompt += f"""## Current file states

### blog-recent.md
```
{blog_current}
```

### changelog-recent.md
```
{changelog_current}
```

"""
    for path, content in product_files.items():
        user_prompt += f"""### {path}
```
{content}
```

"""

    user_prompt += """## Instructions

Based on the new entries above, generate updated versions of any files that need changes.

Return a JSON object where keys are file paths and values are the complete new file content.
Only include files that actually need changes. For example:

{"blog-recent.md": "# Planning Center Blog...\\n...", "products/groups.md": "# Groups\\n..."}

If a product file needs updating, include the COMPLETE file content (not just the diff).
If no product file needs updating, only include blog-recent.md and/or changelog-recent.md.

IMPORTANT: Return ONLY the JSON object. No markdown fences, no explanation."""

    print("  Calling Claude API...")
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )

    response_text = message.content[0].text.strip()

    # Parse the JSON response
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        # Try to extract JSON from potential markdown fences
        if "```" in response_text:
            json_start = response_text.find("{")
            json_end = response_text.rfind("}") + 1
            if json_start >= 0 and json_end > json_start:
                return json.loads(response_text[json_start:json_end])
        print(f"  Error: Could not parse Claude response as JSON", file=sys.stderr)
        print(f"  Response: {response_text[:500]}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="AI-powered content updater for the Planning Center knowledge base."
    )
    parser.add_argument(
        "--entries",
        required=True,
        help="JSON array of new entries to process",
    )
    args = parser.parse_args()

    # Parse entries
    try:
        entries = json.loads(args.entries)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in --entries: {e}", file=sys.stderr)
        sys.exit(1)

    if not entries:
        print("No entries to process.")
        return

    print(f"Processing {len(entries)} new entries...")

    # Fetch full content for each entry
    fetched_content = {}
    for entry in entries:
        if entry.get("link"):
            fetched_content[entry["link"]] = fetch_content(entry["link"])

    # Call Claude to generate updates
    updates = call_claude(entries, fetched_content)

    if not updates:
        print("No updates generated.")
        return

    # Write updates
    print(f"\nWriting {len(updates)} file(s)...")
    for path, content in updates.items():
        write_file(Path(path), content)

    # Output summary for the PR body
    summary_parts = []
    for entry in entries:
        summary_parts.append(f"- **{entry['title']}** ({entry['feed']}) — {entry['date']}")

    summary = "\n".join(summary_parts)
    files_changed = ", ".join(f"`{p}`" for p in updates.keys())

    pr_body = f"""## New Content Detected

{summary}

## Files Updated

{files_changed}

---
*Auto-generated by the content update workflow. Please review before merging.*
"""

    # Write PR body for the workflow to use
    pr_body_path = Path("/tmp/pr_body.md")
    pr_body_path.write_text(pr_body, encoding="utf-8")
    print(f"\nPR body written to {pr_body_path}")
    print("Done.")


if __name__ == "__main__":
    main()
