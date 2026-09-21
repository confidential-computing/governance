# CCC TAC Bi-Weekly Meeting Minutes: September 17, 2026

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
* MR recorded the meeting minutes.  
* DM reviewed the agenda, noting there has been some reshuffling of topics since the agenda was sent out earlier in the week. 

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [x] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [ ] Fritz Alder (NVIDIA)   
- [x] Mingshen Sun (TikTok)   
- [ ] Nathaniel McCallum (AMD)  
- [x] Rene Kolga (Google)  
- [ ] Scott Raynor (Intel)  
- [ ] Yongzheng Wu (Huawei) 

### Alternate Voting Members

- [x] Dan Middleton (NVIDIA, TAC Chair)   
- [ ] David Kaplan (AMD)   
- [ ] Keith Moyer (Google)   
- [x] Simon Gallagher (Microsoft)   
- [ ] Simon Johnson (Intel) 

### Project Staff

- [ ] Ben Sternthal (LF PMO)   
- [x] Michelle Roth (LF PMO)  
- [x] Mike Bursell (CCC ED) 

### Other Attendees

* Andrew Gilbert  
* Chenghong Wang  
* David Oswald (Durham University)   
* Hesham ElBakoury (Innovax Technologies)  
* Hiroki Chen (Indiana University)   
* Jason Rogers (Invary)  
* Jens Albers (Fr0ntierX)   
* Jonathan Begg (Fr0ntierX)  
* Jordi Guijarro (Open Nebula)  
* Mark Novak (JP Morgan Chase)   
* Manu Fontaine (Hushmesh)  
* Melissa McGregor (Corvex)  
* Mic Bowman (Intel)   
* Milica Spuzic (Microsoft)   
* Nick Renner (Fr0ntierX)   
* Ofir Azoulay-Rozanes (Anjuna)   
* Paul Howard (ARM)  
* Qifan Wang (Durham University)   
* Ram Pai (IBM)   
* Sakul Gupta (Micron)  
* Solomon Cates (Google)  
* Steven Bellock (NVIDIA)  
* Syama Poluri (Dell)   
* Weijie Huang  
* Yanxi Lin

## **Welcome New Community Members**

* Nick Renner (Fr0ntierX): Introduced himself as a recent PhD graduate of New York University, now joining Fr0ntierX as principal engineer alongside Jens Alberts.  
* Melissa McGregor (Corvex): Introduced herself as leading Corvex's integration into the CCC. Described Corvex as a "neocloud" that has been developing confidential computing products, with a particular focus on securing model weights and making confidential computing usable up the stack from the hardware layer. Noted that more technical staff from Corvex will join TAC activities in the near future.

## **Old Business**

* DM provided a brief recap of the September 03, 2026 meeting, noting the IETF Rats Working Group draft submission, CCAF proposal, and the ongoing work on the Agentic AI white paper. 

## **Announcements**

* DM noted the recent (monthly) Governing Board meeting, which is responsible for matters such as CCC funding. He shared TAC updates with the board, including the Occlum project winding down and upcoming news from the dStack project. There were no board decisions this month directly affecting the TAC. DM reiterated his standing encouragement for member companies to make direct project contributions to CCC open source projects.

## **New Business**

* **Research Grant Presentation: Side-Channel Attacks on Confidential LLMs** – David Oswald (DO) and Qifan Wang (Durham University)  
  * DO and QW presented their CCC-funded research on side-channel leakage in large language models running in confidential computing environments, focusing on scenarios where an LLM runs in a GPU TEE supported by a CPU TEE (e.g., Intel TDX/AMD SEV-SNP paired with an NVIDIA H100 confidential GPU).  
  * The project targets KV-cache-related leakage sources — e.g., CPU-side memory access patterns, TDX timing behavior, prefix-cache reuse patterns, and encrypted CPU–GPU transfer timing/volume — and plans to evaluate existing mitigations (e.g., constant-time flags, cache partitioning) before proposing new ones.  
  * The project is a \~9-month effort; the team plans to build a full TDX/SEV \+ H100 test workflow (starting with vLLM), publish results, and submit a paper.  
  * Discussion: Alec Fernandez (AF) asked whether these exploits would still apply once the industry moves from bounce-buffer CPU–GPU communication to a TDISP-based composite TEE with a direct encrypted PCIe channel. DO/QW responded that CPU-side and power-based leakage is likely to remain largely generic regardless of transport, while PCIe traffic-pattern leakage would change significantly under TDISP. Mike Bursell (MB) asked about project timescale (\~9 months); DO noted hardware availability (H100s, and an incoming Blackwell system) is a practical constraint for academic research. Hesham ElBakoury asked for the referenced Meta confidential-AI white paper link; DO shared it in the meeting chat and offered to distribute the underlying slide PDF as well.  
