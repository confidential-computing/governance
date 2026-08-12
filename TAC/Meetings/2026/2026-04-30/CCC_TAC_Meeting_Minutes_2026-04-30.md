# Confidential Computing Consortium

## Minutes of the Technical Advisory Council

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

### Meeting details

**Date**: Thursday, April 30, 2026

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

* Dan Middleton (DM), chairing on behalf of Fritz Alder, opened the call at approximately 8:10 am PT
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation
* Benjamin Sternthal created the meeting minutes based on the transcript
* DM reviewed the agenda

### Roll Call / Attendance

Quorum was not confirmed by the chair during the meeting. Five voting members are required for quorum. A vote on the Three Degrees document was deferred to the mailing list.

#### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* AMD - Nathaniel McCallum / David Kaplan
* Google - Rene Kolga+ / Keith Moyer
* Huawei - Zhipeng (Howard) Huang
* Intel - Raynor Scott / Simon Johnson
* Meta - Henry Wang / Kevin Hui
* Microsoft - Alec Fernandez+
* Nvidia - Fritz Alder / Dan Middleton+
* Red Hat - Yash Mankad / Ram Pai+
* TikTok - Mingshen Sun+ / Yao Zhang
* Shielded Technologies - Bob Blessing-Hartley

#### Other Attendees

* Caroline (Microsoft Corporation)
* Cédric Fournet (Microsoft Corporation)
* Jens Albers (Fr0ntierX Inc)
* Jeremy Powell (Advanced Micro Devices)
* Jörg Rödel (Advanced Micro Devices)
* Julian Stephen
* Leonardo Garcia (Linaro Limited)
* Michelle Roth (The Linux Foundation)
* Mike Bursell (Confidential Computing Consortium)
* Mona Vij (Intel Corporation)
* Ofir Azoulay-Rozanes (Anjuna)
* Rithikha Rajamohan (EQTY Lab)
* Simon Gallagher (Microsoft Corporation)

## Welcome New Community Members

* Mike Bursell introduced Michelle Roth as the new PMO for the CCC, covering while Ben Sternthal is on PTO. Michelle noted that Ben will be unavailable for approximately two weeks in China, and she will be the point of contact for program management questions. Support requests can be sent to support@confidentialcomputing.io.
* Cédric Fournet introduced himself as a researcher in security and cryptography at Microsoft Azure Research in Cambridge, UK, with over 10 years of experience in confidential computing. This was his first TAC meeting.
* Leonardo Garcia noted he is no longer representing Linaro in the group and is now attending as an individual community member.

## Meeting Minute Approval & Old Business

* DM recapped the previous meeting (April 16): Mark Novak presented the Trustworthy Workload Identity SIG proposal, Gramine completed its annual review, and Alec Fernandez (AF) provided an update on the CCC's ISO liaison relationship.
* Mike Bursell (MB) reported that he has been confirmed as the backup ISO liaison representative, able to stand in for AF when needed. AF noted the importance of this given ISO's formal procedures.

## Announcements

* MB noted the Confidential Computing Summit program is expected to be announced soon; he served on the program committee.
* DM noted no other CFPs or conferences on the immediate horizon.

## New Business: TAC Document Updates

* DM proposed updating two existing TAC publications: the "Technical Analysis of Confidential Computing" white paper (last updated November 2022) and the "Common Terminology for Confidential Computing" document (last updated December 2022). Both need to reflect developments such as GPUs, smart NICs, composite devices, containers, and newer TEE architectures (TDX, SEV-SNP, CCA).
* **Technical Analysis document**: AF volunteered to lead an update scoped to correcting misalignments with the TAC's current vision—no new sections, only wording updates—with a target of having a draft ready for the next TAC meeting (May 14) and final approval before the Confidential Computing Summit in mid-June. MB agreed with the scoping approach and suggested flagging areas needing future expansion for a subsequent version. AF plans to work in a Google Doc for ease of collaborative editing.
* **Terminology document**: AF and Cédric Fournet (CF) discussed the scope. AF noted the terminology document requires more substantial rework—including updated content on TDX, SEV-SNP, CCA, confidential devices, and containers—and suggested a dedicated working session to create a new outline, with community members signing up for individual sections. CF asked about the best venue for new content on composite devices and composite attestation; DM suggested it could go in the terminology document as new chapters, or potentially a separate document depending on volume, and that the typical workflow starts with a Google Doc before moving to Markdown in the governance repo. AF offered to recruit contributors, including CF. DM committed to sending a note to the mailing list to solicit volunteers.

