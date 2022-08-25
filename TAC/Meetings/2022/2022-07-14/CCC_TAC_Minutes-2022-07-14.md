# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, July 14, 2022

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
Dave Thaler (DT) opened the call at 7:02am PT. He welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.

DT reviewed the agenda and asked for any additions.

### Roll Call / Attendance

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Hongliang Tian (Tate) *
* **Arm** - Thomas Fossati * / Michael Lu
* **Google** - Iulia Ion
* **Huawei** - Zhipeng (Howard) Huang *
* **Intel** - Dan Middleton * / Simon Johnson
* **Meta** - Eric Northup / Shankaran Gnanashanmugam
* **Microsoft** - Dave Thaler (TAC chair) *
* **Red Hat** - Lily Sturmann * / Dimitrios Pendarakis

" * " indicates attending

#### Other Attendees
* Alec Fernandez (Microsoft)
* Drasko Draskovic (Ultraviolet)
* Eric Voit (Cisco)
* Henk Birkholz (Fraunhofer)
* Jethro Beekman (Fortanix)
* Mark F. Novak (JP Morgan Chase)
* Matthieu Legre (Cysec)
* Naveen Cherukuri (NVIDIA)
* Nick Vidal (Profian)
* Penglin Yang (China Mobile)
* Samuel Ortiz (Rivos)
* Vikas Bhatia (Microsoft)
* Xinxin Fan (Iotex)
* Kurt Taylor (Linux Foundation)
* Helen Lau (Linux Foundation)

### Meeting minute approvals
**Proposed:** That the minutes of the [June 30, 2022](../2022-06-30/TAC_Minutes-2022-06-30.md) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was reached and the minutes were approved by the voting members of the TAC (with comments from DT merged). 
 
### Open Action Items
1. [Stephen] Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
(Please report back that project maintainers have been made aware of the training, and have been asked to take it.)
1. [Mentors] Mentors to reach out to the project for getting the maintainers involved in Common Test Infrastructure
1. [Kurt/Helen] work with Outreach for setting up a first draft of the CCC wikipedia page - (Outreach agenda item)
1. [Mark N, Thomas F, Naveen C, Steve VL, Eric N] governance subgroup - collaborating on the governance topic, SIG formation and status update requested
1. [Mentors] Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done - Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181)
1. [KT] to set up a meeting to define scope and technical requirements with LF IT, Dave T, Dan M, Alec F, Nick V (LF IT ready, just need a time per email)
1. [Mentors/Kurt] to collect questions for determining interest in creating an "Infrastructure" slack channel for discussing best practices, Kurt to send reminder email July 21st

### Completed Action Items
1. [Helen] initiate email to board to vote on OSTP doc after MV comes back with edits (Done)

### TEEP Use case for Confidential Computing in Network
* Penglin Yang discussed use cases draft document
* https://github.com/PenglinYang/teep-usecase-for-cc-in-network

### Finalize Common Terminology white paper for LF CS

* DT Discussed the open issues against the common terminology draft
* Issue https://github.com/confidential-computing/governance/issues/117
  * discussed and closed
* Issue https://github.com/confidential-computing/governance/issues/116
* Eric Voit (EV) discussed the existential question
  * Is the terminology about the technology or the packaging
  * discussion ensued - marketing terms needed, picture should change, keep packaging model terms, just add marketing terms
* Seek EUAC input for marketing terms
*  DT - goal is not to devalue the brand of Confidential Computing, 2 sets of terms, technical and marketing terms
* **ACTION**: Eric Voit (EV) to post diagram source
* **ACTION**: MN, EV and AF - Send email to EUAC to assist in definition of marketing terminology (Done)

### Testing Hardware 
* Nick Vidal discussed increasing hardware limits from $7500 to $10,000
* **ACTION**: KT to Add budget slide to next meeting agenda
* NV showed Enarx demo, seeking feedback
* Vote on budget increase at the next meeting

### Any other business
* Conflict for next meeting during IETF TEEP - cancel next meeting, will meet again in 4 weeks, Aug 11
  * TEEP meeting at IETF - https://datatracker.ietf.org/meeting/114/agenda/
  
DT closed the call at 9:01am PT.
