# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, October 6, 2022

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
   * Kurt Taylor (KT) captured the meeting minutes
   * DT reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

   * Accenture - Giuseppe Giordano
   * Ant Group - Hongliang Tian (Tate)
   * Arm - Thomas Fossati / Michael Lu
   * Google - Cfir Cohen + / Catalin Sandu
   * Huawei - Zhipeng (Howard) Huang +
   * Intel - Dan Middleton + / Simon Johnson
   * Meta - Eric Northup + / Shankaran Gnanashanmugam
   * Microsoft - Dave Thaler (TAC chair) +
   * Red Hat - Lily Sturmann  / Dimitrios Pendarakis

   " + " indicates attending

***Other Attendees***

   * Alec Fernandez (Microsoft)
   * Eric Voit (Cisco)
   * Francois-Xavier Marseille (Thales)
   * Jethro Beekman (Fortanix)
   * Matthieu Legre (Cysec)
   * Naveen Cherukuri (NVIDIA)
   * Nick Vidal (Profian)
   * Penglin Yang (China Mobile)
   * Xinxin Fan (IoTex)
   * Mark Novak (JP Morgan Chase)
   * Ahmad Atamli (NVIDIA)
   * Alec Fernandez (Microsoft)
   * Andy Dellow (Huawei UK)
   * Francois-Xavier Merseille (Thales)
   * Henk Birkholz (Fraunhofer SIT)
   * Ionut Mihalcea (ARM)
   * Suresh Sugamar (TII)
   * Ravi Sahita (Rivos)
   * Drasko Draskovic (Ultraviolet)
   * Helen Lau (Linux Foundation)
   * Kurt Taylor (Linux Foundation)

**TAC Tech Talks**

* Andy Dellow - HC / RISC-V Security
   * Capability Hardware Enhanced RISC Instructions (CHERI) https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/
   * email: security@lists.riscv.org
* Ravi Sahita - RVI Sec/TC-SIG/AP-TEE TG (Trusted Computing SIG in Application Process in Trusted Execution Environments) Task Group
   * AP-TEE specification Github - https://github.com/riscv-non-isa/riscv-ap-tee/tree/main/specification
   * Linux Plumbers discussion on AP-TEE - https://lpc.events/event/16/contributions/1167/attachments/1069/2071/LPC2022_Sahita_Conf_Comp_on_RISCV.pdf
   * Salus (TSM) Github - https://github.com/rivosinc/salus
   * Platform Security Model Specification Github - https://github.com/riscv-non-isa/riscv-platform-security-model
* ACTION: [Lily] recommendation is to make sure Keystone is participating

**Meeting Minute Approval**

Proposed: That the minutes of the September 22, 2022 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

   * Quorum was reached and the minutes were approved by the voting members of the TAC. KT to amend if there was a missing action or recommendation from the MPC presentation.

**IETF Hackathon**

* https://www.ietf.org/how/runningcode/hackathons/115-hackathon/
* Veraison project asking for 1K to cover travel
* Outreach: Not about sponsoring the event, supporting a project, TAC to decide
* Dan Middleton (DM) asked for clarification on Veraison's participation, volunteered to take the idea to the Attestation SIG
* DT proposed a change in budget to cover some approved travel expenses, same approval process as a hardware request
* PROPOSED: Projects can request up to $2k per year for travel to hackathons or conferences for open source projects to promote and/or test their project. Requests are approved by the TAC on a case by case basis.
   * Deferred due to not having quorum, will continue vote via email or the next meeting

**Common Test Infrastructure**

* Only heard back from 3 projects, only one finding it useful so far, wait to check with Occlum
* If no additional interest, defer the proposal for common test, projects can request later if needed

**Outreach Committee**

* CCC Landscape and Solutions Map - Nick Vidal (NV)
   * Like CNCF, not just landscape but solutions using services
   * DT noted that commercial offerings should not be included on the website
   * ACTION: [Kurt/Nick] add this discussion to the Governing Board agenda, Nick to start the Solutions Map discussion via email
* Wikipedia - NV discussed an edit-a-thon for creating the CCC page
   * Seeking volunteers to help define the draft - https://docs.google.com/document/d/1G-bvnXLg4l1r5mMoMRQH7a6bufwGW_7w45bKcy_zdOE/edit#heading=h.lbcyx38ifcd4
   * Wikipedia process linked in the email thread

**Common Terminology Whitepaper Working Session**

* DT reviewed the current open PRs for terminology
	* Remove confidential container term #141
	  * https://github.com/confidential-computing/governance/pull/141
	  * Closed, instead use #142
	* Fix confidential container definition #142
	  * https://github.com/confidential-computing/governance/pull/142
	  * Will merge by next meeting if no objections
	* Proposal to include attestation in definition of Confidential Computing #135
	  https://github.com/confidential-computing/governance/pull/135
	  * ACTION: [Kurt] add this to Governing Board agenda
	* Narrow list of example technologies #140
	  * https://github.com/confidential-computing/governance/pull/140
	  * Will merge by next meeting if no objections

**Election Timeline**

* DT reviewed the election timeline
	* Nominations Nov 4th
	* Chair and Vice Chair election, consider nominating

**Other Business**

   * Next meeting October 20th - No Tech Talk
   * DeftT Protocol Tech Talk proposed, pending date
   * DM would like to hear about more new project proposals

Meeting adjourned 9:01 am PT