## CCC Project Review: COCONUT-SVSM

* Jörg Rödel (JR), creator and maintainer of COCONUT-SVSM, presented the project's annual review. COCONUT-SVSM is a platform to provide secure services to confidential workloads (mission updated from "confidential virtual machines" to "confidential workloads" to reflect expanded scope).
* JR described three operating modes: SVSM mode (current, where Coconut acts as a service provider to an enlightened guest OS), paravisor mode (on the roadmap, where Coconut proxies between guest OS and hypervisor to support guests with minimal enlightenments), and a new standalone mode where Coconut runs workloads directly without a guest OS.
* Development highlights from the past year include VirtIO VSOCK support, KBS (Key Broker Service) attestation support via a host-side attestation proxy, kernel threads, debugging improvements, CI/workflow improvements, security improvements, and boot flow improvements.
* Development statistics: 755 non-merge commits (up 5.5% year-over-year), 267 merges, ~20,000 lines of code added, 25 contributors in the past year (up 10%), and 39 total contributors to date. Company engagement remains broad, with contributors from AMD, Google, HPE, IBM, Intel, Microsoft, Red Hat, SUSE, and others, plus growing university research engagement.
* The project began monthly development releases in August 2025, serving as development checkpoints with enhanced testing. Signed release tags are assigned, but no stable backports are performed.
* The OpenSSF Scorecard rating improved to 8.8 after addressing CI permission issues and insecure project dependencies, with further improvements planned (e.g., better security process documentation).
* **Development outlook**: The biggest missing piece for upstream adoption is KVM Planes support—a major KVM architectural enhancement for privilege separation within VMs that will serve as the frontend for AMD SEV-SNP VM Privilege Levels, Intel TDX Partitioning, ARM CCA Realms, and Microsoft Hyper-V Virtual Secure Mode. JR has a proof-of-concept on Linux 6.17 and expects a new version based on 7.0 or 7.1. The goal is significant progress this year.
* Persistence support (CocoonFS) is the next major work item, needed to save vTPM state across CVM reboots (required for LUKS/BitLocker disk encryption) and planned UEFI variable store support. CocoonFS is a Merkle-tree-based integrity-protected and encrypted filesystem developed by SUSE community members, currently under review as a pending PR. It prioritizes security over performance (uses AES-GCM, requiring full file rewrites on updates). DM and CF asked about rollback protection; JR acknowledged that rollback is only preventable at the whole-filesystem level, and cross-reboot rollback protection remains an unsolved problem. Mona Vij (MV) confirmed Gramine faces the same open problem.
* JR described the new standalone workload mode, which would provide a subset of the Linux syscall interface in Coconut userland, enabling workloads written in any language (not just Rust) using Linux developer toolchains. MV pointed out synergies with Gramine TDX, which does similar work. JR confirmed interest after watching the Gramine TDX presentation from two weeks prior. DM expressed enthusiasm for potential cross-project integration between two CCC projects.
* The project is participating in Google Summer of Code for the first time (hosted under the QEMU umbrella) with two proposed projects: observability support and PCID/CPUID handling improvements.
* Community remains stable with weekly development calls (10–15 attendees), a weekly TSC meeting (4 members), in-person meetups at FOSDEM, Plumbers Conference, and OC3, and collaboration via GitHub, a mailing list, and a Matrix chat room.
* MB asked about project maturity; JR reported that Linux distributions are beginning to package COCONUT-SVSM, though full upstream deployment awaits KVM Planes support in KVM and QEMU. One cloud service provider has an SVSM-based instance in preview.
* MB raised the EU Cyber Resilience Act (CRA) and its implications for open source projects, noting that all CCC projects should consider whether they need an official open source steward via the CCC and Linux Foundation. MB offered to give a future tech talk on the topic; JR expressed interest.
* MB asked about the vTPM implementation; JR clarified that the vTPM is not tied to a hardware TPM but rather to the AMD security processor (SEV-SNP).
* AF asked about CocoonFS; JR described it as a Merkle-tree-based filesystem with encryption and integrity protection in a single layer (as opposed to stacking LUKS + dm-verity + a filesystem). JR offered to share the CocoonFS specification (available in the Coconut SVSM repository pull requests) to the TAC mailing list. AF mentioned Microsoft's ReFS as a potentially related reference; MV shared a link to Gramine's encrypted filesystem.

