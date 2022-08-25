# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, August 11, 2022

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
* Dave Thaler (DT) opened the call at 7:05am PT
* DT welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation 
* Helen Lau (HL) captured the meeting minutes
* DT reviewed the agenda and asked for any additions

### Roll Call / Attendance
#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Hongliang Tian (Tate) 
* **Arm** - Thomas Fossati / Michael Lu
* **Google** - Cfir Cohen * / Catalin Sandu
* **Huawei** - Zhipeng (Howard) Huang 
* **Intel** - Dan Middleton * / Simon Johnson
* **Meta** - Eric Northup / Shankaran Gnanashanmugam
* **Microsoft** - Dave Thaler (TAC chair) *
* **Red Hat** - Lily Sturmann / Dimitrios Pendarakis

" * " indicates attending

#### Other Attendees
* Alec Fernandez (Microsoft)
* Ananya Garg (Microsoft)
* Boris Bokun (Ultraviolet)
* Catalin Sandu (Google)
* Drasko Draskovic (Ultraviolet)
* Helene Khaykovich (JP Morgan Chase)
* Ionut Mihalcea (Arm)
* Jethro Beekman (Fortanix)
* Mark F. Novak (JP Morgan Chase)
* Matthieu Legre (Cysec)
* Mike Bursell (Profian)
* Mona Vij (Intel)
* Penglin Yang (China Mobile)
* Shalom Shefa (Cisco)
* Simon Frost (Arm)
* Xinxin Fan (Iotex)
* Helen Lau (Linux Foundation)

The TAC would like to announce 2 new representatives from Google, welcome Cfir Cohen and Catalin Sandu!

### Meeting minute approvals
**Proposed:** That the minutes of the [July 14, 2022](../2022-07-14/TAC_Minutes-2022-07-14.md) meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was not reached and the minutes were not approved by the voting members of the TAC
 
### Open Action Items
1. [Stephen] Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
(Please report back that project maintainers have been made aware of the training, and have been asked to take it.)
1. [Mentors] Mentors to reach out to the project for getting the maintainers interest for involvement in Common Test Infrastructure
1. [KT] to set up a meeting to define scope and technical requirements with LF IT, Dave T, Dan M, Alec F, Nick V (LF IT ready, just need a time per email)
1. [Kurt/Helen] work with Outreach for setting up a first draft of the CCC wikipedia page - (Outreach agenda item)
1. [Mark N, Thomas F, Naveen C, Steve VL, Eric N] governance subgroup - collaborating on the governance topic, SIG formation and status update requested (Done)
1. [Mentors] Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done - Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181)
1. [Mentors/Kurt] to collect questions for determining interest in creating an "Infrastructure" slack channel for discussing best practices, Kurt to send reminder email July 21st (Done, no response)

### Completed Action Items
1. [Helen] initiate email to board to vote on OSTP doc after MV comes back with edits (Done)

### SIG Charter
* Mark Novak (MN) presented the Governance SIG progress report
* Created a charter document, PDF sent to HL for distribution 

	**ACTION**: HL to distribute to TAC (Done)

* Two goals of the SIG:
	* Support for creation of effective regulatory frameworks
	* Create repeatable patterns (not code), recommendations around tooling

* 7-step process
	* Articulate desired state of the system
	* Measure actual state of the system
	* Compare against desired state
	* Respond by restoring desired state
	* Test trigger undesirable states
	* Document all steps and results above
	* Present to authorized/interested parties
 
* Support for Regulatory Frameworks
	* 5 constituencies
		* Silicon vendors
		* Cloud providers
		* ISVs
		* Regulated Consumers
		* Regulators
			* The regulator MN is trying to bring in works with regulators around the world and is not part of a regulatory agency
 
* Patterns and Tooling
	* This is a work in progress over the next few months

* Questions about possibly changing the name from Governance 
* MN wants to call for a vote at the next meeting
	* Create a mailing list, repository if vote passes
	* TAC to please review the document before the meeting

### Finalize Common Terminology whitepaper for LF CS
* Dan Middleton (DM) wants to add DRAFT to the title as the draft isn’t final yet
* The table doesn’t match the definitions Open question: what would marketing people use other than Confidential VM?
* Alec Fernandez and Ananya Garg are collaborating and will provide suggestions soon
* A question was raised about whether or not a consensus will be reached with the terminology
* DT said Microsoft Azure is close to reaching a marketing term definition, but would like to hear from more organizations
* Mona Vij (MV) doesn’t agree with the definition of confidential container in the packaging model, This is still up for discussion
* DT reviewed why the document needs to stay focused on maintaining the CCC brand, Discussion ensued
* DT reviewed open issues, asked for volunteers

	**ACTION:** HL add Penglin (GitHub ID: PenglinYang) and Alec Fernandez (GitHub ID: AlecFernandez) And Ananya Garg (GitHub ID: angarg05) as assignee with Dan Middleton on Issue #125 (Done)

### TEEP Use case for Confidential Computing in Network
* Penglin Yang discussed status, asked to please comment
* DT reviewed history

###Testing Hardware 
* Enarx seeking to increase the project test budget to $10K for hardware, vote over email - quorum was not reached, didn’t vote
* Each project can use $7500 as approved in the budget

### Common Test Infrastructure
* DT reviewed, deferred to the next meeting

### Outreach
* DT reviewed past TAC Tech Talks, deferred to the next meeting
* DT reviewed tentative talk topics
* MV discussed NSF - New center for Distributed Confidential Computing
	* https://www.nsf.gov/awardsearch/showAward?AWD_ID=2029543
	* MV asked if CCC can help fund this effort, open source
	* DT suggested the new center program managers to present to the TAC
	* MV to invite them to present some time in September

### Any other business
* **ACTION**: HL add Catalin to Slack and link to YouTube (Done)

DT adjourned the meeting at 9:26 am
