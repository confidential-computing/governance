# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, October 16, 2025

**Time**: 8a-9a US Pacific Time

* **Zoom**: [https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e] 

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

* Dan Middleton (DM) opened the call at 8:05 am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Renu Chauhan (RC) & Riaan Kleinhans (RK) created meeting minutes.
* DM reviewed the agenda


### Roll Call / Attendance

A quorum was not achieved

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum+ / David Kaplan
* Arm - Paul Howard+  
* Google -  Catalin Sandu+ 
* Huawei - Zhipeng (Howard) Huang 
* Intel - Raynor Scott / Simon Johnson
* Meta - Henry Wang / Kevin Hui
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder+ / Dan Middleton+
* Red Hat -  Yash Mankad / Ram Pai 
* TikTok -  Mingshen Sun+ / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley 

   " + " indicates attending

#### Other Attendees
* Caroline Perez-Vargas (Microsoft)
* Donghang Lu
* Henk Birkholz  
* Jens Albers (Fr0ntierX Inc)  
* Keith Moyer (Google LLC)
* Leonardo Garcia
* Manu Fontaine (Hushmesh)  
* Mona Vij (Intel Corporation)  
* Mike Bursell (CCC)
* Ofir Azoulay-Rozanes (Anjuna) 
* Renu Chauhan (Linux Foundation)
* Riaan Kleinhans (Linux Foundation)
* Shelven Zhou  
* Victoria de Quehen
* Yuxia Zhan   
 

## Welcome New Community Members
Keith Moyer (KM) introduced themselves from Google.

## Meeting Minute Approval & Old Business
* Meeting minutes will be approved via GitHub. DM reviewed the old Business covered in the previous meeting. 

## Announcements
Download from the Board meeting:
Mike Bursell (MB) briefed the key outputs from the Board meeting on Oct 15, 2025.MB shared:
The Governing Board recently set a high-level strategy that will be broken down into actionable items with an appropriate budget at the next board meeting
The strategy aims to balance supply-side and demand-side work to encourage adoption
Future focus areas include work with regulators, compliance, and standards


## GRC SIG Attendance
DM discussed the GRC SIG experiencing decreased attendance, possibly due to diverging interests between governance and regulatory compliance topics. Alec Fernandez (AF) noted a bifurcation in the SIG between those interested in governance versus those focused on regulatory compliance. A proposal was made to potentially restructure to better address both areas.

## Budget proposal for 2026
DM gave a brief overview of the budget proposal for 2026: 
The overall budget will be smaller next year after deficit spending this year to use the surplus.
The test infrastructure budget will be reduced, as actuals were lower than allocated
Proposal to redirect $100,000 (previously for Technical Community Architect) to fund two projects with $50,000 each
Mona Vij raised concerns about the Gramine project funding, as Intel's funding has disappeare,d and the project has slowed significantly

## Trustless Attestation Verification in Confidential 
Donghang Lu (DL) presented an update on TikTok's zero-knowledge attestation verification project.
They've open-sourced two implementations: one using Circom and another using RISC-0.
The RISC-0 version was just released and offers better performance (20-30 seconds vs 20-30 minutes) 
Discussion about the project's purpose to exclude attestation verification services from the Trusted Computing Base (TCB).
Questions raised about the practical benefits given performance trade-offs

Yuxia Zhan asked about the necessity of zero-knowledge properties in TikTok's attestation services, and Donghang explained that while standard attestation logic doesn't require zero-knowledge, they chose it for its efficiency, as no faster cryptographic proof was found. Donghang also mentioned potential future use cases for zero-knowledge properties in scenarios requiring data location compliance, where detailed network topology could be hidden while still verifying correct machine locations. Fritz Alder inquired about multi-party computation as an alternative, but Donghang clarified that MPC protocols weren't suitable for their attestation verification server model, which requires a peer-to-peer setting.
Discussion ensued with follow-up questions from the presentation.

 
## Future Meetings 

## Topic Schedule 2025  &  Future Business

## Any Other Business / Topic Schedule 2025

Next meeting October 30, 2025. The meeting was adjourned by DM at 08:59 am PT





