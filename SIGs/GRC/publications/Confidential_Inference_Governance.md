# ![CCC GRC logo](./images/ccc_grc_logo.png)
# Confidential Inference Governance

# Context

Owners of confidential workloads implementing AI Inference Services (AIISs) need to understand what controls related to data-in-use protections must be deployed as part of and alongside such services.
Several classes of actors are involved in developing, hosting and using an inference service, and the members of these classes do not fully trust members of other classes.
Data-in-use protections can help meet these expectations while keeping the required trust relationships to a minimum.

A properly governed AI Inference Service must be subjected to a set of Confidential Computing-specific Control Objectives in order to satisfy the requirements of each Persona **[1]**.

## Assumptions and Pre-Requisites

This pattern assumes that the inference runtime is itself a Confidential Workload and that the controls of the Confidential Workload Governance pattern **[7]** have been applied to it.
It further assumes the existence of a properly governed Verifier per Verifier Governance **[8]**, and that any inference gateway, retrieval front-end or Model Context Protocol (MCP) server sitting between client and inference runtime is governed as a Trusted Intermediary per Proxy and Gateway Governance **[9]**.
This pattern does not restate the requirements of those patterns; it inherits them.

# Problem

AI inference services process sensitive model assets and data assets across mutually untrusted actors.
In many deployments, the Model Owner, the End User, the Data Owner and the Service Provider each have distinct responsibilities and distinct concerns, yet none of them can safely assume that the others are trusted with the plaintext model or plaintext data.

The governance problem is to define the minimum and sufficient controls needed to assure confidentiality and integrity of both data and model while allowing an inference workload to operate in a shared or hosted environment.

## Roles

| Role | Description and Trust Relationships |
| :---- | :---- |
| **Model Owner (MO)** | Owns the model assets and is concerned with model confidentiality, model integrity and authorized deployment. The MO controls the keys wrapping model weights and adapters, and declares the expected workload identity. The MO trusts the Verifier Tenant directly and the Service Provider only transitively and minimally. |
| **End User (EU)** | Provides ephemeral inputs and relies on the service to process them without exposing them to unauthorized actors. The EU trusts the attested workload identity directly, and the MO and SP only to the extent that attestation and policy bind them. |
| **Data Owner (DO)** | Owns persistent data used as input for inference or as a retrieval source. The DO controls the keys protecting that data at rest and the retention policy governing it. The DO trusts the attested workload identity directly and the SP transitively. |
| **Service Provider (SP)** | Operates the hosting infrastructure, and is decomposed as in the sibling patterns into System Operator, Service and Tenant roles where those are distinct. The SP is expected to provide physical security, timely patching and platform operation. The SP is **not** trusted with plaintext model or data assets and **MUST NOT** be the sole gate for key release. |
| **Verifier (V)** | Appraises Evidence produced by the inference workload and issues Attestation Results. Governed per **[8]**. The MO, DO and EU trust the Verifier Tenant directly; where the Verifier Service is operated by the SP, the residual exposure described in **[8]** applies. |
| **Key Release Authority (KRA)** | Releases wrapped model and data keys only on presentation of satisfactory Attestation Results and policy evaluation. May be instantiated separately per actor class. |
| **Trusted Intermediaries (TI)** | Inference gateways, retrieval front-ends, API gateways and MCP servers in the request path. Governed per **[9]**. |

In certain cases these roles can be combined.
A first-party service may combine MO and SP; a single-tenant deployment may combine DO and EU.
Each combination collapses a trust boundary and **MUST** be documented as such.

## Assets

Integrity is required for every asset listed below, and the availability of each asset is assumed to be mandatory for the correct functioning of the inference service.
The `RC` column indicates whether the asset **R**equires **C**onfidentiality.
The list assumes a multi-tenant inference service; single tenancy is the trivial case and is covered implicitly.

