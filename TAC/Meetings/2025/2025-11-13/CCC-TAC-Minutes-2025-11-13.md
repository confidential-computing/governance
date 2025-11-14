# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, November 13, 2025

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
* Renu Chauhan (RC) created meeting minutes.
* DM reviewed the agenda


### Roll Call / Attendance

A quorum was not achieved

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum / David Kaplan
* Arm - Paul Howard  
* Google -  Rene Kolga / Keith Moyer+
* Huawei - Zhipeng (Howard) Huang 
* Intel - Raynor Scott+ / Simon Johnson
* Meta - Henry Wang / Kevin Hui
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder / Dan Middleton+
* Red Hat -  Yash Mankad+ / Ram Pai 
* TikTok -  Mingshen Sun+ / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley 

   " + " indicates attending

#### Other Attendees
* Donghang Lu
* Hesham
* Jens Albers (Fr0ntierX Inc)
* Ijlal 
* Manu Fontaine (Hushmesh)  
* Matthieu LEGRE (CYSEC SA)
* Mike Bursell (Linux Foundation)
* Ofir Azoulay-Rozanes (Anjuna) 
* Renu Chauhan (Linux Foundation)
* Sakul Gupta
* Steven Bellock (NVidia)
* Sungho Yoon (Samsung)  
 

## Welcome New Community Members
No one introduced themselves at the meeting.

## Meeting Minute Approval & Old Business
* Meeting minutes will be approved via GitHub. DM reviewed the old Business covered in the previous meeting. 

##TAC Chair/Co-chair Elections
DM mentioned the current open TAC Leadership elections for 2026.  He requested to nominate if anyone is interested.

## Announcements
*  Cancel meeting 2025-11-27 (U.S. Thanksgiving)
DM mentioned to cancel the meeting on 2025-11-27. Renu Chauhan confirmed that the meeting is cancelled for 2025-11-27 via chat.


##  Vote on 2026 project allocations
* DM requested voting on the 2026 project allocations. 
Veraison - PM 
SPDM - Security Audit 
Gramine - Maintainer
* Keith Moyer requested awareness of the expense magnitude for the projects before voting.DM mentioned the budget details are: 
Total available: $100,000
Brewing split between two projects at $50,000 each
There is a change from the previous practice of spreading the money around more thinly


* Voting Process: 
The voting mechanism being used is a thumbs-up button on a GitHub issue, where TAC voting members from premier companies can vote.
Each voting member gets 2 votes to vote on two of the proposals


## Discussion: Recent publications
DM discussed the recent publications. Alec Fernandez (AF) focused on recent publications, particularly an ANSI report about confidential computing. 
 The key points discussed were:  
The report correctly notes that in cloud environments, there's still a shared responsibility model, even with confidential computing's reduced TCB (Trusted Computing Base) 
Cloud service providers are still part of the TCB for physical security, key management, and attestation verification 
The ANSI report's summary seemed bearish on confidential computing, but the actual report was more nuanced, recommending its use while understanding the threat model clearly
The committee is considering what technical responses or documentation updates might be needed for 2026, based on industry uncertainty about the technology 


* KEY CONCERNS RAISED:  
Physical security requirements may need to be stronger than initially thought 
The shared responsibility model needs clarification in the CCC documentation 
Attestation key extraction vulnerability could require tying attestations to specific machines/platforms, which Mike strongly opposed as a "hugely retrograde step"


The committee acknowledged that who should provide attestation remains a major unsolved problem for confidential computing.


* Key Action Items:
 New regulatory and standards SIG will engage with ANSI (Roman from Red Hat to lead)
 Attestation SIG will discuss technical patterns for attestation in context 
 The TAC committee discussed the plans to update its white papers to address these concerns and clarify the shared responsibility model.

## Future Meetings 

## Topic Schedule 2025  &  Future Business

## Any Other Business / Topic Schedule 2025

Next meeting  December 11, 2025. The meeting was adjourned by DM at 08:59 am PT
