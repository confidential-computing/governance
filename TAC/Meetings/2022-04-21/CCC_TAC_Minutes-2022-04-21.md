# Confidential Computing Consortium 
## Minutes of the Technical Advisory Council 

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, April 21, 2022

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)
* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io) ([ical](https://calendar.google.com/calendar/ical/c_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics), [Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com))
* **Recordings**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLmfkUJc39uMjaB_I1dYW72I44kr9QzG_B)

### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Zongmin Gu
* **Arm** - Thomas Fossati / Michael Lu
* **Google** - Iulia Ion
* **Huawei** - Zhipeng (Howard) Huang
* **Intel** - Dan Middleton / Simon Johnson
* **Meta** - Eric Northup / Shankaran Gnanashanmugam
* **Microsoft** - Dave Thaler (TAC chair)
* **Red Hat** - Lily Sturmann / Dimitrios Pendarakis

## Links

* **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io)
* **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io)
* **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)
* **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)
* **YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io)
* **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org)
* **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io)
* **Contact the CCC**: [confidentialcomputing.io/contact-us/](https://confidentialcomputing.io/contact-us/)

## Agenda and Minutes

### Welcome

Rep. Thaler opened the call at 7:05am PT. He welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.

### Roll Call / Attendance

#### Voting members

* Dave Thaler (Microsoft)
* Lily Sturman (Red Hat)
* Simon Johnson (Intel)
* Zhipeng (Howard) Huang (Huawei)
* Thomas Fossati (Arm)
* Dan Middleton (Intel)


#### Attendees

* Eric Voit (Cisco)
* Penglin Yang (China Mobile)
* Steve Van Lare (Anjuna)
* Jethro Beekman (Fortanix)
* Henk Birkholz (Fraunhofer-Gesellschaft)
* Vijay Nayani (Huawei)
* Xinxin Fan (IoTeX)
* Sampo Sovio (Huawei)
* Ravi Sahita (Rivos)
* Kurt Taylor (Linux Foundation)
* Shubhra Kar (Linux Foundation)

### Meeting minute approvals

#### Approved by voting members

**Proposed:** That the minutes of the [April 07, 2022](../2022-04-07/TAC_Minutes-2022-04-07.pdf) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

 * Quorum was reached, however the minutes of April 7th meeting were not approved due to changes being needed.

#### Pending approval
 * None

### TAC Tech Talks
 *  [Code Scanning via LFX Security](LFX%20Security.pdf) - Shubhra Kar (Linux Foundation)
 *  Dan - would like to hear feedback from Enarx
 *  DT - project mentors to work with projects to get code scan running on github
 *  Action item: KT to add all projects to LFX Security 
    *  https://security.lfx.linuxfoundation.org/


### Open Action Items

1. **[Stephen Walli, Dan Middleton, Aeva Black]** Develop a CoC escalation process, to be presented to TAC and governing board.
    * Dan Middleton has opened a PR for review https://github.com/confidential-computing/governance/pull/92

1. **[Stephen, Zongmin]** Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.
    * Open Enclave maintainers are close to 100% trained (Dave Thaler)
    * Veracruz lead has taken the course (Thomas Fossati).
    * Please report back that project maintainers have been made aware of the training, and have been asked to take it.

1. **[Kurt Taylor]** Investigate prior efforts to finalize Graduated lifecycle language, and if needed file an issue to finalize Graduated lifecycle language. (DT) summarized options for resolution: 1) Adopt new stages 2) talk about proposal and fix it 3) delete the proposed new terms and just use the the two currently adopted stages, sandbox and incubation

2. **[Kurt Taylor]** Check if terminology document markdown format will work with LF Creative team and check on their timeline for completing the formatting for the whitepaper (Done)
   * Markdown is fine, timeline is 1-3 weeks, depending on length and complexity)

2. **[Kurt Taylor]** Code scanning via LFX Security - add all missing projects to security for scanning, get more details on instructions on installing github bot (Done) 
    * Projects can set up the bot and repos they want scanned by following these instructions: https://community.lfx.dev/t/how-to-install-and-configure-bots-to-secure-your-projects/181


### Completed Action Items


### Project overviews


### Interns
* Dan Middleton (DM) - many new interns introduced in slack - needs clarity on where the interns are assigned
* Need both Nick Vidal (NV) and DM here - keep on agenda for next meeting

