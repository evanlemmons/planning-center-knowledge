# Publishing

Last Updated: 2026-02-11
Source: planningcenter.com/publishing + pcopublishing.zendesk.com docs

## What It Is
The content management system and web editor for Church Center. Churches use Publishing to control what congregants see in Church Center, build custom pages, manage sermon video/audio libraries, and customize branding. Tagline: "Your church app and web editor." Publishing is the gatekeeper for all Church Center content.

## Pricing
Three tiers with distinct feature gates:

| Plan | Price | Includes |
|------|-------|----------|
| Essential | Free | App management, home page, page analytics |
| Plus | $15/mo | Custom pages, color themes |
| Premium | $32/mo | Audio/video channels, sermon notes |

## Core Capabilities

### Page Management
- **Built-in pages**: Auto-generated for each subscribed PC product (Calendar, Check-Ins, Directory, Giving, Groups, Signups). Content controlled in the respective product; visibility/navigation controlled in Publishing
- **Custom pages**: Drag-and-drop block editor with blocks for: Button, Contact, Divider, Event Schedule, Image, Location, Section Header, Social, Text, Video, Grid (up to 3 columns)
- **Planning Center blocks**: Calendar (up to 6 events), Registrations, Giving (link to specific fund), Sermons (gallery, single episode, auto-surface livestream)
- Pages support draft mode (save without publishing); can be duplicated, archived, and restored
- Page access can be restricted by membership type (from People) -- built-in pages cannot be restricted, only custom pages
- Page URLs set at creation and CANNOT be changed later
- QR codes auto-generated for each page; multi-campus support for campus-specific pages

### Church Center Customization
- **Theme**: Customize color scheme to match church branding
- **Navigation**: Drag-and-drop editor for menu; add custom pages, built-in pages, or external links
- **Mobile app**: Toggle Church Center mobile app on/off
- **Analytics dashboard**: Track congregation engagement with content
- Church Center can serve as the church's primary website

### Sermons
- **Channels**: Top-level containers for sermon content (e.g., "Contemporary Service", "Youth Service"). Requires Premium plan
- **Series**: Organize episodes within a channel by theme/topic
- **Episodes** support:
  - **Livestream**: Embed live video with configurable countdown and "Watch now" duration
  - **On-demand video**: Pre-recorded links (livestream NOT auto-converted to on-demand)
  - **Audio/Podcast**: Upload MP3/AAC/MP4 or link to hosted audio; auto-generates RSS feed
  - **Sermon notes**: Fill-in-the-blank notes for congregants to follow along
- **During-sermon features**: Attendance tracking, donations (link to Giving funds), chat (requires Groups subscription even at free tier)
- Default links per channel: attach People forms, Giving funds, external URLs, or Services Order of Service

### Podcast Publishing
- Auto-generated podcast feed URL from sermon audio
- Push to Apple Podcasts and Spotify
- Audio downloads from uploaded files count against subscription tier; externally hosted audio does not
- Spotify listens do NOT count against tier; Apple Podcasts listens DO
- Cannot import existing external podcasts into Publishing

## Key Workflows
1. **Set up Church Center**: Create home page -> Customize theme/branding -> Publish built-in pages -> Configure navigation
2. **Weekly sermon publishing**: Create episode in channel -> Configure livestream or upload video -> Add sermon notes -> Optionally push audio to podcast
3. **Custom page creation**: Add page -> Drag blocks -> Save draft -> Publish -> Optionally add to navigation
4. **Built-in page management**: Publish/unpublish product pages -> Add to or remove from navigation

## Admin vs Church Center
| Area | Admin (Publishing app) | Congregant (Church Center) |
|------|----------------------|---------------------------|
| Pages | Create, edit, draft, publish, archive | View published pages; restricted pages limited by membership type |
| Navigation | Drag-and-drop editor | See configured navigation on web and app |
| Sermons | Create channels/series/episodes, configure livestream, manage podcast | Watch livestream/on-demand, listen to audio, view notes, chat |
| Theme | Set colors and branding | Experience the themed Church Center |
| Analytics | View engagement dashboard | N/A |
| Mobile app | Activate/deactivate | Download and use Church Center app |

## Integration Points
- **All PC Products**: Built-in pages surface each product's congregant-facing content in Church Center
- **Services**: Sermons integrate with service types; Order of Service linkable from episodes
- **People**: Forms linked from episodes; membership types control page access; directory is a built-in page
- **Giving**: Funds linked from sermons; Giving built-in page; Giving page must be published for Text2Give
- **Groups**: Groups subscription required for sermon chat (even free tier); Groups built-in page
- **Calendar**: Calendar block on custom pages (up to 6 events); Calendar built-in page
- **Registrations**: Signups built-in page; Registrations block on custom pages
- **Check-Ins**: Check-Ins built-in page (app only, shows same-day events)

## Notable Details
- Publishing is the gatekeeper for Church Center -- it controls what congregants see and access
- Cannot create a branded app icon in mobile app stores; the Church Center icon always displays
- Cannot use a custom/purchased domain; all websites use ".churchcenter" in URLs
- Some Church Center pages can be embedded into existing church websites, but directory, event signups, and event request forms cannot
- The "Me" page is always available in Church Center (cannot be hidden)
- Sermon livestream videos are NOT automatically converted to on-demand -- must be re-added manually
- Chat during sermons creates a new conversation per episode that cannot be accessed later
- Deleting a channel deletes all episodes and uploads permanently
- Custom page URL slugs are permanent after creation
