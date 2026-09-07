# CCC TAC Bi-Weekly Meeting Minutes: August 20, 2026

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

* Michelle Roth (MR) opened the call at 7:13 am PT.  
* MR welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* MR recorded the meeting minutes.  
* MR reviewed the agenda. A slight schedule adjustment was announced: the MITRE paper presentation has been moved to the September meeting due to last-minute scheduling conflicts with the presenters. All other agenda items remained as scheduled.


## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [ ] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [ ] Fritz Alder (NVIDIA)   
- [ ] Mingshen Sun (TikTok)   
- [ ] Nathaniel McCallum (AMD)  
- [ ] Rene Kolga (Google)  
- [x] Scott Raynor (Intel)  
- [ ] Yongzheng Wu (Huawei) 

### Alternate Voting Members

- [ ] Dan Middleton (NVIDIA, TAC Chair)   
- [ ] David Kaplan (AMD)   
- [ ] Keith Moyer (Google)   
- [x] Simon Gallagher (Microsoft)   
- [ ] Simon Johnson (Intel) 

### Project Staff

- [ ] Ben Sternthal (LF PMO)   
- [x] Michelle Roth (LF PMO)  
- [ ] Mike Bursell (CCC ED) 

### Other Attendees

* Edward (Boggis-Rolfe)  
* Eric Hibbard (Samsung)  
* Hesham ElBakoury (Innovax Technologies)  
* Ijlal Ioutfi (Canonical)  
* Jens Alberts (FrOntierX)   
* John Manferdelli (Certifier Framework Project)  
* Julian Stephen (IBM)   
* Kevin Hui (Meta)  
* Kevin Jones (Edge and Node)  
* Manu Fontaine (Hushmesh)   
* Mark Novak (JP Morgan Chase)   
* Ofir Azoulay-Rozanes (Anjuna Security)   
* Raghu Yeluri (Intel)   
* Ram Pai (IBM)   
* Rithikha Rajamohan (EQTY Lab)  
* Sakul Gupta (Micron)   
* Steven Bellock (NVIDIA)  
* Syama Poluri (Dell) 

## **Welcome New Community Members**

* Kevin Jones (Founder of OneClaw, oneclaw.xyz): Noted that OneClaw uses Google Confidential Compute to execute intents, keeping secrets and credentials isolated from AI agents.  
* Edward Boggis-Rolfe (UK-based Startup): Working on confidential RPC (Remote Procedure Calls) with transport and attestation-agnostic serialization for enclaves and non-enclaves. The project supports synchronous/asynchronous I/O and one-way function calls across multiple languages (starting with C++ and Rust), modernizing a 90s technology (Carmen/Corba). A prototype is accessible on his GitHub.  
* Raghuram (Raghu) Yeluri (Intel): Joined the call as a guest. He works in confidential computing at Intel and drafted the initial version of the Agentic AI paper.

## **Old Business**

* No active old business was discussed during this meeting.

## **Announcements**

* Linux Plumbers Conference: Taking place in October 2026\. Members planning to attend are encouraged to set up informal meetups. There is no formal CCC gathering scheduled as the Confidential Computing Summit was held recently.  
* RATS Working Group Interim Meeting: Mark Novak announced that an interim meeting of the IETF Remote Attestation Procedures (RATS) Working Group is scheduled for September 2026\. The Trustworthy Workload Identity (TWIC) task group is preparing a draft to present at this meeting. Mark encouraged TAC members to participate.  
* Call for Updates: Members were reminded to share any upcoming fall conference plans or community announcements via the TAC Slack channel or mailing list.

## **New Business**

* Certifier Framework project update \- John Manferdelli (JM)  
  * Organizational and Community Updates: Following VMware's acquisition by Broadcom, the project was released to open source under the Apache license. While VMware contributors have transitioned to other roles, JM continues to maintain the project with new contributions from Datica (co-founded by John and Paul England, who were among the original Microsoft TPM developers).  
  * NSF Grant & Collaborations: The project recently (about two weeks ago) received a National Science Foundation (NSF) grant. They will be collaborating with USC, the University of Virginia, and several federal government agencies. The funding is primarily targeted at health, scientific, and analytical applications.  
  * Technical Architecture & Capabilities:  
    * Currently supports AMD SEV-SNP and Intel SGX as primary platforms.  
    * Early support is established for Berkeley Keystone and Samsung ISLIT (ARM CCA).  
    * Includes a simulated enclave allowing development on non-confidential hardware.  
    * TPM Support Added: (1) Allows developers using TPMs (which lack encrypted memory) to easily transition to more secure enclaves with simple declarations. (2) Enables equivalent confidential computing protection in VMs using virtual TPMs where cloud providers only attest to lower-level booting.  
  * New Utilities: Introduced shell-level management programs for VMs to simplify system administration.  
    * Granular Resource Protection Prototype: Added a new client library to support granular protection based on additional authentication keys.  
    * Multiple Trust Domains: A single program or VM can now operate across multiple trust/security domains.  
    * Java Support: Ongoing efforts to resolve bugs in the initial Java support developed by a summer intern.  
  * Roadmap & Future Work:  
    * Plans to support ARM CCA, Raspberry Pi (requires firmware updates), iOS, Amazon Nitro, Intel TDX, and NVIDIA Hopper (hardware access pending).  
    * Support for DICE (TPM-like IoT mechanism).  
    * Researching automatic container specification, measurement, and deployment (VMM to VM to Kubernetes/containers).  
    * Integrating automated formal methods using AI and side-channel protection in the presence of an adversarial VMM.  
    * Seeking grants to build "off-the-shelf" appliances and applications.  
    * Potential future migration of the Go-based service to Rust.  
  * Q\&A:  
    * Edward Boggis-Rolfe (ER) asked if trust domains can be dynamically linked at runtime. JM clarified that programs can be added dynamically to a domain via Certifier rules, but the framework does not support dynamic code linking (which would require signature verification).  
    * ER asked about transport protocols. JM clarified it is transport-agnostic; TLS with mutual authentication is the default.  
    * ER asked about daisy-chaining trust zones (A \-\> B \-\> C). JM explained that the Certifier maps one-to-one to a security domain (in or out) to keep things simple, though a single program can belong to multiple domains.

