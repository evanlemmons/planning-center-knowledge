# Planning Center Developer Platform

Last Updated: 2026-02-11
Source: developer.planning.center, planningcenter.com/developers, planningcenter.com/integrations

## Integration Tiers

Planning Center's integrations directory categorizes partners into three tiers:

### Built by Planning Center (First-Party)
Integrations PC builds and maintains. These live inside PC products and are fully supported by PC's own teams.

| Partner | Category | Notes |
|---------|----------|-------|
| BoxCast | Video | Stream services/events from Church Center website and app |
| Checkr | Background checks | Order background checks from within People (Popular) |
| Mailchimp | Email | Send mass emails to People lists via Mailchimp campaigns (Popular) |
| PraiseCharts | Music | Import lyrics, chord charts, lead sheets, audio into Services (Popular) |
| RehearsalMix | Music | Link instrument/vocal-specific audio mixes to Services |
| SongSelect | Music | Import lyrics and chord charts from SongSelect into Services (Popular) |
| Zapier | Automations | Connect PC to other tools via automated workflows |

### Verified Add-on (Partner UI Inside PC)
Partners who build React-based UI components that render **inside Planning Center's own interface** using the add-on framework. This is the newer, deeper integration model. These partners go through a formal process with PC and use a component library and insertion points provided by PC.

| Partner | Category | Notes |
|---------|----------|-------|
| Clearstream | Texting, Email | Send/schedule texts from inside PC (Popular) |
| MinistrySafe | Background checks | Order trainings, background checks, sync users inside People |
| Protect My Ministry | Background checks | Background screening and child safety training |
| RehearsalPack | Music | Import music files from MultiTracks.com into Services |
| Text In Church | Texting | Text/email People lists with automated workflows |

### Third-Party
External tools that connect via the public API. They build their own UI and sync data externally. PC lists them in the integrations directory but does not maintain the integration.

Current listed partners include: ProPresenter (Popular, presentation), AboutYourPeople (consulting), Adjace (directory), Altitude.Team (consulting), Assess Me (people management), aware3 (church management), bltn (communication), CareNote (people management), and more (paginated list continues beyond initial load).

### Key Differences Between Tiers
- **Built by PC**: PC owns the code, handles support, deepest product integration
- **Verified add-on**: Partner's UI renders inside PC products via React components; partner owns the code but uses PC's design system and insertion points; requires formal partnership process
- **Third-party**: Partner builds externally against the public API; no UI inside PC; can self-submit for directory listing via an Asana form

## API Overview

- **Type**: REST API conforming to JSON:API 1.0 specification
- **Base URL**: `https://api.planningcenteronline.com`
- **File uploads**: `https://upload.planningcenteronline.com/v2/files` (multipart/form-data)
- **Format**: JSON:API -- resources wrapped in `{ "data": { ... } }`, supports `?include=` for related resources, `where[attr]=value` filtering, and named `filter` parameters
- **Developer portal**: `https://api.planningcenteronline.com/oauth/applications`
- **All requests act on behalf of a user** -- permissions match the authenticated user's access level in PC

## Authentication

### Personal Access Tokens (PAT)
- Best for: single-church integrations, internal tools, scripts
- Generated at the developer account page
- Sent via HTTP Basic Auth (`app_id:secret`)
- Tied to a specific user's permissions

### OAuth 2.0
- Best for: third-party products serving multiple churches
- Recommended setup: create a dedicated PC organization for your app (free tier gives full API access with sample data)
- Supports standard OAuth 2.0 flow
- Supports PKCE (Proof Key for Code Exchange) for public clients
- Supports OpenID Connect (OIDC) for identity
- Scopes exist -- a `PELICAN` error hint means a required scope is missing
- Tokens expire (`BABOON` error) and can be revoked (`CAPUCHIN` error)

### Important Rules
- Tokens/secrets must never be posted publicly; they are auto-disabled if found exposed
- A `User-Agent` header should be specified
- Token management at: https://api.planningcenteronline.com/oauth/applications

## Rate Limiting

- **Default limit**: 100 requests per 20 seconds per user (subject to change)
- **Response headers**: `X-PCO-API-Request-Rate-Limit`, `X-PCO-API-Request-Rate-Period`, `X-PCO-API-Request-Rate-Count`
- **Exceeded**: HTTP 429 with `Retry-After` header indicating seconds to wait
- **Webhooks**: No rate limits on webhook deliveries

## Versioning

