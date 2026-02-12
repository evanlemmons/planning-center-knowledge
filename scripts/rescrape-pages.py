#!/usr/bin/env python3
"""
Re-scrape Planning Center marketing pages and detect changes.

Called by the page-rescrape GitHub Action on a semi-annual schedule.
Fetches all URLs from page-urls.json, cleans raw/ pages with Claude API,
compares against existing content, and outputs changed files + PR body.

Usage:
  python scripts/rescrape-pages.py
  python scripts/rescrape-pages.py --dry-run  # Fetch and compare without writing
"""

import argparse
import json
import os
import re
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
TODAY = datetime.now().strftime("%Y-%m-%d")

CLEANING_RULES = """You clean web page captures for a knowledge base about Planning Center (church management software).

Apply these rules to the raw page content:

### Keep
- Source comment: `<!-- Source: URL | Captured: YYYY-MM-DD -->`
- Product features and capabilities
- Pricing tiers, details, and processing fees
- FAQs
- Integration notes (how products connect)
- Admin vs. member/church distinctions
- Workflow descriptions
- Technical details (supported formats, limits, requirements)

### Strip
- `![...]()` image tags (screenshots, logos, icons, backgrounds)
- CTA buttons and links ("Start for free", "Watch our video", "Sign up", "Select plan", "Get started")
- "Trusted by X churches" sections and customer logo grids
- "Jump to:" in-page navigation links
- Site navigation headers and footers (product menus, company links)
- Duplicate sections (e.g., carousel slides + expanded versions of the same content)
- Customer testimonials and social proof quotes
- Demo, support, and blog promotional CTAs
- App store download badges and links
- "More Products" or cross-sell sections
- Decorative or redundant headings that don't add information

Return ONLY the cleaned markdown. Start with the source comment line.
Match the style and structure of the existing version provided for reference.
Do not add commentary or explanations outside the markdown content."""

REFERENCE_SYSTEM = """You compare web page content against an existing knowledge base file about Planning Center (church management software).

Identify factual changes: new features, changed pricing, removed content, updated statistics, new products, changed policies. Ignore cosmetic wording differences, layout changes, or reordering of existing content.

Return ONLY valid JSON with no markdown fences:
{"has_changes": true/false, "changes": ["description of change 1", "description of change 2"]}

If nothing meaningful changed, return: {"has_changes": false, "changes": []}"""


def load_manifest() -> dict:
    """Load the URL manifest from page-urls.json."""
    manifest_path = REPO_ROOT / "scripts" / "page-urls.json"
    with open(manifest_path, encoding="utf-8") as f:
        return json.load(f)


def read_file(path: str) -> str:
    """Read a file relative to the repo root."""
    full_path = REPO_ROOT / path
    if full_path.exists():
        return full_path.read_text(encoding="utf-8")
    return ""


def write_file(path: str, content: str):
    """Write a file relative to the repo root."""
    full_path = REPO_ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8")
    print(f"  Updated: {path}")


def fetch_page(url: str) -> str:
    """Fetch and extract markdown content from a URL via trafilatura."""
    print(f"  Fetching: {url}")
    try:
        downloaded = trafilatura.fetch_url(url)
    except Exception as e:
        print(f"  Error fetching {url}: {e}", file=sys.stderr)
        return ""

    if not downloaded:
        print(f"  Failed to fetch: {url}", file=sys.stderr)
        return ""

    content = trafilatura.extract(
        downloaded,
        output_format="markdown",
        include_links=True,
        include_tables=True,
    )
    return content or ""


def normalize_for_comparison(text: str) -> str:
    """Normalize text for comparison by stripping capture dates and whitespace."""
    # Remove capture date line (it changes every run)
    text = re.sub(r"Captured: \d{4}-\d{2}-\d{2}", "Captured: DATE", text)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_raw_page(client: anthropic.Anthropic, url: str, raw_content: str,
                   existing_content: str) -> str:
    """Use Claude to clean a raw page capture per the KEEP/STRIP rules."""
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        system=CLEANING_RULES,
        messages=[{
            "role": "user",
            "content": f"""URL: {url}

Existing cleaned version (match this style):
---
{existing_content}
---

New raw capture to clean:
---
{raw_content}
---

Clean this capture. Use the capture date {TODAY}."""
        }],
    )
    return message.content[0].text.strip()


def check_reference_page(client: anthropic.Anthropic, url: str, label: str,
                         fetched_content: str, existing_content: str) -> dict:
    """Use Claude to check if a reference page has meaningful changes."""
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=REFERENCE_SYSTEM,
        messages=[{
            "role": "user",
            "content": f"""Page: {label} ({url})

Freshly fetched web page content:
---
{fetched_content[:4000]}
---

Existing knowledge base file:
---
{existing_content[:4000]}
---

List any factual changes between the web page and the existing file."""
        }],
    )

    response_text = message.content[0].text.strip()
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        # Try to extract JSON from potential markdown fences
        if "{" in response_text:
            json_start = response_text.find("{")
            json_end = response_text.rfind("}") + 1
            if json_start >= 0 and json_end > json_start:
                try:
                    return json.loads(response_text[json_start:json_end])
                except json.JSONDecodeError:
                    pass
        print(f"  Warning: Could not parse response for {label}", file=sys.stderr)
        return {"has_changes": False, "changes": [], "error": "Parse error"}


