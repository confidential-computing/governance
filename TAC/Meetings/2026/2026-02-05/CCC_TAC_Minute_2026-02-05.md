# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

### Meeting details

**Date**: Thursday, February 05, 2026

**Time**: 7a-09a US Pacific Time

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

* Nathaniel McCallum (NM) opened the call at 7:05 am PT
* NM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Renu Chauhan (RC) created meeting minutes.
* NM reviewed the agenda:The agenda was adjusted to remove Fritz's presentation and add two items to the end: Mike Bursell's talk on AVS and a discussion about the attestation SIG GitHub repo.


### Roll Call / Attendance

A quorum was achieved

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum+ / David Kaplan
* Arm - Paul Howard  
* Google -  Rene Kolga+ / Keith Moyer+
* Huawei - Wu Yongzheng+ 
* Intel - Scott Raynor+ / Simon Johnson
* Meta - Ahmed Magdy+
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder+ / Dan Middleton+
* TikTok -  Mingshen Sun+ / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley 

   " + " indicates attending

#### Other Attendees
* Artem Barger (Modelyo)
* Catalin Sandu (Google)  
* Caroline Perez-Vargas (Microsoft)
* Chris Ramming
* Henk Birkholz
* Jens Albers (Fr0ntierX Inc)
* Ijlal Loutfi (Canonical) 
* Leonardo Garcia
* Manu Fontaine (Hushmesh)
* Mark Novak
* Matthieu LEGRE
* Mike Bursell (Linux Foundation)
* Mike Bartock
* Ofir Azoulay-Rozanes (Anjuna) 
* Renu Chauhan (Linux Foundation)
* Riaan Kleinhans (Linux Foundation)
* Roman Zhukov (Red Hat)
* Simon Gallagher 
* Steven Bellock (NVidia)
 

## Welcome New Community Members
Mike Bartock (MB) introduced themselves to the meeting.

## Meeting Minute Approval & Old Business
* Meeting minutes will be approved via GitHub. NM reviewed the old Business covered in the previous meeting. 

## Announcements
Dan Middleton (DM) announced that the Linux Security Summit and Open Source Summit will be held in Minneapolis in May. Mike Bursell (MB) and DM encouraged submissions for confidential computing topics. 
[Link](https://events.linuxfoundation.org/open-source-summit-north-america/program/cfp/)

## Project Grant
DM reported that due to budget constraints, the board can currently support only one grant rather than the originally planned two. Based on previous voting, the Veraison proposal received the most votes and will be funded. The TAC agreed to proceed with this single grant.
[Link](https://github.com/confidential-computing/governance/issues/330)


## TAC operations 
DM proposed the soft rule, requiring TAC voting members to subscribe to the mailing list, Slack, and GitHub, and to demonstrate consistent participation to count toward quorum.MB raised concerns about the TAC's authority to enforce voting removal without board approval. Alec Fernandez (AF) and Henk Birkholz (HB) supported the idea of a "dynamic quorum" to ensure business velocity.
DM requested the TAC members to provide feedback for the rule or comment on the issue.[Link](https://github.com/confidential-computing/governance/pull/335)
The TAC members are to review and comment on Pull Request before the next meeting on Feb 19,2026.


## NIST 
Mike Bartock presented an update to the "Hardware-Enabled Security" report (NIST IR 8320). He invited the CCC to contribute updates regarding new technologies, remote attestation, and cloud use cases.
[LINK](https://nvlpubs.nist.gov/nistpubs/ir/2022/Nist.IR.8320.pdf)
AF will coordinate a "V-Team" or subteam to manage contributions and review.


## NIST RFI
Mike Bursell presented a draft response to the NIST RFI on AI agentic security.[Link](https://docs.google.com/document/d/1ZQrcYbA_Sv75NEvqMzC_07dy-KPL-zypFhuVaUU_X-E/edit?usp=sharing).The TAC group proposed a timeline requiring TAC approval by March 5th to meet the submission deadline of March 9th.The TAC agreed to motion the Governing Board (GB) to allow the TAC to approve and submit the response directly on the 5th,Mike Bursell will own the document.


## Guidance Docs 
DM introduced three adoption patterns for documentation: Managed Attestation, Key Release to TEE, and Clean Room implementation.
Blueprint A (Managed Attestation) [Link](https://docs.google.com/document/d/1yUhUqtXkyVYYRr5QGHGI2Wfz8O9HJy--Xf97zAX2ZKg/edit?usp=sharing)
Blueprint B (KMS Integration) [Link](https://docs.google.com/document/d/1dle-5JjgoIIsyrFvhbLD9rSh3ZWFEaN4Dbr7TFRbn9w/edit?usp=sharing)
Blueprint C (The Collaborative Clean Room) [Link](https://docs.google.com/document/d/1TxnEUnkxXfKrE0bN9lcAyxH-z78JMxWACYlGhnHvpDc/edit?usp=sharing)
Managed Attestation & Key Release: Simon Gallagher (Microsoft) volunteered to draft these, utilizing Azure examples genericized for the CCC.
Data Clean Room: Rene Kolga (Google) and Mingshen Sun (TikTok) will collaborate on this draft.
Rough drafts are due by the end of February, with fine-tuning to follow in March.

## Topic Schedule 2026  &  Future Business
DM & NM discussed the future topics scheduled for 2026, including the Annual project review, tech talks and the TAC Goal topics. 

## Any Other Business

Attestation SIG Repository Relocation: MB discussed moving the Attestation SIG repository under the main CCC GitHub organization to comply with Linux Foundation rules. MB will investigate permissions with Renu/Riaan and coordinate the migration with Keith Moyer.
ANSSI Paper Feedback: There was a discussion regarding a response to an ANSSI paper on confidential computing. The TAC agreed a full rebuttal is not necessary. Instead, the CCC should frame a response acknowledging the paper's valid points regarding shared responsibility in confidential computing environments. Roman Zhukov will be included in the next meeting to ensure his involvement. 
Attestation Verification Services (AVS) Overview: MB presented a "mind dump" on AVS, covering policy management, delegation, and complex trust relationships. NM warned against the CCC creating a centralised AVS, citing anti-competitive concerns. Mingshen Sun suggested exploring Web3/decentralised technologies for consensus. Ofir Azoulay-Rozanes raised concerns about the effectiveness of software measurements in closed systems where code isn't visible. [Slide link](./AVS%20choices.pdf)


## Future Meetings 
Next meeting  February 19, 2026. NM adjourned the meeting at 08:45 am PT.





