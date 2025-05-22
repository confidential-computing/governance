# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, April 03, 2025

**Time**: 7a-9a US Pacific Time

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

* Dan Middleton (DM) opened the call at 7:03 am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Renu Chauhan (RC) created meeting minutes based on the publicly available recording after the TAC meeting
* DM reviewed the agenda

### Roll Call / Attendance

A quorum was not needed

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum   / David Kaplan
* Arm - Paul Howard + 
* Google - Catherine Zhang+    / Catalin Sandu 
* Huawei - Zhipeng (Howard) Huang 
* Intel - Dan Middleton (TAC chair) +  / Simon Johnson
* Meta - Henry Wang / Kevin Hui
* Microsoft - Alec Fernandez +  
* Nvidia - Fritz Alder  
* Red Hat -  Yash Mankad   / Ram Pai 
* TikTok -  Mingshen Sun  / Yao Zhang
* Shielded technologies - Bob Blessing-Hartley + 

   " + " indicates attending

#### Other Attendees

* Bryan Kelly
* Emily Fox
* Henk Birkholz (Fraunhofer Institute)
* Hesham ElBakoury
* Jens Albers
* Leonardo Garcia
* Manu Fontaine (Hushmesh)
* Mark Novak (JP Morgan Chase)
* Muhammad Usama Sardar
* Nicolae Paladi
* Nicolas
* Ofir Azoulay-Rozanes (Anjuna)
* Phil Bladen
* Richard Zak
* Mike Bursell (CCC)
* Haitao Huang (CCC)
 

## Welcome New Community Members
Phil Bladen introduced himself

## Meeting Minute Approval & Old Business

* Meeting minutes will be approved via Github.


## Old Business

* DM reviewed the old Business covered in the previous meeting. 

### Announcements 
* TWI SIG is official! : DM mentioned that Trustworthy Workload Identity SIG have been finalized. The outcome was submitted as a Pull Request (PR) on GitHub and approved asynchronously. This approval has officially initiated the SIG's work. Mark Novak (MN) encouraged participation in the Tuesday Workload Identity SIG meetings.

* Board meeting 3/26: DM mentioned the board meeting that had taken place since the previous tech meeting. He stated that no major decisions were recalled from the board meeting. Updates regarding the TWI sig and other ongoing projects were provided and well-received by the board.

* OC3: DM raised the topic of the OC3 conference. He acknowledged that there was likely no time to discuss it within the current meeting's agenda & suggested that in a future meeting, it would be beneficial to have a recap of interesting points from the OC3 conference. He proposed an open discussion on takeaways and insights from the event & invited attendees to volunteer to provide a recap in a future meeting.

 
## Annual project updates
* Annual Project Review Enarx was presented by Richard Zak (RZ). There were some technical questions and discussions following the Enarx presentation. DM thanked RZ for his continued work on the "Enarx" project and for preparing the update. DM reminded RZ to send any relevant bills, as the consortium project funding is available for use.

## Quick Topics:  
* Project Liasion: DM initiated a discussion regarding the project liaison roles & clarified that each tech member is intended to buddy up with a project or working group. Dm added that the following four projects currently do not have assigned buddies: Enarx, Gramine, Keystone, and Occulum.DM invited Bob Blessing-Hartley (BBH) to consider becoming the liaison.BBH stated he would do a little more research to see what is appropriate.
DM further mentioned that information regarding these roles is largely captured in the governance repository and encouraged attendees to review it, acknowledging that some tribal knowledge may not yet be documented.

Nicolas (IBM) inquired about the absence of the Confidential Containers project (from the CNCF) from the current discussion table. Mike Bursell (MB) explained that Confidential Containers is part of the CNCF. The project made a deliberate decision, based on its container focus, to join the CNCF rather than the Confidential Computing Consortium (CCC). Consequently, the CCC does not have significant direct involvement with the project. MB acknowledged that individuals within the current meeting may still work on Confidential Containers.
Paul Howard(PH) mentioned that the Certifier Framework project community has requested assistance in securing funding for an internship opportunity. They have a technical proposal involving a research student from the University of Missouri. The request is for funding from the Confidential Computing Consortium (CCC) to support this mentored internship.PH, being new to the Certifier Framework project and unfamiliar with the CCC funding application process, sought guidance on how to proceed in his liaison role to support this request.
DM acknowledged the interest and the identification of a project and student. DM suggested that the CCC governance repository contains information on the funding process, although it might appear complex. He recommended that Paul Howard contact Yash Mankad or Riaan, who have more direct knowledge of this process.

* ISO Liaison: Alec Fernandez (AF) informed the group about a project proposal at ISO to create a document defining confidential computing. He added that the draft document is titled "Definitions or an introduction to confidential computing." Due to copyright restrictions, the draft cannot be circulated at this time. AF mentioned that he is initiating the formal process of establishing a liaison with ISO. The goal is to determine the appropriate entity (Linux Foundation, Joint Standards Foundation, or Confidential Computing Consortium) to hold the liaison. He also added that he is consulting with legal counsel at the Linux Foundation for guidance on the correct approach. He highlighted that the potential ways to engage with ISO include: 
Submitting a white paper for approval as an ISO standard. 
Collaborating with an existing ISO working group.
AF noted that the current ISO draft uses definitions that are primarily SGX-centric and cites work that is also heavily focused on SGX. He aims to broaden these definitions to include other confidential computing technologies like TDX and those from AMD and Arm.

* Security Baseline introduction
Emily Fox (EF) presented an introduction to the Security Baseline. The presentation generated a significant number of questions from attendees & were effectively addressed by EF. DM requested a unification of best practices, badges, and OSPS (Open Source Project Security )baseline. EF acknowledged this concern and stated it would be a priority for her team to reconcile the best practices badging system, especially as passing criteria is a requirement for many LF Foundation projects.
[Slide](./LFMS%20Baseline.pdf)
[Slide](./LFMS%20Baseline.pdf)

* Project Issues
DM mentioned the backlog of issues. The group maintains a backlog of issues, though they don't heavily rely on GitHub for agenda management. DM informed that Mark Novak opened an issue to update charter definitions. No immediate action is required.DM provided a recommendation to use a directory within the governance repository for version control of formalized documents.
Next Steps: 
 Nathaniel to accept the code owner's invitation.
 Identify the individual associated with the username "Dirk Nono".
 Ensure all SIG charters are listed in the governance repository's overview and readme.
Verify the completeness of the project listing in the Projects readme.
Technical members to review and clean up GitHub issues.

* Tech Talk  
Bryan Kelly presented a tech talk titled “Why should we trust computing hardware/firmware?” 


## Topic Schedule 2025  


## Projects

## SIGs

## Any Other Business / Topic Schedule 2025

Topics for the next meeting were discussed and added to the agenda slide.

Next meeting: April 17, 2025

The meeting was adjourned by DM at 09:05 am PT