| Asset | Role | Description of the Asset | RC |
| :---- | :---: | :---- | :---: |
| **Inference System** | SP | Physical hardware, firmware, hypervisor and optionally the host operating system on which the inference runtime executes | N/A |
| **Inference runtime software** | SP / MO | Deployed executable code constituting the serving stack, including kernels, schedulers and accelerator drivers inside the boundary | No |
| **Inference runtime configuration** | MO | Configuration values governing execution, batching, caching and I/O, *excluding* cryptographic keys | No |
| **Model weights** | MO | Trained parameters, including base weights and any adapters (e.g., LoRA) applied at serving time | Yes |
| **Model architecture** | MO | The ordering and structure of computations used to transform inputs into outputs | Opt |
| **Model measurement / reference values** | MO | Measurements of the model artifact and adapters used in attestation and key-release decisions | No |
| **Policy bundle** | MO / DO / EU | The measured set of egress, retention, tool-invocation and key-release policies in force for a given workload identity | Opt |
| **System prompt and guardrail configuration** | MO / DO | Non-user-supplied instruction and filtering configuration carried into the context window | Opt |
| **Ephemeral data** | EU | Transient user prompts, intermediate responses, retrieval results, activations and short-lived inference state | Yes |
| **Attention / KV cache** | EU / DO | Retained attention state and prompt caches reused across requests or sessions for latency reduction **[3]** | Yes |
| **Persistent data** | DO | Cached prompts, sensitive data sources used during inference, vector stores, embeddings, and other retained artifacts | Yes |
| **Inference evidence records** | MO / DO / EU | Policy-bound, hashed or sealed records of which model identity processed which request under which policy | Opt |
| **Actor key material** | MO / DO / EU | Wrapping, signing and session keys controlled independently by each actor class | Yes |
| **Tool and egress credentials** | MO / DO | Credentials used by the workload to authenticate to retrieval endpoints, external APIs, agentic services and MCP servers **[4]** | Yes |
| **Attestation Evidence and Attestation Results** | SP / MO | Evidence produced by the inference workload and the corresponding Attestation Results relied upon for key release | Opt |

These assets do not all carry the same governance requirements.
Data assets may be short-lived or retained for future access, while model assets may be kept constant over time or updated under controlled change management.

## Summary of Concerns

The resulting governance problem is not only about encryption.
It is about whether plaintext model and data assets can be kept inside a verifiable confidentiality boundary,
whether that boundary is properly identified, and whether releases of keys and access to data are governed by attestation, policy and measured identity rather than by service-provider discretion.
The concerns that must be addressed are:

1. Maintaining end-to-end confidentiality of data at rest, in transit and in use, including under the performance optimizations characteristic of inference serving
2. Ensuring that every actor class has the ability to secure its own secrets and identities independently of the others
3. Verifiable integrity and authenticity of the model throughout its lifecycle, including authorized updates and rollback
4. Ability for end users and data owners to audit how their data is processed, retained and egressed
5. Safe invocation of tools and agents with respect to data disclosure and malicious execution
6. Protection of model assets from disclosure or exfiltration via host access, device and accelerator memory, and persistence artifacts
7. Applying the correct governance model for each type of sensitive data, distinguishing ephemeral from persistent
8. Maintaining isolation between tenants and between sessions where execution and cached state are shared
9. Establishing that the Verifier and Key Release Authority on which the whole scheme depends are themselves trustworthy and sufficiently available
10. Assuring the End User and Data Owner that a given output was produced by the attested model under the attested policy, and was not altered in transit

## Scope and Limitations

This pattern focuses on steady-state inference.
Training-time behaviour is out of scope.
Where a deployment permits the model to modify itself during regular post-deployment use — including online learning, fine-tuning on user data, or writes into a retrieval index that subsequently influences inference — that change **MUST** be governed as a model update under Concern 3 and Solution 3, or placed out of scope explicitly in the deployment's own documentation.
A deployment **MUST NOT** rely on the steady-state scoping of this pattern while permitting ungoverned self-modification.

This pattern does not attempt to solve application-level privacy policy, model alignment, or legal compliance.
Confidential Computing can ensure that the workload is measured, attested, and able to keep plaintext assets within a trusted boundary; it does not by itself determine whether the application is lawful, minimally invasive, or aligned with the data owner's policy requirements.
Those remain application-level, organizational and legal obligations, and the goal of this pattern is scoped to the boundary and attestation controls specific to Confidential Computing.

Privacy is a tighter constraint than data confidentiality in that it involves not merely "bulk" protection of data against unauthorized access using encryption (where access controls are applied to cryptographic keys), but rather filtering out the data based on some privacy requirements before it can be shared (where access controls are applied to
the data itself).
**Confidential Computing by itself cannot provide assurances of the proper implementation of privacy controls.**

# Forces

The following forces are the real tensions that make the problem difficult.
Each force addresses the correspondingly numbered concern in the Summary of Concerns above.

