# Check-Ins

Last Updated: 2026-02-11
Source: planningcenter.com/check-ins + pcocheck-ins.zendesk.com docs

## What It Is
Planning Center's attendance and child safety tool. Churches use it to check people in and out of events quickly and safely, with a strong focus on children's ministry security. Tagline: "Keep children safe, give parents peace."

## Pricing
Tiered by unique check-ins on the busiest day of the week. Occasional spikes (Christmas, Easter) allowed. All plans include all features, unlimited stations, people, and events.

| Daily Check-Ins | Price |
|-----------------|-------|
| 10 | Free |
| 30 | $15/mo |
| 75 | $32/mo |
| 200 | $69/mo |
| 500 | $115/mo |
| 1,000 | $179/mo |
| Unlimited | $239/mo |

## Core Capabilities

### Event Management
- Events contain sessions (specific dates), locations (rooms/areas), and times
- Event times define actual start time, check-in begin time, and check-out end time
- Events can be one-time or recurring; multiple service times within a single event (recommended over separate events for cleaner reporting)
- Archive, delete, or copy locations between events
- Events can be campus-specific (recommended: unique events per campus)

### Locations & Labels
- Locations support age/grade filters, capacity limits, and room assignments
- Labels (name tags, security tags) printed via thermal printers at check-in
- Two default labels; custom labels configurable with fields: name, security code, phone number, medical notes, consecutive number, custom fields
- Supported printers: Brother, Citizen (iOS/Android), Dymo, Zebra (Mac/Windows); can print from volunteers' phones
- Security labels cannot be reprinted (by design, for safety)

### Station Types (3 types, unlimited stations)
- **Manned Station**: Volunteer-operated. Search by name, add visitors, edit profiles, override filters, check out, send emergency texts. Works anytime
- **Self Station**: For returning families. Search by phone, barcode, or mobile pass. Only during configured show/hide times
- **Roster Station**: Digital class list for teachers. Auto-populates based on past attendance. Locked to a specific location
- Quick presets, station pairing, station keys, and announcement slides available
- Available on iOS, Android, and desktop apps
- Station users do NOT need Check-Ins login permissions -- only an editor needs to create the station

### People & Security
- Household structure links adults and children; trusted people (authorized pickup) and not-authorized people (flagged at checkout)
- Security codes: 4-character alphanumeric, change each check-in. One security label per household by default; options for 2-code or 2-label printing
- Medical notes and allergy fields displayed on labels and stations
- Grade tracking with annual promotion tool; profile photos for identification
- Background check integration via Checkr (or manual tracking); locations can require cleared checks for volunteer check-in
- Emergency text messaging from manned/roster stations to parents/trusted adults

### Attendance & Reporting
- Check-in types: Regular vs. Volunteer
- Headcounts: manual totals via separate free Headcounts app (no individual check-ins)
- Attendance can be added to past sessions retroactively
- Reports: attendee lists, person activity over time, event charts, attendance trends
- Lists: first-time visitors, households without contact info, etc.

## Key Workflows
1. **Setup**: Create event -> Add locations with age/grade filters -> Configure labels -> Create stations -> Connect printers -> Train volunteers
2. **Check-in**: Person arrives -> Searches at station (phone, name, barcode, Church Center QR) -> Selects household members -> Labels print -> Child goes to location
3. **Checkout**: Parent shows security code -> Volunteer verifies on station -> Checks authorized pickup list -> Child released
4. **Reporting**: View attendee lists -> Track activity over time -> Generate trend reports

## Admin vs Church Center
- **Admin (web)**: Full event configuration, station management, label design, reporting, people management, permissions
- **Church Center**: Pre-check-in from app before arriving, generate QR code to scan at station, mobile passes saved to Apple/Google Wallet
- Church Center requires: Publishing page active, Check-Ins page published, navigation item added
- "Allow Complete Check-In" setting lets congregants finish check-in without scanning at a station

## Integration Points
- **Services**: Scheduled volunteers auto-marked as "Volunteer" check-in type when times/location names match; attendance synced both ways
- **Groups**: Check in group members at events
- **Registrations**: Take attendance for signups; sync signup times and assignment types as locations
- **Church Center**: Pre-check-in, QR code scanning, mobile passes
- **People**: Background checks, household management, custom fields on labels
- **Publishing**: Controls Church Center page visibility and navigation

## Permissions Model
- **Editor**: Full access to all Check-Ins features
- **Viewer**: Read-only access
- **Headcounter**: Headcount entry + view only

## Notable Details
- Primary marketing angle is child security, not general attendance
- No special equipment required beyond any device; label printers optional but recommended
- Self and roster stations only work during event show/hide times; manned stations and web browser can check in anytime
- Roster stations auto-populate based on past attendance within a configurable timeframe
- Setup recommendation: test printers at least a week in advance; minimum 5 Mbps internet
- VBS (Vacation Bible School) and portable/mobile church setups are documented use cases
- Keyboard shortcuts available for faster operations
- Barcode scanning supported on manned and self stations
