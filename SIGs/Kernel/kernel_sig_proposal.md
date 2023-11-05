# Proposal: CCC Linux Kernel SIG

This proposal seeks to accelerate Confidential Computing feature velocity in the Linux kernel. 
By creating a Linux Kernel SIG in the CCC we can foster community dialog to develop vendor neutral
architectural approaches to new features and thereby reduce complexity in associated kernel patches.


# Background:

One of the technical limitations to the adoption rate for Confidential Computing is the speed at
which we as a community can add features to the Linux kernel. Each vendor has similar needs of the
kernel but has historically presented significantly different ABIs. To contain complexity and manage
maintainability, the Linux kernel community tries to prevent proliferation of unnecessarily vendor
specific ABIs. Often the opportunity for commonality is unclear until multiple vendors have proposed
separate interfaces [0].
 
The CCC as the home of open collaboration for Confidential Computing hardware vendors, software
vendors, and end users facilitates a unique environment for exchanging views on features and
requirements. Up to this point in time though most CCC collaboration has been on user space software
and use cases. The Linux kernel community has not been a regular part of discussions and the CCC has
not been a regular participant on the Linux Kernel Mail List (LKML)[1]. Bringing these communities
together in a structured forum has the promise of accelerating their joint work towards broad
availability of Confidential Computing in Linux environments.


# Scope:

1. Facilitate dialog between Linux kernel and Confidential Computing subject matter experts:
    * to facilitate direction for topics that need formal collaboration,
    * to have an additional venue to facilitate direction for topics that are stalled on LKML,
      which would benefit from higher bandwidth communication, 
    * to have a common place to record decisions and formalize the output for others to reference,
    * and to introduce new technical topics emerging in either domain, e.g., attestation mechanisms
      approaching standardization.
2. Create recommendations for other organizations and communities such as LKML, IETF, etc.
   on topics at the intersection of the Linux kernel and Confidential Computing.


# Governance:

The CCC adheres to a culture of Minimum Viable Governance [2].
We prefer not to create rules that inhibit the progress of substantive work.
 
All are welcome at all CCC community forums. This SIG is targeted to all Linux kernel maintainers
and Confidential Computing vendors, project contributors, and end users with a dependence on the
Linux kernel. Meetings will follow standard CCC practices of inclusivity and openness adhering to
the community code of conduct [3] and the Linux Foundation’s Antitrust policy [4].


## Decision Making:

This SIG will use consensus decision making [5] wherein not all participants must be in full
agreement but that there should not be a strong consensus against a proposal [6].
 
In most cases we expect that once the SIG reaches consensus on a kernel topic, contributors will
propose aligned patches to LKML without any explicit communication from the SIG or the CCC.
 
If a formal CCC recommendation to another organization, e.g., IETF, TCG, eBPF Foundation, etc. is
required, the SIG will rely on the CCC Technical Advisory Council (TAC) to ratify proposals from the
SIG.
 
The pipeline of activity is expected (but not required) to look like this: 
1. Identify feature need on mailing list or informal forum.
2. Exchange community proposals in the SIG.
3. Achieve informal consensus in the SIG.

    a. Author patches and take them to the appropriate community, e.g., LKML.

    or

    b. Raise an agenda item for the CCC TAC to formally ratify a proposal and publish to the
       appropriate organization.


## Initial Logistics:

The community will set its own meeting cadence starting from an initial cadence of meeting twice per
month. The CCC will provide a Zoom channel. At the end of each meeting a new chair may volunteer to
organize the agenda for the next meeting. The chair role confers no other responsibility or
authority beyond collecting agenda requests from the community and enforcing minutes and good order.
In addition to video meetings, the community will use an existing Discord channel for ongoing
communication. No mail list is required at this time.
 
 

# References:
[0] https://lore.kernel.org/all/64876bf6c30e2_1433ac29415@dwillia2-xfh.jf.intel.com.notmuch/
 
[1] https://lore.kernel.org/linux-coco/
 
[2] Sarah Novotny, Stephen Walli, “Minimum Viable Governance”, Linux Foundation Open Source Summit Europe 2020, https://www.youtube.com/watch?v=C2-_MjzP-Rs  
 
[3] https://github.com/confidential-computing/governance/blob/main/code-of-conduct.md
 
[4] https://www.linuxfoundation.org/legal/antitrust-policy
 
[5] https://en.wikipedia.org/wiki/Consensus_decision-making
 
[6] See Rust’s Final Comment Period (FCP) https://github.com/rust-lang/rfcs
