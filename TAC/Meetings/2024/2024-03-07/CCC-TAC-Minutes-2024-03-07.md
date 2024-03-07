# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, March 6, 2024

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e) 

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


#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Arm - Nathaniel McCallum +  / Michael Lu
* Google - Cfir Cohen + / Catalin Sandu 
* Huawei - Zhipeng (Howard) Huang 
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Alec Fernandez +
* Red Hat - Lily Sturmann  / Yash Mankad +
* TikTok - Mingshen Sun + / Yao Zhang

   " + " indicates attending

#### Other Attendees

* Bokdeuk Jeong
* Dayeol Lee
* Drasko Draskovic
* Frits Adler
* Hesham ElBakoury
* Kanth Ghatraju
* Kevin Hui
* Manu Foutaine
* Mark Novak
* Mingshen Sun
* Nathaniel McCallium
* Offir Azoulay-Rozanes
* Vini Jaiswal
* Wenhui Zhang


* Ben Sternthal (LF)
* Riaan Kleinhans (LF)
* Mike Bursell (LF)

## Welcome

Dan Middleton (DM) opened the call at 7:05 am and reviewed the anti trust policy.

## Agenda and Minutes

Dan Middleton (DM) reviewed the agenda for the meeting. 

### Roll Call / Attendance

Since no votes would be occurring in the meeting roll call was skipped.

## Welcome New Community Members

* Mingshen Sun from TikTok introduced themselves

## Meeting Minute Approval & Review

* Meeting minutes will be approved via Github
* DM reviewed the previous meeting minutes

## Announcements

* Riaan Kleinhans(RK) spoke to updating the website with Kernel SIG
* Fritz Alder (FA) asked if the meetings would be posted to YouTube. DM announced that, with the meeting now being hosted on the LF platform, the sessions would be recorded and uploaded.
* DM asked if there were any last-minute items related to OC3 
* DM stated that the 3/21 meeting would be during Kubecon and asked if the meeting should be canceled. 
* It was agreed that the 3/21 meeting would still occur and be a working session for Mark and that we would move the Occlum annual review. 


## Glossary

MB reviewed the rationale for creating a CCC Glossary. MB shared the document with the audience and asked that folks use suggest mode or comments when making suggestions or asking questions. MB then went on to review each definition with the TAC. Discussion ensued. 

DM asked about the outcome we are looking for. MB states that we can not come up with plain-language versions without creating the complete, proper definition first. MB suggested that the complete definition goes in the glossary/GitHub and that the plain language version goes on the website.

Alec Fernandez(AF) asked how the TAC feels about putting our definitions into Wikipedia, and he said he supports this. MB stated that some would be.

Discussion on glossary items ensued. 

AF stressed the need for real-world examples. MB stated that this was within the scope of this work and asked AF for help. Nathaniel McCallum also volunteered to assist. 

Nathaniel articulated the action item in chat as “Produce a document defining the roles of the supply chains that feeds into Confidential Computing as an aid to define terms such as Trust Anchor and Root of Trust”.

Alec articulated the action item in chat as “Alec to contact Nathaniel and Mike Bursell to deliver a hierarchy definitions necessary to introduce the concept of "Root of trust" using current commercial providers of the hardware/firmware/software that produce tools necessary to provide a hardware-based, attested root of trust and verify it”.

Offir Azoulay-Rozanes (OAR)  proposed that the group should consider who is the expected audience for the glossary work. DM pointed out that CSA is one of the intended audiences.


## Keystone Annual Review

Dayeol Lee (DL) reviewed the Keystone project's goals. DL then summarized the content of the annual review and reviewed the key milestones from the previous review. DL reviewed the current state of the annual milestones. 

DM requested clarification around the hardware root of trust. DL elaborated on the topic.
DM asked for people on the call who have access to information to help support the work. AF said he would reach out to DL.

DL asked if there were standardization efforts around remote attestation. DM stated that this was within the scope of what the Attestation SIG discusses. A technical discussion ensued. DM suggested that DL bring these topics to the Attestation SIG. AF stated that he could assist in getting a date for discussion. 

DL reviewed the goals the project will attempt to achieve in order to reach the Graduation stage. 

DM reminded DL that we have a community architect. DL mentioned that Sal had reached out about admin access to their GithHub repository. MB stated that this was a decision for the project and that Sal was employed by the Linux Foundation. DM mentioned that Sal’s goal is to help projects and that DL should feel free to reach out to them to understand more.

DL reviewed the requested budget allocation for the Keystone project. DL stated that the free tier for GitHub is currently enough but they may need additional funds for GitHub actions. DL stated that they want to purchase additional RISC-V hardware. DL then mentioned they might want video conferencing support. 


## Upcoming Calendar

DM requested that individuals accountable for TAC objectives register for a discussion session.


## Any Other Business / Schedule

Vini Jaiswal (VJ) asked if anyone could present on the recent EU policies. DM said we could solicit this content from members from CCC.  MB stated this is a complex area and encouraged folks to share back with their findings. 

Next meeting March 21, 2024

Meeting adjourned at 08:55 am PT
