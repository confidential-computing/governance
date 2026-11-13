# **CCC TAC Bi-Weekly Meeting Minutes: November 12, 2026**

## **7 \- 9am PST**

## **Links**

> * **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io/)  
> * **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io/)  
> * **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)  
> * **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)  
> * **CCC YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io/)  
> * **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org/)  
> * **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io/)  
> * **Contact the CCC**: [confidentialcomputing.io/contact-us/](http://confidentialcomputing.io/contact-us/)  
> * **Zoom for CCC TAC meetings**: [https\://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e)  
> * **Recording**: [YouTube](https://www.youtube.com/watch?v=gd9JlFpF9vU)

## **Agenda and Minutes**

> * Simon Gallagher (SG) opened the call and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.  
> * Mike Bursell (MB) asked to add TAC chair nominations as an additional other-business item, which SG agreed to address after the Confidential Computing System discussion.  
> * SG noted there were no voting topics on the agenda and conducted a brief roll call.  
> * SG reviewed the agenda: Islet project annual review (Bokdeuk Jeong), NVIDIA confidential bare metal tech talk (Dan Middleton), and a Confidential Computing System/composability discussion, with chair nominations to be addressed as other business.

## **Attendance**

Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present. There were no voting topics this meeting, so quorum was not formally assessed; checkmarks below reflect roll call, transcript speaker evidence, and LFX participant records.

### **Voting Members of the TAC**

☐ Ahmed Magdy (Meta)  
☐ Alec Fernandez (Microsoft)  
☐ Bob Blessing-Hartley (Shielded Technologies)  
☑ Fritz Alder (NVIDIA)  
☐ Mingshen Sun (TikTok)  
☐ Nathaniel McCallum (AMD)  
☑ Rene Kolga (Google)  
☑ Scott Raynor (Intel)  
☐ Yongzheng Wu (Huawei)  
☐ Caihua Li (Volcano Engine)  
☐ Alpha Compute (rep TBD)

### **Alternate Voting Members**

☑ Dan Middleton (NVIDIA, TAC Chair)  
☐ David Kaplan (AMD)  
☐ Keith Moyer (Google)  
☑ Simon Gallagher (Microsoft)  
☐ Simon Johnson (Intel)

### **Project Staff**

☐ Ben Sternthal (LF PMO)  
☐ Michelle Roth (LF PMO)  
☑ Mike Bursell (CCC ED)

### **Other Attendees**

☑ Artem Barger (Modelyo)  
☑ Bokdeuk Jeong (Samsung Electronics Co. Ltd.)  
☑ Daniel Masny (Meta)  
☑ Edward Boggis-Rolfe  
☑ Hesham ElBakoury (Innovax Technologies)  
☑ Jens Albers (Fr0ntierX Inc)  
☑ Jordi Guijarro (OpenNebula Systems)  
☑ Manu Fontaine (Hushmesh)  
☑ Marcus Davey (SevenLayerLabs)  
☑ Mark Novak (JPMorgan Chase & Co)  
☑ Mona Vij (Intel Corporation)  
☑ Ofir Azoulay-Rozanes (Anjuna Security, Inc.)  
☑ Sakul Gupta  
☑ Steven Bellock (NVIDIA Corporation)  
☑ Thore Sommer (Veraison Project)   
☑ Tom Jones (VeriClouds)

## **Welcome New Community Members**

> * Marcus Davey (MD), SevenLayerLabs: Introduction noted MD's company had just joined the CCC and deploys confidential environments on non-confidential silicon, as well as on a combination of confidential and non-confidential silicon simultaneously, for sovereign AI use cases.

## **Old Business**

> * Nothing substantive carried over for formal discussion. SG pointed newer and remote attendees to the October 29 meeting's recording and minutes on GitHub for context on the prior session's topics (storage, Confidential Inference Governance doc proposal, VirTEE project review, Attestation SIG review).

**Announcements**

> * No TAC meetings on November 26 or December 24 due to the US Thanksgiving and Christmas holiday periods.  
> * MB announced that nominations for TAC chair are now open, as Dan Middleton (DM) is stepping down after several years in the role; interested members should submit a short paragraph about themselves and their aims for the role. The agenda deck lists a nomination deadline of Thursday, November 19, 2026\. DM offered to help onboard whoever takes on the role.

## **New Business**

> * **Islet Project Annual Review** — Bokdeuk Jeong (BJ)  
  * BJ presented the annual review of the Islet project, which brings confidential computing to ARM-based mobile and end-user devices through Android OS confidential-computing enablement and confidential runtime frameworks.  
  * BJ noted updates to the project's dependency list following the addition of new repositories this year, confirmed the project's license remains Apache 2.0 across its original repositories, and reported the project achieved a passing OpenSSF Best Practices badge this year.  
  * Lines of code increased by about 2.5 times year over year, even though commit count decreased, because larger implementations were pushed as single release commits; the project added 23 new repositories this year.  
  * For 2027, BJ identified vulnerability analysis as the top priority, with plans to run intensive AI-assisted security auditing across the codebase to proactively identify and mitigate potential vulnerabilities.  
> * **Tech Talk: Confidential Bare Metal** — Dan Middleton (DM)  
  * DM introduced NVIDIA's new confidential bare metal offering, announced publicly about a month earlier at an NVIDIA company conference in Berlin and now documented on NVIDIA's Confidential Computing website and technical documentation site alongside existing COCO product docs.  
  * DM explained the offering provides hardware-level security protections for model providers renting bare-metal servers in data centers they do not control, using NVIDIA's Grace/Vera CPUs paired with Blackwell GPUs and specialized secure firmware, without requiring second-level page table support.  
  * DM described how confidential bare metal blocks a BMC's and DPU's normal out-of-band PCIe access, and stores measurements in a platform security controller integrated into the NVIDIA CPU complex, serving a role similar to a TPM.  
  * Mona Vij (MV) asked clarifying questions comparing the approach to TDX, SEV, CCA, and Intel TXT secure boot; DM confirmed confidential bare metal is a distinct approach using secure firmware and DRTM (Dynamic Root of Trust for Measurement) rather than any of those.  
  * Edward Boggis-Rolfe (EBR) asked whether CPU-only bare metal servers would be available and whether there is an early-access program; DM confirmed standard product availability with no special early-access process for confidential computing.  
  * Fritz Alder (FA) added context distinguishing containerized deployment scenarios from owning and operating an entire bare-metal server under this model.  
> * **Discussion: Confidential Computing System (Composability)** — presented by Mike Bursell (MB) and DM on behalf of Paul, who was unable to attend.  
  * MB described a proposal, discussed at a recent Governing Board meeting and sponsored by Paul, for the TAC to begin defining higher-level, systems-level confidential computing architectures that compose multiple TEEs together, building on the CCC's existing primitive-level work (TEE definitions, attestation) and on the "Three Degrees of Confidential Computing" paper published earlier this year.  
  * DM noted that industry peers, including Meta and Apple, have published visible systems-level architectures composing multiple TEEs, while most current CCC literature addresses protecting a single memory space.  
  * Simon Gallagher (SG) and MB framed the effort by analogy to a finished product, like a car, rather than individual components, so that organizations could adopt complete solution patterns rather than build from primitives.  
  * Ofir Azoulay-Rozanes (OAR) asked whether this would make confidential computing as easy to adopt as TLS for existing applications, such as confidential containers and Kubernetes workloads, rather than defining new types of applications. MB clarified the intent covers both: enabling new types of applications and attestation relationships, and architectural patterns (referred to informally as a "castles" framework) for best-practice composition.  
  * EBR raised the need for a simple accreditation or certification concept so that non-technical users and organizations could recognize a conformant confidential system, noting the space is still "a bit woolly" and difficult for most organizations to implement today.  
  * MB polled the group for reactions; no objections were raised to the TAC taking on this work, and MB proposed relaying that consensus, rather than a formal vote, back to the Governing Board.

## **Work in Progress**

> * Islet project: 2027 focus on AI-assisted vulnerability analysis and security auditing across the codebase.  
> * Confidential Computing System/composability proposal: consensus reached to relay to the Governing Board; next steps pending GB response and possible formation of a new SIG.

## **Future Business**

> * Next meeting will be December 10, 2026\.  
> * Rotating chair: Rene Kolga (RKo), tentatively, pending confirmation with Keith Moyer, as RKo has a conflicting speaking engagement on confidential computing and cancer research on the same date.  
> * A new Japan Chapter of the CCC is launching, with a kickoff meeting on December 10, 2026 in Tokyo following OSS Japan; MB plans to attend both events, and a blog post about the chapter is forthcoming.  
> * Draft topics for upcoming meetings include 2027 TAC goals and a storage topic (Chandra Nelogal); members with a talk proposal were encouraged to submit an outline via the mailing list linked from the project's Git repo.  
> * MB is exploring engagement with a RISC-V-associated project for a future TAC presentation, and following up with Hesham ElBakoury (HE) on introducing confidential computing to the chiplet community.

## **Action Items**

> * Mike Bursell: Follow up with the TAC community on chair nominations (submissions due Thursday, November 19, 2026).  
> * Simon Gallagher: Coordinate with Rene Kolga and Keith Moyer on the rotating chair for the December 10, 2026 meeting.  
> * Rene Kolga: Check with Keith Moyer on his availability to chair the December 10, 2026 meeting.  
> * Mike Bursell: Follow up with Hesham ElBakoury to introduce confidential computing to the chiplet community.  
> * Mike Bursell: Work with the RISC-V-associated project contact to arrange a future TAC presentation.  
> * Simon Gallagher: Share the talk-submission link/details in chat.  
> * Simon Gallagher: Follow up with Edward Boggis-Rolfe on his Slack talk proposal to route it to the correct channel.