1. **Performance optimization pushes plaintext outward (Concern 1)**

   Data must remain protected in storage, during transport, and while being processed in
   memory.
   Inference serving, however, achieves its latency and throughput targets precisely by moving state out of the narrowest possible scope: prompt and KV caching **[3]**, paged attention, continuous batching, speculative decoding, tensor parallelism across devices, and tiering of cache to host memory or local storage.
   Every one of these creates a new location where plaintext may exist or a new channel across which it must travel.
   The force is that the techniques that make inference economically viable are the same techniques that widen the plaintext footprint, and if any of the three protection modes is missing, weak or misconfigured at any of those locations, the security of the entire system is at risk.

2. **Multiple principals require independent trust domains (Concern 2)**

   The MO, EU, DO and SP each control different parts of the system and each has different risk exposure.
   No single identity provider can be the universal trust anchor for all key release decisions.
   Multiple independent actors imply multiple key hierarchies, policy domains and attestation expectations.
   The force is that confidentiality requires independent, actor-specific governance without forcing any two parties to trust one another, while the workload itself must nonetheless assemble assets from all of them inside a single boundary.

3. **Model authenticity must be verifiable without disabling legitimate updates (Concern 3)**

   The MO needs to ensure that the deployed model is the expected model and not an unauthorized substitute.
   The EU and DO need assurance that they are interacting with the intended model.
   At the same time, the MO needs the flexibility to deploy updated models and adapters and to roll forward or back under controlled conditions.
   The force is that authenticity requires strict identity and provenance checks while also allowing safe change — and that every accepted measurement left valid for the sake of rollback is a version an attacker may try to pin the service to.

4. **Data-flow auditing must be possible without exposing plaintext data (Concern 4)**

   The DO and EU need evidence that private data was processed only for the intended purpose and not copied, persisted, logged or exfiltrated.
   However, storing raw prompts or raw retrieval content in audit logs defeats confidentiality.
   The force is a tension between auditability and confidentiality: evidence must be collected without making
   plaintext data visible to the wrong parties.

5. **External tool and agent invocation creates new disclosure paths (Concern 5)**

   Modern inference systems call retrieval tools, external APIs, MCP servers **[4]** and agentic services.
   These may sit outside the primary runtime and create additional confidentiality boundaries that are hard to govern.
   Data may be copied into tool calls, logs, traces, metrics, or prompts sent to other services, and tool output re-entering the context window is itself an untrusted input.
   The force is that inference utility and autonomous behaviour are valuable, but they also create exfiltration paths that must be controlled and measured.

6. **Model and data plaintext leak through host access, device memory and persistence artifacts (Concern 6)**

   The model may be exposed through accelerator memory, checkpoint files, crash dumps, paging and swap, intermediate caches, telemetry, profiler output or debugging artifacts.
   Plaintext weights and activations must also cross the link between the CPU TEE and each accelerator, and accelerator TEE support, confidential-computing modes and link encryption remain uneven across hardware generations and deployment estates.
   Model weights are high-value, durable, exfiltratable assets **[5]**.
   The force is that performance optimizations and operational convenience increase the number of places where model plaintext can exist, while the hardware needed to protect those places is not uniformly available.

7. **Ephemeral and persistent data have different governance characteristics (Concern 7)**

   Some data is intentionally short-lived, while other data is intentionally retained.
   The EU and DO may want their data to remain ephemeral in the sense that it is not retained after use, but inference systems commonly persist prompts, cache keys, retrieval results, embeddings or telemetry.
   The force is that data can be expected to be ephemeral yet still end up in logs, caches, indexes or traces unless policy and controls explicitly prevent it — and that the system cannot distinguish the two classes unless someone has classified them in advance.

8. **Shared execution and shared cache erode tenant and session isolation (Concern 8)**

   Inference services batch requests from multiple sessions, and frequently multiple tenants, into a single forward pass, and reuse cached attention state across requests to avoid recomputation.
   A confidentiality boundary that excludes the host but admits several mutually distrustful tenants to the same computation and the same cache has not resolved their exposure to one another.
   The force is that the economics of serving reward aggregation across tenants and sessions, while confidentiality requires their separation.

9. **The scheme inherits a trust and availability dependency on the Verifier and Key Release Authority (Concern 9)**

   Policy-controlled key release is only as trustworthy as the Verifier that appraises Evidence and the authority that releases keys; a compromised Verifier leads to insecure reliance and loss of assets in the same manner as a compromised Certificate Authority **[8]**.
   Where the Verifier Service is operated by the same Service Provider the workload is being protected against, full protection of data-in-use against that provider may not be achieved.
   Simultaneously, gating key release on attestation introduces a new hard dependency in the serving path: a Verifier or KRA outage is an inference outage.
   The force is that reducing trust in the Service Provider increases both trust in and dependence on the attestation infrastructure.

