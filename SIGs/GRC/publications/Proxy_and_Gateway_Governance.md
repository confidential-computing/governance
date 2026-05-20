# ![CCC GRC logo](./images/ccc_grc_logo.png)
# Proxy and Gateway Governance

# Context

Proxies **\[1\]** and Gateways **\[2\]**, referred to in the rest of the documents as “**Trusted Intermediaries**”, are ubiquitous in enterprise computing. They perform a variety of functions, often in response to operational, security and regulatory requirements. Trusted Intermediaries perform a wide range of functions, including web application firewalls, traffic inspection, protocol translation, data leakage prevention, API gateways, load balancers, etc.[^1] By their very nature, Trusted Intermediaries are part of the trust relationship between the client and the server. A properly governed Trusted Intermediary must be subject to a set of Confidential Computing-specific Control Objectives in order to satisfy the requirements of each Persona **\[3\]**.

# Problem

Whenever one (or more, sequentially deployed) Trusted Intermediaries (TIs) have to exist between a Confidential Computing client and server, the challenge is to introduce them without breaking the expectations of data confidentiality and integrity.

The discussion that follows will refer to the following Roles and Assets inherent in the Trusted Intermediary space.

# ![PnG_Governance](./images/Proxy_and_Gateway_Governance.png)

## Roles

| Role | Description and Trust Relationships |
| :---- | :---- |
| **TI System Operator (TSO)** | The Cloud Service Provider (CSP) or a similar entity that owns and/or operates the hardware and optionally the operating system on which the Trusted Intermediary runs. |
| **TI Service (TS)** | The entity that operates and bears responsibility for the secure operation of the TI Service on the hardware that TSO is responsible for. The TS may support a single customer or multiple customers defined here as Trusted Intermediary Tenants. The TS trusts[^2] the TSO, yet may choose to minimize that trust by operating the TS software within a TEE. |
| **TI Tenant (TT)** | The entity that operates and bears responsibility for the portion of the TI Service hosting a given TI Tenant. The TT relies upon the correct operation of the TS. The TT trusts the TS directly and TSO transitively. Operationally, the TT may require attestations from the TS as the TT relies on the trustworthiness of the TS. The TT may choose to minimize the trust it places in the TS by running the TT software inside a TEE. |
| **Clients and Servers (per Tenant)** | The entities that rely on and are impacted by the TT decisions. Often the Client and the Server are associated with the same TT. Trust is placed in the TT directly and the TS and TSO transitively. |

In certain cases these roles can be combined. For instance, if a CSP operates a TS for all its tenants, the roles of TSO and TS may be combined. Similarly, a single-tenant TS could combine the roles of TS and TT.

## Assets

| Asset | Role | Description of the Asset | RC[^3] |
| :---- | :---: | :---- | :---: |
| **TI System** | TSO | Physical hardware and optionally the operating system on which the (multi-Tenant) TS runs | N/A |
| **TS Software** | TS | Deployed executable code that constitutes the TS and is shared by all TI Tenants | No |
| **TS Configuration** | TS | Configuration values that define the execution of the TS and integration with its supporting services (if any) | No |
| **TT Software** | TT | Deployed Tenant-specific executable code, including any plug-ins and extensions. | No |
| **TT Configuration** | TT | Configuration values that define the execution of the TT and integration with its supporting services (if any) | Opt |
| **TT Secrets** | TT | Secrets (encryption, signing) utilized by the TT for its secure operation | Yes |
| **TT Policies** | TT | The set of policies used by the TT in order to perform the reverse proxy functions (policies are distinct from executable code and configuration) | Opt |

# Forces

Depending on individual circumstances, the Trusted Intermediary System Operator, the Trusted Intermediary Service and the Trusted Intermediary Tenant are all potential threat vectors. Finally, Trusted Intermediaries may serve multiple mutually distrustful Tenants sharing the same Service.

The following considerations thus become important subjects of Trusted Intermediary governance:

1. **Security and Trust Concerns:** Trusted Intermediaries by design decrypt and sometimes modify traffic between the client and the server. This may conflict with the core expectations of Confidential Computing where the confidentiality and integrity of data must be maintained end-to-end. Each Trusted Intermediary adds another participant into the client/server trust relationship, which must itself be secured and have a mechanism for establishing and maintaining trust of all parties.  
     
2. **Balancing Security and Privacy:** There's a delicate balance between the need for security through inspection and the privacy expected of Confidential Computing. Organizations might need to implement solutions, including combining transport-level encryption with application-level encryption, where only certain application-level traffic is inspected, based on predefined criteria with regards to metadata (protocol, origin, destination, frequency of transmission, etc.), relevant regulatory regimes, or other considerations. The goal is to control the exposure of sensitive data while still maintaining a secure and compliant environment.  
     
