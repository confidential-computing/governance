# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, April 16, 2026

**Time**: 8a-9a US Pacific Time

* **Zoom**: [https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e)

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

* Alec Fernandez (AF) opened the call at 8:10 am PT
* AF welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Benjamin Sternthal created meeting minutes based on the transcript
* AF reviewed the agenda

### Roll Call / Attendance

No formal roll call was conducted as no votes were scheduled.

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum+ / David Kaplan
* Google - Rene Kolga+ / Keith Moyer
* Huawei - Zhipeng (Howard) Huang
* Intel - Raynor Scott+ / Simon Johnson
* Meta - Henry Wang / Kevin Hui
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder / Dan Middleton+
* Red Hat - Yash Mankad / Ram Pai
* TikTok - Mingshen Sun+ / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley

#### Other Attendees

* Ahmed Magdy (Meta Platforms, Inc.)
* Benjamin Sternthal (The Linux Foundation)
* Eric Hibbard (Samsung)
* Hesham ElBakoury (Innovax Technologies)
* Jens Albers (Fr0ntierX Inc)
* Jeremy Powell (Advanced Micro Devices)
* Manu Fontaine (Hushmesh)
* Ofir Azoulay-Rozanes (Anjuna)
* Piotr Zmijewski (Intel Corporation)
* Richard Zak (Booz Allen Hamilton, Inc.)
* Tom Jones (VeriClouds)
* Yi Liao (Automata Network)

## Welcome New Community Members

* Don Porter reintroduced themselves as a professor who has worked in confidential computing for a while and is a Gramine project maintainer.
* Kailun Qin introduced themselves as a member of the confidential computing team at Intel and a Gramine maintainer.

## Meeting Minute Approval & Old Business

* Alec Fernandez (A)F skipped old business due to a slide deck issue; the agenda moved directly to presentations.

## Tech Talk: Trustworthy Workload Identity for Replicated Workloads (JPMorgan Chase)

* Mark Novak (MN), chair of the Trustworthy Workload Identity SIG, presented a proposal for furnishing replicated confidential workloads with trustworthy identities using industry-standard bound credentials (X.509 certificates, workload identity tokens), with no changes required to the workload's clients or servers.
* MN described the business case: enterprises with ubiquitous workload identity (e.g., SPIFFE) want to gradually roll out confidential computing without disrupting existing relying parties. The proposal ensures a workload can be moved into a TEE with no or minimal code changes, and zero impact on its clients and servers—a key deployment requirement MN termed "relying party empathy."
* The proposal focuses on replicated (horizontally scaled) workloads—containers, serverless functions, and VMs that are functionally indistinguishable from the perspective of authentication and authorization—and can therefore share the same credential and cryptographic material.
* MN described how the proposal fits into the standards landscape: IETF RATS provides the building blocks and data formats; WIMSE (Workload Identity for Multi-System Environments) handles credential usage; the proposal addresses the gap of credential provisioning and credential acquisition, which currently falls in a "no-man's land" between the two.
* The provisioning flow involves the workload owner pre-assigning an identifier, predicting attestation results, generating cryptographic keys stored in an HSM with an access-control policy tied to attestation results, and creating credentials (public certificate plus a wrapped signing key). The acquisition flow involves each workload instance performing remote attestation using existing unmodified mechanisms, then using the attestation results to retrieve the unwrapped signing key inside the TEE.
* MN asked the TAC for review of the proposal document (shared via the mailing list as a Google Doc and PDF), support at the Vienna IETF meeting in July (submission deadline July 6), and eventually reference implementations from hyperscalers to demonstrate interoperability.
* Henk Birkholz (HB) expressed support and suggested exploring alignment with Microsoft's Confidential Computing Framework (CCF) for retaining ephemeral attestation state, and noted format synergy between WIMSE identity tokens and EAT (Entity Attestation Token) formats from RATS.
* Dan Middleton (DM) asked whether the WIMSE/SPIFFE identifier could carry additional assurance from the confidential computing attestation. MN argued against enriching the token, stating that additional assurance visible to relying parties would break the zero-impact deployment goal and shrink the addressable market.
* AF committed to shepherding the proposal review within Microsoft and connecting MN with relevant contacts (Greg Kostel, Cedric/CCF team). Rene Kolga (RK) volunteered to do the same at Google. MN will reach out to other hyperscalers independently.

## Gramine Annual Review