10. **Output integrity is asserted by the same party the user is protecting against (Concern 10)**

    The EU and DO care not only that their input was kept confidential but that the output they received was produced by the attested model under the attested policy.
    Yet the response traverses the SP's network and, commonly, one or more Trusted Intermediaries whose purpose is to inspect and modify traffic **[9]**.
    The force is that end-to-end assurance of provenance must coexist with intermediaries that are deliberately
    authorized to alter the stream.

# Solution

The terms MUST/SHOULD/MAY etc. below are used in accordance with **[2]**.
Every SHOULD recommendation is explained separately in the "SHOULD vs. MUST Clarifications" section towards the end of this document.

Confidential inference is achieved when plaintext Model Assets and Data Assets exist only inside an attested confidentiality boundary, and keys that unwrap those assets are released only when policy is satisfied.
Each numbered solution below resolves the correspondingly numbered force.

![Trust domains, attestation and policy-controlled key release](./images/confidential_inferencing_a.svg)
![Request path, default-deny egress, persistence and evidence](./images/confidential_inferencing_b.svg)

1. **Establish a measured confidentiality boundary and encrypt all of its I/O (resolves Force 1)**

   1. The AI inference runtime — comprising the CPU TEE, any accelerator TEEs, the measured model image, the measured policy bundle and in-boundary execution state — **MUST** be the only place where plaintext model and in-use data exist.
   The host operating system, hypervisor, service-provider operators and co-tenants **MUST** remain outside the trust boundary.
   2. Inputs and outputs **MUST** traverse authenticated, encrypted channels bound to the attested workload identity; see **[10]** for one mechanism.
   3. Persistent stores, retrieval systems, vector stores and caches **MUST** be protected with DO- or EU-controlled keys and **MUST** only be decrypted inside the boundary.
   4. Any state tiered out of the boundary for performance reasons — including KV cache spilled to host memory or local storage — **MUST** be encrypted and integrity-protected with keys that exist only inside the boundary, or **MUST NOT** be tiered.
   5. Each enabled optimization that widens the plaintext footprint **MUST** be enumerated in the deployment's documented TCB and reflected in the measured configuration, so that it is an attested property rather than an operational convenience.

2. **Bind workload identity to measured software and hardware, under per-actor trust domains (resolves Force 2)**

   1. Each deployable AI inference workload **MUST** have a verifiable identity derived from hardware attestation, firmware measurements, runtime measurements, model and adapter measurements, and the policy bundle.
   That identity **MUST** be comparable against the expected identity independently declared by the MO, DO and EU.
   2. Model and data keys **MUST** be released only after attestation proves that the workload is running in the expected environment and satisfies the relevant policy.
   MO-controlled keys protect model assets; DO- and EU-controlled keys protect sensitive data and sessions.
   The SP **MUST NOT** be treated as the sole gate for key release.
   3. Each actor class **MUST** be able to maintain its own key hierarchy, its own policy authority and its own attestation expectations, and **MUST** be able to withhold release unilaterally without depending on another actor's identity provider.
   4. Separation of duties **MUST** be satisfied, including decoupling the platform hardware Trust Anchor used in appraisal from the organizational root of trust used by the Identity Provider.
   5. Verifier Tenants and workload owners **SHOULD [b]** be permitted to bring their own keys for wrapping model assets, protecting data at rest, and signing evidence records.
   Keys **SHOULD [b]** be rotated with some periodicity and **MUST** be rotated on suspected or actual compromise (**[11]**, **[12]**).

3. **Make model maintenance, update and rollback part of governance (resolves Force 3)**

   1. Model artifacts, adapters and policy bundles **MUST** be signed, and their measurements **MUST** participate in the workload identity of Solution 2.1.
   2. Authorized updates and rollbacks **MUST** be governed by measured identity, signed artifacts and policy-controlled key rewrapping.
   Unauthorized substitution **MUST** fail key release and **MUST** block execution.
   3. Reference values for superseded model versions **MUST** be retired from appraisal policy in a timely fashion following successful deployment of up-to-date versions, per the Verifier Hygiene requirements of **[7]**.
   Where blue-green or staged deployment requires two versions to be simultaneously valid, the overlap window **MUST** be bounded and documented.
   4. Changes to the roots of trust governing model provenance **MUST** be approved by all interested parties ahead of time, and all changes to measurements and appraisal policy **MUST** be documented, published, cryptographically verifiable and audited.
   5. The build and supply chain producing the model artifact and serving stack **MUST** be governed per **[7]**; independent reproducibility of the model measurement **SHOULD [c]** be provided.

