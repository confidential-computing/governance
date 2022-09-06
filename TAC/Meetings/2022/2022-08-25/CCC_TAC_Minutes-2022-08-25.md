# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, August 25, 2022

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)
* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io) ([ical](https://calendar.google.com/calendar/ical/c_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics), [Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com))
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
* Dave Thaler (DT) opened the call at 7:04am PT
* DT Welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation 
* Kurt Taylor (KT) captured the meeting minutes
* DT reviewed the agenda and asked for any additions

### Roll Call / Attendance
#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Hongliang Tian (Tate) 
* **Arm** - Thomas Fossati * / Michael Lu
* **Google** - Cfir Cohen * / Catalin Sandu
* **Huawei** - Zhipeng (Howard) Huang *
* **Intel** - Dan Middleton * / Simon Johnson
* **Meta** - Eric Northup * / Shankaran Gnanashanmugam
* **Microsoft** - Dave Thaler (TAC chair) *
* **Red Hat** - Lily Sturmann * / Dimitrios Pendarakis

" * " indicates attending

#### Other Attendees
* Alec Fernandez (Microsoft)
* Ben Fischer (Red Hat)
* Graham Bury (Microsoft)
* Ananya Garg (Microsoft)
* Henk Birkholz (Fraunhofer)
* Nick Vidal (Profian)
* Drasko Draskovic (Ultraviolet)
* Mona Vij (Intel)
* Jethro Beekman (Fortanix)
* Kurt Taylor (Linux Foundation)

### Meeting minute approvals
**Proposed:** That the minutes of the [July 14, 2022](../2022-07-14/TAC_Minutes-2022-07-14.md) and [August 11, 2022](../2022-08-11/TAC_Minutes-2022-08-11.md) meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was reached and the minutes were approved by the voting members of the TAC, with the changes listed in the reviews. Lily Sturmann (LS) and Thomas Fossati (TF) abstained.
 
### Open Action Items
1. [Stephen] Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
(Please report back that Keystone has been made aware of the training, and have been asked to take it.) 
	* LS appointed to be Co-mentor for Keystone
	* ***ACTION*** - KT to get the maintainer's email address for LS
2. [Mentors] Mentors to reach out to the project for getting the maintainers interest for involvement in Common Test Infrastructure
1. [KT] to set up a meeting to define scope and technical requirements with LF IT, Dave T, Dan M, Alec F, Nick V (LF IT ready, just need a time per email)
1. [Kurt/Helen] work with Outreach for setting up a first draft of the CCC wikipedia page - (Outreach agenda item)
1. [Mark N, Thomas F, Naveen C, Steve VL, Eric N] governance subgroup - collaborating on the governance topic, SIG formation and status update requested (Done)
1. [Mentors] Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done - Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181)(Open Enclave complete)
1. [Mentors/Kurt] to collect questions for determining interest in creating an "Infrastructure" slack channel for discussing best practices, Kurt to send reminder email July 21st (Done, no response)
2. [Dan] Resolve scheduling for next Tac Tech Talk, maybe shift to Sept 8th

### Completed Action Items
1. [Helen] initiate email to board to vote on OSTP doc after MV comes back with edits (Done)

### Governance SIG Proposal
* Mark Novak (MN) was not available, DT reviewed the proposal for a vote, allowing everyone attending to read and comment
* TF asked about regulators, DT clarified
* Eric Northrup (EN) shared latest version of the document
* Alec Fernandez (AF) noted that the workgroup had signed off on the latest document being reviewed
* There were questions on the definition of evidence, review of meeting notes, discussion ensued
* DT asked for a vote, DT conducted a role call vote 
* ***APPROVED***: Governance SIG approved, Mark Novak appointed as Chair

### Common Terminology whitepaper for LF CS
* DT reviewed PRs against the whitepaper
* PRs from Dan Middleton (DM)
	* Add DRAFT to the title as the draft isn’t final yet (merged)
	* Redraft prerequisites as attestation (merged, with comments)
* AF and Ananya Garg (AG) presented their work to correct contradiction of terms, discussion ensued
  * AF to submit a PR with presentation
* Discussion to continue next meeting

### Testing Hardware 
* Deferred to the next meeting

### Common Test Infrastructure
* Deferred to the next meeting

DT adjourned the meeting at 9:06 am
