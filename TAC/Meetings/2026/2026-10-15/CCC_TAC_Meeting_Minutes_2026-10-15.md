# CCC TAC Bi-Weekly Meeting Minutes: October 15, 2026

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
* **Zoom for CCC TAC meetings**: [https\://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e) 

## **Agenda and Minutes**

* Dan Middleton (DM) opened the call at 7:03 am PT.  
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.  
* MR recorded the meeting minutes.  
* DM reviewed the agenda: a VirTEE project update, the 2027 TAC budget, final edits on the Agentic AI paper, and a new post-quantum cryptography (PQC) discussion.  
* DM took a quick roll call for quorum: Nathaniel McCallum (AMD) and Scott Raynor (Intel) were present; no one from Google, Huawei, Meta, TikTok (Mingshen Sun), or Shielded Technologies (Bob Blessing-Hartley) was on the call. DM noted the TAC did not have quorum and the group would avoid formal votes, working instead by general consensus as usual.

## **Attendance**

Per the \[charter\](https\://charter.confidentialcomputing.io), all \[CCC Premier members\]([https\://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [ ] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [ ] Fritz Alder (NVIDIA)   
- [ ] Mingshen Sun (TikTok)   
- [x] Nathaniel McCallum (AMD)  
- [ ] Rene Kolga (Google)  
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
- [x] Michelle Roth (LF PMO)  
- [x] Mike Bursell (CCC ED) 

### Other Attendees

* Chandra Nelogal  
* David Dooling (Arjuna)  
* Edward Boggis-Rolfe  
* Jagannathan (Jag) Raman (Oracle)   
* Jens Albers (Fr0ntierX)   
* Jeremy Powell (AMD)   
* Kailun Qin (Intel)   
* Manu Fontaine (Hushmesh)  
* Mona Vij (Intel)   
* Nick Renner (Fr0ntierX)   
* Ofir Azoulay-Rozanes (Anjuna)   
* Rachel Wan (Google)   
* Steven Bellock (NVIDIA)  
* Thore Sommer (Veraison Project) 

## **Welcome New Community Members**

* David Dooling (Anjuna Security): Introduced himself, joining from St. Louis, working with Ofir Azoulay-Rozanes on Anjuna’s confidential computing platform.

## **Old Business**

* DM provided a brief recap of the October 1, 2026 meeting, noting the 2027 funding GitHub issue (open for over a month), Michelle Roth’s discussion of project lifecycle process and benefits, a well-received dstack project update, and a final call for comments on the Agentic AI paper. DM noted he’d checked the CCAF document before building this agenda and, seeing no additional comments since, did not plan to revisit it in depth today.


  
**Announcements**

* A new Premier member, Alpha Compute, was welcomed; no designated TAC representative from them has been identified yet. DM noted some attendees may already have met Alpha Compute’s leader, Brittany, who spoke at this past summer’s Confidential Computing Summit.  
* TAC chair election season is approaching; DM reiterated he will not be running again this year and welcomes anyone interested in stepping up, offering to help them find their own approach to running the role.  
* The CCC governing board met the day before (Oct 14\) and discussed the TAC’s requested 2027 budget. DM reported healthy discussion and no critical pushback, with the board planning to take a couple more weeks to review before voting.

## **New Business**

* **2027 TAC Budget / Project Funding (GitHub issue \#393)**  
  * Simon Gallagher (SG), CCC Treasurer, reiterated that any further TAC budget asks should be logged in the GitHub issue soon so they can be rolled into the board’s budget process.  
  * Edward Boggis-Rolfe asked what the funding can be used for and what counts as an “admitted” project. DM explained TAC funding goes to projects already admitted to the CCC, framed as either removing obstacles for maintainers or amplifying their existing work; admission requires the project be open source under a recognized license (e.g., Apache 2.0 or similar) and go through the project proposal process documented in the governance repo (Project Submission Template, Project Progression Policy).  
  * DM noted that what the board was asked to approve yesterday included continued support for Veraison (a project with broad applicability across hardware architectures, previously funded by board vote) and a new ask for a security-audit bid for the SPDM project; the TAC hasn’t yet decided which specific project would receive the audit, reasoning that audits are more valuable for projects with enough maturity to avoid heavy churn.  
* **Gramine funding request** — Mona Vij (MV): MV reiterated essentially the same request as the prior meeting, with additional detail. Gramine remains one of the most broadly adopted SGX-era confidential computing projects, but lost Intel’s formal backing last year; it retains some NSF funding and volunteer maintainers, but some maintainers can no longer work on it unpaid. With Intel now end-of-lifing SGX (and most CSPs expected to drop SGX support over the next 3–4 years), the project’s focus has shifted to Gramine-TDX, which remains proof-of-concept (versus Gramine-SGX’s production maturity) — roughly 70% of the code is shared, with the remaining \~30% reflecting a different software architecture split across separate Gramine-VM and Gramine-TDX components. MV noted SEV-SNP and Arm CCA support could follow relatively easily once the VM-based architecture is solid. MV asked for CCC funding to bring Gramine-TDX to “cloud-ready” maturity, noting Gramine is close to the only major CC project without a big-company backer.  
  * MV separately asked whether past equipment/infrastructure budget CCC has provided to Gramine could be redirected toward this ask; SG and DM clarified infrastructure funding (the up-to-\$7,500/year line item) is allocated per-year and would need to be requested again for the following year, though in practice underused amounts are sometimes reapportioned.  
  * MV raised a broader question: whether CCC projects without a backing company inherently struggle, citing Gramine and another project that lost Red Hat’s support, and offered to personally make the case for Gramine’s value to any interested member company present. DM agreed this reflects the general dynamic in open source — companies invest once a project is adopted into production and tied to revenue — and that early-stage projects face a “chicken and egg” problem; MV agreed and reiterated her belief Gramine-TDX can reach production viability with modest additional support.  
  * DM agreed to send a note to the board including MV’s additional request; SG asked that it be tracked in the GitHub issue for a clear record, which DM agreed to.  
* DM noted this year’s funding ask is larger than any prior year’s; direct project funding is unusual for open source foundations but core to the CCC’s purpose, so the TAC intends to ask what it can of the board and membership.  
* SG, in his first budget cycle as Treasurer, encouraged the community to bring forward multiple well-justified, itemized asks (what would be delivered for the money) rather than raw totals, to support future prioritization conversations, noting CCC funding isn’t unlimited.  
* **Agentic AI White Paper — Final Edits**  
* Status: since the Oct 1 meeting, Mike Bursell (MB) and Raghu (Raghuram Yeluri, again not present) restructured and simplified the paper, and additional comments/responses had come in since.  
* Ofir Azoulay-Rozanes (OAR) flagged an unresolved consistency issue: the paper is largely framed around agents, but also references protecting model weights/LLMs in a way that could wrongly imply protecting the agent also covers the LLM. She left the comment unresolved for group discussion rather than editing it herself, noting the existing risk/mitigation table at the end may already cover this point.  
* DM asked whether anyone present had hands-on experience building agents to weigh in on whether a “lightweight” agent typically bundles its own on-device model versus calling out to a cloud-hosted one. MB and Edward Boggis-Rolfe (EBR) said they had (EBR mentioned running llama.cpp inside SGX); OAR noted that in her experience the LLM is frequently a separate/external component even when self-hosted. MB noted the current wording (possibly his own earlier edit) may need to anticipate future deployment architectures rather than only the current state; DM opened a to-do to address this offline.  
* EBR also raised “agentic governance” considerations — validating that an agent is connecting to a legitimate MCP service and vice versa — and referenced related work led by Mark Novak in the GRC SIG on confidential inference/training, and mentioned (without detailing) a confidential-computing-aware MCP wrapper he’s built, offering to demo it at a future meeting.  
* Manu Fontaine (MF) walked through several proposed edits built around the idea that TEEs provide not just execution isolation but full-entropy random number generation inside the trust boundary, letting software agents generate their own keys and cryptographically isolate their own knowledge:  
* A more rigorous definition of agent identity tied to verified execution and authentication credentials, emphasizing that any unverified external trust dependency undermines the whole chain. **DM called for objections; none raised (called twice) — accepted by consensus.**  
* Wording tying this key-generation capability to delegated authority and chained agent-to-agent authentication. **DM called for contrary feedback; none raised — accepted.**  
* A new “Agentic Knowledge Isolation” property added to the paper’s concluding list of CC properties. OAR asked that the same concept also be reflected earlier, in the identity/trust section (not just the later table), so the paper doesn’t give a false impression that attestation and software measurement alone are sufficient — agreed by the group, noted as a partial (not full) data-layer coverage improvement, since an agent that can encrypt/protect its own knowledge only partially closes that gap.  
* Discussion on a table of example CCC projects referenced in the paper: DM said he deliberately excluded two projects Rene Kolga (not present) had suggested — one single-contributor project and one non-CCC project — feeling it odd to point readers at an unaffiliated project, but did add Gramine (at MV’s suggestion) with a short blurb for each listed example. OAR questioned whether several of the listed examples are genuinely AI/Agentic-specific versus generic CC capabilities, and whether a reader could connect them back to the paper’s narrative. MB and MF argued for keeping the list as useful pointers, provided they’re clearly framed as supporting infrastructure; MF suggested adding a short sentence under each project explaining how it supports the Agentic story specifically, citing Gramine/small-TCB computing as foundational work relevant to Agentic use cases too. OAR agreed this framing helps, drawing a comparison to an existing CCC paper’s phased approach to CC adoption, and cautioned against over-compressing content into one document; MF agreed and suggested framing it as a focused “Agentic AI toolkit” of CCC components rather than going deep on each one.  
* DM asked MB whether the earlier Mike/Raghu restructuring intended this paper to be followed by a second, more reference-architecture-focused paper; MB confirmed that’s the plan — ship this paper first, then build a more rigorous reference architecture on top, which had the group’s general support. EBR argued the deeper underlying challenge for such a follow-on paper is interoperability across different agent communication protocols (REST, gRPC, WebSockets, MCP, A2A, etc.); he described his own approach of an RPC-style abstraction over a shared confidential-computing substrate, with protocol-specific formatting layered on top, and offered to demo this at a future meeting.  
* DM proposed accepting the paper largely as-is, resolving the one or two remaining loose ends (chiefly the model-weights/LLM-boundary wording) offline with Raghu (and Mike or others interested), and then publishing.  
* **Decision:** DM asked whether there was any “heartburn” with proceeding to publish the paper substantially in its current form, once the model-weights wording is finalized. MB asked if this meant the group was approving it; DM confirmed, noting the TAC likely lacked quorum for a formal vote and, per normal practice, works by general community consensus rather than formal votes. **No objections were raised — the paper is approved to publish once DM finalizes the model-weights language with Raghu and circulates it for offline acknowledgement.**  
* **Post-Quantum Cryptography (PQC) SIG Proposal — Rachel Wan (Google, formerly IBM)**  
  * Rachel Wan (RW) proposed forming a new Special Interest Group (SIG) under the TAC focused on PQC readiness strategy and industry guidance, citing PQC as a strategic priority on par with digital sovereignty, rising attention across the industry (including from Google), and a desire for the CCC to engage proactively. Proposed key themes: gathering technical roadmap input from hardware partners (Intel, AMD, NVIDIA, Arm), publishing PQC use cases and guidance content, and connecting the TEE story to business value without overpromising.  
  * DM offered general guidance on chartering new CCC SIGs based on past experience: favor a narrow, concrete scope and a single initial deliverable over a broad, governance-heavy charter or open-ended list of activities, since groups with momentum around one deliverable tend to succeed while open-ended discussion groups tend to lose steam. He suggested starting a mailing-list thread and, in parallel, opening a governance-repo issue to sketch out the charter.  
  * Mike Bursell (MB) outlined three possible scope directions, cautioning the group to be explicit about which are in scope (they need not be mutually exclusive): (1) PQC support within core confidential-computing architecture itself (e.g., firmware/attestation support for PQC algorithms) — which he felt is close to “table stakes” and possibly more coordination than TAC-led work; (2) extending existing CCC-adjacent standards work (e.g., RATS-TLS) to properly incorporate PQC algorithms, aligned with external standards bodies (IETF, IEEE) — which he felt fits well within the TAC’s normal remit; and (3) a broader policy/architecture question of how confidential computing can help address “harvest now, decrypt later” risk and support quantum-computing-preparation/legacy-migration planning generally — which he was less certain fits the SIG’s scope.  
  * Chandra Nelogal (CN) asked whether the SIG’s scope is primarily industry-scanning/documentation of PQC alignment work already underway elsewhere (citing TCG Storage’s PQC-aligned messaging protocol work and SPDM’s already-released PQC-aligned spec update) versus original technical work; MB confirmed this maps to his “bucket two” framing (reacting to and integrating with external standards work, rather than leading new primary work).  
  * **Consensus: proceed with Rachel leading formation of the SIG via a mailing-list discussion thread and a governance-repo issue to sketch the charter**; EBR mentioned he’s working on a pluggable key-exchange protocol (not yet including lattice-based/PQC schemes specifically), and CN cited his TCG Storage and SPDM standards background as potentially relevant.  
* **Data Storage Requirements for Confidential Computing** — Chandra Nelogal  
* CN asked for agenda time at the October 29 meeting to present data storage requirements as they pertain to confidential computing. DM confirmed there should be room on the agenda.

## **Work in Progress**

* VirTEE project update — not delivered this meeting; presenter Tyler Finelli did not join. Expected to be rescheduled to the October 29 meeting.

## **Future Business**

* Next meeting will be October 29, 2026\.  
* Rotating chair(s): Mingshen Sun, if available, is expected to co-chair.  
* VirTEE project update (Tyler Finelli) — rescheduled from this meeting.  
* Attestation (working group/SIG) update expected.  
* Chandra Nelogal to present data storage requirements for confidential computing.  
* CCAF (CACAF) document: Mike Bursell noted the governing board briefly discussed, the day before, how to move the CCAF document forward, though he could not recall the specific outcome. DM asked all attendees to continue reviewing and commenting on the CCAF document (links on the mailing list), specifically considering whether its current content aligns with how their own company would define confidential computing.  
* PQC SIG formation to begin via mailing list and governance repo issue.

## **Action Items**

* Dan Middleton: Send a note to the governing board including Mona Vij’s additional Gramine funding request.  
* All project maintainers / TAC members: Continue submitting 2027 budget and project funding asks into GitHub issue \#393, with clear itemized justification, as soon as possible.  
* Mona Vij: Provide a short chunk of wording for the Agentic AI paper recognizing/clarifying the earlier model-weights/agent feedback.  
* Dan Middleton: Work offline with Raghu (and Mike Bursell or others interested) to finalize wording on model weights/LLM-vs-agent trust boundaries in the Agentic AI paper, then send a note to the mailing list for offline acknowledgement before publishing.  
* Rachel: Start a thread on the governance mailing list and open an issue in the governance repo to sketch out the PQC SIG’s charter.  
* Chandra Nelogal: Prepare and present data storage requirements for confidential computing at the October 29, 2026 TAC meeting.  
* All attendees: Review and provide feedback on the CCAF (CACAF) document via the links on the mailing list.  
* Edward Boggis-Rolfe: Offered (not firmly scheduled) to demo his confidential-computing MCP wrapper / RPC-based interoperability work at a future meeting.


---

