# Planning Center Knowledge Base

A curated, AI-assistant-friendly knowledge base about Planning Center's products, platform, and ecosystem. Built for use with [Claude Code](https://claude.com/claude-code), Claude Projects, or any AI assistant that works with markdown files.

## What's Included

- **Company overview** -- founding, team, product suite, key selling points
- **12 product deep-dives** -- features, pricing, workflows, integration points
- **Developer platform** -- API, OAuth, webhooks, add-on framework
- **Competitive landscape** -- how PC compares to Tithe.ly, Pushpay, Breeze, ChurchTrac
- **Security & compliance** -- SOC 2, PCI, GDPR, encryption, incident response
- **Legal & privacy** -- ToS, privacy policies, data rights, controller vs processor
- **Onboarding & transitions** -- migration paths, import capabilities, friction points
- **Blog & changelog** -- recent posts and development velocity (auto-updated)
- **Glossary** -- PC terminology, internal terms, church tech jargon

## Quick Start

### Option A: Clone as a standalone project

```bash
git clone git@github.com:evanlemmons/planning-center-knowledge.git
cd planning-center-knowledge
# Open with Claude Code -- CLAUDE.md tells the AI how to use the files
```

### Option B: Add as a git submodule (recommended for existing projects)

```bash
cd your-ai-assistant
git submodule add git@github.com:evanlemmons/planning-center-knowledge.git knowledge/planning-center
```

Then reference files in your project's `CLAUDE.md`:
```markdown
- knowledge/planning-center/overview.md - Company overview
- knowledge/planning-center/products/services.md - Services product details
```

To pull updates:
```bash
git submodule update --remote knowledge/planning-center
```

### Option C: Copy files directly

Download the files and drop them into an existing project or Claude Project. Simple but won't receive automatic updates.

## How Updates Work

### Automated (blog & changelog)
- A GitHub Action monitors Planning Center's RSS feeds twice weekly (Monday & Thursday)
- When new blog posts or changelog entries are detected, an AI-powered script fetches the content, updates the relevant markdown files, and opens a PR
- PRs are reviewed before merging to ensure quality

### Manual (product docs, competitive analysis, etc.)
- Submit a PR with your changes
- Product files should follow the existing format (see any `products/*.md` for examples)

## Contributing

1. **Content corrections** -- Found an inaccuracy? Submit a PR.
2. **New product knowledge** -- Major feature shipped? Update the relevant `products/*.md` file.
3. **Glossary additions** -- New term encountered? Add it to `glossary.md`.
4. **Raw page refreshes** -- Product marketing page changed? Use `scripts/web-capture.py` to re-capture, then clean per `raw/README.md` standards (strip images, CTAs, testimonials, nav, etc.).

### What belongs here
- Planning Center company and product information
- Public-facing documentation, pricing, competitive positioning
- Blog and changelog summaries
- Developer platform reference

### What does NOT belong here
- Personal project context or individual workflows
- Notion content or internal documents behind authentication
- Team-specific assignments or people/role information

## File Structure

```
.
├── CLAUDE.md              # AI assistant usage instructions
├── README.md              # This file
├── glossary.md            # Terminology reference
├── overview.md            # Company overview
├── pricing.md             # Pricing model
├── competitors.md         # Competitive landscape
├── security-and-compliance.md
├── legal-and-privacy.md
├── onboarding-and-transitions.md
├── developer-platform.md
├── blog-recent.md         # Auto-updated
├── changelog-recent.md    # Auto-updated
├── products/              # 12 product deep-dives
├── raw/                   # Raw web captures (reference)
├── scripts/               # Maintenance tools
└── .github/workflows/     # Automation
```