### Project website funding (Gramine)
 * DT Gramine requested funding for a website, theme rebuild and managed infrastructure
 * DT asking for approval - maybe need official policy with review of costs, may need higher budget, propose putting up for vote
 * Jethro Beekman (JB) pointed out that this may be too expensive $150 for simple website, maybe go with another service not managed by LF and save money, can use the budget for another service
 * DM - make it easy for the project, up to $150 as a budget
 * DT - pointed out that the specific amount would be approved on a case-by-case basis
 * DT reviewed actual website
 * DT - would like to see a vote as Gramine is waiting for response
 * DM - asked for context from Eric Voit (EV) as their mentor, EV reported that they have discussed design and proposal
 * JB proposed website maintenence education (wordpress) by the LF for the same amount for upfront cost $500, for creation or education
 * Lily Sturmann (LS)  asked to vote upfront and monthly seperately, DT said it wouldn't help Gramine, because it will be a signup as a package deal
 * DT proposed up to $1800 year, $1000 standard policy for each project to use, vote on each project actual cost on a case-per-case basis as long as it falls into this budget
 * Simon Johnson (SJ) asked for a more specific policy with guidelines for what the TAC would be looking for and what would be approved and what would not
 * DT said that he agreed with SJ and that consistency across the projects is a good thing, SJ said that some clarification on overall professional website design would be good
 * DT called for a vote - slide 11 Proposal: The TAC is willing to fund web hosting to approved projects on request, up to $1800/yr on an ongoing basis, after a one-time up front cost of up to $1000.

 **Approved** - Policy for new budget approved for website
 
 * DT Gramine is waiting, vote for approval for Gramine
 * DT called a vote for Gramine - no objections noted
 
 **Approved** to have Gramine proceed with website request

### CCC Attestation SIG annual review

*  Thomas Fossati (TF) presenting [slides](ccc-attestation-sig-review-2021-2022.pdf)
*  DT and TF proposed vote for approval for Greg Kostal to take over Chair of Attestation from Larry, leads Microsoft Azure Attestation service - Vote ran by JB as vice-chair, since DT recused from voting.

	**Approved** Greg Kostal attestation chair without objections, DT abstains

*  DM reminded everyone that there will be a Tuesday meeting for Attestation


### Outreach update

* No update from the outreach meeting


### Common terminology

 * DT shared the terminology document
 * EV reviewed the plan to take the current document and checkin to Github 
 * EV Trusted Codebase, is a official definition needed Trusted Computing Base (TCB)
 * DM noted that there may already be a definition for Trusted Computing Base
 * EV commented on clarification on TCB definition questions in the document
 * EV marketing communications - comment on confidential VM
 * EV where does TDX fit, where should it appear, need clarification from Intel, clarified by DM, please add TDX
 * DT reminded that TAC doesn't take a position on vendor products, maybe change the word "known" to "claimed", Ravi Sahita (RS) commented he could add RISC-V directions, EV to make changes
 * DT noted that the definitions will never be complete, agreed on RISC-V additions as long as it is an easy add, else we can add it in a future revision
 * DT agreed on expanding the definition for TCB
 * DT asked KT about timeline for LF creative services to produce the whitepaper, preferred initial format for conversion
 * EV, DT discussed where to push initial document for comments, agreed to push to CCC governance repo, maybe in a whitepaper or terminology directory
 * Steve Van Lare (SVL) comments on confidential shared responsibility relating to cloud infrastructure, making sure we have a common definition
 * DT suggested a change terminology as it is not specific to cloud computing
 * SVL goal is to say this is an important topic, just not one to cover in this paper
 * DT proposed to stop using confidential compute and instead only use confidential computing
 * DT changed memory encryption definition instead using memory isolation, EV discussed RAM vs memory vs dynamic memory, change diagram to reflect the change to use memory isolation, Penglin Yang (PY) agreed
 * SVL and EV will write Conclusion/Summary
 * DT proposed EV conversion to markdown, images to be included as links, KT will make sure this format will work with LF Creative team and check on their timeline for completing the formatting for the whitepaper, see Actions


### Any other business
* DT presentations overview, done with project reviews backlog, May 5 TAC tech talk IETF TEE Provisioning, next talk reach out to Mike Bursell for the 19th TAC talk, KT to help schedule
*  DT NIST Cybersecurity Call for comments, by April 25th https://www.federalregister.gov/documents/2022/02/22/2022-03642/evaluating-and-improving-nist-cybersecurity-resources-the-cybersecurity-framework-and-cybersecurity


(DT) closed the call at 8:59am PT.