3. **Regulatory and Compliance:** Depending on the data being processed, the Trusted Intermediary may be subject to regulatory, statutory and contractual compliance requirements. For example, if regulated data flows are present, compliance with data protection regulations (e.g., GDPR, HIPAA, PCI-DSS, FedRAMP, MAS) must be ensured. Local and context-specific laws, policies, contractual obligations and other regulations may also stipulate that traffic be inspected and modified. Compliance entails proving control effectiveness (periodic testing, proofs of policy execution).  
     
4. **System of Record Considerations:** If a Trusted Intermediary takes any policy-driven actions, auditors and incident responders alike will care about the Trusted Intermediary Tenant policies, their histories, as well as controls over who manages these policies.  
     
5. **Conveying Trustworthy Workload Identity:** When a Trusted Intermediary is present between Client and Server workloads, the Trusted Intermediary MAY present the Server’s Workload Identity to the Client and the Client’s Workload Identity to the Server. Alternatively, a Trusted Intermediary MAY present an identity different from the workload on the other end of it. This includes scenarios where multiple Trusted Intermediaries are deployed in sequence, each handling a different Trusted Intermediary function.  
     
6. **Availability and Performance:** While important from the overall governance perspective, there is nothing Confidential Computing specific about satisfying this requirement, so, while noted, it will not be mentioned further in this document.

7. **Traffic Modification Awareness:** Trusted Intermediaries change the content of traffic between clients and servers by design. However, there is nothing about this expected behavior that is specific to Confidential Computing – all such decisions are performed at the application level and are outside the scope of this document.

# Solution

The terms MUST/SHOULD/MAY etc. below are used in accordance with **\[4\]**. Every SHOULD recommendation is explained separately in the “SHOULD vs. MUST Clarifications” section towards the end of this document.

Trusted Intermediary governance aims to achieve the following goals and sure that the evidence is in place to prove it:

1. **Security and Trust Concerns:** Trust in Trusted Intermediaries is established via the following mechanisms:  
     
   1. The Trusted Intermediary Service MUST be properly administered: it runs expected code in a secure configuration on a system properly administered by the TSO.  
   2. The Trusted Intermediary Tenant MUST be executing the most current code and policies of that Tenant in an approved configuration.  
      1. The Tenant has to concern itself with potential rollback attacks on the TI code and configuration. The way these attacks can be mitigated is by following the Workload Governance pattern **\[5\]**. This mitigation works because in order for a Trusted Intermediary to operate securely it needs to obtain certain cryptographic keys, policies and secrets, and for that it needs to successfully perform Remote Attestation. Failure to do so would result in alerts and outages that the TI can easily detect.  
   3. Protect Trusted Intermediary Tenant code and policies  
      1. Policy confidentiality SHOULD **\[a\]** be required  
      2. Code and policy integrity MUST be maintained  
   4. Appropriate lifecycle management of Trusted Intermediary signing and encryption keys, as well as a tamper-evident auditable change log MUST be maintained.  
      1. Trusted Intermediary Tenants SHOULD **\[b\]** be allowed to bring their own cryptographic keys for tasks including, but not limited to, protecting sensitive Verifier Tenant policies and logs at-rest  
      2. Cryptographic keys SHOULD **\[b\]** be rotated with some periodicity and MUST be rotated in case of suspected or actual compromise  
   5. Peer Tenant isolation MUST be achieved for multi-tenant Trusted Intermediaries.

2. **Balancing Security and Privacy:** There are two Trusted Intermediary models that an enterprise may choose from when it comes to traffic visibility: “full” and “partial”:  
     
   1. Under the “full” model, the tenant fully trusts the Trusted Intermediary and expects all traffic to be visible to it and potentially even modifiable by it  
   2. In contrast, under the “partial” model, a portion of the traffic is encrypted end-to-end between the participants (typically, using application-level encryption), and the remaining portion is subject to inspection and processing by the Trusted Intermediary

   

   The balance of security and privacy related to transport-level vs. application-level encryption and the role of the Trusted Intermediary is a decision left to the customer and driven by customer requirements and obligations. The enterprise applies one or the other model at its discretion, guided by appropriate policies, regulations and contracts.

   

3. **Regulatory and Compliance:** Take steps to ensure that the Trusted Intermediary complies with all applicable rules and regulations:

   1. Unknown or unapproved code and policies MUST NOT be deployed to Trusted Intermediaries  
   2. All policies currently in effect MUST be queryable at any time  
   3. The Trusted Intermediary Tenant SHOULD **\[c\]** periodically test correct execution of the Trusted Intermediary policies, such as ensuring that traffic logs are properly redacted, malicious content appropriately removed, data going through the proxy appropriately filtered or sanitized, expected traffic modifications take place, and so on  
   4. The Trusted Intermediary Service MUST maintain evidence of applying policies for all Tenants via tamper-evident logs (proof of execution)

