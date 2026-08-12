# CCC TAC Bi-Weekly Meeting Minutes: June 11, 2026

## 7 \- 9am PDT 

## **Links**

* **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io/)  
* **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io/)  
* **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)  
* **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)  
* **CCC YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io/)  
* **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org/)  
* **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io/)  
* **Contact the CCC**: [confidentialcomputing.io/contact-us/](http://confidentialcomputing.io/contact-us/)  
* **Zoom for CCC TAC meetings**: [https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e) 

## **Agenda and Minutes**

* Dan Middleton (DM) opened the call at 7:05 am PT and introduced Mingshen Sun (MS) as the rotating chair.   
* MS welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* Ben Sternthal and Michelle Roth (MR) recorded the meeting minutes.  
* MS reviewed the agenda.

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

* AMD \- **Nathaniel McCallum+**  / David Kaplan  
* Google \-  **Rene Kolga+** / Keith Moyer  
* Huawei \- Wu Yongzheng  
* Intel \- **Scott Raynor+**  / Simon Johnson  
* Meta \- Ahmed Magdy   
* Microsoft \- **Alec Fernandez+** / **Simon Gallagher+**  
* Nvidia \- Fritz Alder / **Dan Middleton+**  
* TikTok \-  **Mingshen Sun+**   
* Shielded Technologies \- Bob Blessing-Hartley

   " \+ " indicates attending

### Project Staff

* Ben Sternthal (LF PMO)   
* Michelle Roth (LF PMO)  
* Mike Bursell (CCC ED) 

### Other Attendees

* Henk Birkholz (Fraunhofer-Gesselschaft)  
* Ijlal loutfi (Canonical Group Limited)  
* Jens Albers (Fr0ntierX)  
* Jordi Guijarro (OpenNebula Systems)  
* Leonardo Garcia (Linaro)   
* Manu Fontaine (Hushmesh)   
* Mark Novak (JPMorgan Chase & Co)  
* Ofir Azoulay-Rozanes (Anjuna)  
* Radhika Jandhyala (Microsoft)   
* Rithikha Rajamohan (EQTY Lab)   
* Sakul Gupta (Micron)   
* Tom Jones (VeriClouds)

## **Welcome New Community Members**

* There were no new community member announcements.

## **Old Business**

* MS reviewed the major points from the last TAC meeting, with Dan Middleton highlighting the vote for Blueprint C. 

## **Announcements**

* CCC Academic Research Program has received 35 proposals.  
* Need help contacting Attestation SIG co-chairs for an update to TAC.  
* CC Summit  
  * Gauging interest in TAC meetup during the event \- DM will post in Slack to confirm who is interested. 

## **New Business**

* Blueprint C Vote  
  * A vote was taken and with no one in opposition or opposed the resolution to approve the document was passed.  
* Keystone Project Update  
  * Project moving to emeritus, notice will be posted on repo.  
  * A vote was taken and with no one in opposition or opposed the resolution to approve moving Keystone to emeritus was passed. 		  
* OE SDK Project Update  
  * Radhika Fontaine (RF) presented an update on the Open Enclave SDK project, noting that it was started to support the Ts that are partitioned, particularly Opti and SGX although currently only SGX is supported. RF noted that there is also an attestation verification component for the project that is currently used for TDX and SGX attestation verification. RF noted that much is the same with the project, including that Alec Fernandez is still the TAC mentor. RF highlighted that OES DK is now on a 6 month release cadence with 0.19.15 the most recent release, and continues to be maintained by about the same number of contributors. RF noted that the work to delete the Opti code in Open Enclave is ongoing, and all of the maintainers have completed the inclusive open source community orientation. RF reviewed additional support added along with bug fixes and updates. RF noted that work to fix license scan issues that are mostly related to Opti are ongoing as well, and added that progress has been made on the OpenSSF badge from last year. 

## **GRC SIG discussion**

* Mark Novak (MN) presented on the GRC SIG, noting that very low participation in recent months is putting the existence of the SIG at risk. MN reviewed governance terms and motivations, and how these impact confidential computing. MN noted that the Expectations of Ecosystem Participants framework and Verifier governance has been published, along with Confidential Workload governance. MN asked the CCC TAC to review the Proxy & Gateway governance draft and provide feedback. MN noted that the next meeting of the SIG is next Wednesday followed by a break until the end of July.   

## **Tech Talk: Portable Machine Image**

* Nathaniel McCallum presented a tech talk on portable machine images.   
  * The Problem with Current Confidential Computing  
    * Violated Threat Models: Confidential computing assumes the host (management plane) and the guest (application plane) are mutually adversarial. However, in current cloud deployments, the untrusted host often injects the early-stage guest firmware and paravisor, meaning the user-provided Trusted Computing Base (TCB) is compromised.  
    * Dangerous Code Execution: Currently, hypervisors pass executable code (like ACPI AML) across the boundary to the guest during boot, which the guest then executes at the highest privilege level, creating a significant attack vector.  
    * The Attestation Dilemma: To protect against adversarial host inputs, systems currently measure the inputs during boot. However, this ties the guest's attestation identity (and its complexity) to the specific hypervisor or cloud provider being used, destroying the portability of the virtual machine.  
  * The Solution: Portable Machine Images (PMI)  
    * Tenant-Owned Firmware: PMI aims to move guest firmware entirely into the tenant's software supply chain, allowing users to version, scan, and control it just like workload software.  
    * New Boundary Rules: PMI establishes a strict split of responsibilities: the guest defines the resources (e.g., CPU features, minimum configurations, and motherboard topology), while the host allocates the resources (e.g., memory size and plugging in specific devices).  
    * Explicit Pre-Boot Contracts: Instead of the guest dynamically querying the host for platform details at runtime, PMI uses an explicit, well-defined, and versioned contract negotiated before the guest even runs.  
    * Device Tree Overlays: PMI replaces ACPI with Device Tree for the platform definition because Device Tree contains no executable code and supports "overlays". The guest provides the base Device Tree (the "motherboard"), and the host provides an overlay (the "plugged-in hardware"), which the guest then safely merges and translates into ACPI internally.  
  * How PMI is Structured and Executed  
    * The Artifact: A PMI is a Portable Executable (PE) file containing the platform definition, boot payloads, and parallel "launch recipes" (targets). A single PMI can support multiple targets, such as a standard VM, an AMD SEV confidential VM, or an Intel TDX environment.  
    * Passive Hypervisors: The hypervisor reads the PMI's recipe and simply follows a deterministic series of "load" (loading sections to memory) and "fill" (generating requested platform data) actions. If the hypervisor cannot fulfill the contract, it rejects the launch.  
  * The Tooling Ecosystem:  
    * Arma: A tool that analyzes a Linux kernel configuration and automatically generates a compatible PMI image and device layout.  
    * Dillo: The Virtual Machine Monitor (VMM) that reads and executes the PMI.  
    * Tattoo: A tiny, highly secure bootloader bundled inside the PMI (written in \~12,000 lines of safe Rust) that merges the device tree and boots the kernel.  
    * Snuffler: A statically linked test binary that runs inside the guest to validate the hardware configuration.  
  * The Payoff  
    * True Portability: Because the launch recipe is deterministic, any PMI-compliant hypervisor across any cloud provider will produce the exact same attestation measurement (e.g., launch data or MR Enclave hash) for the same image.  
    * Regulatory Compliance: By ensuring the user fully controls the TCB without untrusted cloud provider code injections, PMI satisfies strict requirements emerging from international regulators.  
      

## **Work in Progress**

* Alec Fernandez (AF) noted that Blueprint B is ready, however Ofir Azoulay-Rozanes noted there are a few outstanding comments. AF took the action to ask Simon to address outstanding issues via the mailing list and Slack. AF noted that work still needs to be done on the TAC whitepaper but should be able to get to it next week. 

## **Future Business**

* June 25 meeting cancelled  
* Next meeting will be July 9, 2026  
* Rotating chair(s): Rene Kolga / Keith Moyer

## **Action Items**

* TAC work with [Michelle Roth](mailto:mroth@linuxfoundation.org)to get Blueprint C to the creative team and into PDF for publication.  
* Alec Fernandez to work with Simon to resolve outstanding comments on Blueprint B.   
* TAC to review the Proxy & Gateway governance draft and provide feedback.  
* Michelle Roth to move Keystone to Emeritus on website, ask maintainers to update repository. 

---