def generate_pr_body(raw_results: list, ref_results: list, errors: list) -> str:
    """Generate the PR body markdown."""
    total_raw = len(raw_results)
    total_ref = len(ref_results)
    total_urls = total_raw + total_ref + len(errors)

    body = f"""## Semi-Annual Marketing Page Re-scrape

**Date:** {TODAY}
**Pages checked:** {total_raw} raw + {total_ref} reference URLs ({total_urls} total)

### Raw Page Changes

| File | Status | Summary |
|------|--------|---------|
"""
    for r in raw_results:
        status = "Changed" if r["changed"] else "No change"
        summary = r.get("summary", "—")
        body += f"| `{r['file']}` | {status} | {summary} |\n"

    changed_refs = [r for r in ref_results if r.get("has_changes")]
    unchanged_refs = [r for r in ref_results if not r.get("has_changes")]

    if changed_refs:
        body += "\n### Reference Page Flags\n\n"
        body += "These curated files may need manual updates based on detected web page changes:\n\n"
        for r in changed_refs:
            body += f"**{r['file']}** ({r['label']}: {r['url']})\n"
            for change in r.get("changes", []):
                body += f"- {change}\n"
            body += "\n"

    if unchanged_refs:
        body += "\n### Reference Pages — No Changes\n\n"
        for r in unchanged_refs:
            body += f"- `{r['file']}` ({r['label']})\n"

    if errors:
        body += "\n### Errors\n\n"
        for e in errors:
            body += f"- `{e['url']}` — {e['error']}\n"

    body += """
---
*Auto-generated by the page re-scrape workflow. Review all changes before merging.*
*Raw file changes are ready to merge. Reference page flags require manual curation.*
"""
    return body


def main():
    parser = argparse.ArgumentParser(
        description="Re-scrape Planning Center marketing pages and detect changes."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and compare without writing files",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    client = anthropic.Anthropic()

    raw_results = []
    ref_results = []
    errors = []

    # --- Process raw pages ---
    print(f"\n=== Processing {len(manifest['raw'])} raw pages ===\n")

    for entry in manifest["raw"]:
        url = entry["url"]
        file_path = entry["file"]
        print(f"\n--- {file_path} ---")

        fetched = fetch_page(url)
        if not fetched:
            errors.append({"url": url, "file": file_path, "error": "Failed to fetch"})
            raw_results.append({"file": file_path, "changed": False, "summary": "Fetch failed"})
            continue

        existing = read_file(file_path)

        print("  Cleaning with Claude...")
        try:
            cleaned = clean_raw_page(client, url, fetched, existing)
        except Exception as e:
            print(f"  Error calling Claude: {e}", file=sys.stderr)
            errors.append({"url": url, "file": file_path, "error": f"Claude API error: {e}"})
            raw_results.append({"file": file_path, "changed": False, "summary": "Cleaning failed"})
            continue

        # Compare (ignoring capture date)
        if normalize_for_comparison(cleaned) == normalize_for_comparison(existing):
            print("  No meaningful changes.")
            raw_results.append({"file": file_path, "changed": False, "summary": "—"})
        else:
            print("  Changes detected!")
            raw_results.append({"file": file_path, "changed": True, "summary": "Content updated"})
            if not args.dry_run:
                write_file(file_path, cleaned + "\n")

    # --- Process reference pages ---
    print(f"\n=== Processing {len(manifest['reference'])} reference pages ===\n")

    # Group reference entries by file to avoid duplicate reads
    ref_by_file = {}
    for entry in manifest["reference"]:
        file_path = entry["file"]
        if file_path not in ref_by_file:
            ref_by_file[file_path] = {"existing": read_file(file_path), "entries": []}
        ref_by_file[file_path]["entries"].append(entry)

    for file_path, file_data in ref_by_file.items():
        existing = file_data["existing"]

        for entry in file_data["entries"]:
            url = entry["url"]
            label = entry["label"]
            print(f"\n--- {label} ({url}) ---")

            fetched = fetch_page(url)
            if not fetched:
                errors.append({"url": url, "file": file_path, "error": "Failed to fetch"})
                continue

            print("  Comparing with Claude...")
            try:
                result = check_reference_page(client, url, label, fetched, existing)
            except Exception as e:
                print(f"  Error calling Claude: {e}", file=sys.stderr)
                errors.append({"url": url, "file": file_path, "error": f"Claude API error: {e}"})
                continue

            ref_results.append({
                "file": file_path,
                "url": url,
                "label": label,
                "has_changes": result.get("has_changes", False),
                "changes": result.get("changes", []),
            })

            if result.get("has_changes"):
                print(f"  Changes found: {len(result.get('changes', []))} items")
            else:
                print("  No meaningful changes.")

    # --- Generate PR body ---
    pr_body = generate_pr_body(raw_results, ref_results, errors)

    if args.dry_run:
        print("\n=== DRY RUN — PR body preview ===\n")
        print(pr_body)
    else:
        pr_body_path = Path("/tmp/pr_body.md")
        pr_body_path.write_text(pr_body, encoding="utf-8")
        print(f"\nPR body written to {pr_body_path}")

    # --- Summary ---
    raw_changed = sum(1 for r in raw_results if r["changed"])
    ref_flagged = sum(1 for r in ref_results if r.get("has_changes"))
    print(f"\nDone. {raw_changed}/{len(raw_results)} raw pages changed, "
          f"{ref_flagged} reference flags, {len(errors)} errors.")


if __name__ == "__main__":
    main()