## White Papers and Blueprints

### Three Degrees of Integration

* DM walked through final updates to the "Three Degrees of Integration" document, including consistent graphic styling across all three diagrams (updated to match CCC website/slide deck color scheme), replacement of "operating system" with "guest kernel measurement" for precision, replacement of language framing the third level as the culmination of confidential computing with language framing it as baseline adoption, and minor wording adjustments based on feedback from Ijlal Loutfi, Yulia, and Manu.
* DM presented two options for the first-level diagram: one including the key repository block and one without it. After discussion, the group leaned toward removing it to make the progression between server integration and infrastructure integration more visually stark (AF's preference), though opinions varied.
* MV raised concerns that the document's limitations section should be broadened beyond workload vulnerabilities to include all software running within the TEE boundary (guest kernel, firmware, BIOS). After discussion, DM updated the caveat language to reference vulnerabilities "introduced within the TEE boundary" rather than only the workload. Ofir Azoulay-Rozanes (OAR) noted that Dan had already addressed a similar point in an earlier section. AF added that from a customer perspective, the key benefit of workload measurement is establishing clear ownership and responsibility boundaries for regulated industries (e.g., PCI), even if the total number of vulnerabilities is unchanged.
* MV suggested future documents could address the practical challenges of attestation (maintaining good known values, transparency logs) and TCB size reduction as separate topics. OAR emphasized that running with confidential computing and remote attestation is strictly more secure than without, even with known challenges.
* Due to lack of quorum, no vote was held. DM will issue a call for vote on the Three Degrees document via the mailing list.

### Blueprint C – Confidential Clean Rooms

* Rene Kolga (RK) presented updates to Blueprint C, noting use cases were significantly shortened, and a new section was added distinguishing attestation of the clean room infrastructure from attestation of the business logic running within it. Mingshen Sun contributed simple diagrams. OAR requested that future blueprints include a section for ISV solutions (similar to the one in Blueprint C); DM noted the ISV section approach needs LF advisory approval first, using Blueprint C as a test case.
* The group discussed whether each blueprint should include a self-contained "What is Confidential Computing" section. Simon Gallagher (SG) recommended standard boilerplate across all documents since they will be distributed as standalone PDFs. DM suggested condensing it to one paragraph with a link to the technical white paper. RK agreed.
* RK indicated Blueprint C is ready for final approval and will send a note to the mailing list.

### Blueprint A – Attestation for Workloads on Public Cloud

* SG presented a first draft of Blueprint A, noting he tried to make the content as generic as possible (avoiding Azure-specific focus based on Blueprint B feedback). The draft includes a reference architecture diagram, attestation flow diagrams, three implementation patterns, enterprise integration points, and implementation guidance. AI-generated diagrams (via Copilot) were used as placeholders and will be replaced.
* SG flagged the attestation policy section as too large and plans to condense it, potentially spinning detailed attestation policy content into a separate document. Example references span Azure, GCP, and open source implementations.
* SG highlighted a compliance control mapping table (also generated with Copilot assistance) that maps confidential computing capabilities to frameworks like ISO and CCA directives. AF expressed strong interest in this table, noting it answers questions he has been getting from ISO and previously from the Cloud Security Alliance, and suggested surfacing it to a higher-level TAC document since the control mappings apply broadly to all of confidential computing, not just Blueprint A. SG agreed and suggested sharing with the GRC SIG as well.
* SG noted he still needs to resolve outstanding comments on Blueprint B and plans to do so in the coming days.

## Any Other Business / Next Steps

* Alec Fernandez committed to a tech talk on attestation for TEEs with composite devices (shared responsibility model) at the next meeting (May 14), deferred from this meeting.
* Ijlal Loutfi will serve as the rotating chair for the May 14 meeting. The Keystone project review is also scheduled for that meeting.
* DM will issue a call for vote on the Three Degrees document and Blueprint C via the mailing list.
* Alec Fernandez will circulate a draft update of the Technical Analysis white paper by the next meeting.
* DM will send a note to the mailing list soliciting volunteers for the Terminology document update.
* Members were reminded to review Blueprint A (new draft), continue providing feedback on Blueprint B, and submit final comments on Three Degrees and Blueprint C.
* DM adjourned the meeting at approximately 10:00 am PT.
