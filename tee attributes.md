## TEE Attributes

Required properties to be called a “TEE”:
* ___Data integrity___ - data values stored or being operated upon within the bounds of the TEE cannot be modified by an actor operating outside the TCB.
* ___Data confidentiality___ - data values stored or being operated upon within the bounds of the TEE cannot be determined by an actor operating outside the TCB.
* ___Code integrity___ - software codes executed inside the bounds of the TEE cannot be modified by an actor operating outside the TCB.

TEE's may have other properties:
* _Code confidentiality_ - software codes executed inside the bounds of the TEE cannot be determined by an actor operating outside the TCB.
* _Programmability_ - the extent to which the software codes operated upon inside the bounds of the TEE can be provided by an identified actor.
* _Attestability_ - the mechanism for demonstrating the contents of a TEE is in fact secured by a TEE.
* _Unspoofability (un-clonable) / non-repudiability)_ - when using cryptographic authentication mechanisms in such a manner as it difficult to deny the origin of an assertion (often in referring to identity tied to a transaction).
* _Authenticated launch_ - (aka secure boot) a mechanism for determining that an approved TCB via cryptographic signature is established. As opposed to “measured” launch which just establishes which elements compose the TCB without determination of its origin or acceptability.
* _Recoverability_ - if an error in the TCB of the TEE is discovered the ability for the error to be mitigated. Full recoverability allows for the attestation of the recovered TCB.
* _Isolation_ - A mechanism by which the main properties of data & code integrity can be achieved.
* _Robustness_ - Actors operating outside the TCB may be defined as a software actor (e.g. the host operating system) or a hardware actor (e.g. the platform operator). The extent to which a TEE provides protection from one actor or another is defined by its TCB.
