# Confidential Computing Consortium TAC meeting

*The TAC meets for two hours on alternating Thursdays. All members of the community are welcome to attend and participate.*

## Meeting details

**Date**: Thursday, February 24, 2022

**Time**: 7a-9a US Pacific Time

* **Zoom**: [https://zoom.us/j/184384055](https://zoom.us/j/184384055) (pw: 43690)
* **Calendar**: [https://calendar.confidentialcomputing.io](https://calendar.confidentialcomputing.io) ([ical](https://calendar.google.com/calendar/ical/c_c0pcihr7n2n1k3a38i32d9ag10%40group.calendar.google.com/public/basic.ics), [Google Calendar](https://calendar.google.com/calendar/u/0/r?cid=c_c0pcihr7n2n1k3a38i32d9ag10@group.calendar.google.com))
* **Recording**: [YouTube](https://www.youtube.com/watch?v=cAKU9u0Z0_g)

### Voting members of the TAC

*Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.*

* **Accenture** - Giuseppe Giordano
* **Ant Group** - Zongmin Gu / Tate, Hongliang Tian
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

Rep. Thaler opened the call at 7:04a PT. He welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.

### Roll Call / Attendance

#### Voting members

* Dan Middleton (Intel)
* Dave Thaler (Microsoft)
* Lily Sturman (Red Hat)
* Giuseppe Giordano (Accenture)
* Tate, Hongliang Tian (Ant Group)
* Thomas Fossati (Arm)

#### Attendees

* Eric Voit (Cisco)
* Nick Vidal (Profian)
* Penglin Yang (China Mobile)
* Radhika Jandhyala (Microsoft)
* Ravi Sahita (Rivos)
* Samuel Ortiz (Apple)
* Shalom Shefa (Cisco)
* Simon Johnson (Intel)
* Steve Van Lare (Anjuna)

### Meeting minute approvals

#### Approved by voting members

**RESOLVED:** That the minutes of the [January 13, 2022](../2022-01-13/TAC_Minutes-2022-01-13.pdf) meeting of the Technical Advisory Council meeting of the Confidential Computing Consortium as distributed to the members of the TAC in advance of this meeting are hereby adopted and approved.

#### Pending approval

* [December 16, 2021](../../2021/2021-12-16/TAC_Minutes-2021-12-16.pdf), further updates needed
* [February 10, 2022](https://github.com/confidential-computing/governance/pull/93/files)

### Open Action Items

1. **[Mike, Eric, Stephen, Zongmin]** Recommend diversity and inclusion training to their projects and report back to the TAC on whether the maintainers or the contributors will be taking it and when the expected completion date is.

1. **[Stephen Walli, Dan Middleton, Aeva Black]** Develop a CoC escalation process, to be presented to TAC and governing board.
    * Dan Middleton has opened a PR for review

1. **[Brian Warner]** Add LFX security code scanning for projects as a topic for a future meeting.
    * To be discussed in main agenda as a possible TAC tech talk.

### Completed Action Items

1. **[ALL]** Review, comment and/or correct text in [Common Terminology Document](https://docs.google.com/document/d/1xZ6IX0w0jaWDbLMFNAybTF3FpLnQ5TJ98nzIWbsbFnY/edit). (To be moved to main agenda)


1. **[Dan Middleton]** [PR #92](https://github.com/confidential-computing/governance/pull/92) opened to develop a CoC escalation process.


### Project overviews

* Veraison
    * Dave Thaler (DT) noted that Veraison was approved by the TAC, and is ready for next steps (technical charter, IP transfer, board approval).
* Enarx
    * DT noted that Enarx is ready for its annual review.

1. **[Brian, Dave]** Schedule Veraison for Board review, tech charter development, and IP transfer.

### Open Enclave SDK - annual project review 

Radhika Jandhyala (RJ) reviewed the [Open Enclave SDK annual project review document](https://github.com/confidential-computing/governance/tree/main/TAC/Meetings/2022/2022-02-24). She noted that the communication channels have changed, noting that the Matrix server has been deprecated. She also noted that some dependencies have changed.

DT asked for clarification which SGX SDK is represented in the dependencies, as there are different versions for Windows and Linux. RJ noted that this dependency is specific to the SGX SDK for Linux.

RJ noted that Linux packages have been uploaded to various package repositories and GitHub.

She noted that Open Enclave SDK has a quarterly release cadence. Releases are also made when CVEs are fixed. She noted that the project averages six commits weekly. The committers are making progress towards Inclusive Open Source Communities orientation, and noted that this is being tracked in a github issue.

RJ reviewed intentional work by the project to help diversify the organizations involved. She noted that that OE SDK has not yet published a list of adopters and is not yet ready to request Graduation stage.

RJ next reviewed budget requests. She noted that OE SDK is using Zoom and had a license scan in the fall. She requested an updated license scan once the project has had time to remediate some issues. She noted this is likely the only budget request.

DT requested RJ's opinion whether the project could be ready for Graduation status within the next year. She noted that it could be longer. DT noted that the Graduated lifecycle text has never been finalized. Dan Middleton (DM) asked if this should be a focus for an upcoming meeting.

**Action:** Brian Warner to investigate prior efforts to finalize Graduation lifecycle language, and if needed file an issue to finalize Graduation lifecycle language.

RJ next reviewed the license scan results. Discussion ensued.

**Action:** Brian Warner to update the Google Sheet containing the [list of CCC dependencies](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0) with the changed dependencies noted in the project review document.

### Outreach update

BW reviewed discussions on the Outreach committee. He noted that Outreach discussed OC3, and provided an update on staffing. He noted the Confidential Computing in Healthcare webinar will be delayed.

DT asked if there are any events with speaking and participation opportunities that would be relevant to projects over the next six months. Nick Vidal (NV) noted that Outreach is working on a spreadsheet with this info and doing specific outreach to projects on this topic. He noted he hopes this will be ready for the next call.

NV requested clarification on the date for the Enarx project review. DT reviewed available times. NV requested March 10, 2022 for the Enarx review.

**Action:** Brian Warner to add Enarx annual review to the agenda for March 10th TAC meeting.

BW noted that DM had joined to discuss Diversity, Civility, and Inclusion.

DT noted that there was a recent discussion with an Andrew Braunberg from Futuriom. DT, Richard Searle, and Ravi Sharma participated. He noted that it was a Q&A, and that Andrew had already seen the whitepaper. He noted that the discussion went well.

DM noted that the D&I discussion was based upon the TAC discussion, and was additionally focused on marketing topics. DM noted that the goal is to provide projects with materials they can use as well.

### Common terminology

Eric Voit (EV) reviewed recent changes to the diagram and noted additional context had been added to the bullet points underneath. He noted that additional context was provided regarding Enarx, where one build could be used to maintain a common north-bound interface, allowing a single project to abstract away the isolation technologies underneath. Finally, he noted descriptive text from Enarx that highlights certain aspects which be abstracted, allowing projects to span multiple isolation technologies.

DT noted that it's helpful to have specific examples from projects, in light of the text about Enarx. He suggested that other projects contribute content to the descriptive text as well, to help place the CCC's role in broader context. EV agreed and noted that contributions from other CCC projects would be welcomed. DT recommended that project mentors involve their projects in contributing text.

Steve Van Lare (SVL) agreed that it would be good to include other projects, as there are different TEE solutions based upon architectures, and that there are differences between encryption and isolation in the tech stacks. 

DT continued discussion on the Anjuna glossary definitions related to confidential computing. He noted that the Anjuna definition of Confidential Cloud covers protection of data-in-use, data-in-flight, and data-at-rest. He noted that the definition was broader than the CCC scope, which explicitly refers to data-in-use. He noted that, speaking as the Microsoft rep, he would like to see the document define one or more terms that cover all three areas, in keeping with SVL's original suggestions.

SVL reviewed Anjuna's perspective on Confidential Cloud. Discussion ensued over the boundaries of Confidential Cloud. DT asked from whom the data is confidential. SVL noted that cloud providers have different opinions on the size of the circle of trust. Discussion ensued over what data-in-use means.

EV provided a preview of a future TAC tech talk. He noted that many of the discussions around Confidential Cloud also apply to the networking space. Discussion ensued.

Ravi Sahita (RS) asked if it makes sense to also discuss the layers above CCC's definition. DT noted that attestation is a key component and helps fit the various components together. 

DT summarized the discussion noting there would also be value discussing the other aspects of data protection, as well as cloud and networking. He noted that the whitepaper could ultimately discuss how to tie various aspects together.

Thomas Fossati (TF) asked if anyone is leading activity to create an initial diagram including layers above confidential computing. DF requested volunteers. SVL noted that expanding the discussion into networking would be helpful. RS volunteered to help, as did SVL.

DT requested the TAC members review the current whitepaper.

### Any other business

DT requested a placeholder slide that points to the governance repo to address issues and PRs, time permitting.

**Action:** Brian Warner to add a slide to the deck.

#### Pull request review

* [PR #87](https://github.com/confidential-computing/governance/issues/87): Brian Warner to merge `main` into `master`, delete `main`, and rename `master`.
* [PR #77](https://github.com/confidential-computing/governance/issues/77): Thomas Fossati to review feedback on the whitepaper.
* [PR #71](https://github.com/confidential-computing/governance/issues/71): All actions have been taken, PR to be closed.

### Future topics

DT noted that the TCG TAC tech talk has been rescheduled. He also noted that CCC Attestation will be ready for an annual review in March.

**Action**: Dan Middleton to work with CCC Attestation on scheduling the annual review, tentatively for March 24, 2022.

**Action**: Brian Warner to tentatively schedule a deep-dive into LFX code scanning for April 19, 2022.

### Updating documentation

DT noted that items in slide 16 and 17 aren't on the list of documented project benefits on GitHub.

**Action**: Dave Thaler to open an issue requesting an update to the repo.

DT closed the call at 8:49a PT.