4. **Provide evidence of data flow without exposing the data itself (resolves Force 4)**

   1. Logs, metrics, dumps, traces and crash artifacts **MUST NOT** contain plaintext Model Assets or Data Assets.
   2. The system **MUST** emit policy-bound evidence records showing which model identity processed the request, which policy bundle was applied, which destinations were permitted, which tools were invoked, and whether data was retained or egressed.
   These records **MUST** be based on hashed, labelled or sealed references rather than raw prompt, retrieval or output content.
   3. Evidence records **MUST** be tamper-evident, **MUST** be retained for the required retention period, and **MUST** be producible on demand to the DO and EU within a specified SLA.
   4. Confidentiality protections **SHOULD [a]** apply to evidence records, Evidence and Attestation Results, and the confidentiality offered to historical records **MUST** match that offered to current ones.

5. **Default-deny egress with explicit, measured tool policy (resolves Force 5)**

   1. Inference workloads **MUST** default to denying outbound data flow unless a specific policy permits it.
   2. Calls to external tools, agentic services, MCP servers and retrieval endpoints **MUST** be explicitly scoped by destination identity, allowed data classes and permitted transformation rules, and that scoping **MUST** form part of the measured policy bundle.
   3. Any tool, agent or service that receives plaintext Data Assets **MUST** be considered part of the TCB; such a component **MUST** itself attest, and a secure channel **MUST** be established to it on the basis of that attestation.
   Components that cannot attest **MUST** be treated as untrusted pass-throughs and **MUST** only receive data encrypted to another trusted endpoint.
   4. Tool and retrieval output re-entering the context window **MUST** be treated as untrusted input and **MUST NOT** be permitted to alter egress, retention or key-release policy.
   5. Trusted Intermediaries in the request path **MUST** be governed per **[9]**, including the choice between the full and partial traffic-visibility models, and **SHOULD [f]** themselves execute inside a TEE.
   6. Correct execution of egress and tool policy **SHOULD [d]** be periodically tested, and the Service **MUST** maintain tamper-evident proof of policy application.

6. **Keep plaintext out of host, device and persistence artifacts (resolves Force 6)**

   1. Any device or accelerator that handles decrypted model weights, activations or data **MUST** be considered part of the TCB, **MUST** implement a TEE, and **MUST** be attested; the implementation **MUST** establish a secure channel through device attestation, per **[7]**.
   2. Where accelerator TEEs or confidential link protection are unavailable, compensating controls **SHOULD [g]** be applied and the residual exposure **MUST** be documented and accepted by the MO and DO; absent such acceptance, plaintext assets **MUST NOT** be placed on that device.
   3. Core dumps, swap and paging of boundary memory, profilers, debuggers and interactive attach **MUST** be disabled for production inference workloads, or **MUST** be constrained such that no plaintext asset can be captured.
   4. Checkpoints, model caches, compiled kernels or graphs derived from model structure, and any cached intermediate state **MUST** be sealed to the boundary or encrypted under MO-controlled keys.
   5. Telemetry derived from model execution **MUST** be assessed for inference-enabling leakage **[6]** and **MUST** be reduced to policy-bound records where such leakage is identified.
   6. The TCB **MUST** be minimized to the code necessary for the encapsulated functionality, per **[7]**; lift-and-shift of an unmodified serving environment **SHOULD NOT** be treated as sufficient.

7. **Classify every data asset as ephemeral or persistent and govern retention by measured policy (resolves Force 7)**

   1. Every data asset handled by the inference service **MUST** be class ified at design time as ephemeral or persistent, and that classification **MUST** be recorded in the deployment documentation.
   2. Retention **MUST** default to deny.
   Any retention of prompts, outputs, retrieval results, embeddings, cache entries or traces **MUST** be explicitly permitted by policy, with a defined owner, lawful purpose, maximum lifetime and erasure mechanism.
   3. The retention policy **MUST** form part of the measured policy bundle, so that an EU or DO can verify the retention behaviour of the workload they are about to send data to, rather than relying on an assertion.
   4. Assets classified as ephemeral **MUST** be erased or rendered cryptographically inaccessible at the end of the session or request scope, including from accelerator memory, host-tiered cache and any derived intermediate state.
   5. Persistent assets **MUST** be encrypted under DO- or EU-controlled keys such that revocation of those keys is sufficient to render the retained data inaccessible.
   6. Correct execution of retention and redaction policy **SHOULD [d]** be periodically tested and evidenced.

