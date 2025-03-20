# Trustworthy Workload Identity (TWI) Special Interest Group — Charter
Version 1.0

## Background
Until recently, there were few scenarios demanding data-in-use protections. This is starting to change. Regulatory bodies worldwide **\[1]** are increasingly requiring data-in-use protection and privacy-enhancing technologies. Outside of regulatory requirements, companies are exploring multiparty computation, machine learning training & inferencing, addressing the actual and perceived risks of computing in the public clouds, insider threats, and other reasons for protecting data-in-use. Correspondingly, there is an increased push to harmonize management and governance of human and non-human identities. Enterprises interested in strong assurances around the security of their deployed workloads, for regulatory, contractual and peace of mind reasons, will soon face large and challenging tasks of upgrading their existing IT systems to meet these requirements.
Current ways of issuing and managing workload identities, as well as those required for effective protection of data-in-use, suffer from multiple architectural shortcomings; chief among them:

1. Lack of workload isolation against the hardware and the operating system owners/administrators, as well as peer workload instances
2. Lack of strong binding between a workload credential and the workload instance to which that credential had been issued
3. Inability to associate a credential with a set of decisions leading up to its issuance
_Note that these requirements are related: lack of process isolation eases credential exfiltration and leads to credential leakage and reuse._

In the immediate term, effective Confidential Computing faces a significant challenge: the scale of uplift and immature tooling are both clear barriers. Longer term, however, Confidential Computing provides a vital improvement due to its unique features and broad availability. The TWI SIG will specify Confidential Computing-assisted mechanisms that fit inside the emerging Workload Identity solution ecosystem. The SIG will ensure the evolution of this ecosystem is in alignment with the expectations of the owners and operators of Confidential Computing workloads. These efforts will build on the concept of _Trustworthy Workload Identity_ defined below. Data-in-use protection of workloads that have such identities will be a critical downstream effect.

## Trustworthy Workload Identity — Definition
_Trust_ is a decision, _trustworthiness_ is an externally verifiable/attributable characteristic on which to base trust decisions.

Supporting definitions:

- **Workload** as used in this document restricts the definition of the same term by WIMSE – “a running instance of software executing for a specific purpose” – to just that part of the code and configuration of the (WIMSE-defined) workload that is subject to Remote Attestation.
- **Workload Identifier** is a stable construct around which Relying Parties can form long-lived Workload authorization policies.
- **Workload Identity** is defined exactly as it is by WIMSE **\[3]** – a combination of three basic building blocks: trust domain, Workload Identifier and identity credentials.
- **Workload Credential** is an ephemeral identity document containing the Workload Identifier and a number of additional claims, that can be short- or long-lived and which is used to represent and prove Workload Identity to a relying party (WIMSE calls this "identity credentials").
- **Workload Provenance** is a linkage between a Workload Credential and a trusted entity (e.g., a vendor, developer, or issuer) responsible for the creation and/or attestation of the corresponding Workload.

A **Workload Identity** is said to be **Trustworthy** _iff_ the following three properties hold true:

1. The Workload is confidentiality- and integrity-isolated from its hosting environment as well as peer workloads throughout the lifetime of the Workload instance
2. Any credential representing a Workload Identity is bound to that Workload instance
3. A Workload Credential can be traced back to the Workload’s Provenance and the credential issuer

Practical (deployable, performant, compatible, manageable) solutions in the TWI space will have to satisfy several additional requirements, captured in **\[2]**.

## Goals
We envision ubiquitous use of Trustworthy Workload Identities as the preferred mechanism by which any two workloads can establish trust in each other.

The goals of the TWI SIG are as follows:

1. Precisely define and publish (in **\[2]**) all scenarios and requirements that Trustworthy Workload Identity must meet
2. Create a TWI Reference Architecture that addresses all the scenarios and requirements documented in **\[2]**
3. Achieve integration (“impedance match”) of the TWI Reference Architecture with applicable existing and evolving frameworks, standards and solutions
4. Influence the evolution of the broader Workload Identity solution space as appropriate to ensure that TWI offers a compatible and attractive option
5. Provide reference open source implementations adhering to the Reference Architecture to assist the TWI community
6. Provide a forum for ongoing discussions on TWI topics among members of the Consortium as well as third parties

Importantly, there is also a range of outcomes our work will seek to prevent:

1. Fragmentation of the solution landscape into multiple incompatible or inconsistent approaches
2. Gaps in the availability of solutions which could cause barriers to broad adoption
3. Conflicts with the decisions made inside other CCC working groups (e.g., Attestation SIG, GRC SIG)

