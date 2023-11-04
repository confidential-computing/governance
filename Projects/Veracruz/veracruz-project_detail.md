## Project Proposal Template

### General Information

1.1. Name of Project

Veracruz

1.2. Project Description (what it does, why it is valuable, origin and history)

Veracruz is both a research project and a framework for defining secure
multi-party computations amongst a group of mutually-distrusting principals.
Veracruz makes use of "strong isolation technology", our idiosyncratic term
for a range of hardware- and hypervisor-based isolation mechanisms to establish
a "neutral ground" within which a collaborative computation takes place.  Remote
attestation is used by all principals enrolled in a computation to authenticate
the Veracruz trusted runtime, loaded within a strong isolate, before securely
provisioning their secrets via TLS.  Specific computations are realized by
providing a WebAssembly binary, compiled against a custom ABI, and varying a
global policy which describes the identities and roles of every principal
enrolled in the computation.

Suggested potential use-cases for Veracruz include:

  - Privacy-preserving collaborative machine learning,
  - Privacy-preserving genomics,
  - Secure delegation of complex workloads off computationally-underpowered
    devices,
  - IP protection for novel algorithms,
  - ...and many other potential uses.

In contrast to purely-cryptographic approaches, such as homomorphic encryption,
functional encryption, and secure multi-party computation protocols, which are
typically used to effect some of the privacy-preserving computations listed
above, Veracruz aims to be more efficient, more familiar to programmers, and
more flexible, whilst still offering a strong guarantee of security/privacy.

Veracruz was conceived, and developed by, members of the Security research group
within Arm Research.  Recently, the project reached a state of maturity where we
feel it is viable to continue development ``out in the open'' and try to attract
collaborators to work on the project alongside the original development team.
Toward this end, we have recently submitted a publication (under double-blind
review) describing the project, have started to talk about the project with
existing collaborators and contacts, and now wish to win adoption of the project
by the CCC as a means of furthering these potential collaborations.

1.3. How does this project align with the Consortium's [Mission Statement](README.md)

We align with this mission statement in a number of ways:

  - Veracruz is a flexible framework with many potential use-cases, as discussed
    above.  The project is therefore a demonstration of what novel distributed,
	privacy-preserving computations can be designed and implemented using
	Trusted Execution Environments and related technologies, like Remote
	Attestation protocols.  Indeed, the genesis of Veracruz was the research
	question: "what do new distributed systems look like if TEEs and remote
	attestation protocols become all-pervasive?".  As a result, we were
	motivated to first define a flexible framework within which general
	privacy-preserving computations can be defined (this is now largely done,
	albeit we have plans for improvements and new features), and then find
	potential new use-cases for this framework (this is yet to be done, but we
	have bold ideas, e.g. privacy-preserving grid-compute, map-reduce, and so
	on, all of which will motivate further research).
  - One novelty of Veracruz is its focus on supporting multiple TEE-like
    technologies, which we collectively call "strong isolation technologies":
	Arm TrustZone (under OP-TEE), Intel SGX, and software-based "enclaves"
	using the high-assurance seL4 microkernel, at present, though more may be
	added in the future.  This heterogeneity is, we feel, an under-appreciated
	area of research, not just because it's likely that real distributed systems
	making use of TEEs will require co-operation and co-ordination between
	components written using multiple TEEs (e.g. Arm TrustZone on a mobile phone,
	Intel SGX on a data-centre server), but also because different TEE
	implementations support different Remote Attestation protocols, different
	programming models, and different trust- and threat-models.  One area where
	we have invested a good deal of research time is trying to abstract over
	these differences in Veracruz, providing e.g. a uniform Remote Attestation
	interface to client code interacting with the Veracruz runtime, and
	providing a uniform, albeit simplistic, programming model based around
	WebAssembly and a custom ABI.  We have therefore tried hard to *hide*
	differences between platforms, to the extent possible, by providing some
	common abstractions, which we feel is key to accelerating adoption of these
	technologies.  Some of these ideas, and maybe code, could potentially be
	adopted by other CCC projects (discussed further, below).
  - We hope, by gaining CCC membership for Veracruz, to attract further
    collaborators external to the CCC, and work alongside other CCC projects on
	areas of mutual interest, therefore accelerating the development of Veracruz
	and existing projects.

1.4. Project website URL

Development is currently hosted on a private Git repository within Arm Research.
We are in the process of open-sourcing the code, and will host the project as a
series of public repositories under an umbrella Github organization:
https://github.com/veracruz-project.  We will host a project website using
Github pages, under this account.