4. **System of Record Considerations:** Ensure and be able to prove that the correct and current code as well as policies are applied at all times:

   1. Tamper-evident logs of code versions, policies & cryptographic key histories, as well as associated decisions applied to data transiting the Trusted Intermediary, listing responsible actors (e.g., who has approved and/or applied each change, which policy was used for each decision), MUST be maintained for the required retention period  
   2. Confidentiality offered to the histories or Trusted Intermediary policies MUST match that offered to the active policies

5. **Conveying Trustworthy Workload Identity:** Ensure that the correct Workload Identities are presented both to the Client and the Server sides of a session traversing a Trusted Intermediary.  
     
   1. The mechanisms and protocols involved in bootstrapping, provisioning, acquiring and/or carrying forward credentials at each Trusted Intermediary are deployment and application specific.  For example there are several types of SSO and credentials (OAuth, SAML, OIDC, etc.) between a web client and a web server.   
   2. Confidential Computing offers up a new mechanism for establishing verifiable identities that ought to be considered when using TI.  See Remotely Attested TLS working group draft **\[6\]** for an example.

# Governance Expectations Summary

The numbers in the left column below refer to the relationship matrix in **\[3\]**. Rows listed as N/A indicate that corresponding expectations are listed under different Patterns documents. Trusted Intermediaries are in the “Confidential Application Developers/Managers” category for the purposes of this table.

| \# | Description |
| :---- | :---- |
| **1 \- 6, 8, 10-13, 15** | N/A |
| **7, 9, 14** | Ensure secure administration of TI Hardware, TI Service and TI Tenants. Securely maintain and furnish on demand tamper-evident histories (per-tenant) of TI decisions, within a specified SLA regarding retention period, timeliness, etc. Securely maintain a tamper-evident record of all TI policies for the required retention period. |

# “SHOULD” vs. “MUST” Clarifications

1. The Tenant needs to assess the risks associated with TI policies becoming exposed to attackers and decide based on that assessment whether policy confidentiality is required. The nature of impact of making policies available depends on the type of TI. For example, knowing what traffic sources are allowed may inform an attacker as to which targets to go after.  
2. Many jurisdictions require tenants to securely bring their own keys and for keys to be periodically rotated, thus failure to offer such functionality risks making the corresponding Trusted Intermediary implementation unsuitable for regulated customers.  
3. The correct behavior of the Trusted Intermediary depends on the right code and policies being in place and is assumed to be verified. The Trusted Intermediary Tenant is strongly advised to perform these tests to be sure.

# References

1. Proxy (definition): [https://en.wikipedia.org/wiki/Proxy\_server](https://en.wikipedia.org/wiki/Proxy_server)  
2. Gateway (definition): [https://en.wikipedia.org/wiki/Gateway\_(telecommunications)](https://en.wikipedia.org/wiki/Gateway_\(telecommunications\))  
3. Expectations of Ecosystem Participants [https://github.com/confidential-computing/governance/blob/main/SIGs/GRC/publications/Expectations\_of\_Ecosystem\_Participants.md](https://github.com/confidential-computing/governance/blob/main/SIGs/GRC/publications/Expectations_of_Ecosystem_Participants.md)  
4. Key Words for Use in RFCs to Indicate Requirement Levels: [https://datatracker.ietf.org/doc/rfc2119/](https://datatracker.ietf.org/doc/rfc2119/)  
5. Workload Upgrade Governance Pattern: [https://github.com/confidential-computing/governance/blob/main/SIGs/GRC/publications/Confidential\_Workload\_Upgrade\_Governance.md](https://github.com/confidential-computing/governance/blob/main/SIGs/GRC/publications/Confidential_Workload_Upgrade_Governance.md)  
6. Using Attestation in Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS) [https://datatracker.ietf.org/doc/draft-fossati-tls-attestation/](https://datatracker.ietf.org/doc/draft-fossati-tls-attestation/)  

[^1]:  Trusted Intermediaries are deployed with the full knowledge and consent of all participants and do not require judicial warrants or clandestine deployment. In that respect, they differ materially from lawful intercept, which is outside the scope of this document.

[^2]:  TISO is expected to provide physical security to the hardware, maintain timely patches, etc. The precise degree of trust required depends on the situation and is outside the scope of this document.

[^3]:  Short for “Requires Confidentiality”
