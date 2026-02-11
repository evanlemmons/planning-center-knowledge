# Planning Center Legal & Privacy Reference

Last Updated: 2026-02-11
Source: planningcenter.com/{terms,privacy,congregant-privacy,gdpr}

## The Critical Distinction: Controller vs. Processor

This is the single most important concept for product decisions involving user data:

| Data type | Who controls it | PC's role | Governed by |
|-----------|----------------|-----------|-------------|
| **Church admin/org data** (account info, billing, usage) | PC | Data Controller / Business | Privacy Policy |
| **Congregant data** (member names, attendance, donations, notes) | The church | Data Processor / Service Provider | Congregant Privacy Policy, DPA |

**What this means for product decisions:** When building features that touch congregant data, PC acts on the church's instructions. PC cannot use congregant data for its own purposes, cannot disclose it, and must assist churches in fulfilling data subject requests. When building features that touch admin account data, PC has more latitude but must still follow its own Privacy Policy.

## Terms of Service: Key Obligations

### User Types (matters for permissions/features)
1. **Customer** -- the church/organization (the contracting entity)
2. **Organization Administrator** -- full access, manages account on church's behalf
3. **Authorized User** -- limited access granted by Org Admin
4. **Individual** -- congregant with access to Church Center features (registration, giving, etc.)

### Acceptable Use -- What PC Is For
- **Intended Purpose:** Organizing, scheduling, managing, and participating in events and programs related to non-profit or spiritual missions (worship, volunteers, member communications, donations, admin).
- PC may NOT be used for anything outside this scope.

### What Churches Are Responsible For
- Ensuring all their users comply with ToS and Privacy Policy
- Having the legal basis (including parental consent where required) to enter data about third parties, including children
- Resolving all disputes involving their data and third-party information
- Complying with all applicable laws in their jurisdiction

### What PC Commits To
- Not retaining, using, or disclosing customer data for any purpose other than providing PC
- Notifying the customer within 45 days if contacted by someone with a data dispute
- Providing account cancellation with data deletion after 1 year
- Providing 30-day notice before price changes

### Liability Limits
- PC is provided "as is" with no warranties of any kind
- Maximum liability: amount paid by customer for PC
- All disputes resolved by binding arbitration in San Diego, CA (JAMS rules)
- Claims must be filed within 1 year or are barred
- Class action waiver (30-day opt-out window)
- PC not liable for: Stripe issues, donation disputes, data deletion by Org Admins, unauthorized account access

### Data After Cancellation
- Customer data deleted 1 year after cancellation/termination
- Deleted data is NOT recoverable
- Tax exemption certificates and tax records retained even after full deletion

### AI Policy
- Using PC to train generative AI is expressly prohibited
- PC reserves all rights to license content for AI training/ML development

## Privacy Policy: What PC Collects About Admins

### Data Collected Directly
- **At signup:** Name, email, organization affiliation
- **Automatically:** IP address, browser type/version, pages visited, time/date, time on pages, device identifiers, diagnostic data
- **Cookies:** Used for personalization. See planningcenter.com/cookies for details.
- **Google Analytics:** IP, device type, browsing activity on PC website (anonymized, not combined with PII)

### How PC Uses Admin Data
- Provide and maintain the service
- Customer support and billing
- Service improvement and analytics
- Fraud/spam prevention
- Marketing communications (opt-out available)
- Change notifications

### Data Sharing
- **Service providers** only for providing PC (see subprocessor list)
- **Integration partners** via APIs
- **CircleCo (Circle)** for Planning Center Community
- **Law enforcement** when legally required
- **Business transactions** (merger/acquisition -- with notice)
- **Never sold.** Never shared for targeted advertising.

### Data Retention
- Retained as long as necessary for stated purposes, legal obligations, dispute resolution
- Usage data retained for internal analysis

## Congregant Privacy: The Vulnerable Population

