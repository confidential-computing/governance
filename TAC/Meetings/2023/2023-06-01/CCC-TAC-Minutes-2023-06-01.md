# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, June 1, 2023

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

* Dan Middleton (DM) opened the call at 7:03am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Kurt Taylor (KT) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano 
* Arm - Thomas Fossati + / Michael Lu
* Google - Cfir Cohen  / Catalin Sandu +
* Huawei - Zhipeng (Howard) Huang +
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler +
* Red Hat - Lily Sturmann + / Yash Mankad

   " + " indicates attending

***Other Attendees***

* Mike Bursell (CCC)
* Simon Frost (Arm)
* Pawan Khandavilli (Microsoft)
* Mark Novak (JP Morgan Chase)
* Ofir Azoulay-Rozanes (Anjuna)
* Neil Vexler (Anjuna)
* Sandro Pinto (Universidade Minho)
* Graham Bury (Microsoft)
* Jorg Rodel (SUSE)
* Kevin Zhao (Linaro)
* Leonardo Garcia (Linaro)
* Eric Voit (Cisco)
* Alan Czeszynski (BeeKeeperAI)
* Tyler Fanelli (RedHat, VirTEE)
* Sudish Mogli (BeeKeeperAI)
* Mark Bower (Anjuna)
* Drasko Draskovic (Ultraviolet)
* Larry Dewey (AMD)
* Kurt Taylor (LF)
* Helen Lau (LF)


**Meeting Minute Approval**

Proposed: That the minutes of the May 18, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

* Quorum was reached and the minutes were approved by the voting members of the TAC.


**GRC-SIG Customer Guide and Checklist**

* Pawan Khandavilli introduced the [draft guide and checklist](https://docs.google.com/document/d/1HR6rL2EBAduQnmelrL9Jq-UgTOTwGn2S/edit)
* Started with TAC white papers - compiled into a checklist for vendors and providers in the the form of a questionnaire
* Seeking review from the TAC, next step would be to publish, use for analyst meetings and outreach
* Alan Czeszynski (AC) asked if the blog from Alec Fernandez should also be included into this document
* Dave Thaler (DT) added comments on:
    * Technology checkboxes - needs clarification on how the checkboxes should be used, for example - check one or more checkboxes vs checking all
    * TPM and TCG definition clarification - need a TCG expert to review 
    
    ***ACTION*** Pawan to find a TCG expert for review of the wording, maybe Henk Birkholz or Ned Smith
    
* DM commented about the bottoms up nature of the paper, maybe an additional section for the customers requirements, what are they trying to protect - help them map those requirements to a TEE capabilities
* AC asked for more basic initial description of confidential computing as an introduction, maybe it would not be included in this document, discussion ensued

  ***ACTION*** TAC to review and comment on Customer Guide and Checklist


**VirTEE project submission**

* New project proposal - https://lists.confidentialcomputing.io/g/tac/message/1035
* Tyler Fanelli (TF) reviewed the submission template email
  * DT asked for a submission template, included in the body of the email
  * TF discussed the project technology and value
  * Project developed in Rust, mainly for Linux
  * DT asked on sections 1.2 and 1.3
      * Concern on the sevctl repository, including in the proposal, that it does not meet the requirements of confidential computing
      * See page 7 (from chat - table that folks can inspect. E.g. see "Integrity" rows of that table for SEV vs SEV-SNP guarantees, especially as it applies to the checklist we saw earlier) https://www.amd.com/system/files/TechDocs/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf
    * DM asked for clarification on reference-kbs
    * DM asked how to move forward with the DT concerns, DT proposed to move forward without the 2 repos of concern - sevctl (and sevctl-test in the repo) be removed from the proposal
    * DT asked for a quick review of the proposed Technical Charter
    * DM asked for a roll call vote: Thomas Fossati - Yes, Catalin Sandu - Yes, Howard Huang - Yes, Dan Middleton - Yes, Dave Thaler - Yes, Lily Sturmann - Yes
    * VirTEE project proposal was unanimous approved to be recommended to the Governing Board by the TAC and for it to proceed to the next steps in the process, with the minor changes noted
    
     ***ACTION*** Kurt to work with Tyler on the next steps to take the proposal to the Governing Board for approval


**Member Survey**

* Mike Bursell discussed the member survey, asked for TAC to take the survey during the meeting
* [Member survey](https://linuxfoundation.surveymonkey.com/r/CCCsurveyq223)


**Technical Analysis white paper**

* DM asked for approval for the [PR#167](https://github.com/confidential-computing/governance/pull/167)

   ***ACTION*** Kurt to fix the location of the white paper pictures in the repo


**OpenSSF Best Practices badge** 

* DT proposed that the TAC recommend that projects get the [OpenSSF Best Practices badge](https://bestpractices.coreinfrastructure.org/en)
* DM supported the proposal and suggested that the status of the badge be included as a part of the project annual report template
* MB asked if the TAC believes they are good criteria, all agreed
* TAC unanimously approved that the badge "OpenSSF Best Practices" be a recommended Github repo badge for all CCC projects

   ***ACTION*** Dave to create PR to update the project annual report template with the OpenSSF Best Practices repo badge recommendation


**Progression: Graduation Stage Requirements** (Dave/Howard)

* DT reviewed [PR #171](https://github.com/confidential-computing/governance/pull/171) and [PR #170](https://github.com/confidential-computing/governance/pull/170)
    * Emeritus not addressed in this discussion
    * MB commented on the removal of the graduation stage (PR#171)
       * Should a growing project have more access to funding or less access to funding
       * Simplify the the acceptance criteria
       * MB suggested that the TAC poll the voting representatives
       * DM tabled the topic due to time, will resume discussion next meeting


**Tech Talk: Bao Project**

* Sandro Pinto introduced the [Bao project](http://www.bao-project.org/) and the project technology
* Jose Martins (JM) presented the Bao Hypervisor - completely isolated hypervisor Armv8-A main platform, shifting to Armv8-R
* JM continued presented on Bao & TEE and the project roadmap - virtualization-based TEE - goal is to separate TEE instances for each VM
* [Bao project repo](https://github.com/bao-project)
* DM asked about running on SGX enclaves
   * JM explained the security properties enforced by the hypervisor, a running model of the TEE
   * DT asked about attestation support and how that works with the hypervisor


**Annual Report/Update: Veraison**

* Deferred to a future meeting 
* Simon Frost unavailable - Thomas Fossati to present


Next meeting June 15, 2023

Meeting adjourned at 9:00 am PT
