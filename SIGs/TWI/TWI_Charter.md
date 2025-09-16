# Trustworthy Workload Identity (TWI) Special Interest Group — Charter
Version 1.0

## Background
Until recently, there were few scenarios demanding data-in-use protections. This is starting to change. Regulatory bodies worldwide **\[1]** are increasingly requiring data-in-use protection and privacy-enhancing technologies. Outside of regulatory requirements, companies are exploring multiparty computation, machine learning training & inferencing, addressing the actual and perceived risks of computing in the public clouds, insider threats, and other reasons for protecting data-in-use. Correspondingly, there is an increased push to harmonize management and governance of human and non-human identities. Enterprises interested in strong assurances around the security of their deployed workloads, for regulatory, contractual and peace of mind reasons, will soon face large and challenging tasks of upgrading their existing IT systems to meet these requirements.
Current ways of issuing and managing workload identities, as well as those required for effective protection of data-in-use, suffer from multiple architectural shortcomings; chief among them:

1. Lack of workload isolation against the hardware and the operating system owners/administrators, as well as peer workload instances
2. Lack of strong binding between a workload credential and the workload instance to which that credential had been issued
3. Lack of verifiable composition of the workload, and inability to associate a credential with a set of decisions leading up to its issuance
_Note that these shortcomings are related: lack of process isolation eases credential exfiltration and leads to credential leakage and reuse._

In the immediate term, effective Confidential Computing faces a significant challenge: the scale of uplift and immature tooling are both clear barriers. Longer term, however, Confidential Computing provides a vital improvement due to its unique features and broad availability. The TWI SIG will specify Confidential Computing-assisted mechanisms that fit inside the emerging Workload Identity solution ecosystem. The SIG will ensure the evolution of this ecosystem is in alignment with the expectations of the owners and operators of Confidential Computing workloads. These efforts will build on the concept of _Trustworthy Workload Identity_ defined, defined alongside other related terms in **\[2]**. Data-in-use protection of workloads that have such identities will be a critical downstream effect.

## Goals
We envision ubiquitous use of Trustworthy Workload Identities as the preferred mechanism by which any two workloads can establish trust in each other.

The goals of the TWI SIG are as follows:

1. Precisely define and publish (in **\[3]**) all scenarios and requirements that Trustworthy Workload Identity must meet
2. Create a TWI Reference Architecture that addresses all the scenarios and requirements documented in **\[3]**
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
2. Trustworthy Workload Identity: Definitions, Entities and Relationships: <https://github.com/confidential-computing/twi/blob/main/TWI_Definitions.md>
3. Trustworthy Workload Identity Scenarios and Requirements: <https://github.com/confidential-computing/twi/blob/main/TWI_Requirements.md>
