## Project Proposal - RUST-SPDM

### General Information
1.1. Name of Project

rust-spdm

1.2. Project Description

Security Protocol and Data Model ([SPDM](https://www.dmtf.org/dsp/DSP0274)) is an authenticated secure session protocol defined by [DMTF](https://www.dmtf.org/standards/spdm).

In confidential computing, SPDM can be used for secure communication between a Trusted Execution Environment (TEE) and another entity. For example, TEE-IO architecture requires TEE Security Manager (TSM) using SPDM to communicate with a TEE-IO device. A virtual TPM solution may use SPDM for the communication between the TEE and a vTPM service provider.

rust-spdm is an SPDM implementation with [rust](https://www.rust-lang.org/) programming language.

1.3. How does this project align with the Consortium's [Mission Statement](README.md)  

This project helps accelerate the adoption of confidential computing by providing a reusable component for an emerging usage area. This project is potentially adoptable by any confidential computing project that needs to bring SPDM capable devices into the Trusted Computing Base (TCB).

1.4. Project website URL  

It is at https://github.com/intel/rust-spdm.

1.5. Social media accounts  

N/A

### Legal Information
2.1. Project Logo URL or attachment (Vector Graphic: SVG, EPS).  

N/A - the project does not have a logo.

2.2. Project license.  We recommend an [OSI-approved license](https://opensource.org/licenses), so if the license is not one on the list, explain why.  

Apache-2.0.

2.3. Existing financial sponsorship.  

Intel

2.4. Trademark status.  

rust-spdm is not trademarked.

2.5. Proposed Technical Charter, based on the template.  
([Word version](https://lists.confidentialcomputing.io/g/main/files/TAC/Project%20Submissions/Technical%20Charter%20%28custom+data%29%20--%20LF%20Projects,%20LLC%204-10-2019%20FINAL%20%2811%29.docx),
[PDF version](https://lists.confidentialcomputing.io/g/main/files/Governing%20Board/Docs/LF_Projects_Technical_Charter.pdf)).
Include doc as attachment or give URL of doc.  It is ok to change the
text (e.g., "Technical Steering Committee") to match the actual structure of
the project; projects are free to use whatever governance structure they want.

See attachment

### Technical Information
3.1. High level assessment of project synergy with existing projects under the CCC, including how the project compliments/overlaps with existing projects, and potential ways to harmonize over time. Responses may be included both inline and/or in accompanying documentation.  

No other rust-spdm project in CCC.

3.2. Describe the [Trusted Computing Base (TCB)](https://en.wikipedia.org/wiki/Trusted_computing_base) of the project. If the project supports multiple environments please describe each TCB. Also identify if dependencies of other project (both CCC or non-CCC) TCBs are taken.    

N/A. rust-spdm is an implementation of SPDM protocol. The TCB should be identified by the integrator.

3.3. Project Code of Conduct URL.  We recommend a [Contributor Covenant v2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) based Code of Conduct, so if the Code of Conduct is not based on that, explain why.  

[Contributor Covenant v2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

3.4. Source control URL  

Same github.

3.5. Issue tracker URL  

Same github.

3.6. External dependencies (including licenses, and indicate whether each is a build time or runtime dependency)  

Build time dependency:
* [ring](https://github.com/briansmith/ring)
* [webpki](https://github.com/briansmith/webpki)

3.7. Standards implemented by the project, if any. Include links to any such standards.  

[SPDM](https://www.dmtf.org/dsp/DSP0274)

3.8. Release methodology and mechanics  

Quarterly in github

3.9. Names of initial committers, if different from those submitting proposal  

Jiewen Yao <jiewen.yao@intel.com>

3.10. List of project's official communication channels (slack, irc, mailing lists)  

github

3.11. Project [Security Response Policy](security-response-policies.md)  

github security

3.12. Preferred maturity level (Sandbox, Incubation, Graduation, or Emeritus)  

Sandbox

3.13. Any additional information the TAC and Board should take into consideration when reviewing your proposal.  

N/A
