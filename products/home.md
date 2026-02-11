# Home

Last Updated: 2026-02-11
Source: planningcenter.com/home + pcohome.zendesk.com docs

## What It Is
Home is Planning Center's central landing page and operational hub -- the first thing users see on login. It provides customizable dashboards with church-wide engagement metrics, cross-product task management, and a persistent toolbar across all PC products. "All your ministry work, all in one place."

## Pricing
Free. Included with every Planning Center account -- no separate subscription needed. Start with People (free) to get access.

## Core Capabilities

### Tasks
- Create personal to-do items with title, description, links, due date, and recurrence (daily, weekly, custom)
- Organize into named, color-coded task lists
- "My List" is a private default list per user (cannot be shared)
- Tasks can be created from anywhere via toolbar clipboard icon or directly from notifications (pre-fills title, links back to source)
- Duplicate existing tasks; deleted tasks cannot be recovered
- Tasks are "connected" -- they link back to the event, person, or plan where created

### Task Collaboration
- Share lists with collaborators for team task management (except "My List")
- Collaborators can view, add, edit, and delete tasks; tasks can be assigned to specific collaborators
- Collaborator eligibility: anyone with a permission level that includes People page access in any PC product (varies by product)
- Live updates: completions/deletions instant; name/edit changes require save
- Removing a collaborator unassigns their tasks; inactivated/deleted profiles auto-removed
- Notifications: email + in-product when added/removed as collaborator or assigned a task

### Task Templates
- Reusable templates for recurring processes (post-service cleanup, holiday prep, event planning)
- Relative due dates (e.g., "3 days after list creation") -- ideal for repeatable processes
- Templates can include collaborators who get notified on list creation
- Template creation is web-only; creating lists from templates works on mobile too

### Task Automations
- Automations from other PC products create tasks in Home (People lists/forms, Giving, Groups, Services, Registrations, Calendar)
- Specify task name, list, assignee, and due date (relative days)
- Common: volunteer follow-up, birthday reminders, first-time donor thank-you, background check ordering
- No automations created directly in Home -- always configured in the source product

### Dashboards
- **My Dashboard**: Personal, private; first tab on login; widgets configured per user
- **Shared dashboards**: For teams/ministries/projects; collaborators can be viewers (read-only) or managers (can edit)
- Tab-based layout; "My Dashboard" always far left; other tabs reorderable
- Warning: making yourself a viewer on a shared dashboard locks you out of editing

### Widgets (by product)
- **Calendar**: Pending approvals, Upcoming events
- **Check-Ins**: First time visitors, Most popular stations, Attendance, Headcounts
- **Giving**: Batches in progress, Newest donors, Recurring donation forecast, Donors, Total donated
- **Groups**: Groups overview, Newest group members, Upcoming group events, Attendance, Memberships
- **Home**: Notepad, Quick Links, Tasks (filtered task view)
- **People**: My workflow cards (personal only), Newest profiles, Upcoming birthdays/anniversaries, Workflow overview, Demographic breakdown, List results, New profiles
- **Publishing**: Recently edited pages, Active Church Center app users
- **Registrations**: Recent registrations, Single signup, Attendance, Registrations
- **Services**: My schedule (personal only), Plans forecast, Team breakdown, Attendance, Scheduled

## Key Workflows
1. **Daily task management**: Login -> My Dashboard tasks widget -> create/complete tasks from toolbar or Tasks page -> assign to collaborators
2. **Team project setup**: Create template with tasks and relative due dates -> create list from template -> add collaborators -> assign -> track completion
3. **Ministry dashboard**: Create shared dashboard -> add product-specific widgets -> share with team -> monitor metrics
4. **Cross-product automation**: Event in another product triggers automation -> task auto-created in Home -> assignee notified -> follow-up happens

## Admin vs Church Center
Home is admin-only; there is no Church Center/congregant-facing component. All features (tasks, dashboards) are for church staff and leaders. The Tasks mobile app is a staff tool.

## Integration Points
- **All PC products**: Dashboard widgets pull data from every product; automations from any product can create tasks
- **People**: Workflow cards in toolbar; list data powers widgets; automations from lists/forms create tasks
- **Services/Giving/Groups/Check-Ins/Registrations/Calendar**: Data feeds into widgets; automations can create tasks
- **Publishing**: Church Center app usage data in widgets
- **Toolbar**: Tasks accessible via clipboard icon across all PC products; notifications convertible to tasks

## Notable Details
- **Widget data visibility**: Shared dashboard collaborators see widget data even without product permissions -- data stops if dashboard creator loses access
- **Collaborator permission matrix**: Complex per-product rules determine eligibility -- not everyone with PC access qualifies
- **Personal vs shared widgets**: Some widgets are personal-dashboard-only (My workflow cards, My schedule)
- **Lists must be 24h old**: People list result widgets require lists to be at least 24 hours old
- **Chat on marketing page**: Chat appears on the Home marketing page but is actually a separate product managed by a separate team -- marketing packaging decision, not a product boundary
- **Mobile app**: Dedicated Tasks mobile app (iOS/Android) with full CRUD, push notifications, and template-based list creation