8. **Enforce tenant and session isolation across shared execution and shared cache (resolves Force 8)**

   1. Peer-tenant isolation **MUST** be achieved for a multi-tenant inference service.
   2. Prompt caches, KV caches and any other reusable derived state **MUST** be scoped to a single session and a single tenant unless reuse across a wider scope is explicitly permitted by the policy of every actor whose data is in that state.
   3. Cache lookup keys **MUST NOT** permit a requester to cause, detect or infer a hit on state derived from another tenant's or another session's data.
   4. Where requests from multiple tenants are batched into a single computation, the deployment **MUST** document the isolation mechanism relied upon and **MUST** include it in the measured configuration; where no such mechanism can be evidenced, cross-tenant batching **MUST NOT** be performed.
   5. Resource controls such as throttling and quotas **SHOULD [e]** be imposed per tenant to limit noisy-neighbour effects on availability.

9. **Treat the Verifier and Key Release Authority as governed, available dependencies (resolves Force 9)**

   1. The Verifier relied upon **MUST** be governed per **[8]**, and the deployment **MUST** document which Verifier Tenant is authoritative for each actor class.
   2. Where the Verifier Service or KRA is operated by the same Service Provider against whom data-in-use protection is sought, that residual exposure **MUST** be documented, and mitigations — an independent Verifier Service, a decentralized Verifier, or continuous monitoring and audit of the provider's Verifier — **SHOULD [a]** be applied.
   3. The Verifier and KRA **SHOULD [e]** be provisioned to an availability target in excess of that required of the inference service that depends on them.
   4. Failure to obtain a satisfactory Attestation Result **MUST** result in denial of key release and failure of the inference workload to serve.
   Degraded or fail-open operation on attestation failure **MUST NOT** be implemented.
   5. Breach, newly discovered vulnerability or revoked or leaked key material affecting the Verifier, KRA or model keys **MUST** be promptly notified to all affected parties.

10. **Bind outputs to the attested workload identity and policy (resolves Force 10)**

    1. Responses **MUST** be returned over a channel authenticated to the attested workload identity, such that the EU can establish that the endpoint which produced the output is the endpoint whose identity was appraised.
    2. Where a Trusted Intermediary is authorized to modify the stream, the identity presented to each side **MUST** be governed per **[9]**, and the fact that an intermediary is authorized to modify responses **MUST** be disclosed to the EU and DO.
    3. The evidence records of Solution 4.2 **MUST** be sufficient to associate a given response with the model identity and policy bundle in force when it was produced.
    4. The service **MUST NOT** represent an output as attested where it was produced outside the boundary, including fallback to a non-confidential serving path.

# Resulting Context

A deployment that applies this pattern has a measured inference boundary whose model and data plaintext are unavailable to the Service Provider, with retention and egress behaviour that an End User or Data Owner can verify before sending data rather than after.
It also has three new problems: a hard serving-path dependency on attestation infrastructure (Solution 9), a reduced optimization envelope and therefore a cost and latency penalty (Solutions 1 and 8), and an ongoing model-lifecycle obligation to retire stale reference values (Solution 3.3).

What the deployment does **not** have is any assurance that the application is lawful, privacy-preserving, minimally invasive or aligned.
Those obligations remain, and are set up rather than discharged by this pattern.

# Related Patterns

* **Confidential Workload Governance [7]** — the inference runtime is a Confidential Workload.
Secure design and development, secure and attestable build, supply chain and dependency management, TCB minimization, root-store and cryptography hygiene, and Verifier hygiene are inherited from that pattern rather than restated here.
* **Verifier Governance [8]** — Solutions 2 and 9 depend entirely on a trustworthy Verifier.
That pattern governs the Verifier's administration, policy and key lifecycle, availability, multi-tenancy and histories.
* **Proxy and Gateway Governance [9]** — inference gateways, retrieval front-ends, API gateways and MCP servers are Trusted Intermediaries.
That pattern supplies the full versus partial traffic-visibility models, the rollback-attack mitigation, and the workload-identity conveyance requirements referenced in Solutions 5 and 10.
* **Confidential Workload Upgrade Governance [13]** — governs the overlapping-version case referenced in Solution 3.3.

# Governance Expectations Summary

The numbers in the left column refer to the relationship matrix in **[1]**.
Rows listed as N/A indicate that corresponding expectations are listed under different Patterns documents.

