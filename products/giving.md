# Giving

Last Updated: 2026-02-11
Source: planningcenter.com/giving + pcogiving.zendesk.com docs

## What It Is
Planning Center's donation processing and management product for churches. Handles online and in-person donations, fund management, pledge campaigns, recurring giving, donor reporting, and year-end statements. Designed exclusively for non-profit 501(c)(3) organizations. Tagline: "Make it easy for people to give."

## Pricing
Flat monthly rate by total donations per month (online + batched). No additional fees beyond Stripe processing. Available in USA, Canada, Australia, and New Zealand.

| Donations/Month | Price |
|-----------------|-------|
| 10 | Free + processing fees |
| 75 | $15/mo + processing fees |
| 200 | $32/mo + processing fees |
| 500 | $69/mo + processing fees |
| 1,000 | $115/mo + processing fees |
| 1,500 | $179/mo + processing fees |
| Unlimited | $239/mo + processing fees |

Special offer: free for 12 months while under contract with another donation platform.

### Stripe Processing Fees (Discounted Rate)
- **USA**: 2.15% + $0.30 (card); 0% + $0.30 (ACH)
- **Canada**: 2.2% + $0.30 for registered charities (domestic Visa/MC)
- **Australia**: 1.4% + $0.30 AUD (domestic card); 0% + $0.50 AUD (BECS Direct Debit)
- **New Zealand**: 2.5% + $0.30 NZD (domestic card)

## Core Capabilities

### Donation Tracking
- Tracks monetary donations (tax-deductible) and donor-advised fund/QCD donations (non-deductible)
- Tracks in-kind donations (physical items, stock, services) -- no dollar value assigned per IRS guidelines, acknowledgments only
- NOT a general ledger -- does not handle sales, reimbursements, payroll, or AP/AR. CSV exports for accounting software import

### Funds
- Organize donations by intent (General, Building, Missions, etc.)
- Fund types: Default (always open, auto-selected), Listed (visible on donation form), Direct Link only, Unpublished (admin-only in batches)
- Funds can be opened/closed seasonally; closing hides from form but recurring donations continue
- Funds support ledger codes for accounting integration
- Funds with donations cannot be deleted, only closed. Default fund cannot be closed without contacting support
- Each fund gets a direct link with optional pre-filled amount

### Batches (In-Person Donations)
- Batch groups organize physical donations (e.g., "Sunday 09/08/2024" with Cash and Check sub-batches)
- Batch defaults set fund, payment source, method, labels, and received date
- Check reader (MICR) support for fast check entry
- In-progress batches: uncommitted, visible to admins only, NOT on statements
- Committed batches: donations become official, receipts sent, changes permanently logged
- Counters can create/enter; only admins/bookkeepers can commit

### Recurring Donations
- Set up by donors via Church Center or by admins on donor's behalf
- Configurable frequencies; split across multiple funds supported
- Statuses: Active, On hold indefinitely, On hold until [date]
- Failed donations notify donor (and optionally admins); system does NOT auto-retry, tries on next scheduled date
- If donor profile marked "Deceased," recurring donations auto-pause
- Stripe auto-updates expired credit/debit cards

### Text2Give (US Only)
- SMS-based one-time donations via dedicated toll-free number
- Donor texts "GIVE $amount" with optional fund name/shortcut
- Fund shortcuts simplify long names; can split between funds in single text
- Max single text: $9,999; cannot create recurring via text
- Requires toll-free number registration (3-5 business day approval)
- Requires Church Center Web enabled in Publishing + Giving page published

### Payment Processing
- All online donations through Stripe (PCI Level 1 compliant); no financial data on PC servers
- Payment methods: credit/debit cards, ACH bank transfers, Apple Pay, cash, checks
- "Cover the fee" option lets donors add processing fee to donation
- Admins can manually process online donations

### Automations
- Triggers: when someone gives, donates for first time, or sets up recurring
- Cross-product actions (email, workflow in People, etc.); can include joint donors

## Key Workflows
1. **Sunday batch processing**: Count cash/checks -> Create batch groups -> Enter donations -> Verify totals -> Commit batch
2. **Online giving setup**: Configure Stripe -> Set up funds -> Customize donation form -> Publish Giving page in Publishing
3. **Recurring management**: Monitor failures -> Pause/resume -> Admin edit on donor's behalf
4. **Year-end statements**: Generate annual statements -> Email or print for all donors -> Handle individual requests
5. **Fund management**: Create seasonal funds -> Open/close as needed -> Manage visibility

## Admin vs Church Center
| Area | Admin (Giving app) | Congregant (Church Center) |
|------|-------------------|---------------------------|
| Donations | Enter batches, edit/reassign, refund, bulk edit | Give online, set up recurring, split across funds |
| Funds | Create, configure visibility, set defaults | See listed funds on donation form |
| Payment methods | Add on donor's behalf, view all | Manage own methods, Text2Give |
| Recurring | Create/edit/pause/delete for any donor | Create/edit/pause/delete own |
| Statements | Generate, email, print for all | View own history and statements |
| Reports | Dashboard, donor/donation reports, Stripe payouts | N/A |

## Integration Points
- **People**: Donor profiles sync; new donors in batch entry auto-create People records
- **Church Center**: Online donation form, donor self-service (history, recurring, payment methods)
- **Publishing**: Must be enabled for Church Center Web; Giving page must be published for Text2Give and online giving
- **Stripe**: All payment processing; payout reports for bank reconciliation
- **Automations**: Cross-product triggers (e.g., add to People workflow on first donation)

## Permissions Model
- **Organization Admin**: Full access to everything
- **Giving Admin**: Full access to Giving
- **Bookkeeper**: Commit batches, run reports
- **Reviewer**: View-only access
- **Counter**: Batch entry only; cannot commit or view reports

## Notable Details
- Stripe is the only payment processor; no PayPal option
- Renaming a fund is logged to prevent mismanagement -- close old fund and open new instead
- Bill-pay checks share MICR numbers across bank customers, causing potential donor mismatches with check readers
- Committed batch deletions are permanently logged with who/when
- Text2Give has carrier limitations -- smaller carriers may not support SMS over 140 characters
- Not a QuickBooks replacement, but CSV exports bridge to accounting software
