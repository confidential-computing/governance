# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, July 11, 2024

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

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - David Kaplan / Harold Gilkey +
* Arm - Nathaniel McCallum   / Michael Lu
* Google - Catherine Zhang +
* Huawei - Zhipeng (Howard) Huang
* Intel - Dan Middleton (TAC chair) +  / Simon Johnson
* Meta -  Henry Wang + /  Kevin Hui +
* Microsoft - Alec Fernandez +
* Nvidia - Fritz Alder +
* Red Hat - Yash Mankad +  / Ram Pai
* TikTok - Mingshen Sun + / Yao Zhang

   " + " indicates attending

#### Other Attendees

* Anna Trikalinou (Microsoft)
* Cosmin Aprodu
* Harold Gilkey (AMD)
* Jason Rogers
* Manu Foutaine (Hushmesh)
* Mark Novak (JP Morgan Chase)
* Ofir Azoulay-Rozanes (Anjuna)
* Tiziano Santoto (Google)
* Victor Lu
* Vini Jaiswal (TikTok)
* Yulia Gontar (Superprotocol)
* Sal Kimmich (CCC)
* Ben Sternthal (LF)
* Riaan Kleinhans (LF)

## Welcome

Dan Middleton (DM) opened the call at 7:05 am and reviewed the antitrust policy.

## Agenda

DM reviewed the agenda for the meeting.

## Roll Call / Attendance

Quorum was established.

## Welcome New Community Members

* Cosmin Aprodu introduced themselves.
* Jason Rogers introduced themselves.
* Three folks from Google / [Project Oak](https://github.com/project-oak/oak) introduced themselves.
* Yulia Gontar from Superprotocol introduced themselves.
* Anna Trikalinou introduced themselves.

## Old Business

DM reviewed the GRC and Data Cleanroom Project proposal from the last meeting. Mark Novak (MN) reviewed the NIST announcements from the previous meeting. DM mentioned that the use case document was published yesterday.

## TAC Project Proposal: Data Clean Room

DM opened the floor for discussion and questions on the [Data Clean Room](https://github.com/tiktok-privacy-innovation/PrivacyGo-DataCleanRoom) as a potential new CCC project.  

Fritz Alder (FA) asked for clarification on the primary use case the project intends to address. Mingshen Sun (MS) reviewed the primary use case and provided additional technical details. Discussion ensued

DM asked for clarification on which portion of the “Two-Stage” architecture was included in the project. MS stated that both the programming and execution stages were included. DM asked what the differences were in functionality between this and Google Confidential Space. MS provided technical details on the differences. DM lastly asked how attestation is or is not used in the project. MS stated that it is and provided context on the scenarios where it is used.

Alex Fernandez (AF) asked if the token met the CCC definition of "hardware-based, attested Trusted Execution Environment"? AF asked DM if we should ask the folks at Google if this meets the definition.

Discussion ensued.

DM asked if someone from the TAC wanted to make a motion to vote on the project or if folks wanted more time to consider the project. AF stated that he would prefer more time and to discuss privately with TAC members before voting. DM stated that it would be kept on the agenda and encouraged TAC members to use existing channels to discuss. Fritz Alder and Manu Fontaine agreed that they would like more time for discussion. Vini Jaisal (VJ) offered to reach out to any members that require any further clarification or information.

## TAC Objectives / TAC Goals

DM introduced Henry Wang (HW) and Kenvin Hui (KH) to discuss TAC Goals.
HW announced that they have an internal Attestation encrypted channel establishment library project based on C++ helper functions that they would be interested in open sourcing. They are still working on removing internal dependencies before it is ready. Aiming to open source it before the end of 2024.
DM welcomed the proposal and said the submission is welcome and does not have to be a finished product, leaving room for contributions.

KH discussed starting a working group around open source code transparency for data center owner companies. They have already discussed this with the folks from Project Oak. AF asked if they have looked at the documentation around Azure code transparency service and how this would be different from this proposal.KH he briefly looked at it. The aim of the group would be to bring everyone’s code transparency work together. Started the working group and would aim to bring more roleplayers together.
AF also indicated he would be interested in this work.

DM pointed out that this idea is helpful, but it produces more goals to pursue rather than addressing goals that were already set by the TAC of 2024. He further proposed that KH can start with a blog post figuring out what is already available in the field suggesting a TAC tech talk to solicit community feedback.
Discussion ensured.

## Any Other Business / Schedule

Non

Next meeting July 25, 2024

The meeting adjourned at 08:20 am PT