An AI Inference Service occupies the "Confidential Application Developers/Managers" category for the purposes of this table.
Because the Model Owner may be an actor distinct from the operator of the inference service, this pattern additionally claims the "Component Vendors" rows that carry model-supply olbigations (rows 1 and 4).
Where MO and SP are combined, those rows collaps into rows 9 and 14.

| \# | Description |
| :---- | :---- |
| 2, 5-6, 8, 10-13 | N/A — covered under Confidential Workload Governance **[7]**, Verifier Governance **[8]** and Proxy and Gateway Governance **[9]**. |
| 1 | Suppliers of model artifacts, adapters, serving stacks and accelerators supply accurate component-specific guidance, signed artifacts, and the measurements and reference values needd to construct a workload identity; document accelerator TEE capability, confidential-computing modes and link protection, including where they are absent. |
| 3 | The platform operator provides attestable hardware and accelerator TEEs, and operates such that host operating system, hypervisor, operators and co-tenants remain outside the confidentiality boundary; core dumps, swap and paging of boundary memory, profilers, debuggers, and interactive attach are disabled or constrained such that no plaintext asset can be captured. |
| 4 | The Model Owner provides Data Owners and End Users with verifiable model provenance — signed model and adapter artifacts and published expected measurements — sufficient for them to declare an expected workload identity independently of the Service Provider. |
| 7 | Supply and maintain reference values for the model artifact, adapters, runtime and policy bundle; retire reference values for superseded versions in a timely fashion; bound and document any window in which two versions are simultaneously valid. |
| 9 | Maintain a measured confidentiality boundary for inference and document the TCB, including every enabled optimization that widens the plaintext footprint. Enforce default-deny egress and explicit tool policy; classify every data asset as ephemeral or persistent under default-deny retention carried in the measured policy bundle; achieve peer-tenant and per-session isolation including across batched execution and shared prompt and KV caches; bind outputs to the attested workload identity. Furnish policy-bound evidence of data flow, tool invocation, retention and egress on demand. Disclose authorized traffic-modifying intermediaries and any accepted residual exposure. |
| 14 | Securely maintain and furnish on demand tamper-evident, per-tenant histories of policy, measurement and cryptographic key changes and of the associated attestation, egress and retention decisions, listing responsible actors, within a specified SLA regarding retention period and timeliness. Maintain proof that policy was applied, including results of periodic testing that redaction, filtering and erasure execute as specified. |
| 15 | Evidence of requiring and validating that the expectations set out in rows 9 and 14 are satisfied, including recordinded acceptance of any documented residual exposure such as unattested accelerators or a Service-Provider-operated Verifier. |

# "SHOULD" vs. "MUST" Clarifications

a. Disclosing evidence records, Evidence or Attestation Results may ease an attacker's job, and in the multi-provider Verifier case the available mitigations vary considerably in cost and feasibility.
These protections are best thought of as defence-in-depth, and the right choice depends on the Tenant's assessment of its threat model and of its provider.
Integrity and tamper-evidence of those same records, by contrast, are MUST requirements, since the audit function fails entirely without them.

b. Many jurisdictions require tenants to securely bring their own keys and for keys to be periodically rotated, so failure to offer such functionality risks making the implementation unsuitable for regulated customers.
It is stated as SHOULD because some single-tenant and first-party deployments combine actor roles such that a separate customer key hierarchy adds no protection.
Rotation on suspected or actual compromise is a MUST in all cases.

c. Independent reproducibility of a model measurement is valuable, but large-model build pipelines are frequently not bit-reproducible for reasons unrelated to tampering, including non-deterministic accelerator arithmetic.
Where reproducibility cannot be achieved, compensating controls — cryptographic signing and timestamping of artifacts, and attested build environments per **[7]** — are required instead.

d. The correct behaviour of egress, tool and retention policy depends on the right code and policy being in place and is assumed to be verified.
Periodic testing is the means by which the Tenant satisfies itself that redaction, filtering and erasure actually execute as specified; it is strongly advised rather than mandated because the appropriate test frequency and depth are deployment-specific.
Maintaining tamper-evident proof that policy was applied is a MUST.

e. An enterprise can decide on availability SLAs for the inference service and for the attestation infrastructure it depends upon.
While it is advisable to attain the highest practical availability for the Verifier and KRA — because their failure is now an inference outage — doing so is at the discretion of the customer.
The same reasoning applies to per-tenant resource controls.

