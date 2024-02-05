## Project Proposal Template

### General Information

1.1. Name of Project

VirTEE


1.2. Project Description (what it does, why it is valuable, origin and 
history)

VirTEE describes itself as "An open community dedicated to building 
components for Virtualization-based TEEs". We develop a number of 
libraries and command lines tools to make the development and use of 
TEEs easier. Some of our projects are:

sev Rust library: Provides type-safe APIs to the Linux kernel's SEV 
and SEV-SNP ioctl interface.

sevctl: CLI tool for managing the legacy SEV (i.e. not SEV-SNP) 
firmware device on a host machine.

oci2cw: Scripting tool to convert Open Container Images (OCIs) into 
measured confidential container images.

reference-kbs: KBS attestation server for confidential workloads.

kbs-types: Rust (de)serializable types for the Key Broker Service 
(KBS) attestation protocol.

Our tools are built such that they are not tied to one specific 
project. For example, our sev Rust library has been used by our 
organization internally within the libkrun [1] project. However, several 
other open source communities have come to use this library, notably the 
Confidential Containers [2], Inclavare Containers [3], and Azure vTPM on 
SEV-SNP [4][5] projects. This trend persists with a number of our other 
tools as well.

[1] https://github.com/containers/libkrun

[2] https://github.com/confidential-containers

[3] https://github.com/inclavare-containers

[4] https://github.com/kinvolk/azure-cvm-tooling

[5] https://github.com/mkulke/az-snp-vtpm


Our community's value is in the generalization of its projects. Our 
motivation for founding the group was partly due to having built a 
number of userspace tools/libraries that provided an easy interface to 
interact with TEE environments (notably AMD SEV), and needing somewhere 
to house them under one organization. We've since grown to include 
projects for attestation, and would like to continue our trend of 
building better tools for easy development/interaction with an expanding 
number of TEE architectures.


1.3. How does this project align with the Consortium's [Mission 
Statement](README.md)

We accelerate the acceptance and adoption of confidential computing 
by easing the development cost and effort of building TEE projects. From 
developers leveraging our libraries to build confidential computing 
platforms, to administrators using our CLI and scripting tools to manage 
the TEE certificates and firmware device of a system, we provide 
reliable components for confidential systems.

We also interact with the larger confidential computing community 
in developing protocols and frameworks for building and attesting 
confidential VMs, an example being our work with the Confidential 
Containers organization in defining the Key Broker Service (KBS) 
attestation protocol [1] and managing the Rust kbs-types project used to 
implement this protocol [2]. VirTEE's components are found throughout 
the confidential computing landscape and offers open source projects to 
continually progress the adoption of this technology.

[1] https://github.com/confidential-containers/kbs/blob/main/docs/kbs_attestation_protocol.md 

[2] https://github.com/virtee/kbs-types


1.4. Project website URL

https://virtee.io/


1.5. Social media accounts

Blog: https://virtee.io/blog/

Chat (Matrix): https://matrix.to/#/#virtee:matrix.org

### Legal Information

2.1. Project Logo URL or attachment (Vector Graphic: SVG, EPS).

Attached (virtee.svg).

2.2. Project license.  We recommend an [OSI-approved 
license](https://opensource.org/licenses), so if the license is not one 
on the list, explain why.

Apache License, Version 2.0

2.3. Existing financial sponsorship.

This project is currently developed mainly by employees of Red Hat 
and AMD. However, we receive contributions and have collaborated with a 
number of other developers employed at companies such as IBM and Microsoft.

2.4. Trademark status.

N/A.

2.5. Proposed Technical Charter, based on the template.
([Word version](https://lists.confidentialcomputing.io/g/main/files/TAC/Project%20Submissions/Technical%20Charter%20%28custom+data%29%20--%20LF%20Projects,%20LLC%204-10-2019%20FINAL%20%2811%29.docx), 

[PDF version](https://lists.confidentialcomputing.io/g/main/files/Governing%20Board/Docs/LF_Projects_Technical_Charter.pdf)). 

Include doc as attachment or give URL of doc.  It is ok to change the
text (e.g., "Technical Steering Committee") to match the actual 
structure of the project; projects are free to use whatever governance 
structure they want.

Attached (virtee_technical_charter.docx).


### Technical Information

3.1. High level assessment of project synergy with existing projects 
under the CCC, including how the project compliments/overlaps with 
existing projects, and potential ways to harmonize over time. Responses 
may be included both inline and/or in accompanying documentation.

Due to the broad/general nature of the libraries and tools we 
build, we feel that other CCC projects (especially ones implemented in 
Rust, which could easily take advantage of our libraries) could gain an 
immense benefit from them. Also, our CLI and scripting tools are 
applicable to almost any project looking to administer and attest a TEE 
system.


3.2. Describe the [Trusted Computing Base 
(TCB)](https://en.wikipedia.org/wiki/Trusted_computing_base) of the 
project. If the project supports multiple environments please describe 
each TCB. Also identify if dependencies of other project (both CCC or 
non-CCC) TCBs are taken.

While we have strong support for the AMD SEV environment, we would 
like to extend our reach to bring contributions for other TEE 
architectures (x86, ARM, and potentially RISC-V).


3.3. Project Code of Conduct URL.  We recommend a [Contributor Covenant 
v2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) 
based Code of Conduct, so if the Code of Conduct is not based on that, 
explain why.

https://github.com/virtee/community/blob/main/CODE_OF_CONDUCT.md


3.4. Source control URL

https://github.com/virtee


3.5. Issue tracker URL

Each of the projects in our organization has their own issue 
tracker in its respective git repository.


3.6. External dependencies (including licenses, and indicate whether 
each is a build time or runtime dependency)

Most of our projects are developed in the Rust programming language 
and are licensed under Apache Version 2.0.


3.7. Standards implemented by the project, if any. Include links to any 
such standards.

Our kbs-types crate implements the standard types used for 
attestation via the Key Broker Service (KBS) protocol.

3.8. Release methodology and mechanics

As developments in the confidential computing landscape rapidly 
change, we haven't established a scheduled release cadence, but have 
usually released our software when significant changes/additions have 
occurred. Our mechanics of release are upstream tagged releases, 
crates.io releases (for our Rust projects), and Fedora/RHEL releases 
when needed. This cadence guarantees at least 2 releases per year, with 
a greater frequency for our projects with frequent new features and bug 
fixes.


3.9. Names of initial committers, if different from those submitting 
proposal

Main contributors/maintainers of the project are: Alice Frosi, 
Sergio Lopez, Cole Robinson, Larry Dewey, Tyler Fanelli.


3.10. List of project's official communication channels (slack, irc, 
mailing lists)

virtee on matrix: https://matrix.to/#/#virtee:matrix.org


3.11. Project [Security Response Policy](security-response-policies.md)

Up to this point, we have relied on users addressing security 
issues in our Matrix instance. However, we are considering setting up a 
mailing list for this. Once this is finished, we will release our 
security response policy document indicating that disclosure should be 
directed at that mailing list.

3.12. Preferred maturity level (Sandbox, Incubation, Graduation, or 
Emeritus)

Sandbox


3.13. Any additional information the TAC and Board should take into 
consideration when reviewing your proposal.

N/A