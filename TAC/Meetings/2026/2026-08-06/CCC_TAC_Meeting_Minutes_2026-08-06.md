# CCC TAC Bi-Weekly Meeting Minutes: August 6, 2026

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

* Scott Raynor (SR) opened the call at 7:05 am PT.  
* SR welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* Michelle Roth (MR) recorded the meeting minutes.  
* SR reviewed the agenda.

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [x] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [x] Fritz Alder (NVIDIA)   
- [ ] Mingshen Sun (TikTok)   
- [x] Nathaniel McCallum (AMD)  
- [x] Rene Kolga (Google)  
- [x] Scott Raynor (Intel)  
- [x] Yongzheng Wu (Huawei) 

### Alternate Voting Members

- [x] Dan Middleton (NVIDIA, TAC Chair)   
- [ ] David Kaplan (AMD)   
- [ ] Keith Moyer (Google)   
- [ ] Simon Gallagher (Microsoft)   
- [ ] Simon Johnson (Intel) 

### Project Staff

- [ ] Ben Sternthal (LF PMO)   
- [x] Michelle Roth (LF PMO)  
- [x] Mike Bursell (CCC ED) 

### Other Attendees

* Caroline Perez-Vergas (Microsoft)   
* Jens Alberts (FrOntierX)   
* Jeremy Powell (AMD)  
* Julian Stephen (IBM)   
* Kailun Qin (Intel)   
* Manu Fontaine (Hushmesh)   
* Mark Novak (JP Morgan Chase)   
* Muhammad Usama Sardar (TU Dresden)   
* Ofir Azoulay-Rozanes (Anjuna Security)   
* Ram Pai (IBM)   
* Rui Almeida  
* Tom Jones (VeriClouds) 

## **Welcome New Community Members**

* There were no new community member announcements.

## **Old Business**

* SR reviewed the major points from the last TAC meeting, highlighting that the Occlum project was approved to move to Emeritus. 

## **Announcements**

* The meeting began with a moment of remembrance and a tribute to Dan Williams, a long-time Linux kernel maintainer and former kernel SIG chair who recently passed away. Participants shared memories of his welcoming and patient nature.

## **New Business**

* Trustworthy Workload Identity SIG update \- Mark Novak (MN)   
  * MN provided progress updates on the Trustworthy Identity SIG’s work at IETF 126, detailing contributions to three working groups: WIMSI, RATS, and SEAT, as well as an organization outside of IETF. MN outlined architectural improvements to the WIMSI architecture, addressing credential acquisition and usage separation, and raised concerns regarding drafts currently submitted to the WIMSI working group. MN explained the incompatibility of SPIFFE-inspired architectures with confidential computing and highlighted ongoing efforts to provide architectural guidance. MN discussed the RATS RFC naming and proposed the concept of "ROPs" to address deployment challenges. MN also expressed strong concerns regarding the SEAT working group's approach to attestation extensions in TLS, arguing that separating credential acquisition from usage would resolve key security and governance issues.  
  * Additionally, MN presented a proposed unified model for credential acquisition designed to support multiple mechanisms (including EST, JWTs, WITS, and shared keys) while minimizing trust boundary expansion. The architecture involves adding a CAPI client to workloads to communicate with a CAPI server that interfaces with identity providers and credential stores. MN indicated that a proof of concept based on Verizon will be presented at the September interim meeting, with development taking place over the next four to five weeks.  
  * MN also updated the TAC on the ATF draft and discussed a unified model for workload location and attestation, aiming to present it at the September interim meeting along with accompanying code. MN emphasized the need for a framework that incorporates various location evidence sources and standardizes policy languages. Mike Bursell (MB) confirmed that the Governing Board (GB) has agreed on Agentic AI as a strategic pillar for the CCC, noting existing Linux Foundation projects related to Agentic Computing. The group discussed challenges in defining and securing AI agents versus regular workloads, with MN stressing the need to understand whether these differences are in degree or kind before proposing solutions.  
  * Finally, MN discussed extending the SPIRE Workload API to support confidential computing attestation and called for greater developer and architect participation. MN noted frustration regarding the lack of response to pull request submissions to the TAC over the past three months. Muhammad Usama Sardar (MS) shared a new draft addressing trust problems in protocol design, but MN expressed skepticism regarding the necessity of such modifications if proper remote attestation and TLS authentication are implemented first.

