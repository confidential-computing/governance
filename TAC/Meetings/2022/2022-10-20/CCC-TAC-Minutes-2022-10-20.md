# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, October 20, 2022

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
   * Dave Thaler (DT) opened the call at 7:03am PT
   * DT welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
   * Kurt Taylor (KT) captured the meeting minutes
   * DT reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

   * Accenture - Giuseppe Giordano
   * Ant Group - Hongliang Tian (Tate)
   * Arm - Thomas Fossati + / Michael Lu
   * Google - Cfir Cohen / Catalin Sandu +
   * Huawei - Zhipeng (Howard) Huang +
   * Intel - Dan Middleton + / Simon Johnson
   * Meta - Eric Northup / Shankaran Gnanashanmugam
   * Microsoft - Dave Thaler (TAC chair) +
   * Red Hat - Lily Sturmann + / Dimitrios Pendarakis

   " + " indicates attending

***Other Attendees***

   * Ranjit Narjala (Google)
   * Alec Fernandez (Microsoft)
   * Steve Van Lare (Anjuna)
   * Richard Searle (Fortanix)
   * Johannes Kreisler (not introduced)
   * Nagaraju (Intel)
   * Naveen Cherukuri (NVIDIA)
   * Marc Meunier (Arm)
   * Eric Voit (Cisco)
   * Matthieu Legre (Cysec)
   * Xinxin Fan (IoTex)
   * Drasko Draskovic (Ultraviolet)
   * Kurt Taylor (Linux Foundation)


**Meeting Minute Approval**

Proposed: That the minutes of the October 6, 2022 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

   * Quorum was reached and the minutes were not approved by the voting members of the TAC. 

**Action Item Review**

   * DT Reviewed the action items
   * [Kurt] Capture vote on definition that was taken to the Governing Board for approval
   * [Kurt/Alec] to review and verify the recording and MPC presentation recommendation (Veracruz)
     * Thomas Fossati (TF) set up connection with Veracruz
   * DT and Dan Middleton (DM) discussed test infrastructure, whether Occlum was interested in a common or project specific test infrastructure, administered or not 
   * [Mentor/Dan/Kurt] Occlum Test needs, access to hardware or administered services, ask to cover at annual report
   * DT and Lily discussed the RISC-V Keystone introductions
   * [Helen] work with LF design to update the Technical Analysis whitepaper (section 2.1) with the new Confidential Computing definition, TAC to review draft

**Definition of Confidential Computing**

  * DT discussed the board vote for the updated definition for Confidential Computing

**Budget/Hackathon**

   * DT discussed the 2K budget per year per project and announced the vote

     **APPROVED**: Projects can request up to $2k per year for travel to hackathons or conferences for open source projects to promote and/or test their project. Requests are approved by the TAC on a case by case basis.
   
   * Process is to bring the request to the TAC, KT will take care of processing the funds
   * Areas of CCC Focus - DT discussed updates to CCC focus and goals, updates to Cross-org coordination and other technical bodies
   * DT reviewed the draft budget for 2023

**Community Development**

   * Lily Sturmann discussed meeting with Keystone, community outreach - more contributors and adopting organizations
      * Things CCC can help with, travel budget - conferences and hackathons
      * Slack channel for Keystone - DT discussed a previous meeting where project communications were discussed (OpenEnclave, Enarx) TAC can facilitate, up to the project to determine what service to use
      * Eric Voit asked for an inventory of projects messaging services, what they are currently using, DT reviewed previous discussions on project messaging requirements, suggested website mention or link of messaging service each project is using

        **ACTION**: [Kurt] to verify that project messaging services are listed on the new website, something similar to eBPF Foundation projects summary
   
   * Richard Searle - Discussed End User Advisory Council (EUAC) plan as presented to the Governing Board
      * CCC Projects Day, virtual-only event February 16th 2023
      * Website will go live with a call to action by October 21st, briefing events for projects scheduled by the end of November, socialize at CCC informal event at FOSDEM February 4th 2023, feedback will be provided to project mentors

        **ACTION**: [Kurt] Outreach to make sure that events like this have a home in the new website redesign
      
        **ACTION**: [Kurt] see if LF has best practices documentation for growing a community, if not start a document on a CCC wiki page
      
        **ACTION**: [Kurt] to create TAC Governance Github repo wiki start page
      
        **ACTION**: [Kurt] to get more information on how Hyperledger funds a technical project architect/manager (The title they used in Hyperledger was "Community Architect")

**Common Terminology**

   * DT discussed PR #134 - deferred
   * DT discussed PR #136, Handling of nesting and packaging granularity smaller than TCB, DT  wrote a draft proposal
   * PR #144 Packaging granularity smaller than TCB - DT discussed proposed wording, discussion ensued

**Other Topics**
   
   * DT discussed future Tech Talks
   * DM agreed on scheduling CDCC investigators
   
      **ACTION**: [Kurt] find out who suggested CDCC investigators and follow up
   
   * DT volunteered to talk on the potential relationship between eBPF and Confidential Computing

Meeting adjourned at 8:54 am
