# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, June 2, 2022

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
* Lily Sturmann (Red Hat)
* Dan Middleton (Intel)

#### Other Attendees
* Eric Voit (Cisco)
* Nagaraju (Intel)
* Megan Collier (Investment Group)
* Matthieu Legre (Cysec)
* Nick Vidal (Profian)
* Shalom Shefa (Cisco)
* Mark Novak (JP Morgan Chase)
* Jethro Beekman (Fortanix)
* Ravi Sahita (Rivos)
* Xinxin Fan (Iotex.io)
* Henk Birkholz (Fraunhofer)
* Thomas Hardjono (MIT)
* Penglin Yang (China Mobile)
* Hannes Tschofenig (Arm)
* Kurt Taylor (Linux Foundation)
* Helen Lau (Linux Foundation)

### Meeting minute approvals
#### Approved by voting members

**Proposed:** That the minutes of the [April 21, 2022](../2022-04-21/TAC_Minutes-2022-04-21.pdf) and [May 19, 2022](../2022-05-19/TAC_Minutes-2022-05-19.pdf) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was not reached and the minutes were not approved. 
 
#### Pending approval
 * [April 21, 2022](../2022-04-21/TAC_Minutes-2022-04-21.pdf)
 * [May 19, 2022](../2022-05-19/TAC_Minutes-2022-05-19.pdf)

### TAC Tech Talks
 *  Multi-TEE Systems: PCI-SIG WG Update
 *  Presented by - Mark Novak (MN)
 *  DT added references
  *  [RATS definition for composite devices](https://datatracker.ietf.org/doc/html/draft-ietf-rats-architecture#section-3.3)
  *  [SPDM Overview (1.1.0c)](https://www.dmtf.org/sites/default/files/standards/documents/DSP0274_1.1.0c.pdf)
  *  [SPDM Overview (preview 1.2)](https://www.dmtf.org/sites/default/files/DMTF_SPDM_1_2_Preview.pdf)
  *  [Management Component Transport Protocol (MCTP)](https://en.wikipedia.org/wiki/Management_Component_Transport_Protocol)
 *  DT asked for possible collaboration with the IETF

### Open Action Items
1. [Stephen, Zongmin] Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
 * Please report back that project maintainers have been made aware of the training, and have been asked to take it.
2. [Mentors] Mentors to reach out to the project for getting the maintainers involved in Common Test Infrastructure
3. [Thomas F/Kurt] Update GitHub with Veraison charter
4. [Mike Bursell] Wikipedia update needed - Trusted Computing wiki page
5. [Kurt] to help Dave find discussion on governance subgroup of people in order to get an update on what they have completed (Done)
6. [Mark N, Thomas F, Naveen C, Steve VL, Eric N] governance subgroup - collaborating on the governance topic, SIG formation and status update requested
7. [Kurt] to have LFCS proceed with draft conversion and formatting of white paper PDF (Done)
8. [Mentors] Code scanning via LFX Security - add projects to security for scanning with GitHub bot (Set up the bot by following these [instructions](https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181)

***ACTION*** KT to email TAC for projects to determine if they would like to enable scanning

***ACTION*** KT to take feature request to security scanning team to support Rust language

### Completed Action Items
1. **[Kurt Taylor]** Check if terminology document markdown format will work with LF Creative team and check on their timeline for completing the formatting for the white paper (Done)
   * Markdown is fine, timeline is 1-3 weeks, depending on length and complexity)

2. **[Kurt Taylor]** Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done) 
    * Projects can set up the bot and repos they want scanned by following these [instructions](https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181)

### Common Test Infrastructure
 * DT - review of status
 * DM - asked if there was immediate consumption plans, DT noted that the projects couldn't use it until there was a placeholder, something to start using and sign up for
 * DT reviewed budget approved 50K for LF setup and management, 15K for hardware

***ACTION*** KT to verify 50k estimate for LF resources for Common Test Infrastructure, set up a meeting to define technical requirements, initially SGX, DT and DM and anyone else that is interested

### Outreach update
* DM - mentioned the need to improve the project application process on the website
* NV - they are aware of that as a needed improvement
* NV - the goal is to have the website updates done before Blackhat (early August)
* DT - commented on proposed sitemap content, projects would have a dropdown menu
* NV - LF design team is very responsive and making progress
* DT - discussed the Attestation webinar, 21st of June

### Common terminology
 * DT - asked for status
 * KT - reported that the LF CS team is working on the draft, no update on the date of first draft

### Open Issues and PR's
 * DT - asked DM about [#91](https://github.com/confidential-computing/governance/pull/91), DT noted some updates needed to tac-composition.md, asked for comments on CODEOWNERS file, clarification on the process update for review reminders
   * EV - commented it is difficult to subscribe to just the components that you care about
   * DT - CODEOWNERS could be used per directory path, asked about for discussion on watch functionality vs. CODEOWNERS
   * KT - noted that maintaining a complete list of all regular attendees of the TAC meeting would be very difficult, discussion ensued
   * DT - asked if the [GitHub process](https://github.com/confidential-computing/governance/blob/main/tac-github-process.md) should be updated to not require a PR for uploading meeting artifacts

     ***ACTION***  DT and KT to propose a new process that scopes to a specific category
     
 * DT - [#92](https://github.com/confidential-computing/governance/pull/92) asked for comments of the code of conduct
 
    ***ACTION*** KT to check the Governing Board members list was correct
    
 * DT - discussed [#90](https://github.com/confidential-computing/governance/pull/90) another that DM needs to comment on
 * DT - discussed the charter Project Progression Policy stages as background for Issue [#104](https://github.com/confidential-computing/governance/issues/104), that everything in [Graduated](https://github.com/confidential-computing/governance/blob/main/project-progression-policy.md#graduation-stage) and [Emeritus](https://github.com/confidential-computing/governance/blob/main/project-progression-policy.md#emeritus-stage) has never been voted on, need to revisit and update or accept as is, low priority

### Any other business
* DT reviewed upcoming presentations
  * PCI SIG WG was presented this meeting
  * Enclave device blueprints for Confidential Computing at the edge - June 30
  * Multi-TEE systems (e.g., CPU+GPU+NIC TEEs)
	 * Trust Domains - Mike Bursell possibly July 14th
* No presentation for next meeting June 16th

* KT asked about any upcoming face to face meeting, NV said next was Blackhat 
* DT asked if others were attending IETF in Philadelphia 23 - 24, July 2022 (Saturday - Sunday)
  * DT noted there may be an opportunity to meetup at [IETF Hackathon](https://www.ietf.org/how/runningcode/hackathons/114-hackathon/)

(DT) closed the call at 9:01am PT.
