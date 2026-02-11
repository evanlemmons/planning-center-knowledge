# Groups

Last Updated: 2026-02-11
Source: planningcenter.com/groups + pcogroups.zendesk.com docs

## What It Is
Groups is Planning Center's community management tool for organizing small groups, Sunday School classes, recovery groups, and other communities. Leaders manage attendance, messaging, events, and resources while members connect through Church Center. "Organize groups, communicate with members."

## Pricing
Tiered by active group members per month. All plans include full features and unlimited groups/events. 30-day free trial.

| Members | Price |
|---------|-------|
| 15 | Free |
| 75 | $15/mo |
| 200 | $32/mo |
| 500 | $69/mo |
| 1,000 | $115/mo |
| 1,500 | $179/mo |
| Unlimited | $239/mo |

## Core Capabilities

### Group Structure & Organization
- Unlimited groups, each assigned to a **group type** (Small Groups, Women's Ministry, Mission Teams, etc.)
- Group types define defaults: contact person, description, location, enrollment rules, event defaults, security, leader contact
- Individual group settings can override group type defaults
- Built-in "Unique Groups" type for miscellaneous (cannot be edited/deleted)
- **Children groups** for sub-group nesting
- **Tags** for filtering and organizing (admin-managed, visible in Church Center)
- Duplicate groups (copies structure, settings, optionally members/resources)
- Bulk update groups (edit, archive, create events across multiple groups)
- CSV export of filtered group data

### Membership Management
- Roles: Leader (manages day-to-day operations) and Member
- Enrollment strategies: open signup (anyone can join) or request-based (leader approval)
- Enrollment can be open/closed, with optional close dates and member limits (leaders count toward limits)
- Admins/leaders can add members even when group is closed or full
- **Confidential member lists** for sensitive groups (grief share, recovery) -- anonymous to everyone but leader and admins
- Alert admins when membership exceeds a threshold

### Events & Attendance
- Create events with recurring schedules within groups
- RSVP tracking; attendance tracking with reminders sent 10 min before event
- Attendance via Church Center starting 60 min before event
- Events can be added to the main church Calendar
- **Seasons**: Launch new seasons of groups (seasonal cycles)
- Cancel, delete, or bulk-create events across groups

### Communication
- Email group members (bulk or individual); reminder emails up to 10 days before events
- **Chat** via Church Center for leaders and/or members (enable/disable per group type)
- Communication history tracking; admin notifications for group activity

### Automations
- Trigger-based automated actions at individual group level (e.g., auto-actions on member join/leave)

### Reporting
- All Group Stats (printable PDF); group-level Overview and Attendance tabs
- Filter/sort by type, campus, status, schedule, Church Center visibility, enrollment, tag
- Demographics, attendance frequency, drop-off rates, meeting frequency
- Event notes aggregated view; RSVP tracking reports

### Resources
- Share files and links with leaders and/or members (study materials, curriculum, videos, forms)
- Shared resources available across groups

## Key Workflows
1. **Set up group ministry**: Create group types with defaults -> create groups -> assign leaders -> configure enrollment/visibility -> launch on Church Center
2. **Season launch**: Archive/duplicate previous season -> update settings -> open enrollment -> promote on Church Center
3. **Ongoing management**: Monitor attendance/reports -> follow up via email/automations -> manage member requests -> track group health
4. **Group leader workflow**: Manage members -> create events -> take attendance -> share resources -> communicate via email/chat

## Admin vs Church Center
- **Admin**: Full group CRUD, type/tag management, reporting, People database access, bulk operations, CSV import/export, automation config, membership request approval, admin notes
- **Church Center**: Browse groups by type/tag filters, map view of locations, join (open) or request membership, RSVP to events, take attendance (60 min before event), chat with members, view resources

## Integration Points
- **People**: Member profiles synced; leaders can optionally access entire church database
- **Calendar**: Feeds auto-sync all group events into Calendar; individual Calendar events can also link to Groups (manual connections, no sync)
- **Church Center**: Public group directory, self-service, chat, attendance, RSVP

## Permissions Model
- **Administrator**: Full access to all groups, settings, reporting, People page
- **Group Type Manager**: Scoped to their assigned types; cannot access tags or People page
- **Group Leader**: Scoped to their groups; cannot access Reports, People page, or Settings

## Notable Details
- Children under 13 cannot log into Church Center or access Group messaging (ToS) -- use parent groups or Check-Ins for kids
- Deleting a group type moves its groups to "Unique Groups" -- if a Calendar feed exists, associated events are permanently removed from Calendar
- Open signup enrollment can create security concerns (documented warning)
- If all groups in a type are unlisted, the entire group type is hidden from Church Center
- Group type display order on Church Center is drag-and-drop configurable
- School year/grade management affects group membership (relevant for children's groups)
- Shared locations appear on a map and can be reused across groups
