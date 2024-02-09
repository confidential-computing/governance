# Confidential Computing Consortium projects

The [Confidential Computing Consortium](https://confidentialcomputing.io) hosts multiple projects related to confidential computing.

## Index of Projects

* [Certifier Framework For Confidential Computing ](#certifier-framework-for-confidential-computing)
* [Enarx](#enarx)
* [Gramine](#gramine)
* [Keystone](#keystone)
* [Occlum](#occlum)
* [Open Enclave SDK](#open-enclave-sdk)
* [spdm-rs](#spdm-rs)
* [Veracruz](#veracruz)
* [Veraison](#veraison)
* [VirTEE](#virtee)

---

## Certifier Framework For Confidential Computing 

The Certifier Framework for Confidential Computing consists of a client API called the Certifier API and server-based policy evaluation server called the Certifier Service.

The Certifier API greatly simplifies and unifies programming and operations support for multi-vendor Confidential Computing platforms by providing simple client trust management, including attestation evaluation, secure storage, platform initialization, secret sharing, secure channels and other services.

**Status:** Incubation

#### Links

* [Project detail](./Certifier_Framework/2023_Certifier_CCC_Project_Proposal.pdf)
* [GitHub](https://github.com/ccc-certifier-framework/certifier-framework-for-confidential-computing)
* [Proposal](./Certifier_Framework/2023_Certifier_CCC_Project_Proposal.pdf)
    * Accepted by TAC: 2023-10-19   
    * Accepted by Governing Board: 2024-01-17
* [Charter](./Certifier_Framework/Certifier_Framework_for_Confidential_Computing_Technical_Charter_2-5-2024.pdf)


## Enarx

<img height="100" src="https://github.com/confidential-computing/artwork/raw/main/enarx/enarx-logo-horizontal-black.svg">

Enarx provides a run-time TEE based on WebAssembly, allowing developers to deploy applications without any rewrites from languages like Rust, C/C++, C#, Go, Java, Python, Haskell and many more.

**Status:** Incubation

#### Links

* [Project detail](./Enarx/enarx-project_detail.md)
    * [2021 review](./Enarx/enarx-annual-review-2021.pdf)
* [Website](https://enarx.dev)
* [GitHub](https://github.com/enarx)
* [Proposal](./Enarx/enarx-accepted_proposal.md)
    * Accepted by TAC: 2019-10-31
    * Accepted by Governing Board: 2019-10-31
* [Charter](./Enarx/Enarx_Technical_Charter-2020-02-14.pdf)
* [Artwork](https://github.com/confidential-computing/artwork#enarx)

#### Webinars

* [A Technical Introduction to Enarx](https://confidentialcomputing.io/webinar-enarx/)

#### Funding requests

* [Server (2021-12-14)](./Enarx/Enarx_Hardware_Request-2021-12-14.pdf)

## Gramine

<img height="100" src="https://raw.githubusercontent.com/confidential-computing/artwork/main/gramine/gramine-logo-horizontal-color.svg">

Gramine is a library OS, similar to a unikernel. Compared to running a complete guest OS in a virtual machine (VM), Gramine is much lighter weight. A particular use case for Gramine is Intel® Software Guard Extensions (Intel® SGX), where applications do not work out-of-the-box. Gramine solves this problem, with the added security benefits. Gramine can serve as a compatibility layer on other platforms.

**Status:** Graduation

#### Links

* [Project detail](./Gramine/gramine-project_detail.md)
    * [2021 review](./Gramine/gramine-annual-review-2021.pdf)
* [Website](https://gramineproject.io)
* [GitHub](https://github.com/gramineproject)
* [Proposal](./Gramine/gramine-accepted_proposal.md)
    * Accepted by TAC: 2020-04-02
    * Accepted by Governing Board: 2021-09-15
* [Charter](./Gramine/Gramine_Technical_Charter-2021-08-31.pdf)
* [Artwork](https://github.com/confidential-computing/artwork#gramine-project)

#### Webinars

* [Gramine](https://confidentialcomputing.io/webinar-gramine/)


## Keystone

<!--<img height="100" src="">-->

Keystone is an open-source project for building trusted execution environments (TEE) with secure hardware enclaves, based on the RISC-V architecture. Our goal is to build a secure and trustworthy open-source secure hardware enclave, accessible to everyone in industry and academia.

**Status:** Incubation

#### Links

* [Project detail](./Keystone/keystone-accepted_proposal.pdf)
    * [2022 review](./Keystone/keystone_review-2022.pdf)
* [Website](https://keystone-enclave.org/)
* [GitHub](https://github.com/keystone-enclave)
* [Proposal](./Keystone/keystone-accepted_proposal.pdf)
    * Accepted by TAC: 2020-07-23
    * Accepted by Governing Board: 2021-03
* [Charter](./Keystone/Keystone_Technical_Charter-2021-03-08.pdf)
* [Artwork]() (TBD)

#### Webinars

* [Keystone](https://confidentialcomputing.io/keystone-webinar/)

## Occlum

<img height="100" src="https://raw.githubusercontent.com/confidential-computing/artwork/main/occlum/occlum-logo-horizontal-color.svg">

Occlum makes running applications inside enclaves easy. It allows one to run unmodified programs inside enclaves with just a few simple commands. And Occlum is open-source and free to use.

**Status:** Incubation

#### Links

* [Project detail](./Occlum/occlum-project_detail.docx)
    * [2021 review](./Occlum/occlum-annual-review-2021.pdf)
* [Website](https://occlum.io/)
* [GitHub](https://github.com/occlum/occlum)
* [Proposal](./Occlum/occlum-accepted_proposal.pdf)
    * Accepted by TAC: 2020-08-20
    * Accepted by Governing Board: 2021-09-15
* [Charter](./Occlum/Occlum_Technical_Charter-2021-03-29.pdf)
* [Artwork](https://github.com/confidential-computing/artwork#occlum)

#### Webinars

* [Occlum](https://confidentialcomputing.io/webinar-occlum/)

## Open Enclave SDK

<img height="100" src="https://raw.githubusercontent.com/confidential-computing/artwork/main/open_enclave_sdk/open-enclave-sdk-icon-color.svg">

Open Enclave SDK is an open source framework that allows developers to build Trusted Execution Environment (TEE) applications using a single enclaving abstraction.

**Status:** Graduation

#### Links

* [Project detail](./Open_Enclave_SDC/open_enclave_sdk-project_detail.docx)
    * ([2020 review](./Open_Enclave_SDK/open_enclave_project_review-2020.md))
* [Website](https://openenclave.io/sdk/)
* [GitHub](https://github.com/openenclave/openenclave)
* [Proposal](./Open_Enclave_SDC/open_enclave_sdk-accepted_proposal.pdf)
    * Accepted by TAC: 2019-10-31
    * Accepted by Governing Board: 2019-10-31
* [Charter](https://github.com/openenclave/openenclave/blob/2554287d88aba93f41a1518b29c57c386c1ecb4b/docs/Community/sig-release/charter.md)
* [Artwork]() (TBD)

#### Presentations

* [TAC presentation](./Open_Enclave_SDK/Open_Enclave_TAC.pdf)

#### Webinars

* [Open Enclave SDK](https://confidentialcomputing.io/webinar-open-enclave-sdk/)

## spdm-rs

This project provides a Rust language implementation of SPDM, IDE_KM and TDISP. These protocols are used to facilitate direct device assignment for Trusted Execution Environment I/O (TEE-I/O) in Confidential Computing.

**Status:** Incubation

#### Links

* [Project detail](./spdm-rs/project-submission-rust-spdm.md)
* [GitHub](https://github.com/ccc-spdm-tools/spdm-rs)
* [Proposal](./spdm-rs/project-submission-rust-spdm.md)
    * Accepted by TAC: 2023-09-22   
    * Accepted by Governing Board: 2024-01-17
* [Charter](./spdm-rs/spdm-rs-Technical-Charter-Final_1-3-2024.pdf)


## Veracruz

<img height="100" src="https://raw.githubusercontent.com/confidential-computing/artwork/main/veracruz/veracruz-logo-horizontal-color.svg">

Veracruz is a research project exploring the design of privacy-preserving distributed systems. Veracruz uses strong isolation technology and remote attestation protocols to establish a “neutral ground” within which a collaborative, multi-party computation between a group of mistrusting principals takes place.

**Status:** Incubation

#### Links

* [Project detail](./Veracruz/veracruz-project_detail.md) ([FAQ](./Veracruz/veracruz-faq.pdf))
    * (2021 review)[./Veracruz/veracruz-annual-review-2021.pdf]
* [Website](https://github.com/veracruz-project)
* [GitHub](https://github.com/veracruz-project)
* [Proposal](./Veracruz/veracruz-accepted_proposal.md)
    * Accepted by TAC: 2020-09-03
    * Accepted by Governing Board: 2021-04-14
* [Charter](./Veracruz/Veracruz_Technical_Charter-2021-03-08.pdf)
* [Artwork](https://github.com/confidential-computing/artwork#veracruz)

#### Webinars

* [Veracruz](https://confidentialcomputing.io/webinar-veracruz/)

## Veraison

<img height="100" src="https://raw.githubusercontent.com/confidential-computing/artwork/main/veraison/veraison-logo.svg">

Project Veraison builds software components that can be used to build an Attestation Verification Service.

**Status:** Graduation

#### Links

* [Project detail](./Veraison/veraison-ccc-project-veraison-proposal.pdf)
* [Website](https://github.com/veraison)
* [GitHub](https://github.com/veraison)
* [Proposal](./Veraison/veraison-ccc-project-veraison-proposal.pdf)
    * Accepted by TAC: 2022-02-04
    * Accepted by Governing Board: 2022-05-18
* [Charter](./Veraison/Veraison_Technical_Charter_2022-04-28.pdf)
* [Artwork](https://github.com/confidential-computing/artwork/tree/main/veraison/veraison-logo.svg)

## VirTEE

<img height="100" src="https://raw.githubusercontent.com/confidential-computing/artwork/main/virtee/virtee.svg">

VirTEE is an open community dedicated to developing open source tools for the bring-up, attestation, and management of Trusted Execution Environments.

**Status:** Incubation

#### Links

* [Project detail](./VirTEE/virtee-accepted_proposal.md)
* [Website](https://virtee.io/)
* [GitHub](https://github.com/virtee)
* [Proposal](./VirTEE/virtee-accepted_proposal.md)
    * Accepted by TAC: 2023-06-01
    * Accepted by Governing Board: 2024-01-17
* [Charter](./VirTEE/VirTEE_Technical_Charter_8-29-2023.pdf)
* [Artwork](https://github.com/confidential-computing/artwork/tree/main/virtee)

<!-- #### Webinars -->


<!--
---

## Emeritus Projects

There are currently no Emeritus projects in the CCC.
-->
