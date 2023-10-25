# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*


### Meeting details

**Date**: Thursday, October 19, 2023

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
* Ben Sternthal (BS) and Helen Lau (HL) assisted with the meeting minutes
* DM reviewed the agenda


### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*


* Accenture - Giuseppe Giordano 
* Arm - Nathaniel McCallum + / Michael Lu
* Google - Cfir Cohen  / Catalin Sandu +
* Huawei - Zhipeng (Howard) Huang 
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler + / Alec Fernandez +
* Red Hat - Lily Sturmann  / Yash Mankad +

   " + " indicates attending


***Other Attendees***

* Aditya Gurajada (VMWare)
* Bokdeuk Jeong (Samsung)
* Chris Ramming (VMware)
* Drasko Draskovic (Ultraviolet)
* Eric Voit (Cisco)
* Henk Birkholz (Fraunhofer Institute)
* Ionut Mihalcea (Arm)
* John Manferdelli (VMWare)
* Kanth Ghatraju (Oracle) 
* Leonardo Garcia (Linaro)
* Marc Meunier (Arm)
* Mark Novak (JP Morgan Chase)
* Ofir Azoulay-Rozanes (Anjuna)
* Shalom Shefa (NVIDIA)
* Ye Li (VMware)

* Ben Sternthal (LF)
* Helen Lau (LF)
* Mike Bursell (CCC)


**Meeting Minute Approval**

DM reviewed the minutes of the last meeting.

Upon motion duly made and seconded all were in favor. It was therefore:

RESOLVED: That the minutes of the October 5, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.


** Action Item Review **

* Chris Ramming (CR) volunteered to create a draft (https://docs.google.com/document/d/1VkPfJSyUciDaFJGeRLf1jPizV9Tp57N9OYpI82a4xu0/edit) of a IAB response at the last Attestation meeting. 
* Dave Thaler’s (DT) opinion is that the IAB response should come from the TAC or CCC (GB). If it comes from the GB, it would require board approval. DT stated that the response is from the Attestation SIG’s perspective and is ready for TAC review. Dan Middleton suggested that this be reviewed in the board meeting next week. DT agreed with the goal of sending this out on November 4th. 
* Henk Birkholz (HB) shared the following links, (https://csrc.nist.gov/glossary/term/attestation, https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity/software-supply-chain-security-guidance-2), and discussed the definitions of “Attestation” according to NIST. HB urged the team to not use the term Attestation without an accompanying clarification/qualification due to the different definitions of the term. 
* Mike Bursell (MB): NIST doesn’t cross check definitions from different organizations.
* CR brought up his concerns with the definitions of appraisal vs certification. Discussion ensued. MB mentioned that we do have a terminology document and that final definitions should go there.
* DM urged TAC voting members to vote on the RFI response as there is a governing board meeting on Monday, October 23.
* DM discussed the project list and the role of mentors. MB expressed concern around scaling projects and mentors. DT pointed out that mentors do not have to be TAC members, and that they can be contributors. DT suggested that mentors can also be a community manager.
* MB brought up that the CCC is looking for a Technical Community Architect to be the glue and grease for the projects.


*** Action item: Yash Mankad will follow up with Lily to see if the action item is to get maintainers to respond to the survey and meet. ***


** Certifier Framework Project Proposal **

* John Manferdelli mentioned the corporate contributions to the project and invited other folks to join. DT asked for a review on the proposal and charter. Discussion ensued.
* Update the adopted date on the technical charter after the governing board approves.
* DT motioned to approve Certifier Framework Project.
* Results: Google: Yes. Intel: Yes. Microsoft: Yes. Red Hat: Abstain. Arm: Yes.
* Next step: legal review then goes to the governing board for approval.


** CCC Response to IAB Statement on Attestation**

* DT agrees with Henk that both definitions should be included and which definition the CCC agrees with. CR suggested adding it as a footnote. DT thinks that Henk would want it as a paragraph.

*** Action item: DM will send out a vote to the TAC mailing list and bring it to the governing board on Monday, October 23. ***


** 2024 TAC Objectives**

* Working doc: https://docs.google.com/document/d/1l5ekwOC0KhVwmBebaR9WHlFoCrM6mQEQolMo84-4kkk/edit
* MB suggested that there should be cross committee collaboration as well as cross project collaboration.
* MB encouraged TAC attendees to go to your premier board rep and for general members go to your general member rep to align on objectives
* DM asked the voting members for their opinion on what their highest priority is for 2024.
* Alec Fernandez mentioned that outreach is the highest priority. Success depends on awareness of confidential computing. It is apparent when working in the GRC SIG that there isn’t enough awareness of confidential computing.
* Catalin Sandu would like to prioritize improving linux kernel upstreaming.
* Yash Mankad would like to see how the projects that the CCC have approved fill in the gaps.
* Nathaniel McCallum would like to figure out how to strengthen our security stance and endorsement structure.
* DM put owners on the priority list. Owners will be responsible for crafting the language and list KPI’s/measurable outcomes.
* Alec Fernandez will ask the GRC SIG to come up with measurable outcomes for informing regulators / compliance organizations.


** TAC Budget**

* DM opened up the discussion to the group to see if there are additional asks for the 2024 budget.
* DM intends to go to the board with a flat 2024 budget proposal, the same as the 2023 budget proposal.


** Next Agenda**

* Samsung will send in a Project proposal (Islet) to the TAC mailing list for review.


Next meeting November 2, 2023

Meeting adjourned at 8:59 am PT