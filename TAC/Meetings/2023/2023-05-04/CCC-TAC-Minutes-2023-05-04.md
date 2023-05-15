# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, May 4, 2023

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

* Dan Middleton (DM) opened the call at 7:08am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Kurt Taylor (KT) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano 
* Arm - Thomas Fossati + / Michael Lu
* Google - Cfir Cohen + / Catalin Sandu
* Huawei - Zhipeng (Howard) Huang +
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler +
* Red Hat - Lily Sturmann  / Yash Mankad +

   " + " indicates attending

***Other Attendees***

* Mike Bursell (CCC)
* Jethro Beekman (Fortanix)
* Eric Voit (Cisco)
* Thore Sommer (Keylime)
* Jorg Rodel (SUSE)
* Vidhya Krishnan (NVIDIA)
* Alan Czeszynski (BeeKeeperAI)
* Ettore Di Giacinto (Spectro Cloud)
* John Ferlan (Red Hat)
* Tyler Fanelli (Red Hat)
* Mona Vij (Intel)
* Ofir Azoulay-Rozanes (Anjuna)
* Michal Kowalczyk (Invisible Things Lab)
* Matthieu Legre (Cysec)
* Mark Novak (JP Morgan Chase)
* Alec Fernandez (Microsoft)
* Henk Birkholz (Fraunhofer)
* Drasko Draskovic (Ultraviolet)
* Larry Dewey (AMD)
* Kurt Taylor (LF)
* Helen Lau (LF)


**CCC Executive Director Introduction**

* Mike Bursell introduced himself as the new ED for the CCC and spoke briefly about his near-term goals
  * Improving visibility at conferences
  * Increasing membership
  * Adding new projects
  * Creating a member survey

**Meeting Minute Approval**

* The meeting minutes of April 20th were discussed and the TAC agreed to come back to the approval vote later in the meeting after the discussed changes are made

  ***ACTION*** Kurt took an action to fix the errors in the Maintainer file to add Yash Mankad


**Gramine progression discussion**

* DM discussed the Gramine progression details in the [Gramine graduation petition](https://docs.google.com/document/d/1gx72Zh8fX7Zg-r7qKk19fFRC4-RXkyGGGno8KueQ4H4/edit#heading=h.lzjh6k7yo3pt)
* Dave Thaler (DT) pointed out that the TAC has never actually agreed on the graduation requirements, so the TAC cannot approve any project for graduation without first approving the graduation stage definition
* DT posted the link to the [Growth Plan document](https://github.com/confidential-computing/governance/blob/main/growth-plans.md)
* Eric Voit (EV) posted the link to the [CNCF definitions](https://www.cncf.io/projects/)
* EV commented that the stages text was initially copied from the CNCF definitions
* Mona Vij (MV) asked anyone using Gramine to notify the project and to be added to the Github page
* Discussion ensued on community participation and commit quality, more details need to be added to the graduation definition
* DT added in chat - The graduation stage requirements draft text currently says: "Have a defined governing body of at least 5 or more members (owners and core maintainers, or similar technical role), of which no more than 1/3 is affiliated with the same employer."
* DT brought up that according to the [Gramine CONTRIBUTING document](https://github.com/gramineproject/gramine/blob/master/CONTRIBUTING.rst#management-team-maintainers), Gramine does not meet the requirements for Graduation.
* DM discussed adding the recommendation for the project maintainers to take the LF training on DEI (link above)
* Michal Kowalczyk asked how does a company being funded by another company be documented? for example is the Invisible Things company different from Intel?
* DM proposed: a formal vote for Gramine to move to Incubation stage - unanimous approval from all the voting representatives attending (Thomas Fossati, Cfir Cohen, Zhipeng (Howard) Huang, Dan Middleton, Dave Thaler, Yash Mankad)


**TAC Goal Topic: Education**

* Cfir Cohen discussed the Outbound Education topic
  * At RSA conference, the speaker asked how many of the 12 people had heard of Confidential Computing, 2 people raised their hands, demonstrating the gap in Outbound Education
  * Review of White papers, blog posts
  * CCS talks planned
  * Other ideas: Mike Bursell expressed interest and volunteered to help however possible
  * Meet customers where they are - go to industry conferences that are not only security focused, discussion ensued
  * Sync with the similar efforts in the Outreach committee
  * DT asked about the "As measured by" bullets in the TAC Goal Topic slide - "We promoted" isn't "measured" per se, are there good ways to actually measure the promotion?
  * CC talked about Use cases - tie to technology offerings - also overlaps with Outreach goals
  * MV asked if we have engaged regulatory bodies, DM discussed where this is covered with interfacing with NIST and the work in the GRC Sig


**Update: Attestation SIG - Shanwei Cen, Greg Kostal, Keith Moyer - deferred to next meeting


**Meeting Minute Approval**

Proposed: That the minutes of the April 20, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

* Quorum was reached and the minutes were approved by the voting members of the TAC. 


**Tech Talk: VirTEE**

* Tyler Fanelli (TF) and Larry Dewey (LD) - [VirTEE project website](https://virtee.io/)
* Discussed libraries and tools - confidential workloads and containers
* Goal of the project - Make it easier to develop confidential virtualization, lower barriers to entry, not tied to a specific hardware architecture
* DT asked if the [KBS protocol spec](https://github.com/confidential-containers/kbs/blob/main/docs/kbs_attestation_protocol.md), have they considered submitting to the IETF RATS Working Group for review? LD agreed that would be a good discussion
* MB asked about attestation 
* Thomas Fossati asked about defining an API for interacting with verifiers, perhaps a RESTful API, TF agreed to interact with VirTEE
* LD added that they are working toward sandbox stage as a new project for the CCC
* DT asked about SEV and SMP - supported and promoting
* DM asked about CCA vs Realms
* LD mentioned that the project is active on Matrix #virtee:matrix.org

**OSS NA**

* DT asked if anyone was going to Vancouver, mentioned the eBPF talk, just Mike and Dave from TAC
* DT asked for any confidential computing talks to be posted to the TAC mailing list


**Action item review**

* DM reviewed the current state of the action items
* KT reviewed the TAC white paper PR and asked for review, DM asked to focus on wording not formatting

 ***ACTION*** Kurt to ask Outreach committee about the source for the 

* DM talked about the project progression - asked that the document be reviewed before the next meeting 
  * Project Progression - [PR #160](https://github.com/confidential-computing/governance/pull/160)
* Come back to Gramine funding
* DM discussed adding maintainers to subscribe to the security mailing list

  ***ACTION*** Kurt to resend email to TAC list for the project volunteers monitoring the security list


**Any other business**

* Next meeting May 18th, 2023
  * DM discussed presentations for the next meeting
    * TAC Goals Nick and Dan for DEI
    * Attestation SIG
    * Keylime by Thore Sommer, with TPM refresher
    * Veraison for June 1
    
    ***ACTION*** Dave to lead a short graduation stage discussion

Meeting adjourned at 9:04 am PT
