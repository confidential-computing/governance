# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, May 18, 2023

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

* Dan Middleton (DM) opened the call at 7:04am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Kurt Taylor (KT) assisted with the meeting minutes
* DM reviewed the agenda

### Roll Call / Attendance

***Voting members of the TAC***

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* Accenture - Giuseppe Giordano 
* Arm - Thomas Fossati + / Michael Lu
* Google - Cfir Cohen + / Catalin Sandu
* Huawei - Zhipeng (Howard) Huang
* Intel - Dan Middleton (TAC chair) + / Simon Johnson
* Meta - Eric Northup / Shankaran Gnanashanmugam
* Microsoft - Dave Thaler +
* Red Hat - Lily Sturmann  / Yash Mankad +

   " + " indicates attending

***Other Attendees***

* Mike Bursell (CCC)
* Thore Sommer (Keylime/FHNW)
* Ofir Azoulay-Rozanes (Anjuna)
* Mark Novak (JP Morgan Chase)
* Leonardo Garcia (Linaro)
* Pawan Khandavilli (Microsoft)
* Nick Vidal
* Kevin Zhao (Linaro)
* Marc Meunier (Arm)
* Vidhya Krishnan (NVIDIA)
* Neil Vexler (Anjuna)
* Alec Fernandez (Microsoft)
* Eric Voit (Cisco)
* Zahara Tarkhani (Microsoft)
* Simon Frost (Arm)
* Ravi Sahita (Rivos)
* Drasko Draskovic (Ultraviolet)
* Xinxin Fan (IoTeX)
* Sonemaly Phrasavath (AMD)
* Mona Vij (Intel)
* Shanwei Cen (Intel)
* Kurt Taylor (LF)
* Helen Lau (LF)


**Outreachy internship**

* Zahara Tarkhani introduced herself and discussed the hardware needed for the mentorship
* All agreed to continue the discussion via email


**Meeting Minute Approval**

Proposed: That the minutes of the May 4, 2023 meeting of the Technical Advisory Council of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

* Quorum was reached and the minutes were approved by the voting members of the TAC. 


**Board Meeting Recap**

* DM briefly recapped the Governing Board meeting also held this week


**Project progression discussion**

* DM introduced the discussion on fixing the current project progression policy 
 * Project Progression proposal [PR #160](https://github.com/confidential-computing/governance/pull/160)
* Dave Thaler (DT) presented on the Graduation stage
  * Background: [Issue #104](https://github.com/confidential-computing/governance/issues/104) from April 2022
  * Sandbox and Incubation stages were approved soon after initial project formation, but further stages were never discussed or approved
  * Need is to define the differences and benefits of Graduation
  * One approach is to remove it alltogether [PR #171](https://github.com/confidential-computing/governance/pull/171)
  * The other approach is to define the Graduation phase [PR #170](https://github.com/confidential-computing/governance/pull/170)
    * Emeritus not addressed in this proposal
    * [Growth Plan document](https://github.com/confidential-computing/governance/blob/main/growth-plans.md)
    * Discussion on employer wording - proposed that employer would include subsidaries and contractors, what fraction affiliated with project
    * Numer of committers - make more clear than only the subjective term "healthy number"
    * OpenSSF Best Practices   https://bestpractices.coreinfrastructure.org/en/criteria
        * From OpenSSF "Bus factor "- minimum number of maintainers that would have to suddenly disappear for the project to stall
        * In chat: Independent of this, I would love to see the TAC recommend OpenSSF Best Practices badge for all projects.  Can discuss next time.
  * Mike Bursell proposed that the TAC debate the 2 options, what the levels are for: example - would the funding be higher or lower for graduation
* DM asked the TAC to review the proposals for discussion at the next meeting


**Tech Talk: Keylime**

* Thore Sommer (TS) presented on the Keylime (CNCF project)
  * Background on TPM - Trusted Platform Module
    * PCR extend algotithm
  * Questions and discussion on measurement
  * Keylime architecture and example of process at runtime
  * SEV-SNP vTPM proof-of-concept: https://github.com/svsm-vtpm/
  * Plans:
      * move UEFI log parser to pure Python, evaluating policy engines
      * General attestation infrastructure
  * Work with CCC for common terminology and possible hosting plugin, possible additional future modules
    * DT discussed the plugin hosted in the CCC would be similar to Veraison
    * MB asked if attestation - is there a danger in combining TEE and TPM attestation, pointing out the differences between them - discussion ensued
    * DM asked about other areas of use or examples
    * From chat: For the CRTM (initial measurment) (definition)]https://trustedcomputinggroup.org/wp-content/uploads/TCG_PCClient_PFP_r1p05_v23_pub.pdf)
    * DT asked about the attestation architecture - relying party needing to be able to tell they are a TEE


**TAC Goal Topic: Community Health**

* Nick Vidal (NV) and DM on Community Health
* DM presented on DCI
  * Requirements, Recommendations and Resources (as a part of Minimum Viable Governance)
  * Review of 2022 DCI accomplishments
    * Linux Foundation [Diversity and Inclusivity Courses](https://www.linuxfoundation.org/about/diversity-inclusivity)
* NV discussed the examples from the Outreach committee
  * Outreachy - mentoring: Enarx and Veracruz have had previous mentees
  * New Vice Chair - Kate George
  * Highlighted International Women's Day


**Update: Attestation SIG**

* Shanwei Cen (SC) presented
* No change in the SIG mission or scope
  * DT asked if the mission would need to changed since they may not actually be developing software
  * Thomas Fossati (TF) noted that there is proof of concept work underway, Mona Vij (MV) commented that there were also efforts to commonize components
* License scans - provide feedback on outstanding issues on license scans

  ***ACTION*** Kurt to get the latest recommendations on how the LF LFX license scans are started and what code-bases are supported

* Progression Status - Attested TLS / TLS + CWT, Interoperable TLS, HTTPA
  * Proposal to start a new track on composite attesters
* 3 projects:
    * TF discussed the Attested TLS Proof-of-Concept, MV asked how to get involved, email TF
    * Interoperable RA-TLS
    * Formal specification of attestation mechanisms


**Any other business**

* Next meeting June 1, 2023

Meeting adjourned at 9:01 am PT
