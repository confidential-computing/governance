# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, July 13, 2023

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
* Kurt Taylor (KT) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano 
* Arm - Thomas Fossati + / Michael Lu
* Google - Cfir Cohen / Catalin Sandu 
* Huawei - Zhipeng (Howard) Huang 
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler +
* Red Hat - Lily Sturmann / Yash Mankad +

   " + " indicates attending

***Other Attendees***

* Isaac Chute (RISC-V)
* Ofir Azoulay-Rozanes (Anjuna)
* Richard Zak (Enarx, Booz Allen)
* Leonardo Garcia (Linaro)
* Pawan Khandavilli (Microsoft)
* Mark Novak (JP Morgan Chase)
* Drasko Draskovic (Ultraviolet)
* Eric Voit (Cisco)
* Henk Birkholz (Fraunhofer Institute)
* Alec Fernandez (Microsoft)
* Ramesh Madhira (Qualcomm)
* Sudish Mogli (BeeKeeperAI)
* Hesham ElBakoury (Nortel)
* Mike Bursell (CCC)
* Kurt Taylor (LF)
* Helen Lau (LF)


**Meeting Minute Approval**

Proposed: That the minutes of the June 15, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

* DM reviewed the prior meeting minutes
* Quorum was reached and the minutes were approved by the voting members of the TAC


**2023 TAC Goals**

* DM reviewed the current state of the TAC goals
* Project Progression
   * DM discussed the PRs for project progression stages
   * DM asked for additional thoughts on the proposal for removing the Graduation stage
   * DT asked about renaming incubation and proposed that it be handled with a new PR instead of delaying these being resolved
   * DM asked for a vote to approve the removal of Graduation stage
      * 5 voting members had already approved the PR - the proposal was approved as shown in [PR #171](https://github.com/confidential-computing/governance/pull/171)
      * [PR #170](https://github.com/confidential-computing/governance/pull/170) was then closed, with comments that the TAC chose PR #171 instead
* Cross-org / Cross SIG coordination
   * One goal was NIST, DM asked for update from Mark Novak, the GRC SIG has not made much progress yet and was looking for NIST contacts
   * Mike Bursell (MB) commented that gathering regulations that are relevant to CCC was a common topic from survey and CCS feedback, starting with the TAC
      * DT asked whether this should come from the GRC SIG, MB suggested that the TAC drive the list to initially help the GRC, discussion ensued
* DM asked for better definition of goals and deliverables for Community Education, discussion ensued
   * List of planned [Event participation](https://docs.google.com/spreadsheets/d/1DntsVhFh03bQA1CfpH0phR_Y9cZpWyd6M5gYAP5UFp0/edit?pli=1#gid=386640387)
   * DT offered to create an author list and letting [Google Scholar](https://scholar.google.com/citations?view_op=list_works&hl=en&user=QMoSURoAAAAJ&gmla=AMpAcmSQFtRlf-V1oLpmeqtI6mDuttPZCqaM-SZHYrBBU7KzxHTgZrLjW1-6K9pvIlJQ-3dBDTj74PlTX1v9Xvg7NLfQS__eqlZAwQDCgrWcpTnw8mhNEBvXHfuSig) help with "H" Factor for an author

     ***ACTION Complete*** Dave volunteered to create an author listing for Google Scholar
     https://scholar.google.com/citations?user=QMoSURoAAAAJ&hl=en
   
   * Richard Zak asked for sponsorship for DefCon, DM asked for clarification of role at the conference, for Enarx project vs CCC representation, will discuss offline


**Attestation Wikipedia Article**

* DM looking to home the effort for the new wikipedia page in either the TAC or the Attestation SIG, MB and Thomas Fossati volunteered to help
* Henk Birkholz mentioned that he was involved in the TCG Attestation Working Group as Co-Chair and volunteered to help
* Work offline in a Google doc and work via the mail list, with updates in SIG


**Other Business**

* DT asked the TAC to work on the Travel policy [PR 177](https://github.com/confidential-computing/governance/pull/177) which was edited and merged after TAC approval in the meeting

   ***ACTION*** Kurt to see if LF expense template can be shared and linked to this document


Next meeting August 10, 2023 (July 27, 2023 will be canceled)

Meeting adjourned at 8:31 am PT
