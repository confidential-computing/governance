# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, May 5, 2022

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)
* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io) ([ical](https://calendar.google.com/calendar/ical/c_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics), [Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com))
* **Recordings**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLmfkUJc39uMjaB_I1dYW72I44kr9QzG_B)

### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Zongmin Gu
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
Rep. Thaler opened the call at 7:05am PT. He welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.

### Roll Call / Attendance
#### Voting members
* Dave Thaler (Microsoft)
* Zhipeng (Howard) Huang (Huawei)
* Thomas Fossati (Arm)
* Dan Middleton (Intel)

#### Attendees
* Eric Voit (Cisco)
* Penglin Yang (China Mobile)
* Steve Van Lare (Anjuna)
* Mingliang Pei (Ming) (Broadcom)
* Hannes Tschofenig (Arm)
* Mark Novak (JP Morgan Chase)
* Naveen Cherukuri (NVIDIA)
* Yogesh Deshpande (Arm)
* Nick Vidal (Profian)
* Simon Johnson (Intel)

#### Also Participating  
 * None

### Meeting minute approvals
#### Approved by voting members

**Proposed:** That the minutes of the [April 07, 2022](../2022-04-07/TAC_Minutes-2022-04-07.pdf) and [April 21, 2022](../2022-04-21/TAC_Minutes-2022-04-21.pdf) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was not reached and the minutes were not approved.
 
#### Pending approval
 * None

### TAC Tech Talks
 *  IETF Trusted Execution Environment Provisioning (TEEP)
 *  Presented by - Mingliang Pei (MP), Hannes Tschofenig (HT), Dave Thaler (DT)


### Open Action Items
1. **[Stephen Walli, Dan Middleton, Aeva Black]** Develop a CoC escalation process, to be presented to TAC and governing board.
    * Dan Middleton has opened a PR for review https://github.com/confidential-computing/governance/pull/92

1. **[Mike, Eric V, Stephen, Zongmin]** Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
    * Open Enclave maintainers are close to 100% trained (Dave Thaler)
    * Veracruz lead has taken the course (Thomas Fossati).
    * Please report back that project maintainers have been made aware of the training, and have been asked to take it.

### Completed Action Items
1. **[Kurt Taylor]** Investigate prior efforts to finalize Graduated lifecycle language, and if needed file an issue to finalize Graduated lifecycle language. (Done)
   * Issue created to track [Issue #104] (https://github.com/confidential-computing/governance/issues/104)

2. **[Kurt Taylor]** Check if terminology document markdown format will work with LF Creative team and check on their timeline for completing the formatting for the whitepaper (Done)
   * Markdown is fine, timeline is 1-3 weeks, depending on length and complexity)

2. **[Kurt Taylor]** Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing GitHub bot (Done) 
    * Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181

### Project overviews


### Interns
* Dan Middleton (DM) - many new interns introduced in slack
* Nick Vidal (NV) - many people interested in Confidential Computing, Veracruz and Enarx participating in Outreachy, Veracruz selected two candidates, Enarx selected one, internships last for 3 months, Enarx interns have published articles that are getting a lot of attention, next round, maybe have interns go to the project slack channels so they will be better oriented, details in the Outreach newsletter 

### Common Test Infrastructure
 * DT - existing $15K budget for a GitHub CI/CD actually running on hardware, multiple projects could share that cost, need person to maintain that hardware, proposing LF person to maintain, asked Brian Warner (LF) and Stephan Walli (Governing Board), wondering if it would need a full person, asked for thoughts for moving this forward, proposing raising this amount
 * DM - might be good to get the maintainers involved
 
 ***ACTION*** mentors to reach out to the project for getting the maintainers involved
 
 * NV - Enarx has benefited form hiring a person, looking at hiring an intern, supports a LF person managing GitHub CI/CD

### Outreach update

* NV - Wikipedia changes, interns were intimidated, seeking another solution
* DT - reviewed changes needed, seeking a volunteer to make the changes

### Common terminology

 * DT shared the action status
 * Steve Van Lare (SVL) - led comments on the conclusion/summary discussion ensued
 * EV - state of the .md file, current on document comments
 * DT - proposed to merge the document, no objections, merged
 * EV - will add new summary as a new PR
 * DT - asked HT and MP to review
 * DM - asked about the need for DCO-like sign off for contributions to the document DT agreed on the need, question to LF
 
 ***ACTION***  Kurt to find out if there is a DCO needed for the Governance repo on GitHub [Issue #107] (https://github.com/confidential-computing/governance/issues/107)


### Any other business
* DT - Logging and Error Reporting presentation by Mike Bursell for the May 19th TAC Tech Talk, NV to confirm with Mike
* DT asked for new topics


(DT) closed the call at 8:51am PT.