* **Research Grant Presentation: Verifiable Data Governance in Confidential VMs** – Chenghong Wang (CW) and Hiroki Chen (HC) (Indiana University)  
  * CW and HC presented their project on verifiable data governance: ensuring that data flows inside confidential VMs adhere to user-defined policies, not just that computation is isolated. They outlined three guarantees — policy enforcement, capture of an immutable processing history, and offline/remote verifiability of that history.  
  * Key design: a small, formally verified "DECO" monitor, implemented in Rust and running at a higher-privilege VMPL level than the (untrusted) guest Linux kernel, enforcing information-flow-control policies for function-as-a-service workloads without needing to trust or replace the guest kernel (contrasted with approaches like Gramine-TDX that replace the kernel outright).  
  * HC presented preliminary results on an asynchronous system-call design (using message-signaled interrupts and VMPL transitions) intended to reduce the performance cost of the security monitor; benchmarks on Redis YCSB showed 83–95% of native baseline performance. The Rust implementation of the DECO monitor has been formally verified against an abstract state machine.  
  * Discussion: DM asked whether the team was familiar with the Coconut-SVSM project and noted a distinction from Gramine-TDX; HC confirmed familiarity and clarified DECO's philosophy is to preserve, not replace, guest kernel functionality while confining its security-relevant effects. AF thanked HC for clarifying that distinction.  
* **CMU Research Study: Confidential Computing Adoption in Biomedical Research** – Yanzi Lin (YL)  
  * YL, a PhD student at Carnegie Mellon, described an interview study investigating stakeholder perspectives on adoption challenges for confidential computing in biomedical/healthcare research. The study has strong coverage of hospital, research-informatics, and compliance perspectives, and is now seeking introductions to industry vendors who have worked with healthcare/biomedical customers.  
  * YL requested that attendees introduce her to relevant contacts, either directly or via her CMU email, and offered to share a recruitment blurb.  
  * DM suggested YL also engage the CCC's Outreach Committee (meets alternating Wednesdays, 8am PT) and relevant mailing lists. Rene Kolga shared a link to ML Commons' MedPerf initiative in chat as a potentially related effort. Mic Bowman offered to personally facilitate an introduction to that group and invited YL to join related policy discussions.  
* **CCC Research Grant Program Update** – Mingshen Sun (MS)  
  * MS reported that the CCC's research grant program received 35 proposals from institutions worldwide this cycle, with two university projects (the two presented above) selected for funding at $45,500 each. DM thanked MS for leading the program and Fritz Alder for helping review proposals.  
* **TAC Funding for Research (2027 Budget Brainstorm)** – Dan Middleton (DM)  
  * DM raised the idea of the TAC setting aside budget to continue funding research of this caliber going forward, but deferred detailed discussion in the interest of time (to allow time for the continuous attestation presentation). DM asked attendees to drop ideas into chat or the mailing list and said he would dig up a related GitHub issue from last year to use as a place to collect funding ideas.  
  * MB flagged that setting aside TAC budget for this purpose is more legally/organizationally/tax-complex than expected, and that such a research fund more likely needs to be funded directly by member companies rather than reallocated from existing TAC budget.  