- **Format**: Date-based (`YYYY-MM-DD`), set per-app or per-request via `X-PCO-API-Version` header
- **Matching**: Equal-to-or-less-than algorithm (your date maps to the nearest prior version)
- **Minimum version**: `2018-08-01`; anything earlier returns HTTP 400
- **`LATEST`**: Available but not recommended for production -- expect breaking changes
- **Breaking changes**: Announced via the API News mailing list (auto-subscribed when you create an app)

## Webhooks

- **Purpose**: Real-time push notifications when data changes in PC (alternative to polling)
- **Protocol**: POST to your endpoint; verify authenticity via `X-PCO-Webhooks-Authenticity` header (HMAC-SHA256)
- **Management UI**: https://api.planningcenteronline.com/webhooks
- **Permissions**: Scoped to the creating user's access level
- **Retry schedule**: Up to 16 retries over ~5.4 days (30s, 1m, 2m, 4m, 8m, 16m, 32m, 64m, 2.1h, 4.2h, 8.5h, 17h, then daily for 4 days)
- **Failure handling**: Email after 1 hour of failures; second email before deactivation at ~5.4 days; mass failures in 24h auto-deactivate
- **Deactivation**: Respond with HTTP 410 to voluntarily deactivate a subscription
- **Rate limits**: None on webhook delivery
- **Events**: Product-specific (e.g., `people.v2.events.person.updated`); available events documented per product in the Webhooks API reference

## Add-ons (Verified Partner Framework)

Add-ons represent a deeper integration tier than the standard API. Key characteristics:

- **What they are**: OAuth applications with React-based UI components rendered **inside** PC's web interface
- **What makes them different**: Partners build features that appear natively within PC products, not in a separate app. Users interact with partner functionality without leaving PC.
- **Technology**: React components, PC-provided component library, defined "insertion points" within PC products
- **Tooling**: Dedicated Add-ons CLI for development
- **Auth**: OAuth-based, with additional add-on-specific API reference
- **Process**: Starts with reaching out to PC -- this is a formal partnership, not self-service
- **Guidelines**: PC provides design and UX guidelines that add-on partners must follow
- **Example**: Clearstream's texting UI renders directly inside PC People, with all content below a designated insertion point controlled by Clearstream's developers

### Add-on Documentation Sections
Process, Terminology, Building Your First Add-On, Add-ons CLI, Insertion Points, Component Library, API Reference, OAuth, Guidelines

## Available API Products

The API is split into product-specific sections. Products with API access:

| API Section | PC Product |
|-------------|------------|
| People | People (membership database) |
| Services | Services (worship planning) |
| Check-Ins | Check-Ins (attendance) |
| Giving | Giving (donations) |
| Groups | Groups (community engagement) |
| Calendar | Calendar (scheduling/facilities) |
| Publishing | Publishing (website pages) |
| Registrations | Registrations (signups/payments) |
| API | Cross-product / general |
| Current | Current user context |
| Webhooks | Webhook management |

See `planningcenter/products` for detailed information about each product's features.

**Not listed in API**: Home, Music Stand, Church Center -- these do not currently have public API endpoints.

## Libraries & Community

- **Official library**: `pco_api` (Ruby gem) -- https://github.com/planningcenter/pco_api_ruby
- **GitHub org**: https://github.com/planningcenter (bugs and API questions go to the `developers` repo issues)
- **Community**: "API & Development" channel in the PC user community (https://planningcenter.com/community)
- **Language support**: HTTP + JSON, so any language works; no other official client libraries beyond Ruby
- **API Explorer**: Available in the developer account for testing with real org data

## Key Constraints

1. **No API for Home, Music Stand, or Church Center** -- these products are absent from the API reference
2. **User-scoped permissions** -- every API request inherits the authenticated user's permission level; no way to exceed it
3. **Rate limits** -- 100 requests per 20 seconds per user; bulk operations require careful throttling
4. **No real-time streaming** -- webhooks are push-based but one-directional; no WebSocket or event stream API
5. **File uploads are two-step** -- upload to a separate endpoint first, then reference the UUID
6. **Add-ons require partnership** -- you cannot self-serve into the verified add-on tier; it requires reaching out to PC
7. **Versioning floor** -- cannot use API versions before 2018-08-01
8. **Community-only support** -- PC does not debug your application; support is via GitHub issues and the community channel
9. **Webhook scope** -- webhooks only return data the creating user has permission to see
10. **Limited official libraries** -- only Ruby has an official wrapper; all other languages rely on generic HTTP/JSON:API clients
