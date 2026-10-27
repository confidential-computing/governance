# CCC TAC Bi-Weekly Meeting Minutes: October 1, 2026

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
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* MR recorded the meeting minutes.  
* DM reviewed the agenda. 

## **Attendance**

Per the \[charter\](https\://charter.confidentialcomputing.io), all \[CCC Premier members\]([https\://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [ ] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [ ] Fritz Alder (NVIDIA)   
- [ ] Mingshen Sun (TikTok)   
- [ ] Nathaniel McCallum (AMD)  
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
- [x] Michelle Roth (LF PMO)  
- [x] Mike Bursell (CCC ED) 

### Other Attendees

* Chandra Nelogal  
* Hang Yin (Phala, dstack Project)  
* Hesham ElBakoury (Innovax Technologies)  
* Jagannathan (Jag) Raman (Oracle)   
* Jens Albers (Fr0ntierX)   
* Jeremy Powell (AMD)   
* Manu Fontaine (Hushmesh)  
* Mark Novak (JP Morgan Chase)  
* Mona Vij (Intel)   
* Nick Renner (Fr0ntierX)   
* Ofir Azoulay-Rozanes (Anjuna)   
* Sakul Gupta (Micron)  
* Steven Bellock (NVIDIA)  
* Thore Sommer (Veraison Project)   
* Yogesh Deshpande (Arm) 

## **Welcome New Community Members**

* Jagannathan “Jag” Raman from Oracle (JR): Introduced themself as a confidential computing and remote attestation specialist at Oracle, attending this TAC meeting for the first time (though he regularly attends the Veraison weekly meetings and a bi-weekly confidential computing meeting). JR raised a question about virtual TPMs (VTPMs) in confidential computing, looking for pointers to relevant open source discussion forums. DM clarified that VTPM is an overloaded term — some implementations are purely software-based with no hardware backing and aren’t properly “confidential computing” — and noted that of the four major CC-capable CPU architectures, three (Intel TDX, Arm CCA, and RISC-V CoVE) have native runtime measurement registers, while AMD SEV-SNP does not, which is typically why people reach for VTPM-based approaches there.  
* Chandra Nelogal from Wiwynn (CN): Introduced themself as working for a server ODM company, with a long-standing interest in confidential computing applied to storage (both at the device level — HDD/SSD — and the system/storage-array level), driven by CPU/GPU vendors and hyperscalers increasingly looking at confidential compute for storage. CN noted prior involvement chairing the TCG Storage Work Group and currently chairs an IEEE working group in this space. DM invited CN to come back and lead a discussion on this topic at a future meeting once they have had a chance to gather requirements from CPU/GPU vendors and hyperscalers; CN said the next meeting (Oct 15\) conflicts with the OCP Global Summit, but offered to do so, tentatively, at the November meeting.

## **Old Business**

* DM provided a brief recap of the September 17, 2026 meeting, noting the research grant project updates, the TAC budget discussion that was introduced (and has since been open for community feedback via a GitHub issue for the past couple of weeks), Jens Albers’ walkthrough of the MITRE-collaborative continuous attestation paper, and work done on the CCAF proposal. DM noted the Agentic AI white paper was intended to get attention but did not receive any material work at the last meeting.


  
**Announcements**

* Linux Plumbers Conference is coming up early next week; Mike Bursell (MB) noted the Linux Security Summit is also happening next week in Prague, with no specific CC-focused sessions on the agenda this time, but historically a good venue for informal CC conversations (including a confidential computing “birds of a feather” session). Neither DM nor anyone else present expected to attend in person; MB offered to find and share links for remote participation options.  
* TAC chair election season is approaching. DM announced he does not intend to put himself forward as TAC chair for the coming year, as his responsibilities are expected to shift toward the governing board, and encouraged others in the community to consider stepping into the role. MB echoed this, emphasized Dan isn’t going anywhere, and invited anyone interested to reach out to discuss what the role involves.

## **New Business**

* **Project Lifecycle / 2027 Budget & Support Discussion** — Michelle Roth  
  * MR explained that, as part of getting up to speed supporting the CCC and with budget season approaching, she has been reviewing how CCC projects are currently supported and reaching out to project maintainers, with an eye toward whether the CCC could support projects differently or better. She noted the current standing line item of up to \$7,500/year per project for hardware/software does not appear to be heavily used, and invited projects to raise other funding needs (grants, research, event/travel support, etc.) so the TAC can take proposals to the governing board for 2027\.  
  * DM added that unused project-specific budget (e.g., underused test infrastructure funds) has in the past been reapportioned to where it was needed — this is partly how Veraison’s funding this calendar year was supported.  
  * **Gramine** — Mona Vij (MV): Mona reported that Gramine (originally focused on Intel SGX) was supported by Intel for a long time, but Intel dropped that support last year. Several companies (including IBM and various startups) use Gramine but have never financially supported the project; it currently has only volunteer maintainers, and Intel’s former key maintainers can no longer afford to work on it unpaid. The focus has shifted from SGX to TDX (a Gramine-TDX proof of concept already exists), but MV has been unable to get major companies to commit to supporting a lightweight CVM approach. MV asked whether the CCC could fund one or two maintainers (likely from Intel) to continue pushing Gramine-TDX toward production quality.  
    * MB offered to connect with MV offline about known Gramine users who might be willing to help support the project (to run in parallel with, not instead of, CCC funding).  
    * Manu Fontaine (MF) noted Microsoft recently announced plans to retire their SGX servers within three years, and expressed strong interest (though noting Hushmesh is small) in helping push cloud service providers toward supporting a small-attack-surface approach like Gramine-TDX, since keeping the CSP out of the TCB is central to the point of confidential computing.  
    * MV noted an earlier conversation with Microsoft (via a contact named Vikas) about a Gramine-TDX transition plan that didn't go anywhere, and said she’d try again. Simon Gallagher (Microsoft, CCC Treasurer) offered to help broker/route that conversation on Microsoft’s side; MF asked to be looped in as well.  
  * **Veraison** \- Thore Sommer (TS): TS outlined three budget dimensions Veraison is currently evaluating: (1) infrastructure — moving beyond their current GitHub-org-hosted setup toward more automated testing/deployment, especially as more CC hardware from more vendors needs to be supported and deployment use cases grow; (2) project management — dedicated maintainer/contact-person support to push the project and help it advance toward graduation within the CCC and other venues; and (3) mentorships — continuing past success with LFX mentorships and potential interns.  
  * DM asked everyone to log funding needs into GitHub issue \#393 so he can take proposals to the governing board. He also shared last year’s budget-request issue for reference, noting that a planned SPDM project security audit and support for Gramine both went unfunded last year due to budget cuts, and he’s hopeful for a better budget this year.  
  * MB emphasized that funding and promoting open source projects is core to the CCC’s purpose, noted that more CCC projects are used commercially than people may realize, and strongly encouraged everyone (live or watching the recording) to add their thoughts to issue \#393.  
  * DM raised that the historical split between outreach and TAC/project budget may be disproportionate, since outreach funding tends to get consumed quickly on conference support, whereas project funding has more lasting benefit.  
* **Ambassador and/or Mentor programs**  
* Simon Gallagher (SG) noted the existing CCC budget includes a line item for an “ambassador program” and asked whether the group wanted to capture related funding needs here.  
* MR clarified that ambassador programs (outreach, event participation, content creation, geographic/community representation) and mentorship programs (onboarding new contributors and pairing them with existing projects/community members) serve different goals and are typically budgeted/scoped separately. Both would need their own scoped proposal and community support before funding is approved; funding for either is separate from the TAC project-support line item.  
* DM noted that in the past, Yash (Red Hat) led the CCC’s mentorship program, and that none of these programs run without someone from the community stepping up to lead them (even a modest time commitment). MB confirmed that he, Michelle, and Ben can provide operational/logistical support, but the community still needs someone to serve as the lead.  
* **Agentic AI White Paper — Review Status**  
  * Scott Raynor (SR), standing in for lead author Raghu (Raghuram Yeluri), who was again absent, reported that Raghu had already gone back through and addressed most previously open review comments, including adding a new table, but it was unclear whether the original commenters had confirmed they were satisfied with those responses.  
  * Ofir Azoulay-Rozanes (OAR) and MB both said they were unaware updates had been made and would need to re-review before weighing in further.  
  * MB raised an immediate comment on the paper’s title: he’s comfortable discussing “Agentic Computing” in the body of the paper, but felt strongly the title itself needs to include “Agentic AI,” since that’s the terminology people are actually searching for. MF said that, as a general (non-voting) community member, he doesn’t have a formal vote on the document, but agreed with the concern and was fine with the change.  
  * DM clarified that the CCC does not generally distinguish between voting and non-voting member input on community documents like this — the goal is general consensus from whoever participates, not unanimity.  
  * Following a brief audio/recording glitch, MF responded to OAR’s underlying concern about the paper’s framing (see below), arguing that the core value proposition of confidential computing for Agentic AI is knowledge isolation, not just execution isolation: a software actor running in a TEE that can generate its own full-entropy keys can protect its own information end-to-end, creating a verifiable chain of provenance, confidentiality, and custody as data moves between software actors and ultimately into a model. He noted the model itself remains stochastic, but everything else — weights, code, prompts, system prompts — can have guaranteed provenance and integrity. He acknowledged this capability is broader than Agentic AI specifically, which prompted MB to half-joke about a possible follow-on paper on confidential computing for agentic/distributed systems more generally.  
  * OAR clarified her concern more precisely: she’s worried the paper’s current framing risks telling potential customers that the CCC’s general confidential-computing messaging simply carries over unchanged to Agentic workloads, without being specific about what unique problem is actually solved (e.g., an agent can have a non-spoofable identity, but what does that identity actually guarantee?). She felt this creates a false impression of CC’s value for Agentic specifically, and noted a comment from Rene Kolga (not present) raising the same concern — that the content read as the generic CC story rather than something Agentic-specific.  
  * MB reframed the discussion around two foundational questions he felt need to be answered before the paper can move forward: (1) who is the paper’s target audience/persona (e.g., low-level developers, engineers, CFOs/business decision-makers, people buying systems, marketing audiences — he noted these are all very different audiences and the current draft seems to address several at once); and (2) what specific problems does Agentic AI have that confidential computing uniquely solves, rather than the generic “why CC is good” pitch the CCC makes for everything else. MB suggested the paper may ultimately need to be split into more than one document to properly serve different audiences.  
  * Chandra Nelogal (CN) raised a related point of confusion in the current draft: the second paragraph of page 2 doesn’t clearly define who the “attestation verifier” is in the scheme described (e.g., is it the storage device, or the processor executing the confidential workload?). DM suggested this maps to the concept of a “relying party” and recommended CN add a clarifying comment directly into the document, since the current language may be too technical for the intended audience.  
  * DM noted that Rene Kolga, who originally raised the audience question in a GitHub issue, was not present to clarify his original intent live; DM had looked back at that issue but felt it didn’t fully resolve the question. DM’s own view is that current CCC white papers generally try to aim for a middle ground between a highly technical audience and a high-level decision-making audience.  
  * Separately, SR flagged a related open/unresolved comment in Section 3 (the last line of 3.2) concerning use of a protected, hardware-backed random number generator. MF explained this ties back to his knowledge-isolation argument: a workload that can generate full-entropy keys inside its own trust boundary — and only recovers access to those keys after being independently re-verified by an attestation verifier (e.g., on restart) — provides a composable security primitive that avoids ever exposing keys to a cloud provider or other control plane. MF noted he had already added some less-technical language to the document earlier in the week, in response to a request from Raghu to simplify an earlier, more technical version of his comment.  
  * OAR proposed, and the group agreed, that the concrete action item is to explicitly answer, at the top of the document: (1) who is the target persona for the paper, and (2) what Agentic-AI-specific problems — solvable only by confidential computing — the paper should present to that persona. OAR added these two questions to the top of the document live during the meeting.  
  * MB committed to reviewing the paper the next day with these two framing questions in mind. Hesham ElBakoury mentioned there are existing surveys on the applicability of confidential computing to Agentic AI and agreed to add relevant links/examples directly into the document itself (rather than the meeting chat, at MB’s request, so the references aren’t lost).  
  * SR confirmed he would follow up with Raghu offline about the outstanding comments and try to get him to attend the next meeting, noting the group is coming up on a stretch with fewer meetings around the holidays, so this should be prioritized soon.  
  * DM closed the topic by asking everyone to finish their comments on the Agentic AI paper before the next meeting.  
* **CCAF Framework**  
  * Not reached this meeting. DM noted the group will need to turn attention back to the CCAF paper at the next meeting and expects it will need considerable additional work.

## **Work in Progress**

* **Annual Project Review: dstack** — Hang Yin (HY), Phala  
  * HY presented dstack’s annual update. dstack is a confidential container runtime designed to simplify deploying confidential workloads (install the runtime, supply a container definition, let it handle attestation, networking, and key management) without sacrificing security guarantees. Networking runs through an attested-TLS gateway; a Key Management Service (KMS) releases keys only after an application is attested and passes policy (policy can reference an external root CA or even a smart contract).  
  * Growth since joining the CCC as a project last year: GitHub stars roughly doubled (from \~200 to \~400+), with PRs, issues, and user engagement activity also roughly doubling. The project progressed through roughly 10 iterations from a 0.5.5 baseline and is now targeting its first stable 0.6 release. Dozens of public and private security reports were addressed this year, typically resolved within about a week.  
  * New hardware/platform support added this year: GCP (Intel TDX-based, but requiring VTPM in addition to GCP’s own attestation since part of GCP’s TCB isn’t fully open source), AMD SEV-SNP (challenging due to the lack of dynamic PCR-style measurement registers; addressed via an ACPI-table firewall approach adapted from Edgeless Systems plus early-boot measurement/policy checks), and AWS Nitro EC2 attestation (not hardware-based confidential computing, but usable via VTPM-based attestation). GPU support expanded from Hopper to also include Blackwell, with the CPU only releasing sensitive data to the GPU after GPU attestation is independently verified.  
  * Orchestration: the team experimented with building a service mesh across multiple dstack CVMs using Envoy and SPIFFE-based workload identities, coordinated by an attesting coordinator and defined via a Terraform plugin — described as a promising experiment, not yet at the maturity of a full Kubernetes-based service mesh.  
  * Performance work: identified and addressed three bottlenecks — (1) the lack of RDMA under NVIDIA’s confidential-computing mode (an industry-wide unsolved problem; dstack published a research preprint characterizing this on Blackwell GPUs), (2) the default QEMU network stack degrading badly under high concurrent-connection counts (addressed by reworking dstack’s network stack), and (3) TDX-module interrupt-handling overhead under I/O-heavy workloads (addressed via interrupt batching, yielding up to \~2.8x performance improvement in some workloads).  
  * Other improvements: migrated the build system (cutting build time from roughly an hour to a few minutes), integrated with Intel Trust Authority, simplified onboarding to a single command, and reworked documentation.  
  * New specification work: proposed an “Attested Confidential Inference” specification so users can verify end-to-end that prompts/outputs are never exposed to any third party, across multiple TEE/GPU providers, using a recursive front-end/back-end verification model (so an end user need only verify the entry point of a multi-hop inference service). dstack also ships a desktop “verifier” client (similar to a VPN client) that can automatically configure coding agents to use attested connections. Reported throughput on their router (listed on OpenRouter) has grown from roughly 1–2 billion tokens/day early this year to over 200 billion tokens/day currently.  
  * Roadmap: additional platform support (Arm CCA, NVIDIA Vera Rubin), continued attestation usability work (including alignment with RATS/trustworthy workload identity standards), production-grade orchestration (Kubernetes/Confidential Containers integration with workload identity and service mesh), potential approaches to the RDMA problem, and eventual TDISP support.  
  * Discussion: Chandra Nelogal asked how dstack addresses data in the I/O subsystem (network/storage), beyond the usual compute/memory confidential-computing threat model. HY acknowledged this is a real, largely unsolved challenge — particularly moving KV-cache data (GPU VRAM → CPU RAM → SSD, and across multiple servers) without RDMA, since NVIDIA’s CC mode disables RDMA/InfiniBand between GPUs, which creates a meaningful performance penalty versus non-confidential competitors. DM (speaking from his NVIDIA background) confirmed NVLink fabric supports direct communication across up to 8 GPUs, but cross-node RDMA remains disabled by design for security reasons. DM also asked why dstack supports such a broad span of cloud/hardware combinations; HY explained this reflects wherever customers can actually obtain GPU capacity, existing cloud-account/policy lock-in at customer companies, and that some high-value customers (e.g., managing blockchain assets) deliberately want multi-cloud deployments to avoid single-provider dependency. Jag Raman asked how dstack worked around SEV-SNP’s lack of dynamic measurement registers; HY described the ACPI-table firewall and early-boot measurement/policy approach (open source, in their repo), noted SEV-SNP still lacks a true append-only dynamic measurement log equivalent, and mentioned the Coconut-SVSM project as another approach to the same problem.

## **Future Business**

* Next meeting: October 15, 2026\.  
* Rotating chair(s): **Unassigned.** Bob Blessing-Hartley is next in the normal rotation but is expected to be unavailable; as of the end of this meeting, no volunteer co-chair had come forward (see Action Items).  
* Annual Project Review: VirTEE.  
* CCAF (CACAF) framework review to resume.

## **Action Items**

* Dan Middleton: Find a volunteer co-chair for the October 15, 2026 meeting (Bob Blessing-Hartley is expected to be unavailable); none had volunteered as of the end of this meeting — coordinate via chat or the support email.  
* All project maintainers: Submit 2027 project budget and support needs into GitHub issue \#393 for governing board consideration.  
* Mona Vij: Pursue a renewed conversation with Microsoft regarding Gramine-TDX support/transition plans.  
* Mona Vij: Follow up with Mike Bursell regarding known Gramine users and potential supporters.  
* Mike Bursell: Email Mona Vij to discuss Gramine users and potential support.  
* Simon Gallagher: Help broker/route a conversation with Microsoft regarding Gramine-TDX support.  
* Thore Sommer: Submit Veraison’s budget/infrastructure, project-management, and mentorship needs into GitHub issue \#393.  
* Community members: Anyone interested in leading the TAC chair role, or leading/supporting an ambassador or mentorship program, should contact Dan Middleton, Mike Bursell, or Michelle Roth.  
* Hang Yin: Share an email address for follow-up questions on dstack (offered during the meeting for side/offline follow-up).  
* Ofir Azoulay-Rozanes: Added two framing questions to the top of the Agentic AI white paper — (1) who is the target persona, and (2) what Agentic-AI-specific problems can only confidential computing solve for that persona — completed live during the meeting.  
* Mike Bursell: Review the Agentic AI white paper against the two framing questions above and share initial thoughts (committed to doing so “tomorrow,” i.e., October 2, 2026).  
* Chandra Nelogal: Add a comment to the Agentic AI white paper clarifying who the “relying party” is in the attestation scheme described.  
* Hesham ElBakoury: Add links/examples of existing surveys on confidential computing’s applicability to Agentic AI directly into the paper document.  
* Scott Raynor: Follow up with Raghu (Raghuram Yeluri) offline on outstanding Agentic AI paper comments and try to get him to attend the next meeting.  
* All TAC members: Finish comments on the Agentic AI white paper before the next meeting.


---