* **Continuous Remote Attestation Framework** – Jens Alberts (JA), with Jason Rogers (Invary) and collaborators from MITRE, and Manu Fontaine (Hushmesh)  
  * JA presented the public-review draft (v0.96) of a continuous remote attestation framework, developed with MITRE, Invary, Fr0ntierX, and Hushmesh, open for public review through the end of the month. The framework addresses a gap in launch-time attestation: existing schemes verify a genuine TEE and starting state but do not continuously verify what happens afterward (loaded executables, kernel modifications, outbound connections, etc.).  
  * The framework builds on RFC 9334 (RATS), defining a three-layer evidence model (L1: genuine TEE/platform state; L2: software/provenance since boot; L3: continuous runtime state, on a policy-defined interval), plus an informative GPU evidence layer. It uses a split-verifier model (raw evidence stays local; only signed results leave the boundary) and recommends three trust outcomes — pass, alert, and fail — with defined behavior on freshness, ordering, authenticity, and silence (a report missed across two intervals is treated as a fail). It does not endorse any commercial product.  
  * Discussion: AF asked whether the paper's "target machine"/"tester" terminology maps directly onto RATS' "attester"/"verifier" terminology; JA confirmed the mapping was intentional and agreed to add an explicit decoder table in the next revision. DM asked JA to clarify the paper's references to "eBPF behavioral sensors" and practical use of IMA (Integrity Measurement Architecture); JA acknowledged the paper needs more elaboration there and offered to follow up in Slack/the TAC channel. Jason Rogers and Ofir Azoulay-Rozanes discussed IMA's role in verifying on-disk and in-memory kernel integrity, and confirmed the framework is not limited to a specific TEE vendor (applies across TDX, SEV-SNP, etc.).  
* **CCAF (Confidential Compute Assurance Framework) Progress** – Solomon Cates (SC), Dan Middleton (DM), Mike Bursell (MB)  
  * DM noted the CCAF document has been migrated to its new, globally accessible Linux Foundation location (per the prior meeting's action item), though comments from the old Google Doc did not carry over automatically.  
  * SC proposed exploring a collaborative reference architecture effort that would connect the CCAF, the continuous attestation framework, and other in-flight work, potentially organized around a concrete customer or industry problem (biomedical and financial services were suggested as candidates). MB noted the TAC has historically been effective at short-term collaborative work but has struggled to pool compute/people resources across companies outside the context of an existing open source project. DM suggested that standing up a formal open source project (with at least one company willing to sponsor it) is the CCC's normal mechanism for pulling together resources like hardware allocations.  
  * DM revisited the scoring/weighting system for CCAF, proposing to cut the scoring section out of the document for now and return to it after the underlying security objectives are further along. SC reiterated CCAF's intent is to serve as a weighting/guidance tool for regulators and standards bodies rather than something shown directly to end customers, and said the team remains open to adjusting or removing scoring/weighting. DM said he still has a fundamental concern with weighting, since the relative importance of a given control depends heavily on use case and threat model. MB noted that several open questions in this space intersect with AWS's areas of expertise; AWS is not currently a CCC member, and MB is working to reconnect with them.

## **Work in Progress**

* Not discussed. 

## **Future Business**

* Next meeting will be October 1, 2026  
* Rotating chair(s): Dan Middleton or Ijlal   
* Annual Project Review: ManaTEE, dstack 

## **Action Items**

* David Oswald / Qifan Wang: Share the link to the referenced Meta confidential-AI white paper and distribute the presentation slide PDF to attendees.  
* Yanzi Lin: Send a recruitment blurb to attendees and join the CCC Slack channel to make herself reachable for introductions.  
* Yanzi Lin: Reach out to the Outreach Committee and relevant mailing lists for industry contacts for her confidential-computing-in-healthcare adoption study.  
* Mic Bowman: Facilitate an introduction between Yanzi Lin and the ML Commons MedPerf initiative.  
* Mike Bursell: Attempt to reconnect with AWS regarding potential involvement in CCC/CCAF-related discussions.  
* Dan Middleton: Copy his previous comments from the old CCAF document into the new document, and ask Mark Bower to do the same.  
* All attendees: Review the new CCAF document and provide feedback/comments within the next week.  
* Jens Alberts: Add a terminology-mapping table (target machine/tester vs. attester/verifier) to the next revision of the continuous attestation framework paper, and follow up (via Slack/TAC channel) on outstanding questions regarding eBPF behavioral sensors and practical use of IMA.  
* Solomon Cates: Continue exploring, with the group, a collaborative reference architecture and/or open source project, potentially anchored to a specific customer or industry use case (e.g., biomedical or financial services).  
* Dan Middleton: Dig up the GitHub issue from last year on TAC funding ideas and circulate it for further discussion.


---

