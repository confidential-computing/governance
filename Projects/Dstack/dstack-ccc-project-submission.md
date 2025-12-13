# General Information

## 1.1. Name of Project

dstack

## 1.2. Project Description (what it does, why it is valuable, origin and history)

Dstack is a developer-friendly and security-first SDK that simplifies the deployment of arbitrary containerized applications into Trusted Execution Environments (TEEs). It enables developers to securely deploy containerized applications in TEEs in minutes using familiar tools like docker-compose. Dstack provides safe management of secrets and sensitive data, along with built-in TLS termination or passthrough reverse proxy for exposed services.

The project was built by Kevin Wang and others from Phala Network, inspired by Andrew Miller (Flashbots & Teleport), and has received contributions from Nethermind and many others. Dstack addresses the gap between raw TEE technology and Zero Trust platform requirements by providing portable confidential containers, decentralized code management, and verifiable domain management.

## 1.3. How does this project align with the Consortium's Mission Statement

Dstack directly aligns with the Confidential Computing Consortium's mission by providing enterprise-grade building blocks for confidential computing applications. It accelerates adoption by making TEE deployment developer-friendly through familiar tools like docker-compose, lowering the barrier to entry. Dstack defines foundational services and frameworks that are Confidential Computing aware through its comprehensive architecture (Dstack-OS, Dstack-KMS, Dstack-Gateway). The project minimizes the need for trust by implementing Zero Trust principles with portable confidential containers, decentralized code management, and verifiable domain management. By enabling seamless deployment of containerized applications in TEEs, Dstack contributes significantly to the development experience and practical adoption of confidential computing in real-world scenarios.

## 1.4. Project website URL

[https://github.com/Dstack-TEE/dstack](https://github.com/Dstack-TEE/dstack)

## 1.5. Social media accounts

[https://x.com/PhalaNetwork](https://x.com/PhalaNetwork)

# Legal Information

## 2.1. Project Logo URL or attachment (Vector Graphic: SVG, EPS).

[https://drive.google.com/drive/folders/1J7oImDgd9FFFq2JNtA313a3aKwPH_HcF](https://drive.google.com/drive/folders/1J7oImDgd9FFFq2JNtA313a3aKwPH_HcF)

## 2.2. Project license. We recommend an OSI-approved license, so if the license is not one on the list, explain why.

Apache License, Version 2.0

## 2.3. Existing financial sponsorship.

This project is sponsored by Phala Network.

## 2.4. Trademark status.

No Trademark Protection.

# Technical Information

## 3.1. High level assessment of project synergy with existing projects under the CCC, including how the project compliments/overlaps with existing projects, and potential ways to harmonize over time. Responses may be included both inline and/or in accompanying documentation.

Dstack complements several existing CCC projects while addressing unique needs in the confidential computing ecosystem:

- **Synergy with Gramine**: While Gramine provides a compatibility layer for Intel SGX applications, Dstack extends this concept by offering a higher-level abstraction focused on containerized applications.
- **Complementary to Open Enclave SDK**: Open Enclave SDK provides a framework for building TEE applications with a single enclaving abstraction. Dstack takes a different approach by focusing on deploying existing containerized applications into TEEs without requiring code modifications.
- **Alignment with VirTEE**: VirTEE's focus on tools for bring-up, attestation, and management of TEEs aligns well with Dstack's goals.
- **Differentiation from Enarx**: While Enarx provides a platform abstraction for TEEs focusing on "private, fungible, serverless" applications, Dstack focuses specifically on containerized applications with familiar Docker tooling. Both projects could share insights on TEE abstraction techniques.
- **Extension beyond COCONUT-SVSM**: COCONUT-SVSM implements a Secure VM Service Module for confidential computing VMs. Dstack builds upon this concept by providing a complete framework for deploying and managing containerized applications within these secure VMs.

Dstack uniquely addresses the developer experience gap in confidential computing by providing a Docker compatible interface for deploying applications in TEEs, with built-in solutions for key management, domain verification, and portable containers. This focus on developer experience and containerization complements the more foundational TEE technologies represented in the CCC.

## 3.2. Describe the Trusted Computing Base (TCB) of the project. If the project supports multiple environments please describe each TCB. Also identify if dependencies of other project (both CCC or non-CCC) TCBs are taken.

The TCB consists of the Dstack codebase, Intel TDX, and other TEE solutions that will be supported in the future.

## 3.3. Project Code of Conduct URL. We recommend a Contributor Covenant v2.0 based Code of Conduct, so if the Code of Conduct is not based on that, explain why.

Contributor Covenant v2.0 based Code of Conduct.

## 3.4. Source control URL

[https://github.com/Dstack-TEE/dstack](https://github.com/Dstack-TEE/dstack)

## 3.5. Issue tracker URL

[https://github.com/Dstack-TEE/dstack/issues](https://github.com/Dstack-TEE/dstack/issues)

## 3.6. External dependencies (including licenses, and indicate whether each is a build time or runtime dependency)

- Intel TDX or equivalent TEE hardware (runtime)
- Linux kernel (runtime)
- Docker/container runtime (runtime)
- Busybox (runtime)
- LUKS for encryption (runtime)
- Wireguard-tools (build time)
- Build-essential, chrpath, diffstat, lz4, xorriso (build time)
- Rust (build time)

## 3.7. Standards implemented by the project, if any. Include links to any such standards.

- TLS/HTTPS for secure communications
- Certificate Transparency (CT) for certificate monitoring
- Certificate Authority Authorization (CAA) for domain security
- Remote Attestation for TEE verification

## 3.8. Release methodology and mechanics

Dstack projects are hosted on GitHub, with releases triggered by GitHub Actions. The automated build process compiles all project components and packages the artifacts. System images are produced using Yocto, a reproducible build tool that ensures consistency and reliability across releases. This approach provides a standardized and automated release process that maintains quality and reproducibility.

## 3.9. Names of initial committers, if different from those submitting proposal Initial committers include:

- Kevin Wang
- Hang Yin
- Shelven Zhou
- Leechael Yan
- Andrew Miller

## 3.10. List of project's official communication channels (slack, irc, mailing lists)

Telegram group: [https://t.me/+RF-yUoDduWAzZTUx](https://t.me/+RF-yUoDduWAzZTUx)

## 3.11. Project Security Response Policy

Dstack follows a responsible disclosure policy with these commitments:

- Responding to security reports within 3 business days with an evaluation and expected resolution timeline
- Not taking legal action against reporters who follow responsible disclosure guidelines
- Maintaining strict confidentiality of reports and reporter information
- Providing regular updates on resolution progress
- Acknowledging reporters publicly (with permission) for discovered vulnerabilities
- Offering rewards based on vulnerability severity, ranging from $1-300 for low severity issues up to $15,000 for critical vulnerabilities

Severity levels are categorized as Critical, High, Medium, and Low, with corresponding reward structures to incentivize responsible disclosure.

## 3.12. Preferred maturity level (Incubation, Graduation, or Emeritus)

Incubation.

## 3.13. Any additional information the TAC and Board should take into consideration when reviewing your proposal.

Dstack includes several key components:

- dstack-vmm: Service running on bare TDX host to manage CVMs
- dstack-gateway: Reverse proxy to forward TLS connections to CVMs
- dstack-kms: KMS server to generate keys for CVMs
- dstack-guest-agent: Service in CVM to serve containers' key derivation and attestation requests
- meta-dstack: Yocto meta layer to build CVM guest images

The project provides innovative solutions for portable confidential containers, decentralized code management, and verifiable domain management, addressing critical limitations in current TEE implementations for Web3 contexts.


