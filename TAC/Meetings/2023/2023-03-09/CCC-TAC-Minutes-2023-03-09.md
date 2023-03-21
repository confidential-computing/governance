# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, March 9, 2023

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)

* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io),
[ical](https://calendar.google.com/calendar/ical/c\_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics),
[Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c\_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com)

* **Recordings**: [YouTube TAC Playlist](https://www.youtube.com/playlist?list=PLmfkUJc39uMjaB\_I1dYW72I44kr9QzG\_B)

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

* Dan Middleton (DM) opened the call at 7:05am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Kurt Taylor (KT) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano
* Arm - Thomas Fossati +  / Michael Lu
* Google - Cfir Cohen  / Catalin Sandu
* Huawei - Zhipeng (Howard) Huang +
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup  / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler  +
* Red Hat - Lily Sturmann  / Dimitrios Pendarakis

   " + " indicates attending

***Other Attendees***

* Alec Fernandez (Microsoft)
* Jethro Beekman (Fortanix)
* Drasko Draskovic (Ultraviolet)
* Eric Voit (Cisco)
* Stephano Cetola (RISC-V)
* Matthieu Legre (Cysec)
* David Gilbert (Red Hat)
* Henk Birkholz
* Tiziano Santoro (Google)
* Yash Mankad (Red Hat)
* Ahmad Atamli
* Ijlal (Canonical)
* Samuel Ortiz (Rivos)
* Xinxin Fan (Iotex)
* Shalom Shefa
* Mark Novak (JP Morgan Chase)
* Nicolae Paladi (CanaryBit)
* Helen Lau (LF)
* Kurt Taylor (LF)


**Meeting Minute Approval**

Proposed: That the minutes of the February 23, 2022 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

* Quorum was reached and the minutes were approved by the voting members of the TAC.


**Action Item Review**

* DM reviewed the action items
* KT reported that the copy/paste problem is fixed
* KT to make progress on PR for markdown source before the next meeting
  * Alec Fernandez mentioned that he had a few other fixes for the next version, will submit a PR when we have the source in markdown
* Howard Huang will come up with a project progression state draft by the end of next week (3/17)
* AF to sync with Dave Thaler for the blog post on attestation addition
* Gramine website refresh reboot is making progress, brief being updated to see if there was a way to come back with a lower cost
* DM/KT need to sync on a CCC security mailing list, discuss those to be added to the list
* Need update from Lily on Keystone questions
* KT commented that the needs to find access to the Keystone website to fix the programs link


**2023 Goals**

* DM discussed 2023 plans
  * Cross-org/Cross SIG 
    * Regulatory work (GRC SIG)
      * MN gave status on objectives that will be updated in April review
    * FHE educational content
  * Community development
    * Outreachy update next meeting


**Project Progression**

* DM overviewed the [progression policy](https://github.com/confidential-computing/governance/blob/main/project-progression-policy.md)
* Gramine has requested to progress in state
* Eric Voit discussed the origin (CNCF) and that it has a different focus than the CCC
  * What are the additional services do projects need or want per stage of progression
  * Only benefit now is visibility (publicity) on the website, no per-state additional benefits
  * [Benefits list](https://github.com/confidential-computing/governance/blob/main/project-progression-policy.md#benefits-of-being-a-recognized-consortium-project)
* Only approved stages are sandbox and incubation, the rest of the document is a proposal and has not been approved
* DT discussed if there was a real need to have different stages
* Mentors to get input from their projects for discussion in the next meeting


**TAC Tech Talk**

* eBPF - Dave Thaler
  * DT presented an overview of eBPF and how it relates to Confidential Computing


**Outreach Update**

* DM summarized OC3
* Helen Lau reported that Ben Fischer is delivering the Keynote to OC3 instead of Stephen Walli
* Mark Novak talked about his presentation - on what stands in the way of broad adoption
* DM talked about a few other talks


**Conformance to Terminology**

* Alec Fernandez discussed the [NVIDIA blog](https://blogs.nvidia.com/blog/2023/03/01/what-is-confidential-computing/)
  * The diagram that shows TEE and the AMD SEV-ES environment - does this meet the definition of Confidential Computing?
  * DM noted that the diagram may have been created before CCC Terminology was published
  * Alec concerned with referring to CC in a blog post with an opinion that is not broadly agreed to as being correct
  * DM posed a GB question for conformance enforcement, DT volunteered Mike Bursell to send email to NVIDIA for possible cleanup of the blog, AF to reach out to MB
  * Nicolae Paladi suggested reusable graphics created and kept up-to-date by the CCC


  ***ACTION*** Kurt to pose the CCC Terminology enforcement question to the Governing Board for discussion


* DT discussed [conformance spreadsheet](https://docs.google.com/spreadsheets/d/1H07OqDilgSWQpf2xZ-yJUSHL249VaXroVv1eeacVOVc/edit#gid=0)
  * Can CC be computationally detectable for implementing a test suite? Needs independent verification, certification programs
  * Test plan that an independent auditor could review and certify, not necessarily code
  * MN agreed to take this forward in the GRC in April


* Next meeting March 23th, 2023

Meeting adjourned at 9:02 am PT
