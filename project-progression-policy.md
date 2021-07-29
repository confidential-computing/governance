## I. Overview
This governance policy describes how an open source project can formally join the
Confidential Computing Consortium (hereafter the "Consortium") via the
[Project Proposal Process](#ii-project-proposal-process). Projects that have joined the Consortium are
"Technical Projects". It describes the [Stages](#iii-stages---definitions--expectations)
a project may be admitted under and what the criteria and expectations are for a given
stage, as well as the acceptance criteria for a project to move from one stage to
another. It also describes the [Annual Review Process](#iv-annual-review-process)
through which those changes will be evaluated and made.

Project progression - movement from one stage to another - allows projects to participate at the level that is most appropriate for them given where they are in their lifecycle. Regardless of stage, all Consortium projects benefit from a deepened alignment with existing projects, and access to mentorship, support, and Consortium resources.

### Benefits of being a recognized Consortium project

Some ways a project can benefit by becoming a Consortium-recognized project include:

1. Recognition: A Consortium project is recognized as meeting the goals of the Consortium, namely protecting data-in-use.
2. Community: The Consortium is fostering a community of like-minded members.
3. Participation: Participate and lead in the ongoing development of the confidential computing paradigm. All projects are assigned a [Mentor](project-mentors.md) to assist in the integration of your project to the Consortium and growth beyond that.
4. Project Support: The Consortium can provide limited funds to support project communication and infrastructure costs for CI/CD.
5. Outreach: Part of the Consortium's mission is to promote the use of confidential computing with various communities and hence its recognized projects, to deliver that outcome.

## II. Project Proposal Process

### Introduction
This governance policy sets forth the proposal process for projects to be accepted into the Consortium. The process is the same for both existing projects which seek to move into the Consortium and new projects to be formed within the Consortium.

### Project Acceptance Process

The acceptance process is a three-stage process: a technical review with the
Technical Advisory Committee (TAC), legal submission to LF Projects, LLC,
and a vote by the Governing Board.

#### Technical Review

Projects are required to present their proposal at a TAC meeting.
This proposal should cover all the items in the [Project Submission Template](https://github.com/confidential-computing/governance/blob/master/project-submission-template.md)
and the [Technical Charter template](https://lists.confidentialcomputing.io/g/main/files/TAC/Project%20Submissions/Technical%20Charter%20%28custom+data%29%20--%20LF%20Projects,%20LLC%204-10-2019%20FINAL%20%2811%29.docx)).

The TAC may ask for changes to bring the project into better alignment with
the Confidential Computing Consortium (adding a governance document to a
repository or adopting a Code of Conduct, for example). The project will
need to make these changes in order to progress further.

Projects are accepted or progress from level to level via a majority vote
of TAC representatives present if quorum is reached or a majority of all
TAC representatives if voting by email, unless a project is being accepted
at or moved to either the Graduation or Emeritus stage, in which a vote of
two-thirds of all TAC representatives is required.

The TAC will determine the appropriate initial stage for the project.
The project can apply for a different stage via the review process.

Once a project passes Technical Review, the TAC will inform the Governing
Board that the submission proposal and Technical Charter are ready for the
next step.

#### Legal Submission

As noted in clause 11 of the [Confidential Computing Consortium (CCC) Charter](https://confidentialcomputing.io/wp-content/uploads/sites/85/2019/12/CCC_Charter.pdf),
the CCC requires that any trademarks be transferred to, or be available for
use by, LF Projects, LLC.  Even if no trademarks exist, the current CCC
policy is that projects be submitted to LF Projects, LLC.

This submission entails sending the proposed Technical Charter (as reviewed
by the TAC), and a signed [Project Contribution Agreement](https://lists.confidentialcomputing.io/g/main/files/TAC/Project%20Submissions/LF%20Projects%20--%20Form%20of%20Trademark%20and%20Account%20Assignment.docx).

This submission might in some cases be done in parallel with, or even
before, Technical Review.  It is recommended though that this be
done after the Technical Review where practical.

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
Every Consortium project has an associated maturity level. Proposed projects should state their preferred maturity level.  There are four maturity levels under this Project Progression Policy:

* Sandbox - projects looking for a foundation with minimal initial resource requirements;
* Incubation - growing projects that are targeting particular growth metrics and looking for resources from the Consortium;
* Graduation - projects that have reached their growth goals and are now on a sustaining cycle of development, maintenance, and long-term support; and
* Emeritus - projects that are approaching end-of-life.

Representatives of Technical Projects may attend TAC meetings and contribute work regardless of their stage.

### Sandbox Stage
**Definition**

The Sandbox stage is for projects that the TAC believes are, or have the potential to be, important to the ecosystem of Technical Projects or the ecosystem of the Consortium as a whole. They may be early-stage projects just getting started, or they may be long-established projects with minimal resource needs. The Sandbox stage provides a beneficial, neutral home for these projects in order to foster collaborative development and provide a path to deeper alignment with other Consortium projects via the graduation process.

**Examples**

1.	New projects that are designed to extend one or more Consortium projects with functionality or interoperability libraries.
2.	Independent projects that fit within the Consortium mission and provide potential for a novel approach to existing functional areas (or are an attempt to meet an unfulfilled need).
3.	Projects commissioned or sanctioned by the Consortium.

**Expectations**

End users should evaluate Sandbox projects with care, as this stage does not set requirements for community size, governance, or production readiness. Sandbox projects will receive minimal support from the Consortium. Projects will be reviewed on an annual basis; they may also request a status review by submitting a report to the TAC.

**Acceptance Criteria**

To be considered for the Sandbox Stage, the project must meet the following requirements:
* 1 [TAC representative](project-mentors.md) that will serve as a sponsor to champion the project & provide mentorship as needed
* A presentation to at the meeting of the TAC

* Upon acceptance, Sandbox projects must list their status prominently on their website/README

### Incubation Stage
**Definition**

The Incubation stage is for projects that are interested in reaching the Graduation stage, and have identified a [growth plan](growth-plans.md) for doing so. Incubation stage projects will receive mentorship from the TAC and are expected to actively develop their community of contributors, governance, project documentation, and other variables identified in the growth plan that factor into broad success and adoption.

In order to support their active development, projects in the Incubation stage have a higher level of access to Consortium resources as provided by the Governing Board of the Consortium. A project's progress toward its growth plan goals will be reviewed on a yearly basis, and the TAC may move a project to the Sandbox stage if progress on the plan drops off or stalls.

**Examples**

1.	Projects that are on their way or very likely to become Graduation projects.
2.	Projects that have developed new growth targets or other community metrics for success.
3.	Projects that are looking to create a lifecycle plan (maintainership succession, contributor programs, version planning, etc.)
4.	Projects that need more active support from the Consortium or TAC mentorship in order to reach their goals.

**Expectations**

Projects in the Incubation stage are generally expected to move out of the Incubation stage within two years. Depending on their growth plans, projects may cycle through Sandbox, Incubation, or Graduation stage as needed.

**Acceptance Criteria**

To be considered for Incubation stage, the project must meet the Sandbox requirements as well as the following:

 * Development of a growth plan, to be done in conjunction with their [project mentor(s)](project-mentors.md) at the TAC.
 * Document that it is being used successfully in production by at least two independent end-user organizations which, in the TAC's judgement, are of adequate quality and scope.
 * Demonstrate a substantial, in the opinion of the TAC, ongoing flow of commits and merged contributions.
 * Demonstrate that the current level of community participation is sufficient to meet the goals outlined in the growth plan.
 * Since these metrics can vary significantly depending on the type, scope and size of a project, the TAC has final judgement over the level of activity that is adequate to meet these criteria.
 * Demonstrate that the project is invested in growing a diverse and inclusive community. Resources and recommendations are available in [diversity and inclusion policies](diversity-and-inclusion-policies.md) and through your mentor.
 * Receive a two-thirds supermajority vote of the TAC to move to Incubation stage.

### Graduation Stage
**Definition**

The Graduation stage is for projects that have reached their [growth goals](growth-plans.md) and are now on a sustaining cycle of development, maintenance, and long-term support. Graduation stage projects are used commonly in enterprise production environments and have large, well-established project communities.

**Examples**

1.	Projects that have publicly documented release cycles and plans for Long Term Support ("LTS").
2.	Projects that have themselves become platforms for other projects.
3.	Projects that are able to attract a healthy number of committers on the basis of its production usefulness (not simply 'developer popularity').
4.	Projects that have several, high-profile or well known end-user implementations.

**Expectations**

Graduation stage projects are "TAC Projects" under the
[Confidential Computing Consoritium Charter](https://confidentialcomputing.io/wp-content/uploads/sites/85/2019/12/CCC_Charter.pdf).
They are eligible to receive ongoing support from the Consortium as determined by the Governing Board, and are expected to cross promote the Consortium along with their activities.

**Acceptance Criteria**

To graduate from Sandbox or Incubation status, or for a new project to join as an Graduation project, a project must meet the Incubation stage criteria plus:

 * Have a defined governing body of at least 5 or more members (owners and core maintainers, or similar technical role), of which no more than 1/3 is affiliated with the same employer. In the case there are 5 governing members, 2 may be from the same employer.
* Have a healthy number of committers from at least two organizations. A committer is defined as someone with the commit bit; i.e., someone who can accept contributions to some or all of the project.
* Explicitly define a project governance and committer process. This is preferably laid out in a GOVERNANCE.md file and references a CONTRIBUTING.md and OWNERS.md file showing the current and emeritus committers.
* Have a public list of project adopters or users for at least the primary repo (e.g., ADOPTERS.md or logos on the project website).
* Other metrics as defined by the applying Project during the application process in cooperation with the TAC.
* Receive a supermajority vote from the TAC to move to Graduation stage.

Projects can move directly from Sandbox to Graduation if they can demonstrate sufficient maturity and have met all requirements above.


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
   or addition to any project mentor(s))?  If nothing has changed
   significantly, there may be nothing to review here.

3. Review any budget allocations relevant to the project, and whether any
   adjustments are needed.
   
4. Review license scans provided by the Linux Foundation. Provide feedback
   on any outstanding issues and evaluate the scanning service from the
   project's perspective.

Projects are encouraged to proactively inform the TAC when something
changes that affects their submission template or Technical Charter (changing a License, security
reporting process, CoC, etc.), rather than waiting for the next annual review.

It is the responsibility of the project's [mentor](project-mentors.md) to help the project determine
what needs to be reviewed by the TAC, and keep the TAC informed.
