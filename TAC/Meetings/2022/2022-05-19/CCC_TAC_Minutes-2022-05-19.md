# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, May 19, 2022

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)
* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io) ([ical](https://calendar.google.com/calendar/ical/c_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics), [Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com))
* **Recordings**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLmfkUJc39uMjaB_I1dYW72I44kr9QzG_B)

### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Hongliang Tian (Tate)
* **Arm** - Thomas Fossati / Michael Lu
* **Google** - Iulia Ion
* **Huawei** - Zhipeng (Howard) Huang
* **Intel** - Dan Middleton / Simon Johnson
* **Meta** - Eric Northup / Shankaran Gnanashanmugam
* **Microsoft** - Dave Thaler (TAC chair)
* **Red Hat** - Lily Sturmann / Dimitrios Pendarakis

## Links

* **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io)
* **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io)
* **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)
* **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)
* **YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io)
* **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org)
* **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io)
* **Contact the CCC**: [confidentialcomputing.io/contact-us/](https://confidentialcomputing.io/contact-us/)

## Agenda and Minutes

### Welcome
Dave Thaler (DT) opened the call at 7:04am PT. He welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.

### Roll Call / Attendance
#### Voting members
* Dave Thaler (Microsoft)
* Zhipeng (Howard) Huang (Huawei)
* Thomas Fossati (Arm)
* Dan Middleton (Intel)
* Giuseppe Giordano (Accenture)
* Lily Sturmann (Red Hat)
* Tate Tian (Ant Group)

#### Attendees
* Eric Voit (Cisco)
* Mike Bursell (Profian)
* Steve Van Lare (Anjuna)
* Mark Novak (JP Morgan Chase)
* Simon Johnson (Intel)
* Jethro Beekman (Fortanix)
* Marc Meunier (Arm)
* Ravi Sahita (Rivos)
* Thomas Hardjono (MIT)
* Ionut Mihalcea (Arm)
* Xinxin Fan (Iotex.io)
* Kurt Taylor (Linux Foundation) 

### Meeting minute approvals
#### Approved by voting members

**Proposed:** That the minutes of the [April 07, 2022](../2022-04-07/TAC_Minutes-2022-04-07.pdf), [April 21, 2022](../2022-04-21/TAC_Minutes-2022-04-21.pdf) and [May 5, 2022](../2022-05-05/TAC_Minutes-2022-05-05.pdf) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was reached and the minutes from April 7 and May 5 were approved. The minutes from April 21 were not approved due to changes being needed.
 
#### Pending approval
 * [April 21, 2022](../2022-04-21/TAC_Minutes-2022-04-21.pdf)

### TAC Tech Talks
 *  Logging, debugging and error management in Confidential Computing
 *  Presented by - Mike Bursell (MB)
 *  Lively discussion on architecture and definitions
 *  DT asked if the TAC should do a white paper or WG, MB - based on blog post, asked for initial blog improvement, Best Practices for next step was propose

### Open Action Items
1. **[Stephen Walli, Dan Middleton, Aeva Black]** Develop a CoC escalation process, to be presented to TAC and governing board.
    * Dan Middleton has opened a PR for review https://github.com/confidential-computing/governance/pull/92

1. **[Stephen, Zongmin]** Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
    * Open Enclave maintainers are close to 100% trained (Dave Thaler)
    * Veracruz lead has taken the course (Thomas Fossati).
    * Please report back that project maintainers have been made aware of the training, and have been asked to take it.

1. **[Mentors]** Mentors to reach out to the project for getting the maintainers involved in Common Test Infrastructure

### Completed Action Items
2. **[Kurt Taylor]** Find out if there is a DCO needed for the Governance repo on GitHub [Issue #107] (https://github.com/confidential-computing/governance/issues/107) (Done)

1. **[Kurt Taylor]** Investigate prior efforts to finalize Graduated lifecycle language, and if needed file an issue to finalize Graduated lifecycle language. (Done)
   * Issue created to track [Issue #104] (https://github.com/confidential-computing/governance/issues/104)

2. **[Kurt Taylor]** Check if terminology document markdown format will work with LF Creative team and check on their timeline for completing the formatting for the white paper (Done)
   * Markdown is fine, timeline is 1-3 weeks, depending on length and complexity)

2. **[Kurt Taylor]** Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done) 
    * Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181

### Project overviews
### Common Test Infrastructure
 * DT - status, noted this topic was reviewed with the Governing Board, seeking feedback from the projects, if would be used by the projects, reviewed the budget amounts
 * DT - main cost is the LF maintainership, not test service or hardware, noted this is not a full-time job from LF
 * DT proposed that the budget be changed and approved to 50K for LF management, 15K for test hardware
 * DT PROPOSED: The TAC budget $50k out of the "Cons. IT Services" $100k line item, to allocate to LF management of Common Test Infrastructure, MB asked for clarification on the proposal from the project feedback, DT asked for input from mentors, no additional feedback provided for usage
 * DM asked for specific written proposal

***APPROVED*** The TAC budget $50k out of the "Cons. IT Services" $100k line item, to allocate to LF management of Common Test Infrastructure

### Projects Update 
#### CCC Attestation
* DT - The topic for the June webinar, a panel discussion, Ben Fischer, MB, Simon Johnson, Mark Novak (MN), DT and others suggested for panel members
* MB asked if he should resign as a co-chair of the project due to being busy, ill, etc - will continue discussion offline 

#### Veraison update
* DT - approved as an official project
* DT Project needs to be added to the website and technical charter put in GitHub repo

***ACTION*** TF to update the GitHub repo with the charter

* DT asked if Howard Huang (HH) would be willing to continue as mentor, HH agreed
* DT asked if TT could contact Zongmin Gu would still be interested in being a mentor for Occlum, TT agreed to check, also noted that Occlum would be interested in using the Common Test Infrastructure

### Outreach update

* DT noted the Panel discussion webinar was discussed in the Project update

***ACTION*** Wikipedia update needed - Trusted Computing wiki page

* DT is seeking a volunteer, MB volunteered

### Common terminology

 * DT - PR for [Conclusion](https://github.com/confidential-computing/governance/pull/108) merged, CPU changed to Processors 
 * DT - PR for [References] (https://github.com/confidential-computing/governance/pull/109) merged with changes from discussion
 * DT Draft is ready for LF Creative Services for PDF draft

***ACTION*** KT to have LFCS proceed with draft of white paper PDF

### Any other business
* DT asked for new topics for presentations
	* TF suggested  a topic - Enclave device blueprints for Confidential Computing at the edge - June 30 or later
	* Multi-TEE systems (e.g., CPU+GPU+NIC TEEs)
	  * PCI SIG WG - MN - June 2
	  * Routers - Eric Voit
	  * Trust Domains - MB

***ACTION*** KT to help DT find discussion on governance work to do, subgroup of people, or maybe a white paper, need update on what they have done, TF was one discussing, Mark talked in this meeting that DT is referring to - make sure this gets on Action item slide (Done) 

***ACTION*** (from April 7th meeting) Mark N, Thomas F, Naveen C, Steve VL, and Eric N expressed interest in collaborating on the governance topic, SIG formation and status update requested

(DT) closed the call at 9:01am PT.