* Kailun Qin (KQ) and Mona Vij (MV) presented the Gramine annual review, with Don Porter (DP) also present as a maintainer. Gramine is a multi-process library OS that enables unmodified Linux applications to run on SGX, graduated to CCC in May 2023.
* KQ reported that Gramine v1.9 (latest production release) shipped in June 2025 with packages for Debian and Red Hat family distros, plus an official Docker image. The project maintains an active community with over 100 open issues and 50 pull requests.
* Key technical progress includes new SGX hardware feature support (AEX Notify, Key Separation and Sharing contributed by a commercial user), TCB migration for encrypted files (contributed by UIUC), new syscall support, performance improvements to the memory manager, and dropping support for legacy drivers and deprecated attestation schemes to reduce maintenance burden.
* KQ presented Gramine TDX, a new backend that repurposes the Gramine library OS for confidential VMs with a minimal TCB and attack surface—reducing over 70% of the codebase compared to a full Linux distro, with only three virtio drivers. This work was published at CCS 2024. Recent progress includes rebasing to the latest Gramine master, adding CI pipelines, and developing a co-VM deployment model that allows Gramine TDX to launch from a co-located parent VM in cloud environments (analogous to AWS Nitro Enclaves).
* MV reported that Gramine SGX is now in maintenance mode—existing customers continue to use it (notably IBM's e-prescription service), but new customer acquisition has slowed. Gramine TDX is the project's growth path. Intel has significantly reduced funding; the primary funding source is now NSF grants (third year). MV noted that three maintainers from Invisible Things Labs have limited availability due to the Intel funding reduction. MV is no longer at Intel but remains committed to the project.
* MV argued that the CCC should take a position on lightweight TDs, noting that current CVM deployments put full Linux distributions (and paravisors) inside the TEE, creating large TCBs with questionable security improvements over Linux with TXT. She pointed to Gramine TDX, Google's Project Oak, and Microsoft's Lightbox as projects pursuing minimal-TCB approaches, and noted that Project Oak maintainers expressed interest in using Gramine TDX if it were rewritten in Rust.
* Ijlal Loutfi noted potential synergies between Gramine TDX and the Coconut SVSM project's ambition (presented at OC3) to move beyond being just a paravisor and toward running general-purpose applications. KQ confirmed he is aware of the initiative and has reached out to the Coconut SVSM community.
* AF discussed Microsoft's interest in supporting both the VM model and the enclave model on TDX to serve customers like Signal who prefer SGX-style small TCBs. AF offered to connect the Gramine team with the OpenVMM (now open source) team at Microsoft to explore integration paths. MV noted that running Gramine on top of an OpenVMM paravisor might enable the "Gramine Linux" backend without requiring the full Gramine TDX stack.
* MV thanked the CCC for funding CI hardware upgrades and noted that the Linux Foundation funds a VPS server for packages.

## ISO Participation Update

* AF reported that the CCC has successfully established a formal liaison relationship with ISO Working Group 4 (convened by SC27), with AF serving as the CCC's representative.
* The ISO terminology standard for confidential computing (ISO 25093) is in final review and expected to be published soon. AF reported achieving 100% alignment between the ISO and CCC definitions of confidential computing, including resolution of differences around attestation.
* The next ISO document (ISO 25546) is in early stages and will cover architecture, requirements, components, and services for confidential computing—originally envisioned as a three-part series but now being combined into a single document titled "Technical Framework and Services." AF shared the chapter outline, which covers hardware root of trust, attestation, remote attestation, key derivation, composite devices, secure channels, and data sealing.
* AF is working to establish a process for sharing excerpts of the ISO document with the TAC for review, then channeling feedback back to Working Group 4 through the liaison. DM agreed this review work belongs within the TAC rather than the Regulations and Standards SIG.

## White Papers and Blueprints

* DM reported that Rene Kolga has been actively editing his document. Simon Gallagher (Microsoft) noted he expects to make progress on Blueprint B (secure key release) shortly.
* DM walked through updates to the "Three Degrees of Integration" document, adding language that explicitly states attestation integration is required before a deployment can claim to have adopted confidential computing, and that without attestation, a deployment does not meet the CCC definition of confidential computing. AF confirmed this addressed his previously raised concerns.
* DM also updated terminology to align with RATS where possible, replacing invented terms (e.g., "policy decision point") with standard RATS terminology while keeping the document accessible to readers unfamiliar with RATS.
* DM set a deadline to finalize the Three Degrees document and the Blueprints at the next TAC meeting (April 30), with a last round of comments due over the next two weeks. Once finalized, documents will be converted to Markdown and placed in version control, then handed to Linux Foundation Creative Services for final PDF layout.

## Any Other Business / Next Steps

* Fritz Alder is the next rotating chair (April 30 meeting); DM noted Fritz was out sick today. Ijlal Loutfi was identified as a potential chair for the May 14 meeting if Yash Mankad is still on leave.
* The Coconut SVSM annual review is scheduled for the next meeting (April 30). AF volunteered to give a tech talk on attestation for TEEs with composite devices at that same meeting.
* AF called for additional tech talk proposals, noting the pipeline of scheduled talks is diminishing.
* Members were reminded to review the Trustworthy Workload Identity proposal (via the mailing list), continue providing feedback on the Three Degrees document and Blueprints, and submit final comments before the next meeting.
* AF adjourned the meeting at approximately 8:49 am PT.
