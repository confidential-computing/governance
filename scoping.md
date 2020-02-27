# TAC Scoping Discussion

## Executive Summary

* The TAC recommends that the scope of the consortium be to
  "promote the widespread use of hardware-based trusted execution
  environments".

* The TAC recommends that the definition of the term Confidential
  Computing be: "Confidential Computing is the protection of data
  in use by performing computation in a hardware-based Trusted
  Execution Environment."

* For both the scope of the CCC, and the definition of confidential
  computing, the TAC recommends avoiding using the following terms
  in ways that imply constraints, as being technically problematic:
  "cloud", "main processor", and "encrypted"/"encryption".

* Similarly, the TAC recommends against any language implying that
  "protecting data in use" is synonymous with "confidential computing",
  as the latter is only a subset of technologies for the former.

## 1. Introduction

This document discusses two related, but different, questions:

1. Should the term "confidential computing" be narrowly scoped to TEEs
   (or even only certain classes of TEE) or more broadly defined?
   [Section 2](#markdown-header-2-fine-grained-questions) breaks this
   question down further.

2. Should the consortium's scope be narrowly scoped to TEE-based projects,
   or be more inclusive?

The board needs to answer each of the above questions, keeping in mind that:

* If a narrow answer is chosen, the focus stays on TEEs, and messaging 
  on terminology might compete with other bodies in the industry that
  also deal with protecting data in use.

* If a broad answer is chosen, more discussion happens inside the CCC and the
  CCC has the opportunity to have more unified messaging across the industry
  regarding protecting data in use.

## 2. Related Terminology

The TAC conducted a survey of various terms in the industry related to
protecting data in use, and
composed the following Venn diagram of technologies:

![Figure 1: Related Terminology](related-terminology.png)

Definitions of the various terms in the diagrams can be found in
[Appendix A](#markdown-header-appendix-a-related-terminology).

The solid blue lines indicate that the area is clearly already in scope
for CCC discussion and projects. The dotted blue lines indicate initial
uncertainty
as to whether they would (or should) fall into any intended definition
of "confidential computing" and/or scope of the CCC.

For example, the term "privacy-preserving computation" is confusingly
similar to "confidential computing", so that a novice reader can easily
think these terms are synonymous. It is up to the board's scoping decisions
to determine the extent to which they are synonymous, related, or disjoint,
based on the TAC's technical information provided in this document,
along with any other relevant considerations.

There are other relevant standards bodies operating in the overall space,
as depicted in the following diagram:

![Figure 2: Related Organizations](related-organizations.png)

In addition to those shown in the diagram, ISO/IEC JTC1/SC27 is now
doing work ([N 20273](https://standardsdevelopment.bsigroup.com/projects/9020-03692)) 
on multiparty computation and may expand to other areas, and the ITU has 
published the
[UN Handbook on Privacy-Preserving Computation Techniques](http://publications.officialstatistics.org/handbooks/privacy-preserving-techniques-handbook/UN%20Handbook%20for%20Privacy-Preserving%20Techniques.pdf)
that covers the entire space of the diagram, even though it has
"privacy-preserving computation" in the title.  While the ISO
work is based on member states, the ITU work has a multistakeholder model.

Based on the CCC scoping, various relationships (e.g., liaisons) might
be appropriate.  (None of the others are legal entities hosting open
source projects, but all of them publish specifications.)

## 2. Fine-Grained Questions

The TAC concluded that each scoping question can be broken down further
into five roughly orthogonal axes, each with a spectrum of narrow-to-broad
options:

1. Hardware/software only or also algorithmic (mathematical)? The TAC
   has rough consensus to focus on promoting the hardware/software end,
   which would exclude purely algorithmic technologies
   such as homomorphic encryption and multiparty computation.

2. Hardware-based (+firmware?) required or also software-only? The TAC 
   has consensus that only hardware-rooted technologies can provide
   the desired level of security, in particular for attestation.
   Software only projects can be considered if they demonstrably
   "promote" the use of hardware-backed solutions.  (For example,
   a development-time-only emulation technology meant to speed development
   of hardware-backed solutions.)

3. Generalized (fully programmable) only, or also configurable
   (semi-programmable) and even specialized (fixed-purpose, non-programmable)
   also?  So far, no one on the TAC has argued for non-programmable, but
   the TAC did not ask the question of whether it would want to reject a
   submission in that category.

4. On-main CPU only, or also separate processors also?  The TAC has consensus
   to recommend that the board include the entire spectrum here.

5. Cloud only, or also on-premises (including IoT) also?  The TAC has consensus
   to recommend that the board include the entire spectrum here.

All five of these are strategy questions for the board to answer, not
technical questions for the TAC per se, although based on the answers
chosen, the TAC will have technical feedback on any resulting wording.

The TAC also discussed that other attributes (e.g., TCB size) are also
important security evaluation criteria for any given solution or project,
but by themselves weren't seen as part of a scoping question per se.

The following table shows how various example technologies fall into the 
above axes, to help illustrate how answers would affect what sorts of 
projects might be accepted or rejected as a result:

![Figure 3: Example Technologies](examples-matrix.png)

## 3. Confidential Computing Definitions

There are various competing definitions of "confidential computing"
including (possibly among others):

* **Gartner report**: Confidential computing is the combination of 
  CPU-based hardware technology and infrastructure as a service (IaaS)
  **cloud** provider virtual machine (VM) images and software tools that 
  enable cloud-using organizations to create completely isolated
  **trusted execution environments (TEE), also called enclaves**. Because
  they offer a form of **encryption** of data in use, these enclaves
  render sensitive information invisible to host OSs and cloud providers.

The TAC observed the following issues with the above definition:

1. It is constrained to only cloud, whereas the TAC consensus is that
   a broader scope is needed, even for projects already in the CCC.

2. The term "encryption" is problematic since some TEEs of interest
   may have other forms of protecting data in use, encryption is just
   one example mechanism.  That is, encryption is a specific mechanism
   rather than a property we are seeking.  You can provide confidentiality
   by access control (for example) and not actually require encryption.

* **[CCC press release](https://www.linuxfoundation.org/uncategorized/2019/10/confidential-computing-consortium-establishes-formation-with-founding-members-and-open-governance-structure/)**: Established in 2019, the Confidential
  Computing Consortium brings together hardware vendors, cloud providers,
  developers, open source experts and academics to accelerate the
  confidential computing market; influence technical and regulatory
  standards; build open source tools that provide the right environment
  for **TEE** development' and host industry outreach and education
  initiatives. Its aims to address **computational trust and security
  for data in use, enabling encrypted data to be processed in memory
  without exposing it to the rest of the system**, reducing exposure
  to sensitive data and providing greater control and transparency for users.

The TAC observed the following issues with the above text:

1. The use of "encrypted" is again seen as problematic.

2. The text is ambiguous about the scope, as the text about
   tools is constrained to "TEE" development, but the aims are broader,
   applying to protecting "data in use", where all of Figure 1 would
   claim to be about protecting data in use.

* **[Mark Russinovich blog](https://azure.microsoft.com/en-us/blog/introducing-azure-confidential-computing/)**: Put simply, confidential computing 
  offers a protection that to date has been missing from public clouds, 
  **encryption of data while in use**. ...
  Confidential computing ensures that when data is "in the clear," which
  is required for efficient processing, the data is protected inside a
  Trusted Execution Environment (TEE - also known as an enclave), an
  example of which is shown in the figure below. TEEs ensure there is
  no way to view data or the operations inside from the outside, even
  with a debugger. They even ensure that only authorized code is permitted
  to access data. If the code is altered or tampered, the operations
  are denied and the environment disabled. The TEE enforces these
  protections throughout the execution of code within it.

The use of "encrypted" is again seen as problematic.  Also the definition
is similarly ambiguous in that "data while in use" is broad (all of Figure 1)
but then the discussion only mentions TEEs.  (A request to Mark for
clarification resulted in him answering that he did not intend the definition
to be limited to TEEs.)

* **[TechTarget definition](https://searchcloudcomputing.techtarget.com/definition/confidential-computing)**: Confidential computing is a concept in 
  which **encrypted** data can be processed in memory to limit access to
  ensure **data in use is protected**. Confidential computing is a concept
  promoted by the Confidential Computing Consortium, which is a group of
  organizations that wants to build **tools supporting the protection of
  data**. This concept is especially suitable for public clouds. 

The use of "encrypted" is again seen as problematic.  However, the rest of
the definition is clearly broadly scoped to protecting data in use (not
phrased to be limited to TEEs), and the article goes on to discuss the CCC
after the above definition.

* **[CCC FAQ definition](https://confidentialcomputing.io/)**:
  Confidential computing focuses on **securing data in use**. Current approaches
  to securing data often address data at rest (storage) and in transit
  (network) but **encrypting** data in use is possibly the most challenging step
  to providing a fully **encrypted** lifecycle for sensitive data. Confidential
  computing will enable **encrypted** data to be processed in memory without
  exposing it to the rest of the system and reduce exposure for sensitive
  data and provide greater control and transparency for users.

The use of "encrypted" is problematic.  The paragraph can also be read as
implying that confidential computing is the only technology in the space of
protecting data in use, which also may be problematic.

The TAC iterated on several proposals for wording around the scope of
what projects the TAC would recommend as being in scope of the CCC.
The following wording obtained rough consensus:

* "promote the widespread use of hardware-based trusted execution environments".

This proposal puts the focus on only hardware-based TEEs, while providing
some leeway with the use of "promote" to allow for non-hardware based
projects that demonstrably promote the use of hardware-based TEEs.

Similarly, the TAC iterated on several proposals for wording around
the definition of the term "confidential computing".  The following
wording obtained rough consensus:

* "Confidential Computing is the protection of data in use by performing
  computation in a hardware-based Trusted Execution Environment."

## Appendix A. Related Terminology

### A.1. Trusted Execution Environment (TEE)

There are many competing definitions of what a "TEE" is, many of which are
listed below:

* **[Wikipedia](https://en.wikipedia.org/wiki/Trusted_execution_environment)**:
  A secure area of a **main** processor. It guarantees code and data loaded
  inside to be protected with respect to confidentiality and integrity. A
  TEE as an isolated execution environment provides security features such
  as isolated execution, integrity of applications executing with the TEE,
  along with confidentiality of their assets.

As noted earlier, the TAC dislikes the above definition because of its
constraint to a "main" processor.

* **[ARM website](https://blog.quarkslab.com/introduction-to-trusted-execution-environment-arms-trustzone.html)**: a secure area inside a **main**
  processor. It runs in **parallel of the operating system**, in an
  isolated environment. It guarantees that the code and data loaded in
  the TEE are protected with respect to confidentiality and integrity. 

Besides the "main" processor issue, another problem the TAC saw with the
above definition is that it assumes there exists a regular operating system
on the same processor.  In some environments (MCUs, FPGAs, etc.), that is
not necessarily the case.

* **GlobalPlatform**: A device that conforms to specifications from GP's
  [TEE Committee](https://globalplatform.org/technical-committees/trusted-execution-environment-tee-committee/).

The above definition excludes various TEEs (including Intel SGX) from its
definition, which the TAC finds problematic.

* **Mike Bursell's strawman**: A hardware-based technique for securing
  sensitive data and algorithms in such a way that even the kernel,
  root user or hypervisor can't see what's going on

The above definition is narrowly scoped to only hardware-based TEEs,
and thus excludes the items in [Section A.1.1](#markdown-header-a-1-1-software-tee).

One relatively minor issue as worded is that it implies that the TEE has
a kernel, root user, or hypervisor, which may or may not be the case.

* **[IETF TEEP WG](https://tools.ietf.org/html/draft-ietf-teep-architecture)**:
  An environment that enforces that only authorized code can execute with
  that environment, and that any data used by such code cannot be read
  or tampered with by any code outside that environment.

Thie above definition is broader, includes language similar to the broader
text in the Mark Russinovich blog, and has no immediate flaws that the TAC
found.  Some TAC individuals would like to see additional constraints
added to it, but there is not necessarily TAC consensus on such gaps.
(Full disclosure: the TAC chair is also a co-editor of the IETF document
with the above definition.)

#### A.1.1. Software TEE

There are multiple products and solutions today that are software-based and
use the term "TEE", ranging from ones meant for production use, to ones
meant just for development of code to be later used on hardware TEEs.

Some examples include:

* **[Virtual Secure Mode (VSM)](https://azure.microsoft.com/en-us/blog/introducing-azure-confidential-computing/)**: a software-based TEE that's
  implemented by Hyper-V in Windows 10 and Windows Server 2016. Hyper-V 
  prevents administrator code running on the computer or server, as well
  as local administrators and cloud service administrators from viewing
  the contents of the VSM enclave or modifying its execution.

* **[QEMU](https://www.linaro.org/blog/arm-trustzone-qemu/) ("quick emulator")**: very widely used open source machine emulator. ... Developers can use 
  the QEMU Arm Security Extensions to develop and work with Trusted
  Execution Environments (TEEs) that are likely to be the primary consumers
  of the added functionality. Secure applications can then be developed
  on the added TEEs without the need for dedicated hardware.

Other examples exist from other organizations not affiliated with the CCC.

### A.2. Privacy-Preserving Computation

* **[multi-party computation (MPC)](https://en.wikipedia.org/wiki/Multi-party_computation)**, or **privacy-preserving computation**: a subfield of
  cryptography with the goal of creating methods for parties to jointly
  compute a function over their inputs while keeping those inputs private.
  Unlike traditional cryptographic tasks, where cryptography assures
  security and integrity of communication or storage and the adversary
  is outside the system of participants (an eavesdropper on the sender
  and receiver), the cryptography in this model protects participants'
  privacy from each other.

* **[Homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption)**: a form of encryption that allows computation on ciphertexts,
  generating an encrypted result which, when decrypted, matches the
  result of the operations as if they had been performed on the plaintext.
  Homomorphic encryption can be used for **privacy-preserving** outsourced
  storage and **computation**. This allows data to be encrypted and
  out-sourced to commercial cloud environments for processing, all while
  encrypted.

Other sources discussing the relationship among these terms, that were
instrumental in constructing Figure 1, include:

* https://baffle.io/blog/homomorphic-and-multiparty-computation/

* https://medium.com/@PlatON_Network/privacy-preserving-computation-secure-multi-party-computation-i-5b09a20053ce

### A.3. Other Terms

* **[secure cryptoprocessor](https://en.wikipedia.org/wiki/Secure_cryptoprocessor)**: a dedicated computer-on-a-chip or microprocessor for carrying out
  cryptographic operations, embedded in a packaging with multiple physical
  security measures, which give it a degree of tamper resistance. Unlike
  cryptographic processors that output decrypted data onto a bus in a
  secure environment, a secure cryptoprocessor does not output decrypted
  data or decrypted program instructions in an environment where security
  cannot always be maintained. The purpose of a secure cryptoprocessor is
  to act as the keystone of a security subsystem, eliminating the need to
  protect the rest of the subsystem with physical security measures.

* **[Trusted Platform Module](https://en.wikipedia.org/wiki/Trusted_Platform_Module)** (**TPM**, also known as ISO/IEC 11889): an international standard
  for a secure cryptoprocessor, a dedicated microcontroller designed to
  secure hardware through integrated cryptographic keys.

* **[hardware security module (HSM)](https://en.wikipedia.org/wiki/Hardware_security_module)**: a physical computing device that safeguards and manages
  digital keys for strong authentication and provides cryptoprocessing.

* **[Secure Element (SE)](https://www.justaskgemalto.com/en/what-is-a-secure-element/)**: a microprocessor chip which can store sensitive data and run
  secure apps such as payment. It acts as a vault, protecting what's inside
  the SE (applications and data) from malware attacks that are typical in
  the host (i.e. the device operating system).

* **[Dedicated Security Component](https://www.commoncriteriaportal.org/communities/docs/cpp_dsc_v10d_DRAFT_20190501.docx)**: the combination of a
  hardware component and its controlling firmware dedicated to providing
  the encompassing platform with services for the provisioning, protection,
  and use of Security Data Objects (SDOs) consisting of keys, identities,
  attributes, and other types of Security Data Elements (SDEs).
