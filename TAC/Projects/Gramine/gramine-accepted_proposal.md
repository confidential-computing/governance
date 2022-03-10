
# Confidential Computing Consortium (CCC) Project Proposal

On behalf of the Graphene Maintenance Team - graphene-team@googlegroups.com

* Łukasz Gleń (Golem Factory)
* Michał Kowalczyk (Invisible Things Lab)
* Dmitrii Kuvaiskii (Intel)
* Don Porter (UNC Chapel Hill)
* Chia-Che Tsai (Texas A&M University)
* Mona Vij (Intel)
* Rafał Wojdyła (Invisible Things Lab)
* Isaku Yamahata (Intel)

1. Name of Project: Graphene Library OS

2. Project Description: (what it does, why it is valuable, origin and history)
    * Graphene library OS is open-source software for executing and protecting existing Linux-compatible applications, without modification of the application binaries, on Intel SGX and potentially other confidential computing platforms.
    * Graphene library OS contributes to the confidential computing community as both a research platform and a porting framework. Graphene accelerates experimentation with and deployment of software on confidential computing platforms, by implementing Linux compatibility on a small host API. The host API is designed to be easy to implement once in a given TEE or on another host OS, and then used by application developers.
    * Graphene library OS was originally developed in the OSCAR Lab at Stony Brook University. It was initially released in June 2014 as a research artifact. It was then ported to Intel SGX in Intel Labs (known as Graphene-SGX) with the v0.4beta release (in July 2016). In October 2018, The Graphene maintainers team was formed as the leadership of the project. In September 2019, the first stable version (v1.0.0) of Graphene was released. 

3. How does this project align with the Consortium's Mission Statement
    * Graphene Library OS accelerates the acceptance and adoption of confidential computing by adapting existing Linux-compatible applications to confidential computing platforms and assisting agile development of confidential computing software.
    * Graphene Library OS is developed as a future enterprise-grade building block for supporting secure system application programming interfaces (APIs) in production software.
    * Graphene Library OS offers confidentiality-aware system services such as credentials, OS states and file systems protection for confidential computing software in order to minimize the trust in the system features of the host infrastructure.

4. High level assessment of project synergy with existing projects under the CCC, including how the project compliments/overlaps with existing projects, and potential ways to harmonize over time. Responses may be included both inline and/or in accompanying documentation.
    * Graphene Library OS complements the Intel Software Guard Extension (SGX) SDK and the OpenEnclave SDK.  At a high-level, SDKs are better suited for designing confidential computing applications from scratch, whereas Graphene facilitates protection of commercial, off-the-shelf (COTS) software on confidential computing platforms. Over time, Graphene library OS may be integrated with the SDKs as a way to securely provide POSIX APIs for the SDKs.
    * Graphene Library OS offers close-to-backward-compatibility for Linux application binaries and is complementary to the platform portability of Enarx. Over time, Graphene library OS may be combined with Enarx for the portability of Linux-compatible application binaries across confidential computing platforms.

