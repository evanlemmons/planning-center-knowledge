# People

Last Updated: 2026-02-11
Source: planningcenter.com/people + pcopeople.zendesk.com docs

## What It Is
People is Planning Center's free membership database -- the foundational "hub" that centralizes information about church members and their activity across all ministries. "Keep people from falling through the cracks." Trusted by over 90,000 churches.

## Pricing
Completely free for every church, regardless of size. Unlimited people, unlimited access. Texting add-on: $5/month (credits purchased by org admin).

## Core Capabilities

### Database Management
- Central people database for all PC products -- profile data flows across Services, Giving, Groups, Check-Ins, etc.
- Add people manually, via CSV import, or through Church Center self-service
- Household management: group into households, track adults/children, assign primary contact
- Duplicate detection and merge (system surfaces potential duplicates)
- Campus assignment per person (requires campuses configured in Accounts)
- Inactivate profiles (removes login, preserves history) or delete (org admin only)
- Spam list management to block unwanted profiles

### Profiles
- Built-in fields: name (first, given/legal, nickname -- all searchable), contact info, social profiles, membership status
- Custom tabs and custom fields for anything not covered by defaults (manager-only to create)
- Profile notes with categories and permissions (prayer requests, pastoral care, health conditions)
- Background checks via Checkr integration with expiration tracking
- Activity tracking across all PC products visible on profile
- Communication history (email and text, retained up to 3 months)

### Lists (Real-Time Reporting)
- Filter/query people across all PC product data (attendance, giving, group membership, etc.)
- Auto-refresh schedules keep lists current; URL reflects filter state (bookmarkable)
- Organize by name, campus, category, or starred
- Actions: send email/text/Church Center announcement, print, export CSV, bulk update
- Automations triggered by list membership changes (added/removed)
- Lists can be shared with collaborators

### Workflows
- Multi-step process tracking with cards representing people moving through steps
- Assign people to steps; "ready" status triggers email notifications
- Per-workflow permissions for who can view/manage
- Cards visible in toolbar across all PC products
- Common uses: visitor follow-up, baptism process, membership classes, volunteer onboarding

### Forms
- Drag-and-drop builder; public shareable URL
- Submissions can trigger automations
- Data flows into profile fields and custom fields

### Automations
- Triggers: person added/removed from a list, form submission
- Actions: send email template, add to workflow, update profile fields, add to group, create a task in Home
- Lists must be set to auto-refresh for automations to work
- History viewable for 32 days; statuses: Success, Pending, Paused, Failed
- Warning: saving/editing list rules pauses all automations on that list

### Communication
- **Email**: Send to individuals or lists; custom from addresses; Mailchimp integration; templates
- **Texting**: Consent-based; send to lists; credits system; toll-free numbers; $5/mo add-on
- **Church Center announcements**: Push to Church Center users
- Notification management for staff/volunteer preferences

## Key Workflows
1. **New person intake**: Added (manual/CSV/Church Center) -> assign household -> assign campus -> add to workflows/lists
2. **Visitor follow-up**: Check-in creates profile -> automation adds to list -> triggers workflow/email/task
3. **Data maintenance**: Duplicate detection -> merge -> CSV import for bulk updates -> lists to find incomplete profiles
4. **Communication campaigns**: Build filtered list -> send email/text/announcement -> view history on profiles
5. **Volunteer vetting**: Form submission -> automation adds to workflow -> background check -> cleared for service

## Admin vs Church Center
- **Admin (People app)**: Full database management, lists, workflows, forms, communication, background checks, custom fields, notes. Staff-only tool.
- **Church Center**: Profile self-update, directory browsing (must be enabled by org admin; people individually invited), form submission, household info management.

## Integration Points
- **All PC products**: People is the central profile store; contact info edited here flows everywhere
- **Check-Ins**: Attendance data on profiles, filterable in lists
- **Giving**: Donation history on profiles; given name used for check matching
- **Groups**: Group membership on profiles and in list filters
- **Services**: Scheduling history on profiles; team membership in lists
- **Registrations**: Event registration data on profiles
- **Calendar**: Event data available for list filtering
- **Home (Tasks)**: Automations can create tasks from list/form triggers
- **Checkr**: Background check initiation and tracking
- **Mailchimp**: Email list sync for marketing campaigns

## Permissions Model
- **Levels**: Manager > Editor > Viewer, plus collaborator-level access on specific resources (lists, workflows, forms, notes, custom fields)
- **Org admin exclusivity**: Only org admins can delete profiles, manage background check settings, purchase texting credits, enable directory, manage unassigned lists
- **Cross-product access**: Permissions in other products (Services, Groups, etc.) grant varying levels of access to People contact data

## Notable Details
- People is for staff; congregants use Church Center directory
- Dedicated mobile app (iOS/Android) for staff with profile lookup, dashboards, lists, forms, workflows
- Adding permissions sends welcome email; upgrading sends notification; downgrading does NOT notify (except org admin removal, which notifies all org admins)
- Lists dependent on other lists: auto-refresh automations should not be used when List B depends on List A -- List A must be manually refreshed first
- Customizable dashboards show giving or attendance trends at a glance
- Two-step verification recommended for data privacy
