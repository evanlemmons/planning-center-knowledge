# Church Center

Last Updated: 2026-02-11
Source: planningcenter.com/church-center + pcochurchcenter.zendesk.com docs

## What It Is
The congregant-facing layer of Planning Center -- a mobile app (iOS/Android) and website where church members interact with data managed by admins in other PC products. Consolidates giving, event signups, volunteer schedules, check-in, groups, sermons, and profile management into a single app experience. Tagline: "Connect people with the life of your church." Trusted by 90,000+ churches.

Church Center is NOT a standalone product with its own admin backend. Admins control what appears through Publishing (page visibility, navigation, theme) and each individual product (content and settings).

## Pricing
Church Center itself is free. Customization is controlled through Publishing:

| Publishing Plan | Price | Church Center Impact |
|----------------|-------|---------------------|
| Essential | Free | App management, home page, analytics |
| Plus | $15/mo | Custom pages, color themes |
| Premium | $32/mo | Audio/video channels, sermon notes |

Features available to congregants depend on which PC products the church subscribes to.

## Core Capabilities

### Authentication & Identity
- Passwordless login only -- phone number (US/Canada) or email (worldwide); verification code via text or email
- Users under 13 cannot log in (based on profile birthdate)
- Mobile app stays logged in 90 days; web session 14 days
- Guest access for limited browsing without login
- Multi-church support: connect multiple churches in one app and switch between them
- Multi-campus: users may be prompted to select campus on login, which filters content

### The Me Page (Always Visible)
- **Profile & Settings**: Edit contact info, notification preferences, household, directory sharing, payment methods
- **Schedule**: Unified view of Services requests, group events, registered events, bookmarks, blockout dates; calendar feed subscription
- **Activity**: Groups joined, giving history, registered events, sermon notes taken
- **My Churches**: Switch between connected churches (mobile app)

### How Each Admin Product Surfaces in Church Center

| Admin Product | What Congregants See | Key Capabilities |
|--------------|---------------------|-----------------|
| **Calendar** | Church calendar of published events | View events, bookmark, filter by campus |
| **Check-Ins** | Same-day check-in events (app only) | Self-check-in via app, scan QR code |
| **People** | Directory (opt-in), profile management, forms | Update profile, manage household, share directory info, fill forms |
| **Giving** | Online donation form, giving history | Give one-time/recurring, manage payment methods, view statements, Text2Give |
| **Groups** | Group listings, group details | Browse/join/leave groups, RSVP to events, chat with group, view members |
| **Registrations** | Signups page with upcoming events | Register self and others, manage registrations, make payments |
| **Services** | Schedule and team assignments | View/accept scheduling requests, add blockout dates, email leaders, team chat |
| **Publishing** | Custom pages, home page, navigation, sermons | View content, watch livestream/on-demand, listen to podcasts, take sermon notes |

### Chat
- Built on Groups infrastructure (requires Groups subscription even at free tier)
- **Group chats**: Enabled per group by admins; leaders or both leaders and members can start conversations
- **Service team chats**: Team leaders start conversations, optionally filtered by plan date
- Hard limit: 100 conversations per group; 101st removes the oldest permanently
- Leaders can edit titles, set "leader messages only," delete all messages
- Members can mute, react, delete own messages; under-13 users and non-members see no chat

### Giving
- Online form with fund selection, one-time and recurring, split across funds
- "Cover the fee" option; credit/debit, ACH, Text2Give (US only)
- Manage payment methods, edit/pause/delete recurring, view history and statements

### Groups
- Browse groups (admin-controlled visibility), join (open, request, or admin-only enrollment)
- Group events with RSVP; group member directory; chat conversations
- Leaders: manage members, create events, take attendance, email members

### Events & Registration
- Calendar view of published events; registration with capacity limits, waitlists, payments, forms
- Register household members or add new people; manage existing registrations

### Sermons
- Livestream with countdown; on-demand video; audio/podcast episodes
- Sermon notes; chat during live sermons; browse channels and series

## Key Workflows
1. **Onboarding**: Find church (by name/location) -> Log in with phone/email -> Set campus -> Update profile -> Explore
2. **Sunday morning**: Check in via app -> Watch livestream if remote -> Give online -> Participate in sermon chat
3. **Group engagement**: Browse groups -> Request to join -> RSVP to events -> Chat with members
4. **Event registration**: Find event on Signups -> Register self and family -> Make payment -> Receive confirmation
5. **Giving**: Set up recurring donation -> Choose funds -> Cover the fee -> View year-end statement

## Integration Points
Church Center unifies the congregant experience across ALL Planning Center products:
- **Publishing**: Gatekeeper -- controls visibility, navigation, and custom content
- **People**: Identity layer -- profiles, households, membership types, directory
- **Giving**: All donations through Stripe
- **Groups**: Powers chat infrastructure (required even for sermon chat)
- **Services**: Scheduling data feeds the Me page schedule view
- **Calendar**: Event calendar view
- **Registrations**: Powers the Signups/event registration flow
- **Check-Ins**: Self-check-in on event day (app only)

## Notable Details
- Passwordless auth only -- no username/password combination exists
- Check-Ins in Church Center is app-only (not available on web)
- Church Center can serve as a church's primary website (via Publishing)
- Cannot create a branded app icon; always displays Church Center icon
- Cannot use custom domain; URLs always include ".churchcenter"
- The Me page cannot be hidden from navigation
- Congregation-facing docs are written for end users, not admins -- admin config docs live under each product's own help center
