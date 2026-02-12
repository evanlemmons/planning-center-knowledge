# Raw Marketing Page Captures

Cleaned snapshots of Planning Center product marketing pages from planningcenter.com. These serve as reference material for the curated `products/` files.

Despite the directory name, these are **not raw dumps** — they've been processed to remove web boilerplate and retain only useful product knowledge.

## Content Standards

When capturing or refreshing pages, clean the output to match these rules.

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

### Expected Result

Cleaned files are typically **70-80% shorter** than raw web captures while preserving all substantive product information.

## Refreshing a Page

1. **Capture:**
   ```bash
   python scripts/web-capture.py "https://www.planningcenter.com/[product]" --output raw/
   ```

2. **Clean** the captured file using the KEEP/STRIP rules above. The capture script outputs whatever the crawler returns — you must manually remove boilerplate.

3. **Verify** the source comment is present and the capture date is current.

4. **Compare** with the corresponding `products/[product].md` — if the marketing page reveals new features or changes, update the curated product file too.

5. **Open a PR** with the cleaned raw file (and any product file updates).

## Reference

See PR #1 for the initial cleanup that established these standards — all 14 files were cleaned from 3,821 to 981 lines.
