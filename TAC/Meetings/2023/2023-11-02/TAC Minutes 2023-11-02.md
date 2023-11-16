# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, November 2, 2023

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
* Arm - Nathaniel McCallum  / Michael Lu
* Google - Cfir Cohen + / Catalin Sandu 
* Huawei - Zhipeng (Howard) Huang +
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler  / Alec Fernandez +
* Red Hat - Lily Sturmann  / Yash Mankad +

   " + " indicates attending


***Other Attendees***

* Bokdeuk Jeong (Samsung)
* Chris Ramming (VMware)
* Christian Killer (Acurast)
* Eric Voit (Cisco)
* Jethro Beekman (Fortanix)
* Jinbum Kim (Samsung)
* Kanth Ghatraju (Oracle) 
* Kevin McCarthy (Inpher)
* Manu Fontaine (Hushmesh)
* Marcela Melara (Intel)
* Mark Novak (JP Morgan Chase)
* Ofir Azoulay-Rozanes (Anjuna)
* Sangwan Kwon (Samsung)
* Sal Kimmich (GadflyAI)
* Sung Lee (VMWare)
* Talha Khan (IBM)
* Thomas Fossati (Linaro)

* Ben Sternthal (LF)
* Helen Lau (LF)
* Mike Bursell (CCC)
* Riaan Kleinhans (LF)


** Announcement on US executive order**

* Chris Ramming discussed the recent US executive order (https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/) and the call to work on privacy enhancing technologies and that the approach people take should be informed by the “US/UK prize contest”. CR went on to detail that this prize did not include hardware. CR stated that this was a negative side effect of how this contest was run. CR asked the TAC for feedback on a set of criteria (https://lists.confidentialcomputing.io/g/tac/message/1197) he has created. 


**Welcome New Community Members**

* Christian Killer’s background is in infosec. He is with Acurast.
* Riaan Kleinhans is the new PM from the LF.
* Sangwan Kwon is with Samsung Research and works on Islet.
* Sal Kimmich (they/them) often supports LF projects with security interventions. They are here to learn more.


**Meeting Minute Approval**

Dan Middleton reviewed the minutes of the last meeting.

Upon motion duly made and seconded all were in favor. It was therefore:

RESOLVED: That the minutes of the October 19, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.


** Moving To LFX Meetings **

* The TAC meeting is moving to LFX Meetings starting on November 16th.


** Action Item Review **

*  CCC response to IAB statement on Attestation
   * Jethro Beekman (JB) discussed feedback he had provided on the draft document. 
   * Yash Mankad (YM) also provided feedback and that this document might be overreaching.
   * JB went on to say that if the goal is to have IAB amend their statement then this entire document should be written with that in mind.
   * Manu Fontaine stated that we are asking them to amend but we are not requiring them to and that we need to make a positional statement. Manu encouraged folks who had alternate views to put their thoughts in writing.
   * Dan Middleton (DM) stated that we could not do a substantial redraft given the amount of time. 
   * Discussion ensued.
   * YM called out that as is, his company would not be able to formally endorse the document.
   * DM asked Yash to think about what would need to change.
        
* ONCD RFI Response
   * Approved by board over weekend

* rust-spdm mentor
   * DM called out a potential issue with the mentor model and projects and that he would be filing an issue for discussion.

* Outreach TAC Sync
   * DM and Kate decided to meet 1:1 and will provide an update in the next TAC meeting.

* Cross-project meeting survey
   * Lily will present on 11/16 or 11/30.

* DM called for a vote on approving the CCC Response to IAB statement on Attestation. Google seconded and voted in favor. Huawei  voted in favor. Intel voted in favor. Microsoft voted in favor via email. Redhat abstained. Microsoft alternate voted in favor. With four votes in favor and one abstention the motion passed. 



** Islet Project Presentation - Bokdeuk Jeong **

* Link to slides: https://drive.google.com/file/d/1TdWsTHWMawDO4V36j6XgjmkpCcJ1CiNZ/view?usp=drive_link
* For physical attack comments (on ISLET)
* ARM CCA consists of two different things, (1) RMM for CPU (similar to other CCs), (2) HES (similar to HSM)
* And ARM CCA recommends storing security keys in HES (dedicated security element).
* So, the one way to measure how it's secure against physical attacks is to look at what's going to be in HES (dedicated chip)


** Attribute-Based Integrity and Trust For the Software Supply Chain - Marcela Melara (Intel) **

* Link to slides: https://drive.google.com/file/d/1Tcse1s8-QrfAvKJxpKEpyUjWBxJ5gHVh/view?usp=drive_link
* Mike Bursell asked DM to put Marcela in touch with Kate George so she can possibly speak at conferences.


Next meeting November 16, 2023

Meeting adjourned at 9:03 am PT