## **Tech Talk**

* “Layered Filesystems and the Confidential Computing Trust Problem” \- Nathaniel McCallum  
  * Nathaniel McCallum (NM) presented a technical talk on layered file systems and the confidential computing trust problem. NM reviewed historical trade-offs in computing infrastructure, highlighting how the industry moved from bare metal to VMs and then to containers, sacrificing security for cost savings at each stage. NM explained that confidential computing faces a comparison problem because it adds privacy to VMs, which the market is actively moving away from. To address this, NM proposed a solution called "Carapace" that uses Linux's Device Mapper tools to enable layered VM images with integrity verification while maintaining security, similar to how containers use OverlayFS but resolving trust issues in confidential computing environments.  
  * NM explained a new approach called "salt chaining" for creating immutable, layered file systems using DM Verity, which uses a single hash to validate the entire chain of layers, eliminating the need for multiple hashes and making distribution more efficient. NM demonstrated how this approach enables base layer deduplication across workloads, incremental updates, and real file system semantics without the workarounds required by OverlayFS, concluding that this solution provides the same cost-savings benefits as containers while allowing VMs to run Linux in the guest environment.  
    

## **Work in Progress**

* Blueprints A\&B  
  * The TAC noted continued progress and ongoing work on the A & B blueprints.  
* Agentic AI paper  
  * The group discussed challenges in defining and securing AI agents versus regular workloads. Mark Novak stressed the need to understand whether these differences are in degree or kind before proposing solutions. The TAC plans to review the Agentic AI paper in the next meeting, with plans to invite author Raghu to attend and participate.  
* TAC whitepaper  
  * Alec Fernandez (AF) announced updates to the primary TAC white paper, noting he has formalized attestation as a required property for TEEs rather than an optional feature, which Muhammad Usama Sardar (MS) and the group agreed with and welcomed. The team also discussed concerns regarding cloud service providers (CSPs) being included in the Trusted Computing Base (TCB) for confidential computing, with AF emphasizing the need to document the current state versus the end goal of reducing CSP dependencies. Additionally, the group discussed AMD's new Volcano SmartNIC and its TDISC compliance. Jeremy Powell (JP) explained that it uses standard SPDM attestation protocols and will provide reference manifests and documentation for verifiers. AF expressed interest in collaborating with JP to create vendor-neutral documentation about composite TCBs (including GPUs and smart NICs) and discussing Azure's Boost implementation. AF will incorporate stack visualizations into the TAC white paper and submit the changes as a pull request to the markdown document after review.

## **Future Business**

* Next meeting will be August 20, 2026  
* Rotating chair(s): Ahmed Magdy

## **Action Items**

* Dan Middleton: Share the link for supporting Dan Williams' family in the chat.  
* Michelle Roth: Share details about the remembrance event for Dan Williams at an upcoming LF event with the group when available.  
* Mark Novak: Email the presentation deck to the TAC.  
* All TAC Members: Periodically check the governance repo for pending pull requests and review/approve them, especially those from Mark Novak.  
* Dan Middleton: Open an issue in the governance repo to start collecting significant adoption hurdles for confidential computing.  
* Alec Fernandez: Reach out to Jeremy Powell to collaborate on a white paper about composite attesters and TCB considerations.  
* Dan Middleton: Provide the original PowerPoint artwork for the stack visualizations to Alec Fernandez.  
* Alec Fernandez: Incorporate the stack visualizations into the TAC white paper and submit changes as a PR to the markdown document after review.  
* Scott Raynor: Invite Raghu to the next meeting (August 20\) to discuss the Agentic AI paper.  
* All Attendees: Review the Agentic AI paper and provide feedback.


---

