# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, June 16, 2022

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
Dave Thaler (DT) opened the call at 7:05am PT. He welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.

DT reviewed the agenda and asked for any additions.

Eric Voit (EV) brought up that Gramine had asked LF Creative Services to redo their website, and they were quoted $5K. They are not pursuing the redo because they feel that this cost is too high. The TAC had approved $1K. 

### Roll Call / Attendance

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano *
* **Ant Group** - Hongliang Tian (Tate)
* **Arm** - Thomas Fossati * / Michael Lu
* **Google** - Iulia Ion
* **Huawei** - Zhipeng (Howard) Huang
* **Intel** - Dan Middleton * / Simon Johnson
* **Meta** - Eric Northup * / Shankaran Gnanashanmugam
* **Microsoft** - Dave Thaler (TAC chair) *
* **Red Hat** - Lily Sturmann * / Dimitrios Pendarakis

" * " indicates attending

#### Other Attendees
* Eric Voit (Cisco)
* Mike Bursell (Profian)
* Alec Fernandez (Microsoft)
* Matthieu Legre (Cysec)
* Mark Novak (JP Morgan Chase)
* Jethro Beekman (Fortanix)
* Ravi Sahita (Rivos)
* Xinxin Fan (Iotex.io)
* Henk Birkholz (Fraunhofer)
* Penglin Yang (China Mobile)
* Naveen Cherukuri (NVIDIA)
* Vikas Bhatia (Microsoft)
* Steve Van Lare (Anjuna)
* Mark Novak (JP Morgan Chase)
* Simonn Johnson (Intel)
* Suhas Hegde (Ruby Protocol)
* Ionut Mihalcea (Arm)
* Kurt Taylor (Linux Foundation)


### Meeting minute approvals
#### Approved by voting members

**Proposed:** That the minutes of the [April 21, 2022](../2022-04-21/TAC_Minutes-2022-04-21.pdf), [May 19, 2022](../2022-05-19/TAC_Minutes-2022-05-19.pdf) and [June 2, 2022](../2022-06-02/TAC_Minutes-2022-06-02.pdf) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was reached and all the minutes were approved (June 2nd with link included in PR comment). 
 
#### Pending approval
* None

### TAC Tech Talks
* None

### Open Action Items
1. [Stephen] Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
 * Please report back that project maintainers have been made aware of the training, and have been asked to take it.
2. [Mentors] Mentors to reach out to the project for getting the maintainers involved in Common Test Infrastructure
3. [Thomas F] Update GitHub with Veraison charter (Done, in Veraison/community repo)
4. [Mike Bursell] Wikipedia update needed - Trusted Computing wiki page (Done)
5. [Kurt/Helen] work with Outreach for setting up a first draft of the Confidential Computing wikipedia page
6. [Mark N, Thomas F, Naveen C, Steve VL, Eric N] governance subgroup - collaborating on the governance topic, SIG formation and status update requested at June 30 meeting
7. [Mentors/Kurt] Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done - Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181)
8. [Kurt] to set up a meeting to define scope and technical requirements with LF IT, Dave T, Dan M, Alec F, Nick V
9. [Mentors] to collect questions for determining interest in creating an "Infrastructure" slack channel for discussing best practices

### Completed Action Items
1. [Kurt] to have LFCS proceed with draft conversion and formatting of white paper PDF (Done)
2. [Kurt] to take feature request to security scanning team to support Rust language
3. [Kurt] to help Dave find discussion on governance subgroup of people in order to get an update on what they have completed (Done)

### Common Test Infrastructure
 * Kurt Taylor (KT) - reported the status, need to set up meeting with LF IT for scope and technical details

### Build Infrastructure Communication 
 * Eric Voit (EV) - Asked about further interest in sharing build environment best practices, better build environment communication, DT suggested a slack channel, EV noted it would need initial content to jump start it
 * DT - asked for next steps, whether to create a slack channel, EV questions for mentor to see if anyone cares first, mentors to post questions to the list,
 * KT will create a slack channel "Infrastructure", only after mentor feedback

### Future of Attestation Webinar
 * DT, Mike Bursell (MB), Lily Sturmann (LS) discussed the webinar
 * LS asked for suggestions on panel questions and if anyone wanted to plug the Attestation SIG

### Outreach update
* DT overview, no additional items

### Common terminology
 * MB - updated on the Governing Board's high praise for creating the white paper 
 * KT - asked for status on the June 7th email thread, EV assured that the thread was addressed in PRs on the comments
 * DT and EV directed discussion on terminology needing clarification
 * KT agreed to take the document back to the LF CS when corrections are complete
 * Penglin Yang (PY) noted that the draft sent in email (June 14th) needed to be discussed at the next meeting

### OSTP Request for Information
* DT - talked about the OSTP request, Governing Board would like to respond, Outreach and TAC to put response into a document to be sent out on July 8, discuss draft at the next meeting June 30th
* KT - noted that there is a document to put the response into [Response document](https://docs.google.com/document/d/1WdOGu2ZPpoIfpcQW7Vs_HCXM14X8CLuAcc4h_j5o4tw/edit)
* MB - volunteered to put in an initial response
* DT - shared guidance on where to focus based on his experience

### Any other business
* DT reviewed upcoming presentations
  * Enclave device blueprints for Confidential Computing at the edge - June 30
  
DT closed the call at 9:02am PT.