To summarize, the overarching goal we must achieve is turning TWI into the [Schelling Point](https://en.wikipedia.org/wiki/Focal_point_\(game_theory\)) of Confidential Computing deployment, both for new and existing applications.

## References
1. TODO: Document summarizing current regulatory landscape
2. Trustworthy Workload Identity Scenarios and Requirements: <https://github.com/CCC-Attestation/meetings/blob/main/musings/workload-identity.md>
3. Workload Identity in Multi-System Environments IETF Working Group: <https://datatracker.ietf.org/wg/wimse/documents/>
4. Confidential Payload Governance pattern: <https://drive.google.com/drive/u/0/folders/1EaXIm1jK3af_oUG7lTLYL9QcS9BRO5gy>

## Notes & Clarifications
### The Deeper Meaning of the TWI Definition
Here we reiterate the TWI Definition and provide additional context and clarification.

First, a couple of quick notes on supporting definitions.

**Workload** as used in this document restricts the definition of the same term by WIMSE **\[3]** – “a running instance of software executing for a specific purpose” – to just that part of the code and configuration of the (WIMSE-defined) workload that is subject to Remote Attestation.
- Workloads can nest (be composed of smaller individual sub-Workloads). These sub-Workloads can have individual Identities used for, e.g., intra-Workload communications. However, any Workload Identity presented externally (as opposed to sister sub-Workloads) is treated as an Identity of the containing Workload as a whole.

**Workload Identifier** is a stable construct around which Relying Parties can form long-lived Workload authorization policies.
- The concept of Workload Identifier is best thought of from the standpoint of the Relying Party. For instance, what constitutes a “Payroll Application” (workload) for purposes of authorizing its access to the “Payroll Database” (relying party) will change as the Payroll Application is upgraded from version N to version N+1, yet the Relying Party policy will not change as the upgrade takes place. The change to Payroll Application’s Reference Values will be 100% contained by the process of Workload Credential issuance.

A **Workload Identity** is said to be **Trustworthy** _iff_ it satisfies the following three requirements:

1. The Workload is confidentiality- and integrity-isolated from its hosting environment as well as peer workloads throughout the lifetime of the workload instance

The following  aspects contribute to a Workload being properly isolated from its hosting environment:
- The Workload needs to execute inside a TEE (or a set of mutually trusting TEEs) on properly designed and trustworthy silicon.
- The Workload needs to be properly governed per the Workload Governance Pattern published by the GRC SIG **\[4]**. This includes aspects of secure design and deployment, proper configuration, and much else.
- Both code and data are subject to the integrity requirement. Whether the code and data require confidentiality is scenario specific: e.g., for sealed-glass proofs, neither code nor data need to be confidential, but for video games both code and data must have confidentiality protection. At a minimum, the confidentiality requirement MUST extend to the mechanism (typically, a cryptographic key) used to prove the Workload Credential to a relying party.

2. Any credential representing a Workload Identity is bound to that workload instance
- A Workload that uses bearer tokens to communicate its credentials cannot be said to have a Trustworthy Identity, since the credential isn’t bound to the workload instance. While this may be required for interoperability and may necessitate additional compensating controls to mitigate the threats, such mitigations are outside the scope of the TWI SIG.

3. A Workload Credential can be traced back to the Workload’s provenance and the credential issuer
- Provenance is a required property of TWI because the first two requirements, while _necessary_, are not _sufficient_ to establish trustworthiness. In layman terms, one may be sure that Bob can keep secrets (confidentiality) and can be reasonably assumed to only execute a given piece of code as well as not tamper with his data (integrity). From those facts alone one cannot tell anything about Bob’s trustworthiness (_reputation_) __– that can be done by “asking around” and that’s where provenance comes in handy.
- Provenance provides linkage between the Workload Credential and some auditable metadata – such as issuer policies, issuance records, or unique identifiers – that ties the Credential to both the Workload instance and the issuer’s trust domain.
- “Lineage” vs. “Provenance”: we use “provenance” here rather than “lineage” deliberately. Provenance may mean a way to identify what source code, build system, etc. were used to generate the confidential computing payload behind the workload. It can also mean a way of establishing that the workload came from a trusted vendor with no way of establishing lineage further than that. Example: an X.509-SVID can contain a serial number. That serial number can be used to associate a credential instance with a set of recorded policy decisions and other data used in issuing this credential. This is just for illustration. A more prescriptive guidance will be an output of the SIG. From ChatGPT:
  - **Lineage** is about **tracing back relationships or transformations** (data or family connections).
  - **Provenance** is about **documenting the origin and history of something** (data records, artifacts, or artworks).
- Provenance, once established, can be used in many ways, chief among them auditing and assisting in real-time authorization decisions. These mechanisms will be specified in the Reference Architecture.
- The binding to the credential issuer is fairly straightforward: the issuer signs the issued credential with their private key.
