# Planning Center Onboarding & Transitions

Last Updated: 2026-02-11
Source: planningcenter.com/getting-started + support articles

## 1. The Getting Started Journey

PC frames the transition as a "choose-your-own-adventure road trip." The marketing page funnels prospects into three paths (brand new, existing user, ChMS transition) and leans on four pillars:

- **30-day free trial** with full features on every product (extendable on request; free plan also available indefinitely)
- **Self-serve data migration** via CSV import, third-party migration partners, or the public API
- **Planning Center University (PCU)** -- free video courses re-recorded 2-3x/year, taught by product specialists
- **Support team** with ~1 hour response time, many of whom have personally migrated churches

The pitch emphasizes low cost of entry (People is always free, a-la-carte pricing, no setup fees) and ease of use. Customer testimonials highlight speed of onramp and intuitiveness. There is no in-person training; everything is online by design so content stays current.

Competitive positioning exists against Pushpay, Tithe.ly, Breeze, and ChurchTrac with dedicated comparison pages and a giving fee savings calculator.

## 2. Three User Paths

### Path A: Brand New to Planning Center (and to ChMS)
- Sign up with everything at the free plan; start with People
- Add data via: (1) online form shared with congregants (preferred), (2) manual entry, (3) CSV import, or (4) third-party migration tool
- **Only profile/people data can be imported.** Giving history and attendance history require manual entry or third-party tools
- Then roll out additional products in recommended order (links to a separate "Rolling Out Products" guide)

### Path B: Existing User Expanding
- Typically a Services-only or Check-Ins-only church adding more products
- Key step: locate and gain admin access to the existing account ("There is no way to merge Planning Center accounts" -- strong warning)
- Account discovery is non-trivial: involves checking billing charges, resetting passwords, contacting finance teams, or reaching out to support
- After gaining access: review current subscriptions, then follow the same product rollout guide

### Path C: Full ChMS Transition (from another system)
- Most complex path; dedicated guide plus system-specific articles for Elexio, FellowshipOne, The City, and Church Community Builder
- Same core flow: sign up for People (free), import people data via CSV, then add products
- Detailed CSV cleanup and import tips provided (see Section 3)

**Key difference between paths:** Path A emphasizes forms for data collection (congregation fills in their own info). Paths B and C assume data already exists somewhere and focus on import mechanics. Path B adds the unique challenge of account discovery/access.

## 3. The Full ChMS Transition Process

### What CAN Be Imported
- **People/profile data only:** names, contact info, addresses, household IDs, birthdates, custom fields, membership status
- Import method: CSV file uploaded through the People data importer (no setup fee)

### What CANNOT Be Imported (Major Gaps)
- **Giving/donation history** -- must use a third-party integration or enter donations manually into batches
- **Attendance/check-in history** -- must add previous sessions and enter attendance manually
- **Groups** -- no import path mentioned; presumably manual recreation
- **Calendar events** -- no import path mentioned
- **Service plans, song libraries** -- no import path mentioned
- **Volunteer schedules** -- no import path mentioned
- **Notes, communications, workflows** -- no import path mentioned

### Recommended Rollout Sequence
1. Sign up for People (free)
2. Clean up and import your CSV
3. Subscribe to additional products in the recommended order (detailed in a separate "Rolling Out Products" article not included in these files)

### System-Specific Import Paths
Dedicated transition articles exist for:

| System | Key Notes |
|--------|-----------|
| **FellowshipOne** | Data export takes 2-3 weeks; use X9400 or P9400 v3.2 report; export attributes individually; detailed field mapping instructions provided |
| **Church Community Builder (CCB)** | Use "Export Individuals" CSV; may be limited to 10 fields at a time; terminology shift: CCB Groups = PC Lists |
| **The City** | Export user data from main group to CSV |
| **Elexio** | Use custom lists for full database export; can choose columns to exclude |
| **Any other system** | Generic CSV path; no system-specific guidance |

### Timeline
- No official timeline is stated anywhere in the docs
- FellowshipOne data export alone takes 2-3 weeks
- 30-day trial is the implied window, though extensions are offered
- Community tips suggest breaking large imports into multiple smaller CSVs