1.5. Social media accounts  

N/A

### Legal Information

2.1. Project Logo URL or attachment (Vector Graphic: SVG, EPS)

N/A

2.2. Project license.  We recommend an [OSI-approved license](https://opensource.org/licenses), so if the license is not one on the list, explain why   

MIT

2.3. Existing financial sponsorship

The project was conceived of, and developed by, members of Arm Research.  This
development will continue for the foreseeable future.

2.4. Trademark status

Veracruz is not trademark protected.

### Technical Information

3.1. High level assessment of project synergy with existing projects under the CCC, including how the project compliments/overlaps with existing projects, and potential ways to harmonize over time. Responses may be included both inline and/or in accompanying documentation.  

Note that a full comparison between Veracruz and OpenEnclave and Enarx, two
existing CCC projects, is included in an attached FAQ document.  Moreover,
Veracruz implicitly builds upon the Linux SGX SDK, the final remaining CCC
project at the time of writing.

In summary, however: Veracruz is a research project exploring how novel
distributed systems can be built using strong isolation and Remote Attestation.
A peculiar aspect of Veracruz is its focus on heterogeneity: we support multiple
strong isolation technologies and therefore must work hard to provide uniform
abstractions over differences in these technologies.  One way that we do this is
by adopting WebAssembly (or Wasm, henceforth) to provide a uniform programming
model based around a simple custom ABI.  We also adopt a Veracruz-specific
attestation service, which interposes between the native attestation service and
protocol tied to a particular strong isolation technology (e.g. the Intel
Attestation Service with EPID for Intel's SGX) and client software.  This
attestation service exposes a uniform attestation protocol, PSA attestation, to
clients irrespective of the particular strong isolate that they are trying to
authenticate.

This attestation model simplifies client code, by removing the need to support
a panoply of different attestation protocols, but also provides an opportunity
to adopt more sophisticated/different models of attestation than those typically
provided by existing attestation services, e.g. allowing clients to provide
declarative descriptions of "what they are willing to trust" and have the
attestation service authenticate or reject an attestation token based on that
description, as appropriate.

Note that we envision any project that supports more than one strong isolation
technology (e.g. if Enarx moved beyond supporting only AMD SEV) to want to
abstract over attestation protocols and services, as the differences between the
various attestation models quickly becomes onerous.  As a result, we foresee the
potential for other projects, in the CCC and outside of it, to adopt our proxy
attestation service, or a similar model.

Moreover, note that both Veracruz and Enarx make essential use of Wasm for
abstraction and sandboxing purposes.  The focus of these two projects is very
different --- Enarx is concerned with protecting legacy workloads when delegated
to untrusted third parties, whilst Veracruz is focussed on providing an
infrastructure for safe collaboration between mutually untrusting principals ---
and therefore the use of Wasm is slightly different in both cases.  Enarx, for
instance, supports the full WASI ABI owing to the fact that they aim to support
unmodified Linux binaries.  Veracruz, on the other hand, has a purposefully
limited ABI that aims to pin the behaviour of the program effecting the
computation down to what is, essentially, a pure (albeit random) function of its
inputs.  As a result, though Enarx and Veracruz appear superficially similar,
and use similar technology sets, the two projects are different but potentially
complimentary: an Enarx-protected application could "call out" to a Veracruz
computation, for instance, to securely collaborate with some other bit of code.

Moreover, as Enarx and Veracruz use similar technologies, there is potential
for collaboration between the two projects in developing e.g. Wasm under
SEV/SGX/TrustZone/seL4/and so on.  In particular, supporting execution
strategies for Wasm, other than interpretation, such as JITting and
ahead-of-time compilation within a strong isolate represents significant amounts
of work.  It would make sense for projects that need this infrastructure to pool
their efforts, rather than repeating work over-and-over again.

Similarly, for implementing remote attestation on Arm TrustZone and seL4 --- two
platforms that Veracruz supports --- there is room for collaboration, too.  At
present, the attestation flow in Veracruz for these two platforms is stubbed out
pending an implementation of e.g. secure boot and other bits of necessary
machinery for these platforms.  This is material that will likely be useful to
any other project supporting these two isolation technologies, and therefore
poses another opportunity for collaboration.

3.2. Describe the [Trusted Computing Base (TCB)](https://en.wikipedia.org/wiki/Trusted_computing_base) of the project. If the project supports multiple environments please describe each TCB. Also identify if dependencies of other project (both CCC or non-CCC) TCBs are taken.  

As Veracruz supports Arm TrustZone, Intel SGX, and seL4, we have a tripartite
Trusted Computing Base.  We handle each separately, in turn:

**Arm TrustZone**:

Users must trust:

  - The OP-TEE trusted execution environment (external dependency)
  - The Baidu Rust TrustZone/OP-TEE SDK (external dependency),
  - The correctness of the implementation of Arm TrustZone,
  - Note that the attestation flow for Arm TrustZone is currently stubbed out.
    When this is completed, users wishing to authenticate a Veracruz instance
	running under TrustZone would also need to trust the measured boot
	implementation, and any external attestation service used. 

**Intel SGX**:

Users must trust:

  - The Intel C/Linux SDK for SGX and its associated tools, e.g. for generating
    ECALL/OCALL bindings (external dependency).
  - The Baidu Rust SDK for SGX that binds the Intel C SDK (external dependency).
  - The correctness of the implementation of Intel SGX,
  - The correctness of the EPID protocol and Intel Attestation Service for
    Remote Attestation on the SGX platform.

**seL4**:

Users must trust:

  - The correctness of the seL4 kernel (external dependency).  Note that this
    kernel is accompanied by strong evidence of its correctness in the form of
	machine-checked proofs.  To trust these, users must trust the Isabelle/HOL
	proof-assistant (i.e. HOL is consistent and that Isabelle/HOL correctly
	implements HOL) and the statements of all correctness theorems.
  - The correctness of the underlying AArch64 implementation.

**Common**:

Users must trust:

  - The correctness of the trusted Veracruz runtime that executes inside the
    strong isolate and which effects the collaborative computation.
  - The correctness of the Veracruz SDK provided to support programmers
    developing computations for deployment on Veracruz.  Note that this SDK
	includes a fork of the standard Rust `getrandom` and `rand` crates for
	working with random numbers and distributions on the Veracruz platform.
  - The correctness of our modifications to the Ring/RusTLS libraries to
    accommodate self-signed certificates, and our derived Remote Attestation
	and provisioning protocols, built using this self-signed certificate
	facility and platform-specific Remote Attestation.
  - The attestation software executing inside a "root isolate", used as part of
    the Veracruz attestation flow, and which is used to attest other isolates.
  - The Veracruz attestation service, which authenticates or rejects PSA
    attestation tokens.
  - The correctness of the PSA attestation protocol, and of the implementation
    of that protocol.
  - The correctness of the TLS protocol, and the implementation of TLS and
    associated material in the Ring/RusTLS libraries (external dependency).
  - The correctness of the Rust compiler and associated toolchains.
  - The semantics of the WASM language, and that the Wasmi/Wasmtime execution
    engines (external dependencies) correctly implement the published semantics.

3.3. Project Code of Conduct URL.  We recommend a [Contributor Covenant v2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) based Code of Conduct, so if the Code of Conduct is not based on that, explain why.  

We have adopted the [Contributor Covenant v2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).
The text of this code-of-conduct is provided verbatim in a document,
`CONTRIBUTING.markdown`, provided in the root directory of the Veracruz
distribution along with other information on how to contribute to the Veracruz
codebase.

3.4. Source control URL  

Development is currently hosted on a private Git repository within Arm Research.
We are in the process of open-sourcing the code, and will host the project as a
series of public repositories under an umbrella Github organization:
https://github.com/veracruz-project

3.5. Issue tracker URL  

This is currently hosted on a private Gitlab instance.  Issues will be moved to
the aforementioned Github repository, as appropriate.

3.6. External dependencies (including licenses, and indicate whether each is a build time or runtime dependency)  

Note that the dependencies below are the "top-level" dependencies of the
Veracruz project in its entirety, as specified in our sub-project's Cargo.toml
build scripts (Veracruz is written in pure Rust).  We do not list transitive
sub-dependencies of our own dependencies.  Moreover, the dependencies below
represent the libraries that we use when writing the trusted Veracruz runtime,
untrusted "bridge" code between clients and the isolate, the Veracruz SDK,
examples, and the Veracruz proxy attestation service.  We write X/Y to denote a
library that is dual licensed under licenses X and Y.

Runtime dependencies:

  - actix-http: MIT/Apache 2.0,
  - actix-rt: MIT/Apache 2.0,
  - actix-web: MIT/Apache 2.0,
  - async_std: MIT/Apache 2.0,
  - base64: MIT/Apache 2.0,
  - bincode: MIT,
  - byteorder: Unlicense/MIT,
  - cfg-if: MIT/Apache 2.0,
  - chrono: MIT/Apache 2.0,
  - clap: MIT,
  - csv: Unlicense/MIT,
  - curl: MIT,
  - diesel: MIT/Apache 2.0,
  - dotenv: MIT,
  - env_logger: MIT/Apache 2.0,
  - failure: MIT/Apache 2.0,
  - futures: MIT/Apache 2.0,
  - getrandom: MIT/Apache 2.0,
  - hex: MIT/Apache 2.0,
  - lazy_static: MIT/Apache 2.0,
  - libc: MIT/Apache 2.0,
  - log: MIT/Apache 2.0,
  - openssl: Apache 2.0,
  - optee_utee (from Rust TrustZone SDK): Apache 2.0,
  - optee-utee-sys (from Rust TrustZone SDK):  Apache 2.0,
  - percent-encoding: MIT/Apache 2.0,
  - pinecone: MIT/Apache 2.0,
  - protobuf: MIT,
  - rand: MIT/Apache 2.0,
  - reqwest: MIT/Apache 2.0,
  - ring: non-standard (ISC-style license, derived from Boring SSL),
  - rouille: MIT/Apache 2.0,
  - rustls: MIT/Apache 2.0/ISC,
  - rusty-machine: MIT,
  - serde: MIT/Apache 2.0,
  - serde_json: MIT/Apache 2.0,
  - sgx_alloc (from Rust SGX SDK): Apache 2.0,
  - sgx_tcrypto (from Rust SGX SDK): Apache 2.0,
  - sgx_tdh (from Rust SGX SDK): Apache 2.0,
  - sgx_trts (from Rust SGX SDK): Apache 2.0,
  - sgx_tstd (from Rust SGX SDK): Apache 2.0,
  - sgx_types (from Rust SGX SDK): Apache 2.0,
  - sgx_ucrypto (from Rust SGX SDK): Apache 2.0,
  - stringreader: MIT,
  - strsim: MIT,
  - toml: MIT/Apache 2.0,
  - typetag: MIT/Apache 2.0,
  - untrusted: ISC,
  - wasmi: MIT/Apache 2.0,
  - wasmtime: Apache 2.0 with LLVM exception,
  - webpki-roots: MPL-2.0,
  - webpki: ISC-style,
  - wee_alloc: MPL-2.0,
  - x509-parser: MIT/Apache 2.0,

Buildtime dependencies:

  - bindgen: BSD 3-clause,
  - cmake: MIT/Apache 2.0,
  - protoc-rust: MIT,
  - target_build_utils: ISC/Apache-2.0,
  - uuid: MIT/Apache 2.0,

Test dependencies:

  - mockall: MIT/Apache 2.0,
  - mockito: MIT

3.7. Standards implemented by the project, if any. Include links to any such standards.  

We implement the PSA attestation protocol, as part of our abstraction over the
various different protocols in use by our supported strong isolation
technologies.  This is a draft IETF standard, see:

Tschofenig, H., Frost, S., Shaw, A., and T. Fossati, "Arm's Platform Security
Architecture (PSA) Attestation Token", draft-tschofenig-rats-psa-token-05 (work
in progress), March 2020.

Available at:

https://tools.ietf.org/html/draft-tschofenig-rats-psa-token

3.8. Release methodology and mechanics

As a research project we have, to-date, not had a defined release strategy.
However, upon open-sourcing we intend to regularly tag (e.g. every four months)
repository source snapshots with a release marker.

3.9. Names of initial committers, if different from those submitting proposal

Derek Miller, Dominic Mulligan, Nick Spinale, Shale Xiong.

3.10. List of project's official communication channels (slack, irc, mailing lists)  

Currently we use a private Slack channel in an Arm-internal workspace.

We intend to switch to a CCC-hosted mailing list as the primary channel for
discussing design and strategy issues if-and-when we are adopted by the CCC, as
well as opening a public Slack channel for more informal discussion about the
project.

3.11. Project [Security Response Policy](security-response-policies.md)  

Security-related bugs can be privately reported to a monitored email alias
(veracruz-project@arm.com).  All security-related bug reports will be treated
seriously, and we will work with the reporter to identify and push a fix.
A document `SECURITY_POLICY.markdown`, in our repository root directory,
fully explains our security policy.

3.12. Preferred maturity level (Sandbox, Incubation, Graduation, or Emeritus)  

Sandbox.

3.13. Any additional information the TAC and Board should take into consideration when reviewing your proposal.

A Frequently Asked Questions ("FAQ") document explaining Veracruz in more detail
has been attached along with this form.