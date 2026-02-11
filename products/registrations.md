# Registrations

Last Updated: 2026-02-11
Source: planningcenter.com/registrations + pcoregistrations.zendesk.com docs

## What It Is
Registrations simplifies event signups, attendee management, and payment collection for church events of all sizes -- from simple potluck headcounts to complex camp registrations with cabin assignments and t-shirt add-ons. "Create custom signups for all your church events."

## Pricing
Tiered by attendees registered for the largest event. Plans can be changed seasonally (scale up for VBS/camps, scale back during quiet periods). 30-day free trial.

| Attendees/Event | Price |
|-----------------|-------|
| 5 | Free |
| 20 | $15/mo |
| 50 | $32/mo |
| 150 | $69/mo |
| 400 | $115/mo |
| 1,000 | $179/mo |
| 5,000 | $239/mo |

Online payments via Stripe: 2.15% + $0.30/transaction (US credit/debit); 0% + $0.30 per ACH bank transfer. Discounted rates for Canadian registered charities. AUD/NZD rates also available.

## Core Capabilities

### Signup Creation
- **Signups** are the core unit -- each represents an event/opportunity
- Two purpose types: "event on a specific date" (with start/end) or "ongoing program/opportunity" (no date)
- Three registration modes: **Named Attendees** (detailed individual info), **Simple Count** (headcount only), **None** (announcement-only)
- Duplicate signups to reuse structure; archive or delete when done
- Organize signups into **categories** for Church Center display

### Selection Types (Attendee Categories)
- Define different attendee categories with distinct pricing, restrictions, and info collection
- Examples: roles (Leader, Volunteer), demographics (Child, Adult), time slots (Morning/Afternoon)
- **Availability restrictions**: Filter by grade, gender, or age (pulls from People profiles)
- Per-selection confirmation messages; can be shown/hidden on Church Center independently
- A "Standard" selection type auto-created with every new signup
- Selection types with active registrations cannot be deleted

### Information Collection
- **Personal info fields** per selection type (optional/required); auto-updates People profiles
- **Attendee questions** and **registration questions** (per-registration, not per-attendee)
- **Attendee forms**: Detailed forms (medical forms, waivers) attachable to signups
- **Add-ons**: Additional purchasable items (t-shirts, meals, activities) with pricing and quantity limits; "Sold Out" display; Named Attendees only
- Emergency Contact field stored only within signup (does not update People profile)
- Profile info already on file cannot be changed by registrant during registration

### Capacity & Waitlist
- Set capacity per selection type or entire signup; displayed on Church Center
- **Waitlist**: Enabled when capacity is set; people join and admitted when space opens
- Incomplete registrations hold a spot for 15 min (48 hours if no capacity set)

### Attendee Management
- Register manually (admin/editor) or via Church Center (self-service)
- Register pairs (two people linked together) or allow registering others on someone's behalf
- **Assignments**: Organize attendees into sub-groups (cabins, teams, buses, dinner tables)
- Attendance tracking via Check-In Station or Check-In Event integration
- Cancel/restore registrations and individual attendees; edit info after registration
- **Subscriber notifications**: Add people to receive alerts on new registrations
- Split registrations (different dates/times) -- Simple Count signups only

### Payments
- **Stripe integration**: Credit/debit, bank account (ACH), Apple Pay, Google Pay
- **Non-deductible payments only** -- tax-deductible donations must go through Giving
- Multi-currency: USD, CAD, AUD, NZD built-in; EUR, GBP, JPY, ZAR via support request
- Cash/check option (admin applies manually); if enabled with required deposit, attendees can bypass deposit
- **Partial payments**: Allow registration without full payment; set minimum deposit (including $0)
- **Discounts**: Date-based (early bird), group/quantity, code-based (promo codes)
- **Scholarships**: Create funds, accept donations to them, apply as payments
- Refunds (full/partial), fund transfers between signups, late fees, receipt sending
- Stripe payout reports (separate from Giving); CSV export of transactions

### Communication
- Email registrants: balance-due reminders, event details, incomplete info reminders
- Custom confirmation emails per signup and per selection type

## Key Workflows
1. **Create signup**: Choose type -> choose mode -> configure selections -> add questions/forms/add-ons -> set pricing -> set Church Center visibility -> test by self-registering -> open publicly
2. **Manage registrations**: Monitor -> use assignments to organize -> filter/report -> manage payments -> send communications -> take attendance
3. **Payment workflow**: Connect Stripe -> set prices -> configure deposits -> collect payments -> send balance reminders -> refund if needed -> reconcile via Stripe reports
4. **Seasonal reuse**: Duplicate previous signup -> update dates/settings -> open registration

## Admin vs Church Center
- **Admin**: Full signup CRUD, register people manually, apply cash/check payments, issue refunds, transfer funds, assignment management, attendance tracking, reporting, CSV exports, Stripe reports, automation config
- **Church Center**: Browse signups by category, view details/pricing/capacity, self-register, make payments (card/bank/Apple Pay/Google Pay/cash-check), pay remaining balance, view confirmation
- **Roles**: Administrator, Manager, Editor, Contributor, Viewer

## Integration Points
- **Stripe**: Payment processing (shared infrastructure with Giving but tracked separately)
- **People**: Attendee profiles auto-updated; grade/gender/age restrictions pull from People profiles
- **Calendar**: Feeds auto-sync signup events; connections link individual signups; can create signups from Calendar
- **Check-Ins**: Set up Check-In Station or Event for attendance at signup events
- **Church Center**: All public signups live here; categories organize display
- **Giving**: Separate product; Registrations payments are non-deductible and NOT visible in Giving

## Notable Details
- New signups default to "Do not include (direct link only)" on Church Center -- useful for testing before public launch
- Grade collection is context-sensitive (label adjusts for summer vs school year)
- Completed test registrations should be manually deleted after testing
- Stripe payouts shared across Registrations and Giving but reported separately
- Stripe cannot pay out in ZAR (collect in ZAR, payout in different currency)
- CSV exports of large datasets may take several minutes
- Registration status defaults to Open on creation