### What Churches Store About Congregants (varies by church)
- Names, contact information
- Attendance and donation history
- Medical/emergency notes (allergies, chronic conditions)
- Social media profiles
- Sensitive notes (e.g., counseling session notes)
- Children's data: names, birthdates, household affiliations, allergies, attendance

### PC's Obligations as Processor
1. Never retain, disclose, or use church data for any purpose other than providing PC
2. Provide appropriate technical and organizational security measures
3. Assist churches in fulfilling their legal obligations regarding data subject rights

### Congregant Rights (exercised through their church, not PC)
- Access, correct, or request deletion of personal data
- Object to processing
- File complaint with data protection authority
- Withdraw consent for future processing

### Children's Data
- PC does not knowingly collect personal info from individuals under 16
- Churches may store children's data for ministry purposes (names, ages, attendance, allergies)
- PC processes this data strictly as processor on church's instructions
- Church is responsible for obtaining parental/guardian consent (COPPA, GDPR, etc.)
- Minimum age to use PC directly: 13 (with parental consent for ages 13 to legal consent age)

## GDPR Specifics

- **DPO:** External EU data privacy firm retained
- **EU/UK Representative:** Calligo (Ireland) Limited, Dublin
- **DPA:** Available on request (https://pcoprivacy.churchcenter.com/people/forms/333096)
- **Data transfers:** US-based servers. Transfer governed by DPA with adequate controls.
- **Legal bases for processing:** Contract performance, legitimate interest, consent, legal obligation
- **Churches and consent:** Consent is not always required -- "legitimate interest" is a valid basis for churches processing member data under GDPR
- **All data held to GDPR standard:** Even though most customers are US-based, PC applies GDPR-level protections universally

### Data Subject Rights (EEA/UK residents)
1. Access, update, or delete personal information
2. Rectification of inaccurate/incomplete data
3. Object to processing
4. Restrict processing
5. Data portability (structured, machine-readable format)
6. Withdraw consent

## Text Messaging & Chat Compliance

### Text Messaging
- Only available to 501(c)(3) non-profits (US carrier requirement)
- Church must obtain consent from each recipient before sending
- Opt-out via "Stop" keyword required
- Credits expire 12 months from purchase; non-transferable
- Text2Give subscriber data never shared with third parties or used for marketing

### Chat
- Chat history may be stored by PC
- **No guarantee of privacy** for chat content
- PC may monitor, block, suspend, or delete chats
- Product implication: any chat feature must communicate this clearly to users

## Quick Reference for Compliance Questions

- [ ] **Who owns congregant data?** The church. PC is the processor.
- [ ] **Can we use congregant data for our own analytics/features?** No. Only for providing PC on the church's instructions.
- [ ] **Can we build features that access congregant data across churches?** No. Each church's data belongs to that church alone.
- [ ] **Do we need consent to process congregant data?** The church needs a legal basis (consent OR legitimate interest OR other). PC processes on their behalf.
- [ ] **What if a congregant asks PC to delete their data?** Direct them to their church. PC assists the church in fulfilling the request.
- [ ] **Can we email congregants marketing for PC?** No. Congregant data cannot be used for PC's own purposes.
- [ ] **What data can we use for product improvement?** Admin account data and anonymized usage data. NOT congregant data.
- [ ] **Can we store children's data?** Churches can, as processor. PC must not collect it for its own purposes. Church handles consent.
- [ ] **Is there a minimum age?** 13 to use PC. Under 13 is strictly prohibited.
- [ ] **What happens to data on account cancellation?** Deleted after 1 year. Not recoverable.
- [ ] **Can churches use PC for health records?** No. Only limited emergency notes (allergies, chronic conditions, care instructions).
- [ ] **Can we add a new subprocessor?** Yes, but subscribers to the subprocessor list must be notified before engagement.
- [ ] **Do we respond to DNT signals?** We do not use website tracking technologies and thus do not respond to DNT signals.
- [ ] **Where do disputes get resolved?** Binding arbitration, San Diego, CA (JAMS). California law governs.
- [ ] **What's our breach notification obligation?** Without undue delay, via email and in-app notification.
