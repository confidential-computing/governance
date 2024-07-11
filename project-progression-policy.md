## I. Overview
This governance policy describes how an open source project can formally join the
Confidential Computing Consortium (hereafter the "Consortium") via the
[Project Proposal Process](#ii-project-proposal-process). Projects that have joined the Consortium are
"Technical Projects". It describes the [Stages](#iii-stages---definitions--expectations)
a project may be admitted under and what the criteria and expectations are for a given
stage, as well as the acceptance criteria for a project to move from one stage to
another. It also describes the [Annual Review Process](#iv-annual-review-process)
through which those changes will be evaluated and made.

Project progression - movement from one stage to another - allows projects to participate at the level that is most appropriate for them given where they are in their lifecycle. Regardless of stage, all Consortium projects benefit from a deepened alignment with existing projects, and access to guidance, support, and Consortium resources.

### Benefits of being a recognized Consortium project

Some ways a project can benefit by becoming a Consortium-recognized project include:

1. Recognition: A Consortium project is recognized as meeting the goals of the Consortium, namely protecting data-in-use.
2. Community: The Consortium is fostering a community of like-minded members.
3. Participation: Participate and lead in the ongoing development of the confidential computing paradigm. All projects are assigned a [Liaison](project-liasions.md) to assist in the integration of your project to the Consortium and growth beyond that.
4. Project Support: The Consortium can provide limited funds to support project communication and infrastructure costs for CI/CD.
5. Outreach: Part of the Consortium's mission is to promote the use of confidential computing with various communities and hence its recognized projects, to deliver that outcome.
6. Mentorship: The [TAC has committed](https://lists.confidentialcomputing.io/g/main/files/TAC/Meetings/2021/09-Sept/TAC%20Minutes%202021-09-09.pdf) to fund one mentee per CCC project that commits to the ["Confidential Computing Consortium Mentorship Program"](https://github.com/confidential-computing/governance/tree/main/mentoring).
7. Test infrastructure: Up to $7500 in budget for hardware and software per year.
8. Video conferencing support: A zoom account for community meetings.
9. Domain name: A domain name registration and renewals can be granted.
10. Mailing lists: For asynchronous community discussions.
11. YouTube Playlist: For publishing community meetings, demos, and other project content.
12. Security Scanning: Optional.
13. LFX tools: Access to Linux Foundation tools to improve many aspects of a project from security to community health [tools](https://lfx.linuxfoundation.org/).

Approved projects can [contact operations](mailto:operations@confidentialcomputing.io) for access to these benefits.

## II. Project Proposal Process

### Introduction
This governance policy sets forth the proposal process for projects to be accepted into the Consortium. The process is the same for both existing projects which seek to move into the Consortium and new projects to be formed within the Consortium.

### Project Acceptance Process

The acceptance process is a three-stage process: a technical review with the
Technical Advisory Committee (TAC), legal submission to LF Projects, LLC,
and a vote by the Governing Board.

#### Technical Review

Projects are required to present their proposal at a TAC meeting.
This proposal should cover all the items in the [Project Submission Template](https://github.com/confidential-computing/governance/blob/master/project-submission-template.md).

The TAC may ask for changes to bring the project into better alignment with
the Confidential Computing Consortium (adding a governance document to a
repository or adopting a Code of Conduct, for example). The project will
need to make these changes in order to progress further.

Projects are accepted or progress from level to level via a majority vote
of TAC representatives present if quorum is reached or a majority of all
TAC representatives if voting by email, unless a project is being
moved to the Emeritus stage, in which a vote of
two-thirds of all TAC representatives is required.

The TAC will determine the appropriate initial stage for the project.
The project can apply for a different stage via the review process.

Once a project passes Technical Review, the TAC will inform the Governing
Board of the submission proposal.

#### Legal Submission

After a succesful TAC vote, the project is ready for a legal review. The legal review is initated by the project filling out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeO1bDGHUP-ZpCo1uynm94YOxZlek6RhCH7o3FnX1lZSXXfSQ/viewform?fbzx=4351560609072672295). The LF project onboarding team will create a draft Technical Charter, a draft Project Contribution Agreement (if needed), and a draft Series Agreement.

As noted in clause 11 of the [Confidential Computing Consortium (CCC) Charter](https://confidentialcomputing.io/wp-content/uploads/sites/85/2019/12/CCC_Charter.pdf),
the CCC requires that any trademarks be transferred to, or be available for
use by, LF Projects, LLC.  Even if no trademarks exist, the current CCC
policy is that projects be submitted to LF Projects, LLC.


#### Governing Board Vote

Once the Technical Review and Legal Submission steps are complete,
the Governing Board will review
the project proposal and the proposed Technical Charter.  If there are
legal questions raised, the Governing Board may refer the matter to
the Legal Committee for review.  This review may occur in parallel with
Technical Review in some cases.

Once any such legal questions have been addressed, the Governing Board will
vote at its next available meeting.

Upon acceptance by the board, the project's approved Technical Charter
must be included in the project's main repository.  This document can
be in whatever format is most appropriate for the project, as long as
the content is the same.

### Spin-off Projects ###

Projects can create multiple subordinate projects that are governed under the structure agreed on and accepted by the TAC.

A project may want to spin out a new project because the original scope, governance or participants are distinctly different from the original agreed project charter, and not merely an organization of code or minor expansion of scope.

In this case a new project acceptance proposal, as defined above, should be submitted to the TAC.

## III. Stages - Definitions & Expectations
Every Consortium project has an associated maturity level. Proposed projects should state their preferred maturity level.  There are three maturity levels under this Project Progression Policy:

* Incubation - projects looking for a foundation with minimal initial resource requirements;
* Graduation - projects that are used in production; and
* Emeritus - projects that are approaching end-of-life.

Representatives of Technical Projects may attend TAC meetings and contribute work regardless of their stage.

### Incubation Stage
**Definition**

The Incubation stage is for projects that the TAC believes are, or have the potential to be, important to the ecosystem of Technical Projects or the ecosystem of the Consortium as a whole. They may be early-stage projects just getting started, or they may be long-established projects with minimal resource needs. The Incubation stage provides a beneficial, neutral home for these projects in order to foster collaborative development and provide a path to deeper alignment with other Consortium projects via the project progression process.

**Examples**

1.	New projects that are designed to extend one or more Consortium projects with functionality or interoperability libraries.
2.	Independent projects that fit within the Consortium mission and provide potential for a novel approach to existing functional areas (or are an attempt to meet an unfulfilled need).
3.	Projects commissioned or sanctioned by the Consortium.

**Expectations**

End users should evaluate Incubation projects with care, as this stage does not set requirements for community size, governance, or production readiness. Incubation projects will receive a basic level of support from the Consortium.

Each project is expected to develop a [growth plan](growth-plans.md), and a project's progress toward its growth plan goals will be reviewed on a yearly basis, as discussed in the [Annual Review Process](#iv-annual-review-process).
They may also request a status review by submitting a report to the TAC.

**Acceptance Criteria**

To be considered for the Incubation Stage, the project must meet the following requirements:
* 1 [TAC representative](project-liaisons.md) that will serve as a sponsor to champion the project & provide guidance as needed
* A presentation to at the meeting of the TAC

* Upon acceptance, Incubation projects must list their status prominently on their website/README

### Graduation Stage
**Definition**

Graduation stage projects will receive guidance from the TAC and are expected to actively develop their community of contributors, governance, project documentation, and other variables identified in the growth plan that factor into broad success and adoption.

In order to support their active development, projects in the Graduation stage have a higher level of access to Consortium resources as provided by the Governing Board of the Consortium. A project's progress toward its growth plan goals will be reviewed on a yearly basis, and the TAC may move a project to the Incubation stage if progress on the plan drops off or stalls.

**Examples**

1.	Projects that have developed new growth targets or other community metrics for success.
2.	Projects that are looking to create a lifecycle plan (maintainership succession, contributor programs, version planning, etc.)
3.	Projects that need more active support from the Consortium or TAC guidance in order to reach their goals.

**Acceptance Criteria**

To be considered for Graduation stage, the project must meet the Incubation requirements as well as the following:

 * Development of a growth plan, to be done in conjunction with their [project liason(s)](project-liaisons.md) at the TAC.
 * Document that it is being used successfully in production by at least two independent end-user organizations which, in the TAC's judgement, are of adequate quality and scope.
 * Demonstrate a substantial, in the opinion of the TAC, ongoing flow of commits and merged contributions.
 * Demonstrate that the current level of community participation is sufficient to meet the goals outlined in the growth plan.
 * Since these metrics can vary significantly depending on the type, scope and size of a project, the TAC has final judgement over the level of activity that is adequate to meet these criteria.
 * Demonstrate that the project is invested in growing a diverse and inclusive community. Resources and recommendations are available in [diversity and inclusion policies](diversity-and-inclusion-policies.md) and through your liaison.
 * Receive a two-thirds supermajority vote of the TAC to move to Graduation stage.

### Emeritus Stage
**Definition**

Emeritus projects are projects which the TAC or a project's maintainers feel have reached or are nearing end-of-life. Emeritus projects may have contributed to the ecosystem, but are not necessarily recommended for modern development as there may be more actively maintained choices. The Consortium appreciates the contributions of these projects and their communities, and the role they have played in moving the ecosystem forward.

**Examples**

1.	Projects that are "complete" by the maintainers' standards.
2.	Projects that do not plan to release major versions in the future.

**Expectations**

Projects in this stage are not in active development. Their maintainers may infrequently monitor their repositories, and may only push updates to address security issues, if at all. Emeritus projects should clearly state their status and what any user or contributor should expect in terms of response or support. If there is an alternative project the maintainers recommend, it should be listed as well. The Consortium will continue to hold the IP and any trademarks and domains, but the project is not expected to draw on Consortium resources.

**Acceptance Criteria**

Projects may be granted Emeritus status via a vote of two-thirds of the representatives of the TAC.


## IV. Annual Review Process

The TAC will conduct a review of each accepted project on an annual basis.

The review includes the following:

1. Review whether any answers to the project's submission template or Technical Charter have
   changed, and if so, review the new answers. A representative from the
   project is responsible for presenting any deltas to the template answers
   since the last review, if any. If there are no changes, there is nothing
   to review here.

2. Review the project's progression status to determine whether the project
   is in the stage that accurately reflects its needs and goals. For example,
   is it already ready to move to another progression level? Is it on track
   at the current level? Is any action needed from the TAC (e.g., change in
   or addition to any project liason(s))?  If nothing has changed
   significantly, there may be nothing to review here.

3. Review any budget allocations relevant to the project, and whether any
   adjustments are needed.
   
4. Review license scans provided by the Linux Foundation. Provide feedback
   on any outstanding issues and evaluate the scanning service from the
   project's perspective.

5. Review the project's [OpenSSF Best Practices Badge](https://bestpractices.coreinfrastructure.org/)
   status.  Does the project display the badge on its github page?
   Has its status advanced since the last TAC review?  Does it expect the
   status to further advance during the next year?

Projects are encouraged to proactively inform the TAC when something
changes that affects their submission template or Technical Charter (changing a License, security
reporting process, CoC, etc.), rather than waiting for the next annual review.

It is the responsibility of the project's [liason](project-liasons.md) to help the project determine
what needs to be reviewed by the TAC, and keep the TAC informed.