f. Running an inference gateway or other Trusted Intermediary inside a TEE materially reduces the trust placed in the hosting operator, but Trusted Intermediary governance is addressed in its own pattern **[9]**, and the feasibility of TEE-hosting a given intermediary varies with its function.
Where the intermediary receives plaintext Data Assets, Solution 5.3 applies and attestation becomes a MUST.

g. Accelerator TEE support, confidential-computing modes and encrypted device links are not uniformly available across hardware generations or cloud estates.
Where they are absent, compensating controls — physical isolation, dedicated non-shared hosts, strongly segregated environments, or repartitioning so that sensitive operations remain on devices that do attest — should be considered.
What is not permitted is placing plaintext assets on an unattested device without documented acceptance of the residual exposure by the Model Owner and Data Owner.

# Glossary

| Term | Definition |
| :---- | :---- |
| **AI Inference Service (AIIS)** | A service that accepts inputs and returns model outputs in steady-state operation, without modifying the model. |
| **Attestation Result** | The output of a Verifier's appraisal of Evidence, relied upon for key release and trust decisions **[14]**. |
| **Ephemeral data** | Data intentionally not retained beyond the request or session scope in which it was supplied or produced. |
| **Evidence** | Claims produced by an Attester about its own composition and state, submitted for appraisal **[14]**. |
| **KV / attention cache** | Retained attention state from prior tokens or prior requests, reused to avoid recomputation **[3]**. |
| **MCP** | Model Context Protocol; a protocol by which models invoke external tools and data sources **[4]**. |
| **Measured identity** | A workload identity derived from hardware, firmware, runtime, model and policy measurements rather than from an assigned credential. |
| **Persistent data** | Data intentionally retained beyond the request or session scope, such as vector stores, embeddings, cached prompts and evidence records. |
| **Policy bundle** | The measured set of egress, tool, retention and key-release policies in force for a given workload identity. |
| **TCB** | Trusted Computing Base; the set of components whose correctness is depended upon for the security of the workload. |
| **TEE** | Trusted Execution Environment; an environment providing isolation of code and data in use from the hosting environment, together with Remote Attestation. |
| **Trusted Intermediary** | A proxy or gateway positioned between client and server with the knowledge and consent of the participants **[9]**. |

# References

1. Expectations of Ecosystem Participants: [./Expectations of Ecosystem Participants](./Expectations_of_Ecosystem_Participants.md)
2. Key Words for Use in RFCs to Indicate Requirement Levels: [https://datatracker.ietf.org/doc/rfc2119/](https://datatracker.ietf.org/doc/rfc2119/)
3. "Prompt Cache: Modular Attention Reuse for Low-Latency Inference", 2024: [https://arxiv.org/abs/2311.04934](https://arxiv.org/abs/2311.04934)
4. "Model Context Protocol (MCP): Language, Security Threats, and Future Research Directions", 2025: [https://arxiv.org/abs/2503.23278](https://arxiv.org/abs/2503.23278)
5. "Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models", RAND Corp.: [https://www.rand.org/pubs/research_reports/RRA2849-1.html](https://www.rand.org/pubs/research_reports/RRA2849-1.html)
6. "Confidential Inference Systems: Design Principles and Security Risks", Anthropic: [https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf](https://assets.anthropic.com/m/c52125297b85a42/original/Confidential_Inference_Paper.pdf)
7. Confidential Workload Governance Pattern: [./Confidential_Workload_Governance.md](./Confidential_Workload_Governance.md)
8. Verifier Governance Pattern: [./Verifier_Governance.md](./Verifier_Governance.md)
9. Proxy and Gateway Governance Pattern: [./Proxy_and_Gateway_Governance.md](./Proxy_and_Gateway_Governance.md)
10. Using Attestation in Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS): [https://datatracker.ietf.org/doc/draft-fossati-tls-attestation/](https://datatracker.ietf.org/doc/draft-fossati-tls-attestation/)
11. NIST SP 800-57, Part 1, Section 5.3 "Cryptoperiods": [https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
12. NIST SP 800-57, Part 1, Section 8.3.5 "Revocation": [https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
13. Confidential Workload Upgrade Governance Pattern: [./Confidential_Workload_Upgrade_Governance.md](./Confidential_Workload_Upgrade_Governance.md)
14. Remote Attestation Procedures (RATS) Architecture RFC: [https://datatracker.ietf.org/doc/rfc9334/](https://datatracker.ietf.org/doc/rfc9334/)
15. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", 2021: [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)
16. Confidential Computing Glossary: [https://github.com/confidential-computing/glossary/](https://github.com/confidential-computing/glossary/issues/2)