5. Describe the [Trusted Computing Base (TCB)](https://en.wikipedia.org/wiki/Trusted_computing_base) of the project. if the project supports multiple environments please describe each TCB. Also identify if dependencies of other projects (both CCC or non-CCC) TCBs are taken.
    * The Intel(R) Software Guard Extension (SGX) (CCC)
    * The GNU C Library (non-CCC)
    * mbedTLS (non-CCC)
    * Intel SGX HW (non-CCC)
    * Intel SGX Platform SW (non-CCC), 

6. Project website URL: [https://grapheneproject.io/](https://grapheneproject.io/)

7. Project Code of Conduct URL (in progress, under discussion): [https://github.com/oscarlab/graphene/blob/501976f93888aa17a1d0af52b0a4e3729425cb79/CODE_OF_CONDUCT.md](https://github.com/oscarlab/graphene/blob/501976f93888aa17a1d0af52b0a4e3729425cb79/CODE_OF_CONDUCT.md)

8. Source control URL: [https://github.com/oscarlab/graphene](https://github.com/oscarlab/graphene)
    * # of releases (as of March 2020): 7
    * # of stars (persons watching this repository): 422
    * # of commits: 1301
    * # of pull requests: 47 open, 875 merged

9. Issue tracker URL: [https://github.com/oscarlab/graphene/issues](https://github.com/oscarlab/graphene/issues)
    * # of issues (as of March 2020): 211 open, 238 resolved

10. Project Logo URL or attachment (Vector Graphic: SVG, EPS)

    SVG: [https://drive.google.com/file/d/19pwVPBHjRXllnqL7hNbjUJcyIrOSv65M/view?usp=sharing](https://drive.google.com/file/d/19pwVPBHjRXllnqL7hNbjUJcyIrOSv65M/view?usp=sharing)  \
EPS: [https://drive.google.com/file/d/1wKGEcQD7-iaP_S1xa9qgHm8txg1hEaDz/view?usp=sharing](https://drive.google.com/file/d/1wKGEcQD7-iaP_S1xa9qgHm8txg1hEaDz/view?usp=sharing) 

11. Project license: LGPL v3 or later [https://github.com/oscarlab/graphene/blob/master/LICENSE.txt](https://github.com/oscarlab/graphene/blob/master/LICENSE.txt)

12. External dependencies (including licenses)
    * The Intel(R) SGX Platform Software (PSW): \
[https://github.com/intel/linux-sgx/blob/master/License.txt](https://github.com/intel/linux-sgx/blob/master/License.txt)
    * The GNU C Library: LGPL v2.1 or later [https://www.gnu.org/software/libc/manual/html_node/Copying.html](https://www.gnu.org/software/libc/manual/html_node/Copying.html)
    * GCC, The GNU Compiler Collection: [https://gcc.gnu.org/onlinedocs/libstdc++/manual/license.html](https://gcc.gnu.org/onlinedocs/libstdc++/manual/license.html)
    * GNU Make: GPL v3 or later \
[https://www.gnu.org/licenses/licenses.html](https://www.gnu.org/licenses/licenses.html)
    * Python 3: Python Software Foundation License \
[https://www.python.org/download/releases/3.4.0/license/](https://www.python.org/download/releases/3.4.0/license/)
    * Google Protobuf: BSD style \
[https://github.com/protocolbuffers/protobuf/blob/master/LICENSE](https://github.com/protocolbuffers/protobuf/blob/master/LICENSE)
    * mbedTLS: Apache 2.0 \
[https://github.com/ARMmbed/mbedtls/blob/development/LICENSE](https://github.com/ARMmbed/mbedtls/blob/development/LICENSE)

13. Release methodology and mechanics
    * Graphene Library OS is released via GitHub ([https://github.com/oscarlab/graphene/releases](https://github.com/oscarlab/graphene/releases)).
    * The major and minor versions of the software are released by the maintainers team periodically. Individual patches are submitted by contributors as pull requests and require sufficient reviews and approvals of the leadership team before being merged into the mainstream version.
    * All contributions to the project must follow the Contributor Guideline ([https://github.com/oscarlab/graphene/blob/master/CONTRIBUTING.md](https://github.com/oscarlab/graphene/blob/master/CONTRIBUTING.md)) as well as the Coding Style Guideline ([https://github.com/oscarlab/graphene/blob/master/CODESTYLE.md](https://github.com/oscarlab/graphene/blob/master/CODESTYLE.md))

14. Names of initial committers, if different from those submitting proposal

    Same as submitters

15. List of project's official communication channels (slack, irc, mailing lists):
    * Support mailing list: [support@grapheneproject.io](mailto:support@grapheneproject.io)
    * Developer mailing list: [team@grapheneproject.io](mailto:team@grapheneproject.io)
    * Developer slack channel: [https://graphene-libraryos.slack.com](https://graphene-libraryos.slack.com)

16. Social media accounts

17. Existing financial sponsorship
    * Graphene Library OS is not financially sponsored by any institution.

18. Trademark status

    “Graphene Library OS” is not registered as a trademark.

19. Any additional information the TAC and Board should take into consideration when reviewing your proposal.

    **Contributors**: There are significant in-kind effort commitments from Intel, Invisible Things Lab, Golem Factory, UNC Chapel Hill, and Texas A&M University to drive the project, as well as additional teams contributing code, including Ali Baba and IBM.


    **Users**: Graphene has a growing user base of both academic and industrial users.  Graphene has been widely used as a building block or baseline to compare against for research papers on SGX.  A number of start-ups are also using Graphene to build their business upon. 


    **Continuous Integration (CI) and Request for Support:** We currently run a Jenkins CI system at UNC to test Graphene.  We are primarily using an assortment of SGX v1 and other odd hardware.  In order to continue growing, as well as stay current with the latest SGX systems, we request eight recent SGX machines to augment our current testing infrastructure.

