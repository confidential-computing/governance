# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, May 14, 2026

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

* Ijlal Loutfi (IL), rotating chair, opened the call at approximately 8:05 am PT
* IL welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Benjamin Sternthal created meeting minutes based on the transcript
* IL reviewed the agenda

### Roll Call / Attendance

No formal roll call was conducted. The chair noted quorum was not expected and no votes were scheduled.

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum+ / David Kaplan
* Google - Rene Kolga / Keith Moyer
* Huawei - Zhipeng (Howard) Huang
* Intel - Raynor Scott+ / Simon Johnson
* Meta - Henry Wang / Kevin Hui
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder / Dan Middleton
* Red Hat - Yash Mankad / Ram Pai+
* TikTok - Mingshen Sun / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley

#### Other Attendees

* Dan S (PremAI)
* Ijlal Loutfi (Canonical)
* Jens Albers (Fr0ntierX Inc)
* Jeremy Powell (Advanced Micro Devices)
* Jianxiong Gao (Google LLC)
* Jordi Guijarro (OpenNebula Systems)
* Ken Fromm
* Kevin Jones
* Manu Fontaine (Hushmesh)
* Milica Spuzic (Microsoft Corporation)
* Olivia Wu (Graviti Technologies)
* Rithikha Rajamohan (EQTY Lab)
* Simon Gallagher (Microsoft Corporation)
* Syama Poluri (Dell)
* Tom Jones (VeriClouds)

## Welcome New Community Members

* No new members introduced themselves.

## Meeting Minute Approval & Old Business

* IL summarized the previous meeting (April 30): COCONUT-SVSM was reviewed, and the group held a working session on the blueprints. No additional items were raised.

## CCC Project Review: Keystone

* No representative from the Keystone project was present to deliver the scheduled annual review. IL made multiple calls for Keystone representatives during the meeting. The review will be rescheduled.

## Tech Talk: Attestation in a World of Composite Devices (Microsoft)

* Alec Fernandez (AF) presented a tech talk on how attestation evolves as confidential computing moves from single-CPU enclaves to composite device environments with GPUs, smart NICs, and CSP-managed infrastructure components. The presentation traced the expanding RATS roles across three generations (SGX enclaves, confidential VMs, and multi-device TEEs), highlighted that heterogeneous attestation evidence formats are a speed-to-market challenge rather than a fundamental limitation, and sparked an extended discussion among attendees on topics including open-source verifiers, transparency logs, reproducible builds, and whether operational control of in-guest code should shift from host to tenant. AF committed to sharing the slides via the TAC mailing list.

## White Papers and Blueprints

* Blueprint authors (Dan Middleton, Rene Kolga, Simon Gallagher) were not present. IL called on all TAC members to review the blueprints offline over the next two weeks, leave comments, and work with the authors to address feedback before the next meeting, with the goal of publishing soon.

## Any Other Business / Next Steps

* IL proposed that future tech talks could adopt a discussion format (presenting open questions rather than solutions) to encourage more contributions and lively discussion.
* Suggested future tech talk topics include: what a modern VMM for confidential computing should look like, and ideal boot firmware for confidential VMs.
* The Keystone annual review will be rescheduled.
* The next meeting is scheduled for Thursday, May 28, 2026. Bob Blessing-Hartley will serve as rotating chair. The agenda includes the SPDM-RS project review and the Attestation SIG annual review.
* IL adjourned the meeting at approximately 9:20 am PT.
