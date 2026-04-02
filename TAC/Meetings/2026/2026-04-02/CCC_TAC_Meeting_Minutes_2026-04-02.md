# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, April 2, 2026

**Time**: 8a-9a US Pacific Time

* **Zoom**: [https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e)

* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io),
[ical](https://calendar.google.com/calendar/ical/c\_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics),
[Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c\_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com)

* **Recordings**: [YouTube TAC Playlist](https://www.youtube.com/playlist?list=PLmfkUJc39uMjaB_I1dYW72I44kr9QzG_B)

## Links

* **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io)
* **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io)
* **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)
* **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)
* **CCC YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io)
* **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org)
* **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io)
* **Contact the CCC**: [confidentialcomputing.io/contact-us/](https://confidentialcomputing.io/contact-us/)

## Agenda and Minutes

### Welcome

* Ahmed Magdy (AM) opened the call at 8:05 am PT
* AM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Benjamin Sternthal created meeting minutes based on the transcript
* AM reviewed the agenda

### Roll Call / Attendance

No formal roll call was conducted as no votes were scheduled.

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum+ / David Kaplan
* Google - Rene Kolga+ / Keith Moyer
* Huawei - Zhipeng (Howard) Huang
* Intel - Raynor Scott+ / Simon Johnson
* Meta - Henry Wang / Kevin Hui+
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder+ / Dan Middleton+
* Red Hat - Yash Mankad / Ram Pai+
* TikTok - Mingshen Sun+ / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley



#### Other Attendees

* Ahmed Magdy (Meta Platforms, Inc.)
* Benjamin Sternthal (The Linux Foundation)
* Eric Hibbard (Samsung)
* Hesham ElBakoury (Innovax Technologies)
* Jens Albers (Fr0ntierX Inc)
* Jeremy Powell (Advanced Micro Devices)
* Manu Fontaine (Hushmesh)
* Ofir Azoulay-Rozanes (Anjuna)
* Piotr Zmijewski (Intel Corporation)
* Richard Zak (Booz Allen Hamilton, Inc.)
* Tom Jones (VeriClouds)
* Yi Liao (Automata Network)

## Welcome New Community Members

* Benjamin Sternthal (The Linux Foundation) reintroduced himself as Director of Program Management at the Linux Foundation, stepping in to support CCC while Renu is on leave and Riaan has moved on.
* Jeremy Powell (AMD) introduced himself as a security architect focused on confidential computing architecture at AMD.

## Meeting Minute Approval & Old Business

* Dan Middleton (DM) reminded rotating chairs to review the prior minutes so they are prepared for the old business section; members should help review and approve minutes via GitHub.
* DM noted the TAC held a productive working session at the previous meeting, reviewing documents quietly before reconvening to discuss comments, and planned to repeat this format.

## Announcements

* DM reminded members that the call for papers for the Confidential Computing Summit (jointly hosted by Opaque and the Linux Foundation) closes next week and encouraged submissions.

## Enarx (NRX) Annual Review

* Richard Zak (RZ) reported no significant progress on Enarx over the past year; the codebase has experienced bit rot, particularly around removed Wasmtime features, and RZ lacks support to address the technical debt.
* RZ noted continued community interest (inquiries from Toyota regarding Arm support, a contributed TDX backend module) but has been unable to secure internal support at Booz Allen Hamilton due to a lack of perceived demand signal for confidential computing.
* Nathaniel McCallum (NM) thanked RZ for his sustained effort and offered to brief Booz Allen VPs on confidential computing under NDA to help demonstrate industry demand.
* NM raised the question of widely adopted individual crates within the Enarx project (e.g., Ciborium, Flagset) that have multi-million downloads, and suggested splitting them into their own GitHub organizations with additional maintainers.
* DM acknowledged that project retirement is a normal lifecycle stage and shared links in Slack to a CCC-commissioned market report (published November 2025) and NVIDIA GTC footage of Jensen Huang discussing confidential computing, to help RZ demonstrate demand signals internally.
* Manu Fontaine (Hushmesh) offered to connect with Booz Allen contacts on use cases in identity and agentic AI, noting traction at NATO and among defense contractors.

## Tech Talk: Platform Ownership Endorsements (Intel)

* Scott Raynor (SR) presented on Intel's Platform Ownership Endorsements (PoE) initiative, originally presented at OC3 by Dr. Bennett Fury. Piotr Zmijewski (PZ), a cloud software architect at Intel responsible for remote attestation services, co-presented.
* SR outlined the threat model: physical attacks (e.g., the .fail attacks on SGX/TDX) allow memory probing and extraction of the attestation key, enabling an attacker to produce forged TD quotes with arbitrary measurements. Intel can revoke compromised platform keys, but there is a window of vulnerability before revocation.
* The PoE solution anchors platform identity to the PCK certificate (signed by Intel and tamper-proof), which contains a unique Platform Instance ID (PIID) generated on first boot and reset only via explicit SGX factory reset or TCB recovery.
* SR described three phases of the PoE approach:
  * **Short-term**: PIIDs are collected and sent to a platform endorser, who creates signed PoE structures (using IETF CoRIM format). At attestation time, the attestation service retrieves and verifies the PoE against the quote's PIID. Intel is not involved at runtime.
  * **Long-term (DCAP integration)**: The PoE structure is stored on the target platform itself, so the platform endorser is not needed at runtime—only the endorser's public key is required by the attestation service.
  * **Much longer-term (Platform Composition Endorsements)**: Intel PCS validates platform composition via device IDs and a trusted supply chain inventory, issuing a Platform Composition Manifest (PCM) that the platform endorser uses to create PoE structures.
* Intel is developing standalone tooling (PIID extractor, PoE generator, PoE evaluator) that will eventually be integrated into the DCAP stack. No new hardware is required for the short- and long-term phases; timelines are not yet public.

### Discussion

* Alec Fernandez (AF) thanked Intel for transparently addressing the .fail attacks and described the shared responsibility model: Intel guarantees firmware security, while CSPs (e.g., Microsoft) guarantee physical security and maintain a secure hardware inventory using their own KMS infrastructure.
* NM raised questions about how Intel determines platform ownership, what happens at end-of-life/resale, and how multi-level leasing arrangements (where the CSP may not own or manage the data center) are handled. SR confirmed ownership is based on registration (not bill of sale), registrations are long-lived (7-year PCK cert), and SGX factory resets can be performed unlimited times to transfer ownership.
* PZ clarified that Intel does not plan to issue ownership claims itself; the platform owner (e.g., the CSP) issues those endorsements.
* DM asked what the CCC can do to help mature the PoE approach. SR requested feedback on the specification and suggested the Attestation SIG as a forum. DM noted that the PoE generator and PoE evaluator tools could be good candidates for CCC open-source projects.
* AF proposed that the CCC author a paper on the shared responsibility model for confidential computing—covering supply chain security, physical possession, and decommissioning—so that Intel and CSPs can each clarify their respective security guarantees.

## White Papers and Blueprints

* DM reported that the Linux Foundation confirmed it is acceptable to mention commercial products in CCC papers if those products are based on CCC or LF projects, though endorsement of one product over another should be avoided. Written guidance is pending; DM advised conservative mentions of existing solutions for now.
* DM set a goal to finalize Blueprints B (secure key release), C (clean room / collaborative computing), and the Three Degrees of Integration paper this month. Blueprint A (key management) still needs an author; Simon Johnson had volunteered, but DM welcomed others to take it on.

## Three Degrees of Integration Document Review

* The TAC conducted a quiet working session to review DM's "Three Degrees of Integration" paper, which describes progressive levels of confidential computing adoption.
* Key debate centered on whether Level 1 (CVM without attestation) should be considered confidential computing. AF and Ofir Azoulay-Rozanes argued that Level 1 does not meet the CCC definition because it lacks hardware-based attestation, and the paper should make clear that Level 3 (workload-specific attestation and key management) is the target. NM agreed, stating that robust attestation in deployment procedures is the industry's most important task.
* Rene Kolga cautioned against dismissing Level 1 entirely, noting that a majority of current CC customers are at Level 1, and the paper should acknowledge it as a valid step on the journey toward full confidential computing.
* DM agreed to strengthen the language around Level 1's limitations and make a stronger statement about striving for Level 3. Remaining comments will be addressed asynchronously.

## Any Other Business / Next Steps

* Members were reminded to review the PoE specification (link to be shared with the presentation), continue providing feedback on Blueprints B and C and the Three Degrees document, and submit proposals to the CC Summit before the CFP closes.
* Richard Zak and Nathaniel McCallum will coordinate offline on splitting widely adopted Enarx crates into independent projects and on a potential VP briefing at Booz Allen.
* Next meeting is scheduled on Thursday, April 16, 2026. AM adjourned the meeting at 9:01 am PT.
