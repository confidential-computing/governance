# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, August 22, 2024

**Time**: 7a-9a US Pacific Time

* **Zoom**: [Zoom](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e)

* **Calendar**: [calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io),
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

### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - David Kaplan / Harold Gilkey
* Arm - Nathaniel McCallum   / Michael Lu
* Google - Catherine Zhang+
* Huawei - Zhipeng (Howard) Huang
* Intel - Dan Middleton (TAC chair)+ / Simon Johnson
* Meta -  Henry Wang /  Kevin Hui+
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder+
* Red Hat - Yash Mankad+  / Ram Pai+
* TikTok - Mingshen Sun+   / Yao Zhang

   " + " indicates attending

#### Other Attendees

* Bokdeuk Jeong (Samsung)
* Harold Gilkey (AMD)
* Henk Birkholz
* Hesham (Innovax Technologies)
* Jason Rogers (Invary)
* Joseph Artgole (ARM)
* Julian Stephen (IBM)
* Kanth Ghatraju (Oracle)
* Leonardo Garcia
* Ofir Azoulay-Rozanes (Anjuna)
* Simon Frost (ARM)
* Stephen Smalley (NSA)
* Thomas Fossati (Linaro)
* Thore Somme
* Dr. Wesley Peck
* Mike Bursell (CCC)
* Sal Kimmich (CCC)
* Ben Sternthal (LF)
* Riaan Kleinhans (LF)

## Welcome

Dan Middleton (DM) opened the call at 7:04 am and reviewed the antitrust policy.

## Agenda

DM reviewed the agenda for the meeting.

## Roll Call / Attendance

Quorum was (not) established.

## Welcome New Community Members

* Julian Stephen (IBM) introduced themselves and stated they were looking at CC as a way of securing AI models.
* Dr. Wesley Peck (Invary) introduced themselves.
* Stephen Smalley (NSA) introduced themselves.

## Old Business & Announcements

DM reviewed the status of the Data Clean Room Project, and onboarding this project to CCC. Riaan Kleinhans (RK) stated that this was in progress.

DM reminded attendees of the OSS EU Mini Summit and that the CFP closes today, August 8th. DM then mentioned KubeCon in Salt Lake City and that CCC would have a booth, he encouraged folks to reach out to Riaan if they were interested in staffing the booth.

## Attestation Business Models

Mike Bursell discussed his efforts to create a working group focused on attestation business models and stated that he recently distributed a [document](https://docs.google.com/document/d/1ViW-y3GiLmBygwpC91diJCEEm8phIN4VSCDkhSsEnQc/edit#heading=h.1cwejrcpvn82) to help start the process.

DM asked to understand the goals and a schedule. MB agreed and stated it was this project was still in the formation period.

## Veraison Project Update

Thomas Fossati and Simon Frost (SF) gave an annual review on [Project Veraison](./Project%20Veraison%20CCC%20Review%202024.pdf).

MB mentioned that he thought the GitHub stats were valuable and would want to see this data whenever we did an annual review.

Discussion ensued.

DM asked about the security badge and then asked which repo would be most appropriate for a new contributor. SF stated that there was a [repo guide](https://github.com/veraison/docs/blob/main/repo-guide.md). DM asked if there had been engagement with the project mentor. Simon stated that there hasn’t. DM stated that there has been discussion about the viability of the liaison model and if it can scale. DM asked if the role of the liaison provides value to the projects.

## Runtime Attestations

Jason Rogers (JR) and Dr. Wesley Peck (WP) presented on [runtime attestations](./Invary%20Runtime%20Integrity%20-%20CCC%20TAC.pdf).

Discussion ensued with interactive questions and answers.

## 2024 CCC TAC Objectives

Fritz Alder (FA) discussed the 2024 objectives of the TAC. He gave feedback on the academic engagement objective and asked the attendees what academic topics would be of interest to the TAC.
MB said that talks on mitigations for attacks related to protocols would be valuable.
FA stated that the PQ talks presented were insightful. He further asked if the group would be interested in academic topics or if the talks should focus on more practical topics.
MB said that he would like to see more of the TAC Tech Talks presented at industry events.
FA said that MB’s point ties in with his next topic, asking the group about what external engagement with academics should be pursued.
MB agreed that it would be helpful to build relationships with academics.
Thore Sommer (TS) said that relationships with academics and providing a platform where academic work could be done and technical questions could be asked and answered would be beneficial. MB added that larger organizations with research groups would be helpful.

Ofir Azoulay-Rozanes said that the missing topic for him is the involvement of hardware providers and cloud providers in discussions about vulnerabilities and mitigations, as well as the development of hardware. FA cautioned against the discussion of “soon to be released” features, as it could violate the antitrust policy. DM said that IP announcements that companies are comfortable sharing would be useful information to discuss as a community.

MB pointed out that the TAC is a technical advisory council, and they should avoid “product pitches.” He suggested seeking advice from the GB about news feeds from vendors, as large companies might overshadow smaller companies. Catherine Zhang (CZ) asked if sponsoring academic conferences would be a good opportunity to discuss the CCC with academics. Discussion ensued about event participation and academic involvement.

Sal Kimmich said that, from their experience working in the academic space, they had no knowledge about the opportunity to join open-source community calls; getting that information out would be helpful for academics.

## Any Other Business / Schedule

Next meeting August 22, 2024

The meeting adjourned at 09:00 am PT
