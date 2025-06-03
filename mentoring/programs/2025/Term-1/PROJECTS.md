# CCC Mentorship Projects Term 1

## Application Instructions

Mentee application instructions can be found [here](mentees/README.md#application-process).

## Completed Mentorship Opportunities

<!-- TOC -->
* [Islet](#islet)
    * [Strengthening Security through Fuzz Testing](#strengthening-security-through-fuzz-testing)
* [Veraison](#veraison)
    * [Harmonizing Open-Source Verifiers with RATS Standards](#harmonizing-open-source-verifiers-with-rats-standards)
    * [Enhancing CoRIM Support](#enhancing-corim-support)
<!-- TOC -->

### Islet

#### Strengthening Security through Fuzz Testing

- Description: Enhance Islet’s security by identifying vulnerabilities early using fuzz testing. This project integrates Cargo Fuzz tools with Islet’s CI pipeline, focusing on testing RMM interfaces (RMI and RSI) based on ARM’s RMM specification.
- Expected Outcome: Deliver a set of robust fuzz tests integrated into Islet’s CI, improving security and compliance with ARM standards.
- Recommended Skills: Knowledge of Rust programming and fuzz testing. Familiarity with confidential computing, virtualization, and ARM architecture is helpful but not required.
- Mentor(s):
    - Bokdeuk Jeong (@bokdeuk-jeong, bd.jeong@samsung.com)
    - Sangwan Kwon (@bitboom, sangwan.kwon@samsung.com)
- Upstream Issue: https://github.com/islet-project/islet/issues/398
- LFX URL: https://mentorship.lfx.linuxfoundation.org/project/fbd406ee-5d76-4d8b-939d-c37d42643fa8

### Veraison

#### Harmonizing Open-Source Verifiers with RATS Standards

- Description: Align Verifiers with the RATS model by defining evidence formats and attestation results, working toward integration with other projects like Keylime. Participants will work on adopting CMW for Evidence and EAT for Attestation Results.
- Expected Outcome: Deliver standardized evidence formats and adoption paths for open-source Verifiers, facilitating seamless integration with the RATS architecture.
- Recommended Skills: Familiarity with RATS architecture, attestation workflows, and policy management. Knowledge of TPM evidence formats is beneficial.
- Mentor(s):
    - Thore (@THS-on, mail@thson.de)
    - Thomas (@thomas-fossati, thomas.fossati@linaro.org)
- Upstream Issue: https://github.com/veraison/.github/issues/6
- LFX URL: https://mentorship.lfx.linuxfoundation.org/project/a3b8d4a8-0651-4059-b100-bcd0ea46b21e

#### Enhancing CoRIM Support

- Description: Strengthen Veraison’s support for CoRIM (Concise Reference Integrity Manifest) by adding signed CoRIM support to Veraison services. Participants will gain experience in RATS architecture, CoRIM specifications, and generating CoRIMs with cocli.
- Expected Outcome: Develop robust CoRIM security features integrated into Veraison’s services, enabling multi-signature and enhanced security for integrity verification.
- Recommended Skills: Familiarity with RATS architecture, CoRIM, and API interaction. Experience with Go or related languages will be helpful.
- Mentor(s):
    - Thomas (@thomas-fossati, thomas.fossati@linaro.org)
    - Sergei (@setrofim, sergei.trofimov@arm.com)
    - Yogesh (@yogeshbdeshpande, yogesh.deshpande@arm.com)
- Upstream Issue: https://github.com/veraison/.github/issues/5
- LFX URL: https://mentorship.lfx.linuxfoundation.org/project/80c135fc-de55-4542-86f5-65b91d267d11
