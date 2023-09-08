# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, September 7, 2023

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)

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

* Dan Middleton (DM) opened the call at 7:04am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Helen Lau (HL) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano 
* Arm - Nathaniel McCallum + / Michael Lu
* Google - Cfir Cohen + / Catalin Sandu 
* Huawei - Zhipeng (Howard) Huang 
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler + / Alec Fernandez  
* Red Hat - Lily Sturmann + / Yash Mankad 

   " + " indicates attending

***Other Attendees***

* Chris Ramming (VMware)
* Drasko Draskovic (Ultraviolet)
* Eric Voit (Cisco)
* Hesham ElBakoury (Nortel)
* Jethro Beekman (Fortanix)
* Jorg Rodel (SUSE)
* Kanth Ghatraju (Oracle) 
* Kevin McCarthy (Inpher)
* Leonardo Garcia (Linaro)
* Manu Fontaine (Hushmesh)
* Ofir Azoulay-Rozanes (Anjuna)
* Samuel Ortiz (Rivos)
* Simon Frost (Arm)
* Sung Lee (VMWare)
* Suyog Pathak (Oracle)
* Thomas Fossati (Linaro)
* Ye Li (VMware)

* Ben Sternthal (LF)
* Helen Lau (LF)
* Mike Bursell (CCC)


**Welcome New Community Members**
Manu Fontaine (Hushmesh) introduced himself a second time.
Sung Lee (VMWare) is interested in donating a project to the CCC.
Welcome Kanth Ghatraju (Oracle).
Welcome Kevin McCarthy (Inpher).

**Meeting Minute Approval**

Proposed: That the minutes of the August 24, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.


**Cross-Project goal updates**

* Lily Sturmann (LS) gave an update on cross-project goals. LS and Eric Voit put together a survey and sent it to the project mentors. There has been 1 response so far. 
* LS will reach out to Ben on an action item that Kurt marked as done.


**Tech Talk: MPC/FL + TEEs; Kevin McCarthy (Inpher)**

* Kevin McCarthy (KM) presented his talk on MPC/FL + TEE and FHE.
* Inpher specializes in the cryptographic space.
* Organizations are asking for hybrid PET solutions.
* Attention to GRC SIG: https://iabtechlab.com/working-groups/privacy-enhancing-technologies-working-group/
* Question: Why is CC not enough? Technology lives with what clients already use: Azure, AWS, etc. Inpher works with their clients strategy.
* Kevin McCarthy will put together a list of regulators to send to Mike Bursell.
* Comment: CC should always be included with other PETs.
* CC hasn't penetrated the market yet.
* Dave Thaler (DT) brought up that Manu posted a link in chat (https://iabtechlab.com/wp-content/uploads/2023/02/FINAL-DRAFT-PUBLIC-COMMENT-Open-Private-Join-Activation-IAB-Tech-Lab.pdf) where the CCC would disagree with the definition of TEE. DT asked KM if IAB would be willing to update the TEE definition should the CCC contact them. KB believes the IAB will update the definition. 

***Action item: Kevin McCarthy will connect IAB with Mike Bursell to request to update the their definition of TEE.***


**Rename stages per agreement in 2023-06-15 TAC meeting**

* https://github.com/confidential-computing/governance/pull/183
* DT made a proposal to include a growth plan at the first stage to get to graduation stage.
* The group agrees that this makes sense.
* MB asked if the GB should vote on the charter. DT: The TAC Chair should report it to the GB for visibility.

*** Action item for all project mentors: Update the stage for each project in the project readme***


**Project Proposal: Rust SPDM**

* Samuel Ortiz (Rivos) joins the proposal as an additional maintainer and sponsor.
* https://github.com/intel/rust-spdm
* Discussion ensues about how this project promotes confidential computing and whether/how it fits the charter.
* Quorum was lost and a vote will move to email or be scheduled for next session.


**web page updates; mentors**

* DT raised a concern on whether or not the diagram deters project submissions. Suggested to move to the current projects landing page.
* MB will work on getting a web content team together within the Outreach committee.


**CISA RFI**

* The response is due on October 9, 2023.
* RFI response will be sent to the board a week prior to the due date to review.
* Working doc: https://docs.google.com/document/d/1hEZZfsmMtBpOYkCpRTMNYFbY9_qEYK_VxMRlXhQxfEU/edit#heading=h.3pkkmtscvc8q
* TAC contributors are encouraged to get bulleted concepts into the google doc immediately. MB will be creating a first draft imminently and it will be easier to incorporate concepts at the outset rather than through revisions.

Next meeting September 21, 2023

Meeting adjourned at 8:52 am PT
