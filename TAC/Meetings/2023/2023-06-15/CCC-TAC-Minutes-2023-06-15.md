# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, June 15, 2023

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

* Dan Middleton (DM) opened the call at 7:06am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Kurt Taylor (KT) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano 
* Arm - Thomas Fossati + / Michael Lu
* Google - Cfir Cohen + / Catalin Sandu 
* Huawei - Zhipeng (Howard) Huang 
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler +
* Red Hat - Lily Sturmann + / Yash Mankad +

   " + " indicates attending

***Other Attendees***

* Mike Bursell (CCC)
* Ofir Azoulay-Rozanes (Anjuna)
* Jethro Beekman (Fortanix)
* Eric Voit (Cisco)
* Neil Vexler (Anjuna)
* Antonio Gomez (Intel)
* Leonardo Garcia (Linaro)
* Victor Lu (TikTok)
* Alec Fernandez (Microsoft)
* Henk Birkholtz (Fraunhofer Institute)
* Drasko Draskovic (Ultraviolet)
* Pawan Khandavilli (Microsoft)
* Sudish Mogli (BeeKeeperAI)
* Henk Birkholz (Fraunhofer)
* Xinxin Fan (IoTeX)
* Mona Vij (Intel)
* Kurt Taylor (LF)
* Helen Lau (LF)


**Outreach update**

* Mike Bursell discussed the upkeep of the wikipedia page - adding an attestation definition to wikipedia, seeking input from the TAC, tabled for later in the meeting


**Meeting Minute Approval**

Proposed: That the minutes of the June 1, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

* DM reviewed the prior meeting minutes
* Quorum was reached and the minutes were approved by the voting members of the TAC


**Annual Report/Update: Veraison** 

* Thomas Fossati presented the annual update
* Minimal deltas from original project proposal - URL changes and license scans, published in project repo
* Attended IETF Hackathon and Fosdem, and will attend CCS
* May use some infrastructure budget in the future
* Project feels that the sandbox progression stage still appropriate - may need multiple project stages for sub-repositories at different levels of maturity, is the stage for project as a whole or per repository, discussion ensued in the TAC
  * The discussion on potential multiple stages for a project tabled for a future meeting in the interest of time
* Completed the OpenSSF Open Source Best Practices badge, 91% score achieved
* TF discussed the technical progress of the codebase and standards work
* Good growth - from 4 up to 22 contributors, with 9 organizations participating, 552 PRs merged - split between standards and services
* Integrated with Veracruz, AttestedTLS PoC, EnactTrust, exploring Keylime
* MB asked if the goals of the project had changed over the last 12 months
  * TF noted that there was not a change in emphasis but there may be some new priorities, for example documentation
* DM asked about the large number of project repositories and if there was a map of the project services, TF discussed the layout of the repos, services should be the starting point, MB asked for an easier pathway for getting started in the project
* Antonio Gomez agreed to help with better getting-started documentation
* DM asked about collaboration - with reference to Eric and Lily inter-project collaboration group
  * TF and Eric Voit (EV) commented that Veracruz is using Veraison

**PR Review**

* DM led a PR review, DT asked about the PR for the Best Practices
DM discussed PR #90 - DT noted that there would be 2 copies of the technical charters, and suggested that they be merged

  ***ACTION*** Kurt to cleanup charters after DM merges #90 ("Projects" directory for the charters not the current "project-charters" directory in governance)
  
* DM discussed PR #176 - DT added the best practices badge to the project annual review guidelines 
* MB asked DT clarified on the policy on vote/approval


**Project Progression**

* DM discussed the PRs for project progression stages, [PR #171](https://github.com/confidential-computing/governance/pull/171) and [PR #170](https://github.com/confidential-computing/governance/pull/170)
  * Most in the meeting expressed no strong opinion - one level such as Graduation discussion, comments by Eric Voit
  * Lily Sturmann suggested 2 levels - incubation and graduation, go with most simple approach
  * MB and DT discussed project funding and whether 4 levels is actually better than 2 or even none, discussion ensued
  * MB suggested a quick poll on whether the TAC had strong feelings about stages, and if not to go with minimal governance, DM polled those in the meeting, the majority did not have a strong feeling, some commenting on agreeing with the 2 stages, DM asked for any comments to be put int he PRs before the next meeting
  * DM discussed [PR #160](https://github.com/confidential-computing/governance/pull/160) - DT clarified the 2 stages and suggested using the benefits as described in the PR
  * DT asked for clarification on the action and took the action to update the PR and create a new PR for the name change
  
  ***ACTION*** Dave to update the PRs and create a new PR for the name changes


**Tech Talk CDCC** - Fan Zhang

* Deferred to a future meeting


**Other Business**

* DM mentioned that the TAC needed to hear from the group chartered with improving the awareness of CC from the 2023 TAC Goals, maybe for upcoming topics for the agenda, MB commented that there would be some related interesting findings from the survey 

* MB brought up the attestation definition for Wikipedia, and would the TAC contribute to the writing of the page - resume effort after CCS

* DM asked about the projects day or maintainers meeting, Lily commented that there has been discussion and a report is coming soon

  ***ACTION*** Kurt to sync with Lily for kicking off a cross-project maintainer's meeting

 ***ACTION*** Kurt to see about Veracruz annual review for the next meeting, determine when the last review took place


Next meeting July 13, 2023

Meeting adjourned at 8:38 am PT
