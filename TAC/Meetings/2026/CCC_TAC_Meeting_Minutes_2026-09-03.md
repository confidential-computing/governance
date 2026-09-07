# CCC TAC Bi-Weekly Meeting Minutes: September 3, 2026

## 7 \- 9am PDT 

## **Links**

* **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io/)  
* **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io/)  
* **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)  
* **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)  
* **CCC YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io/)  
* **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org/)  
* **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io/)  
* **Contact the CCC**: [confidentialcomputing.io/contact-us/](http://confidentialcomputing.io/contact-us/)  
* **Zoom for CCC TAC meetings**: [https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e) 

## **Agenda and Minutes**

* Dan Middleton (DM) opened the call at 7:03 am PT.  
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* MR recorded the meeting minutes (post-meeting).  
* DM reviewed the agenda. Several schedule adjustments were announced: the MITRE paper presentation and the DStack project update were postponed as the presenters and maintainers were unavailable. The agenda was adjusted to focus on the CCAF Framework and the Agentic AI white paper.

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [ ] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [ ] Fritz Alder (NVIDIA)   
- [x] Mingshen Sun (TikTok)   
- [x] Nathaniel McCallum (AMD)  
- [x] Rene Kolga (Google)  
- [x] Scott Raynor (Intel)  
- [ ] Yongzheng Wu (Huawei) 

### Alternate Voting Members

- [x] Dan Middleton (NVIDIA, TAC Chair)   
- [ ] David Kaplan (AMD)   
- [ ] Keith Moyer (Google)   
- [x] Simon Gallagher (Microsoft)   
- [ ] Simon Johnson (Intel) 

### Project Staff

- [ ] Ben Sternthal (LF PMO)   
- [ ] Michelle Roth (LF PMO)  
- [ ] Mike Bursell (CCC ED) 

### Other Attendees

* Edward (Boggis-Rolfe)  
* Eric Hibbard (Samsung)  
* Hesham ElBakoury (Innovax Technologies)  
* Jens Alberts (FrOntierX)   
* Jordi Guijarro (Open Nebula)  
* Mark Bower (Anjuna)  
* Mark Novak (JP Morgan Chase)   
* Ram Pai (IBM)   
* Rithikha Rajamohan (EQTY Lab)  
* Solomon Cates (Google)  
* Steven Bellock (NVIDIA)  
* Syama Poluri (Dell)   
* Tom Jones (VeriClouds)

  
## **Welcome New Community Members**

* Edward Boggis-Rolfe (Secretarium / London): Introduced himself as an expert in platform-independent RPC solutions. He spent six years at Secretarium (which folded eight months ago) developing a transport-, serialization-, and threading-agnostic RPC platform that also works with various attestation solutions. He is currently targeting SGX to enable rapid application development of confidential computing platforms (supporting REST, WebSockets, gRPC) with non-blocking I/O (via io\_uring) and coroutines to run threads efficiently inside enclaves.  
* Solomon (Sol) Cates (Google LLC): Introduced himself as an architect who has been building software solutions since the 1990s, including roles at Symantec, with extensive experience in the military, intelligence, and banking sectors. He recently joined Google and is leading the Regulatory and Standards (R\&S) SIG. His goal is to make confidential computing easier for traditional architects to understand and adopt, and to help drive the Confidential Compute Assurance Framework (CCAF).  
* Mark Bower (Anjuna Security): Introduced himself as the head of product and go-to-market for Anjuna and co-chair of the Cloud Security Alliance (CSA) Confidential Computing Working Group (under the CSA privacy pillar). He highlighted an upcoming executive and technology leader education document that is in its final stages. Next steps for the group will focus on deeper use cases, including confidential AI agents. He noted that Josh Bucher from the CSA also helps run their meetings.

## **Old Business**

* DM provided a brief recap of the August 20, 2026 meeting, noting John Manferdelli's update on the Certifier Framework project and the ongoing work on the Agentic AI white paper. 

## **Announcements**

* IETF RATS Working Group Draft Submission: Mark Novak (MN) announced that the Trustworthy Workload Identity (TWIC) task group is preparing a major revision of their draft architecture for submission to the IETF Remote Attestation Procedures (RATS) working group. The draft is set for the interim meeting on September 14, 2026, with a submission deadline of Friday, September 11, 2026\. The draft proposes an architecture allowing any confidential workload or container to acquire credentials (such as EST, ACME v2, Spire, etc.) seamlessly, similar to how Envoy manages TLS certificates. A companion draft specifically for EST (RFC 7030\) will also be presented to the LAMPS working group. MN requested community reviews on the TWIC mailing list.

## **New Business**

* Dstack Project Update \- TBD   
  * This item was postponed as the maintainers were unable to connect.  
* MITRE Paper \- @Jens   
  * This presentation was postponed due to presenter unavailability.  
* CCAF @Sol   
  * Solomon Cates (SC) presented the Confidential Compute Assurance Framework (CCAF) as a vendor-agnostic framework for trusted execution environments (TEEs). The CCAF aims to establish standardized terminology and components to bridge the gap between regulators (such as BSI, NIST, and NSA), manufacturers, and implementers. Key discussion points included:  
* Document Accessibility: The document is currently a Google Doc, which has caused access issues for some community members. DM suggested migrating it to a Linux Foundation document to ensure global accessibility. SC will grant temporary access to individuals in the interim.  
* Purpose and Objectives: The CCAF serves as a bridge for regulatory compliance and aims to create common measurement tools to assess how far a technology solution is on its confidentiality journey. Solomon emphasized the importance of reference architectures as viewable, understandable maps for executive leadership.  
* Scoring System: DM raised concerns regarding the proposed scoring/rating system. SC explained the scoring was intended to weigh component importance depending on the security requirements of the transaction (e.g., $10 pizza vs. billion-dollar oil transaction). MN strongly recommended against reducing multidimensional security vectors to a single scalar score (the "deadly sin of governance"), which SC agreed with. DM suggested that the group focus first on completing the security objectives (80% of the effort) and address the scoring system later.  
* SIG Coordination: SC proposed coordinating the CCAF, TAC, and GRC SIGs to align terminology and expectations. MN welcomed this and requested SC review the GRC SIG's published patterns on GitHub.  
* Lawful Intercept: Edward Boggis-Rolfe (EBR) raised questions regarding legal intercepts/backdoors required by some countries. MN recommended leaving lawful intercept entirely out of scope of the technology governance framework, which was supported by SC and the group.  
* Agentic AI Paper  
  * The team reviewed comments on the Agentic AI white paper. Since lead author Raghuram Yeluri was absent, DM deferred complex or opinionated comments to the next meeting. Key discussion points included:  
* Terminology Updates: The group agreed to replace the word "encrypted" with "hardware isolated" when referring to GPU high-bandwidth memory (HBM), as current implementations isolate but do not encrypt HBM.  
* Agent-Specific Benefits: Rene Kolga (RK) suggested that the paper focus more on agent-specific benefits (such as the integrity of tools/MCP servers to prevent "rag pool" attacks, and the ease of resetting agent memory by shutting down a TEE) rather than repeating general confidential computing benefits.  
* Supply Chain and Identity: MN noted that supply chain and build integrity are handled via provenance in the TWIC task group. He recommended referencing these existing standard techniques rather than proposing Agentic-specific solutions.  
* Probabilistic Behavior: Tom Jones (TJ) asked about the impact on identity when models, prompts, or inputs change during processing. MN explained that AI/ML behaviors are probabilistic and cannot map code to behavior in a traditional deterministic manner. DM noted that continuous attestation (which may be addressed in MITRE's upcoming paper) is relevant to this problem.  
* Capability Positioning: The team discussed whether confidential computing provides substantial benefits in software-level areas like prompt injection. It was agreed to maintain a realistic, defensive positioning rather than over-promoting capabilities.  
* Next Steps: DM encouraged reviewers to make direct edits using track changes over the next two weeks, aiming for publication after one or two more iterations.  
* TAC Whitepaper \- not discussed. 

## **Work in Progress**

* Other Blueprints \- not discussed. 

## **Future Business**

* Next meeting will be September 17, 2026  
* Rotating chair(s): Dan Middleton  
* Annual Project Review: ManaTEE  
* Rescheduled presentations: DStack project update and the MITRE continuous attestation paper.

## **Action Items**

* Dan Middleton / LF Staff: Migrate the CCAF Google Doc to a globally accessible Linux Foundation document.   
* Solomon Cates: Grant access to the CCAF Google Doc to Hesham ElBakoury and other community members who request it.   
* Solomon Cates: Review the GRC SIG's published governance patterns on GitHub and coordinate with Mark Novak to align terminology.   
* Solomon Cates: Draft an initial scratch reference architecture for CCAF and recruit interested community members to collaborate.   
* All TAC Members: Review the CCAF document over the next two weeks and provide feedback, specifically focusing on whether the listed security objectives are complete and how to define systems.   
* All TAC Members: Review the Agentic AI white paper and provide direct edits and comments, focusing on defining agent-specific benefits (e.g., memory reset, tool integrity) before the next meeting.   
* All TAC Members: Review the TWIC draft submission to the IETF RATS Working Group on the mailing list ahead of the September 11, 2026 deadline.   
* Mingshen Sun: Prepare the ManaTEE annual project review presentation for the September 17, 2026 meeting.   
* Dan Middleton: Reschedule the DStack project update and the MITRE continuous attestation paper presentation for the September 17, 2026 meeting.


---

