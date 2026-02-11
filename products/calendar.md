# Calendar

Last Updated: 2026-02-11
Source: planningcenter.com/calendar + pcocalendar.zendesk.com docs

## What It Is
Calendar is Planning Center's centralized event planning tool for scheduling events, managing facilities and resources, and coordinating approvals -- all from a single calendar shared with staff and congregation. "Centralize event planning and setup."

## Pricing
Free tier available. Pricing scales by number of managed rooms. Unlimited events on all plans.

| Managed Rooms | Price |
|---------------|-------|
| 1 | Free |
| 5 | $15/mo |
| 15 | $32/mo |
| 30 | $69/mo |
| 50 | $115/mo |
| 75 | $179/mo |
| Unlimited | $239/mo |

## Core Capabilities

### Event Management
- One-time or recurring events with flexible recurrence (daily, weekly, custom like "every Mon/Wed")
- All-day events supported; events have name, owner, date/time, template, description, location, tags, Church Center visibility
- **Event templates** for consistent setup across similar events
- Duplicate events, bulk edit, block out events (reserve time/space), hide events from views
- **Multiple calendars** per organization for different scheduling purposes
- Event owners receive all communications about their event
- Keyboard shortcuts available; configurable week start (Sunday or Monday)

### Facility & Resource Management
- **Rooms**: Physical spaces with capacity, descriptions, and approval groups
- **Resources**: Physical items (projectors, sound equipment, chairs) with approval workflows
- **Room setups**: Predefined configurations ("Theater Style", "Classroom") to communicate setup needs
- **Folders**: Organize rooms and resources into logical groupings
- Custom **questions** asked when someone reserves a room or resource
- Automatic conflict detection and double-booking prevention

### Approval Workflow
- **Approval groups**: Named groups of people who approve/reject room, resource, and event request bookings
- Only one person from an approval group needs to approve
- Auto-approval when requester is in the approval group for what they are requesting
- Multiple approval groups assignable per room or resource
- Activity logging on all approval actions; email notifications for approvals/rejections

### Event Request Forms
- Public forms allowing anyone (including people without Calendar access) to request events
- Configurable fields and questions; each form assigned to one approval group
- Shareable via link or embed; automations for request workflows
- Staff requests (team lunches, planning meetings) and congregation requests (weddings, memorial services)

### Tags & Organization
- Tag events for filtering, sharing, and organization
- **Campus tags** for multi-campus churches
- Required tag groups can force tag selection before saving
- Tags drive filtered calendar views and shared calendar feeds

### Sharing & Publishing
- **Church Center**: Publish events as Published or Featured; calendar embed option
- **iCal feeds**: Sync to external calendar apps (Google, Outlook, Apple); feed-based sharing respects tag filters
- **iCal file imports**: Bring in events from other calendar systems
- **Kiosk mode**: Display events on a screen at your church
- iCal sync is one-directional: edits must be made in PC Calendar first

### Connections & Feeds (Cross-Product Linking)
- **Connections** (manual, per-event): Link individual Calendar events to Groups, Registrations, Services, Check-Ins, Home task lists. Widgets show summary info. Can create new Registrations signups or Home task lists from Calendar.
- **Feeds** (automatic, all events): One-way sync from Groups and Registrations into Calendar. All events from source appear automatically. Can only add rooms/resources on the Calendar side.
- Feeds for bulk automation; connections for individual linking

## Key Workflows
1. **Facility setup**: Add rooms (with setups) and resources -> organize in folders -> create approval groups -> assign to rooms/resources
2. **Event creation**: Create event (or use template) -> add schedule -> request rooms/resources -> wait for approval -> publish to Church Center
3. **Event request workflow**: Create form -> share publicly -> submissions reviewed by approval group -> approve/reject -> event created
4. **Cross-product coordination**: Create event -> add connections to Services, Check-Ins, Registrations, Groups, Home -> monitor via widgets
5. **Calendar sharing**: Tag events -> create filtered feeds -> share iCal links or embed on website/Church Center

## Admin vs Church Center
- **Admin**: Full event CRUD, room/resource management, approval workflows, request form management, tag management, multi-calendar management, connection/feed configuration, reporting
- **Church Center**: Browse published/featured events, bookmark events, submit event requests via public forms, view event details, sync events to personal calendars

## Integration Points
- **Groups**: Feeds auto-sync group events; connections link individual events; leaders can submit requests from Groups
- **Registrations**: Feeds auto-sync signup events; connections link individual events; can create signups from Calendar
- **Services**: Connections link events to service plans
- **Check-Ins**: Connections link events to Check-Ins events
- **Home**: Connections link events to task lists; can create task lists from Calendar
- **Church Center**: Event publishing, calendar embed, event request forms
- **External calendars**: iCal feed import/export

## Permissions Model
Five roles: Administrator, Facility Manager, Ministry Leader, Creator, Viewer. Room/resource approval is per-item with different approval groups assignable to each.

## Notable Details
- Calendar is free for unlimited events -- pricing only kicks in for managing multiple rooms
- Designed for staff/facilities; congregants interact via Church Center or event request forms
- Feeds from Groups/Registrations are one-way only (into Calendar, not out)
- Deleting a group type with a Calendar feed permanently removes associated events
- Multiple calendars feature allows separating different types of scheduling
- iOS and Android mobile apps available
- Campus-specific event filtering for multi-campus churches
