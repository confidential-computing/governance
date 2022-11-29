# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, November 17, 2022

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055)] (pw: 43690)

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

   * Dave Thaler (DT) opened the call at 7:05am PT

   * DT welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation

   * Kurt Taylor (KT) captured the meeting minutes

   * DT reviewed and modified the agenda to fit time restrictions

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

   * Accenture - Giuseppe Giordano

   * Ant Group - Hongliang Tian (Tate) +

   * Arm - Thomas Fossati + / Michael Lu

   * Google - Cfir Cohen / Catalin Sandu

   * Huawei - Zhipeng (Howard) Huang +

   * Intel - Dan Middleton + / Simon Johnson

   * Meta - Eric Northup / Shankaran Gnanashanmugam

   * Microsoft - Dave Thaler (TAC chair) +

   * Red Hat - Lily Sturmann + / Dimitrios Pendarakis

   " + " indicates attending

***Other Attendees***

   * Mike Bursell (Profian)

   * Jethro Beekman (Fortanix)

   * Alec Fernandez (Microsoft)

   * Ben Fischer (Red Hat)

   * Bobbie Chen (Anjuna)

   * Hannes Tschofenig (Arm)

   * Nick Vidal (Profian)

   * Alec (Unknown)

   * Kurt Taylor (Linux Foundation)

**Meeting Minute Approval**

Proposed: That the minutes of the November 3, 2022 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

   * Quorum was reached and the minutes were approved by the voting members of the TAC.

**Action Item Review**

   * DT and KT Reviewed the action items

**Terminology Whitepaper**
   
   * DT discussed the definition changes in the FAQ and the action needed in the revision of the whitepapers

   ***ACTION*** [Kurt] to direct the LF Creative to update revision date and version number for the TAC and Outreach whitepapers to reflect the definition change
   
   * DT reviewed [Issue #136](https://github.com/confidential-computing/governance/issues/136) and [PR #144](https://github.com/confidential-computing/governance/pull/144) to see if this PR was sufficient to close the issue, discussion ensued

   ***ACTION*** [DT] to make a one-line PR for the use of the term "confidential"
   
   * DT reviewed [PR #134](https://github.com/confidential-computing/governance/pull/134) DT, Mike Bursell (MB), Dan Middleton (DM) and Eric Voit (EV) discussed

   ***ACTION*** [Ben Fischer] to follow up with the Outreach committee for review of both whitepapers, and LF Creative to export in markdown
   
**IETF Hackathon**

* Thomas Fossati (TF) reported on the IETF Hackathon
* Day and a half in duration, participated with the Veraison project
* End-to-end demo of the attested TLS attestation spec, made great progress
* Evangelized CCC to many participants
* Next IETF hackathons, Japan and July in San Francisco

**Occlum Annual Report**
 
 * Hongliang Tian (Tate) (HT) presented the annual report
 * Project overview, Github metrics, basic functional operation
 * Launching version 1.0 by the end of the year
 * DT asked about needs for test infrastructure
 * VMs rented on the Alibaba cloud, DT asked for actual cost so the budgeted funds could cover it
 * HT commented that on the SGX enabled VMs, might be some requirements for the Linux version
 * Nick Vidal (NV) and HT will discuss the requirements and determine if there will be a cost savings for combining the test infrastructure for Enarx and Occlum (less than 10K per project)
 * HT discussed the need for a new mentor for the project, DT asked for a volunteer

 ***ACTION*** [Kurt] agenda item - follow up on the next TAC meeting for the need for a mentor for the Occlum project
 
 * HT volunteered to mentor the project, to confirm at the next meeting

**Budget proposal** 

 * DT discussed the proposed budget, reviewed with the Governing Board, approved by the end of the year

**Election Summary**

 * DM will become the new TAC chair, starting the role Nov 29th
 * DT to remain active in the TAC to ease transition

**EUAC update**

* Richard Searle (RS) reviewed the CCC Projects Day virtual event February 16, 2023
  * CCC will be socialized at FOSDEM February 4, 2023, also informal social event for the attendees
  * Need: Project logos for stickers, promote in CCC project communities, confirm a presenter and moderator for the event, confirm any project representation at FOSDEM - please confirm by December 5th, information will follow via email
* Looking at sponsoring a second event later in the year, possibly with the GRC SIG

**Outreach Update**

 * Ben Fischer (BF) discussed the potential use of a landscape (similar to CNCF) to map the technical stack, representing all the projects, from more of a marketing standpoint
 * Asking for volunteers to describe where the projects might be in terms of capabilities
 * DT summarized TAC previous work in this area, early briefing slide deck, DM shared previous aspirational work that started to show project categories

Meeting adjourned at 9:01 am PT