## **Agentic AI White Paper**

* Background: Raghuram Yeluri (RY) drafted the paper a couple of weeks ago and is addressing reviewer comments.  
* Proposed Scope and Title Changes: Manu Fontaine (MF) proposed changing the paper's title to "Agentic Computing" to encompass both probabilistic AI models and deterministic software agents. MF emphasized the critical role of TEEs in enabling software agents to generate their own cryptographic keys with no external key management dependencies ("knowledge isolation" in addition to "execution isolation").  
* RY noted that expanding the scope to "Agentic Computing" adds significant complexity and enhances threat models. RY suggested the paper remain focused on Agentic AI (e.g., agent loops and injection attacks) while broader concepts could be addressed in a separate paper.  
* Ofir Azoulay-Rozanes (OA) raised concerns that attesting autonomous agents that receive non-deterministic LLM commands could create "false trust," comparing it to attesting a Kubernetes node rather than specific pods. RY agreed that TEEs can only attest to deterministic components (measurements, verified policies) and cannot measure dynamic code generated by an LLM at runtime. OA suggested this limitation must be clearly articulated in the document.  
* Kevin Jones (KJ) agreed, suggesting that the architecture of how multiple TEEs communicate and verify policies is crucial.  
* Mark Novak (MN) described agents as "re-christened bots with LLM complications" and recommended defining what is "different in kind, not in degree." MN warned against commingling credential acquisition and credential use.  
* MN shared a Cloud Security Alliance (CSA) paper on Agentic Identity as prior art. While it frames the problem well, MN noted its solution is highly complex ("boiling the ocean") and lacks confidential computing integration.  
* RY and MN agreed that the CCC should focus on how confidential computing acts as an enabling capability for existing identity workflows rather than proposing disruptive, ground-up rewrites.  
* MF noted that Hushmesh currently operates a global identity provider built 100% inside confidential compute (Intel SGX) without conventional directory dependencies, demonstrating the feasibility of decentralized, recursive trust.  
* Next Steps:  
  * Contributors are requested to move from "comments mode" to direct document editing with track changes turned on to accelerate progress.  
  * All TAC members are encouraged to read the CSA Agentic Identity paper before the next meeting in two weeks.  
  *  MR will add the Agentic AI paper discussion back to the agenda for the next meeting and post the document link in the TAC Slack channel.  
    

## **Work in Progress**

* Blueprint C Paper: MR reported that the paper has gone through final revisions and is nearly ready for publication. It is scheduled to be published in August 2026\.  
* Other Blueprints: Simon and Alec's blueprints are open for feedback; TAC members are requested to provide comments.  
* MN announced that the GRC SIG has published two major updates:  
  * Verifier Governance Pattern for Trust Anchor Separation (critical for audit compliance).  
  * Proxy and Gateway Governance Pattern (ensuring end-to-end data protection when a trusted intermediary is inserted).  
  * The SIG will now resume work on governance guidelines for confidential inferencing and confidential training. MN shared a scenario involving banks collaborating through a CSP to detect money laundering without exposing customer data or proprietary model weights/architectures.  
  * GRC SIG meetings are held every other Wednesday; invites are available on the CCC calendar.

## **Future Business**

* Next meeting will be September 3, 2026  
* Rotating chair(s): Alec Fernandez 

## **Action Items**

* Mark Novak: Reach out to John Manferdelli via email (johnmanferdelli@hotmail.com) to discuss TWIC and Certifier framework integration.  
* Raghuram Yeluri: Address and close comments on the Agentic AI paper, and schedule a one-on-one meeting with Manu Fontaine to discuss his comments.  
* Raghuram Yeluri: Post the link to the Agentic AI paper in the chat/TAC Slack channel.  
* All TAC Members: Read the CSA paper on Agentic Identity shared by Mark Novak before the next meeting in two weeks.  
* All TAC Members: Start editing the Agentic AI paper directly (using track changes) rather than just adding comments.  
* Michelle Roth: Add the Agentic AI paper discussion to the September 3rd TAC meeting agenda and include the document link in the TAC Slack.  
* Michelle Roth: Publish the Blueprint C paper in August 2026\.  
* TAC Members: Provide feedback and comments on Simon and Alec's blueprints.  
* TAC Members: Join the GRC SIG meetings (every other Wednesday) to contribute to the governance guidelines for confidential inferencing and training.


---

