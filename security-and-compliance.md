# Planning Center Security & Compliance Reference

Last Updated: 2026-02-11
Source: planningcenter.com/{security,gdpr,privacy,terms}

## SOC 2 Type 2

- **Status:** Certified. Audited by Johanson Group (AICPA-approved).
- **Trust criteria covered:** Security, availability, processing integrity, confidentiality, privacy.
- **Scope of audit:** Policies, backup/disaster recovery, incident response, firewall configs, other critical areas.
- **Report availability:** Full report available on request via form: https://pcoprivacy.churchcenter.com/people/forms/411901

## PCI Compliance

- **Level:** PCI Level One compliant merchant.
- **Payment processor:** Stripe (PCI Service Provider Level 1).
- **Key constraint:** PC never stores credit card numbers directly. All payment data flows through Stripe's secure infrastructure.
- **Prohibited:** Collecting banking details, credit card numbers, or financial information outside PC's authorized payment collection systems.

## Infrastructure & Encryption

- **Hosting:** AWS data centers in Virginia (us-east). All servers and infrastructure are US-based.
- **Encryption in transit:** All data encrypted over HTTPS between users and PC.
- **Encryption at rest:** Database-level encryption at rest.
- **Password storage:** One-way encrypted with bcrypt, filtered from all logs.
- **Brute force protection:** Rate limiting on authentication endpoints.

## Data Durability & Recovery

- **Backup strategy:** Multilayered -- point-in-time backups and daily snapshots.
- **Resilience targets:** Hardware failure, regional disasters, malicious acts.

## Vulnerability Management

- **Bug bounty:** Ongoing program through HackerOne. Open to any researcher.
- **Contact:** hackerone@planningcenter.com (average response time < 1 day).
- **Scope:** Penetration testing across all products.

## Secure Development Practices

- Code changes go through: peer review, automated test suite, manual QA (most cases).
- Priority on well-tested, well-reviewed code to prevent security exploits from coding errors.

## Physical & Equipment Security

- **Data centers:** AWS physical security (industry-leading controls, redundancy, availability).
- **Office:** Locked and alarmed during off hours. No servers on premises.
- **Employee devices:** Password protected and encrypted.
- **Customer data access:** Encrypted connection + time-based one-time password (TOTP) required.

## Personnel Security

- All employees sign NDAs at hire.
- Small company with extremely low turnover (for tech industry).
- Many employees are also PC users with their own data in the system (personal stake in security).

## Incident Response

- **Breach notification commitment:** PC will inform affected users via in-app notification and email "without undue delay" upon discovering a breach.
- **Notification method:** Email to last listed address + in-app notification. Users can request mail notifications instead.
- **Contact for disputes:** Within 45 days of being contacted about a data dispute, PC notifies the customer (church).

## GDPR Compliance

- **Stance:** Fully committed. All data (not just EU data) held to GDPR standards.
- **DPO:** Contracted with an EU data privacy firm as Data Protection Officer for ongoing guidance.
- **EU/UK Representative:** Calligo (Ireland) Limited, Dublin. Contact: EURep@calligo.cloud
- **Data Processing Agreement (DPA):** Available on request: https://pcoprivacy.churchcenter.com/people/forms/333096
- **Data location:** US-only (AWS Virginia). Transfers to US are covered by DPA and adequate controls.
- **Legal basis:** Contract performance, legitimate interest, consent, or legal obligation (depends on context).

## CCPA / US State Privacy

- **Role:** Service Provider under CCPA/CPRA.
- **Data sales:** PC does not sell personal information. Does not share data for targeted advertising.
- **Sensitive data:** Used only for providing goods/services, not for secondary purposes.
- **Consumer rights honored:** Access, deletion, correction, portability, opt-out.

## Third-Party Security (Subprocessors)

- **Subprocessor list:** Public at https://www.planningcenter.com/subprocessors
- **Change notifications:** Users can subscribe to receive advance notice before PC engages new subprocessors.
- **Subprocessor obligations:** Same legal and contractual obligations for data security/privacy as PC has to its customers.
- **Key third parties:** Stripe (payments), Checkr (background checks), YouTube, CircleCo (Community), Google Analytics (website only, anonymized).
- **Third-party analytics:** Configured so third parties cannot use activity for their own purposes (e.g., ad personalization).

## Content Moderation & Monitoring

- PC reserves the right to monitor electronically and use automated tools + human moderation.
- Can detect prohibited content, act on violations, suspend/terminate accounts.
- Chat history is stored and is NOT guaranteed private.

## AI Policy

- Using PC content to train generative AI is **expressly prohibited** in the Terms of Service.
- PC reserves all rights to license uses of its content for AI training.

## Prohibited Data Types (Terms of Service)

These must NOT be collected/stored in PC unless expressly authorized:
1. Financial info outside PC's authorized payment systems
2. Health info beyond limited emergency notes (allergies, chronic conditions, care instructions)
3. Sensitive/explicit imagery
4. Content promoting unlawful violence, hate crimes, terrorism
5. Personal data collected for resale
6. SSNs and government-issued ID numbers (exceptions: org tax IDs for Giving, background check integrations via third-party providers, identity verification when legally required)

## Quick Reference for Compliance Questions

- [ ] **Can we store health records in PC?** No. Only limited emergency notes (allergies, chronic conditions, care instructions for events/services).
- [ ] **Can we collect SSNs?** No, except: org EINs/TINs for Giving setup, background checks via third-party providers (not stored in PC), identity verification when legally required.
- [ ] **Is data encrypted?** Yes, in transit (HTTPS) and at rest (database encryption).
- [ ] **Where is data stored?** AWS data centers in Virginia, USA only.
- [ ] **Do we have SOC 2?** Yes, Type 2 certified. Full report available on request.
- [ ] **Are we PCI compliant?** Yes, Level One. Stripe handles all card processing.
- [ ] **Can we use PC data to train AI models?** No. Expressly prohibited in ToS.
- [ ] **Do we sell user data?** No. Never.
- [ ] **Is a DPA available?** Yes, on request via online form.
- [ ] **How fast is breach notification?** "Without undue delay" via email and in-app notification.
- [ ] **Who are our subprocessors?** Public list at planningcenter.com/subprocessors with change notification subscription.
- [ ] **Is chat data private?** No guarantee. PC may monitor, block, suspend, or delete chats.
- [ ] **Can a feature collect financial data outside Giving/Registrations?** No. All financial data must flow through PC's authorized payment systems (Stripe).