### Support Available
- Support team (~1 hr response), PCU videos, in-product help (? icon), community forums (Slack + Facebook), third-party migration partners listed on integrations page

## 4. Current Friction Points & Improvement Opportunities

### Critical Gaps

1. **Only people data imports -- everything else is manual.** This is the single biggest friction point. A church transitioning from a mature ChMS loses their giving history, attendance records, groups, calendar, and service plans unless they do extensive manual work or hire a third party. This creates a real barrier for larger churches with years of data.

2. **No giving history import tool.** The docs say to use a "third-party integration" or enter donations "manually into batches." For a church with years of giving records needed for tax statements, this is a dealbreaker-level gap. The only first-party path is batch manual entry.

3. **No attendance history import tool.** Same problem. Churches that track attendance trends over time lose all historical data unless they manually backfill session by session.

4. **Account merging is impossible.** The docs explicitly warn "there is no way to merge Planning Center accounts." Churches that accidentally created a second account, or that have separate accounts for different campuses, are stuck. This is a known pain point severe enough to warrant a bold warning box.

5. **Account discovery is surprisingly difficult.** Existing users may not know if their church has a PC account. The discovery process involves checking billing charges, trying password resets on every email, asking the finance team, or contacting support. There is no self-serve "find my church's account" tool.

### Process Friction

6. **CSV cleanup is entirely on the customer.** Churches must reformat dates, deduplicate, split large files, and map fields manually before import. Tips come from community members, not from tooling. The recommendation to "sort in Excel" and "break CSVs into smaller pieces" signals a lack of robust import tooling.

7. **System-specific guidance varies wildly.** FellowshipOne has a detailed multi-step export guide. The City gets one sentence. Churches coming from systems without a dedicated article (Breeze, Realm, Shelby, ACS, Rock, etc.) get only the generic CSV path.

8. **No guided migration workflow.** The process is: read an article, export from old system, clean CSV in Excel, import into People, then manually set up every other product. There is no in-product wizard, progress tracker, or step-by-step migration flow.

9. **Product rollout guidance lives in a separate article.** The transition guide ends at "you've imported people, now go read another article." The full journey is fragmented across multiple support articles, not a unified experience.

10. **"Rolling Out Products" order is not documented in any of these files.** It is referenced repeatedly but never included, making it hard for a transitioning church to plan the full scope of work upfront.

### Content & Messaging Issues

11. **Article helpfulness scores are low.** The transition guide is rated 3/6 helpful (50%), the brand-new guide 9/14 (64%), and the existing user guide 4/8 (50%). These are the most critical onboarding articles and half of readers don't find them helpful.

12. **The transition guide was created in 2016.** While updated in Oct 2025, the core structure and system-specific tips (FellowshipOne, The City) reference products that have been sunset or acquired. Missing are guides for current competitors like Breeze, Tithe.ly, Realm, Rock RMS, and Subsplash.

13. **No timeline expectations are set.** A church leader considering the switch has no idea if this is a 1-week, 1-month, or 3-month project. The docs avoid the question entirely.

## 5. Quick Reference: What Can Be Imported from Each System

| Data Type | FellowshipOne | CCB | The City | Elexio | Generic CSV |
|-----------|:---:|:---:|:---:|:---:|:---:|
| People/profiles | Yes (via P9400 report) | Yes (Export Individuals) | Yes (main group export) | Yes (custom list export) | Yes |
| Addresses | Yes | Yes | Likely | Yes | Yes |
| Household relationships | Yes (Household ID) | Unclear | Unclear | Unclear | Yes (if column exists) |
| Custom fields/attributes | Yes (exported individually) | Limited (10 fields at a time) | Not mentioned | Yes (column selection) | Yes |
| Giving history | No | No | No | No | No |
| Attendance history | No | No | No | No | No |
| Groups | No | No | No | No | No |
| Service plans/songs | No | No | No | No | No |
| Calendar events | No | No | No | No | No |
| Volunteer schedules | No | No | No | No | No |

**Bottom line:** Across all systems, only people/contact data moves over. Everything else starts from scratch or requires manual reconstruction.
