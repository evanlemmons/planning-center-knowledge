# Accounts

Last Updated: 2026-02-11
Source: pcoaccounts.zendesk.com docs

## What It Is
Accounts is the foundational administration layer for all of Planning Center -- managing the church's account settings, subscriptions, billing, campuses, security, integrations, and Church Center configuration. Not a product churches "use" day-to-day, but the backbone that controls everything.

## Pricing
Accounts itself is free. It's where churches manage subscriptions and billing for individual PC products.

## Core Capabilities

### Account Setup & Management
- Configure church name, logo, time zone, date format, language preferences (account-wide, affects all products)
- Church Center URL customization (subdomain of churchcenter.com)
- Text messaging setup at the account level (for use in People and other products)
- Account cancellation (org admin only)

### Organization Roles
- **Organization Administrator**: Highest permission -- automatic highest permissions in all subscribed products except Giving. Can manage account settings, campus config, Church Center, security. Recommended: at least two per account.
- **Billing Manager**: Manages subscription and payment info; receives invoices/receipts. The original account creator gets both roles automatically; subsequent people must be explicitly assigned.
- Org admin and billing manager are separate roles -- a person can have one, both, or neither

### Campus Management
- Add multiple campuses with name, address, contact info
- Each campus toggleable for Church Center app search visibility
- Campuses flow into all products: Services (folders/tags), Giving (labels/funds), People (profile assignment, list/workflow filtering), Check-Ins (event folders), Calendar (rooms/resources, tags), Groups (locations, assignments), Registrations (signup filtering), Publishing (app search)
- Campus info only shows across products when more than one campus exists
- Can transition a campus to a separate "church plant" (new independent account)

### Multi-Campus vs Multi-Account Decision
- **Single account**: Staff/volunteers serve across sites; want shared data; lower cost
- **Separate accounts**: Separate tax IDs, bank accounts, or copyright licenses per campus
- Accounts cannot be merged after creation -- permanent decision
- Staff with profiles in multiple accounts can link them for easy switching

### Church Center Setup
- Free with every PC account; web version enabled by default
- Mobile app requires explicit activation in Publishing + free Essential-level Publishing subscription + at least one campus
- Features for congregants: profile management, donations, event registration, group participation, calendar, directory, forms
- Navigation pages can be reordered, hidden, or added in Publishing

### Security
- Login management: help people log in, reset passwords, change login methods (org admin only)
- Two-step verification: can be required for specific or all users
- Security history audit trail
- All org admins notified when any org admin's access is removed

### Subscription & Billing
- Subscribe/unsubscribe to individual products; upgrade/downgrade tiers
- Seasonal plan changes to save money during slow periods
- Credit card, billing address, receipts, payment history management
- Sales tax handling varies by jurisdiction

### Integrations
- **Stripe**: Payment processing for Giving and Registrations (org admin only can disconnect -- requires support request)
- **Checkr**: Background checks (enabled in Accounts, used in People)
- **Mailchimp**: Email marketing (enabled in Accounts, used with People lists)
- **Add-ons vs External connections**: Add-ons are managed within PC; external connections are third-party integrations
- Full integration directory at planningcenter.com/integrations

## Key Workflows
1. **New account setup**: Create account -> add church info/logo -> set localization -> add campuses -> set up Church Center -> configure integrations -> subscribe to products -> add org admins and billing managers
2. **User onboarding**: Org admin grants permissions -> user receives welcome email -> sets up two-step verification
3. **Multi-campus expansion**: Add campus -> configure in each product -> assign people in People -> set up campus content in Publishing
4. **Subscription management**: Review usage -> upgrade/downgrade per product -> adjust seasonally -> manage billing
5. **Church Center launch**: Customize URL -> enable mobile app in Publishing -> configure navigation -> add campuses to search -> share with congregation

## Integration Points
- **All PC products**: Subscriptions, permissions, campuses, and localization settings affect every product
- **People**: Org admins get highest People permissions; login management done in Accounts
- **Giving**: Stripe integration enables online donations; Giving admin is separate (org admins do NOT auto-get Giving access)
- **Publishing**: Church Center mobile app activation, navigation, campus search visibility
- **Calendar/Registrations**: Stripe enables online payments; Church Center hosts public-facing content

## Notable Details
- **Giving is special**: Org admins do NOT automatically get Giving access -- deliberate security measure for financial data
- **Account creator privileges**: Auto-assigned both org admin and billing manager; subsequent people need explicit assignment to each
- **Accounts cannot be merged**: Plan the multi-campus vs multi-account decision carefully
- **Church Center web vs app**: Web is auto-enabled; mobile requires Publishing activation + a campus
- **Stripe disconnect requires support**: Cannot self-service disconnect -- must contact PC support
- **Status page**: Bookmark status.planningcenter.com for outage awareness
- **Support**: Monday-Friday and Sunday mornings; accessible via toolbar ? icon; phone scheduling available
- **Planning Center University (PCU)**: Free training at planningcenter.com/university
- **Localization**: Account-wide time zone and date format affect all products and users
- **Data portability**: Support can undo CSV/iCal imports, but only org admins can request corrections
