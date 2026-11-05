# **CCC TAC Bi-Weekly Meeting Minutes: October 29, 2026**

## **7 \- 9am PDT**

## **Links**

> * **Code of Conduct**: [code-of-conduct.confidentialcomputing.io](https://code-of-conduct.confidentialcomputing.io/)  
> * **CCC Charter**: [charter.confidentialcomputing.io](https://charter.confidentialcomputing.io/)  
> * **LF Training course on DEI**: [Inclusive Open Source Community Orientation (LFC102) (free)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/)  
> * **Declared project dependencies**: [Google Sheets](https://docs.google.com/spreadsheets/d/1UKnbbGWXYLjnPZsox3zmYo59nv3XSXjePfas5E2fER0/edit#gid=0)  
> * **CCC YouTube**: [youtube.confidentialcomputing.io](https://youtube.confidentialcomputing.io/)  
> * **LFX**: [lfx.linuxfoundation.org](https://lfx.linuxfoundation.org/)  
> * **Join the CCC**: [join.confidentialcomputing.io](https://join.confidentialcomputing.io/)  
> * **Contact the CCC**: [confidentialcomputing.io/contact-us/](http://confidentialcomputing.io/contact-us/)  
> * **Zoom for CCC TAC meetings**: [https\://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e](https://zoom-lfx.platform.linuxfoundation.org/meeting/94618773737?password=4b2a5cdf-685a-4ea3-822d-24ff7ddab72e)  
> * **Recording**: [YouTube](https://www.youtube.com/watch?v=SlwH8RKsYkg)

## **Agenda and Minutes**

> * Dan Middleton (DM) opened the call and reviewed the values of the CCC and the antitrust policy of the Linux Foundation.  
> * DM noted there was nothing on the agenda requiring a vote this meeting.  
> * DM reviewed the agenda: storage/confidential compute (Chandra Nelogal), Confidential Inference Governance doc proposal (Mark Novak), VirTEE project annual review (Tyler Fanelli), Attestation SIG annual review (Jim Beaney).  
> * No formal roll call/quorum count was recorded in the transcript this meeting.

## **Attendance**

Per the [charter](https://charter.confidentialcomputing.io), all [CCC Premier members](https://confidentialcomputing.io/members/) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### **Voting Members of the TAC**

☐ Ahmed Magdy (Meta)  
☐ Alec Fernandez (Microsoft)  
☐ Bob Blessing-Hartley (Shielded Technologies)  
☐ Fritz Alder (NVIDIA)  
☐ Mingshen Sun (TikTok)  
☐ Nathaniel McCallum (AMD)  
☑ Rene Kolga (Google)  
☑ Scott Raynor (Intel)  
☐ Yongzheng Wu (Huawei)  
☐ Caihua Li (Volcano Engine)  
☐ Alpha Compute (rep TBD)

### **Alternate Voting Members**

☑ Dan Middleton (NVIDIA, TAC Chair)  
☐ David Kaplan (AMD)  
☐ Keith Moyer (Google)  
☑ Simon Gallagher (Microsoft)  
☐ Simon Johnson (Intel)

### **Project Staff**

☐ Ben Sternthal (LF PMO)  
☑ Michelle Roth (LF PMO)  
☑ Mike Bursell (CCC ED)

### **Other Attendees**

☑ Chandra Nelogal  
☑ Daniel Masny (Meta)  
☑ David Dooling  
☑ Edward Boggis-Rolfe  
☑ James "Jim" Beaney (Intel)  
☑ Jens Albers (Fr0ntierX Inc)  
☑ Jeremy Powell (AMD)  
☑ Manu Fontaine (Hushmesh)  
☑ Mark Gentry  
☑ Mark Novak (JPMorgan Chase & Co)  
☑ Rachel Wan (CCC Outreach)  
☑ Ram McNaught (Qlad)  
☑ Ram Pai (IBM)  
☑ Sakul Gupta  
☑ Steven Bellock (NVIDIA)  
☑ Syama Poluri  
☑ Tom Jones  
☑ Tyler Fanelli  
☑ Yu Yoshida (Superasystem)

## **Welcome New Community Members**

> * Ram McNaught (Qlad): Introduction noted joining about 3 months ago, learning confidential computing.  
> * Daniel Masny (Meta): Introduction noted work as a cryptographer on confidential compute at Meta, with interest in more rigorous industry standards and protocols.  
> * Yu Yoshida (Superasystem): Introduction noted joining from Japan with Superasystem, a new startup member, with interest in post-quantum topics.

## **Old Business**

> * DM noted the 2027 TAC budget request was presented to the board for consideration (decision pending).  
> * The Agentic AI white paper is finalized and has gone to LF Creative for layout/PDF production ahead of website publication.  
> * Follow-up on the proposed PQC SIG (raised previously by Rachel Wan from Google): DM reiterated the group needs 1-3 concrete deliverables from interested participants before a SIG is formalized. Rene Kolga (RKo) agreed to follow up with Rachel.

**Announcements**

> * No TAC meetings over the U.S. Thanksgiving holiday or Christmas Eve.

## **New Business**

> * **Confidential Compute for Storage Devices** — Chandra Nelogal (CN)  
  * CN presented an overview of applying confidential computing concepts to storage devices, noting limited current traction but growing industry interest, particularly driven by GPU companies needing isolated tenant data access. CN's presentation outlined prerequisites: attestation over PCIe (CMA, DOE, SPDM), secure session establishment, and the PCIe TDISP confidential-compute extension.  
  * CN and Mike Bursell (MB) clarified the discussion was specifically about component-level (CC) attestation. CN identified a gap: PCIe specifications define topology for trusted device instances and encryption, but there is no established industry mechanism for mapping virtual functions to backend storage ranges.  
  * DM and CN also discussed key-management challenges for data persisting beyond a confidential VM's lifetime (citing Opal and KeeperIO as partial existing mechanisms); Daniel Masny (DMy) distinguished two separate problems — in-lifetime CVM data access vs. persistent post-lifetime access — noting Meta has specific use cases for the latter.  
  * CN's presentation, covering re-authentication, logical block access, data migration, and ISO 27040 requirements, was cut short for time and will resume in two weeks following CN's return from vacation.  
> * **Confidential Inferencing Governance Pattern** — Mark Novak (MN)  
  * MN presented a new governance pattern for confidential inferencing in ML, part of ongoing GRC SIG work on open-source governance patterns (building on prior proxy/gateway governance patterns).  
  * MN requested feedback on the pull request and noted the GRC SIG may pause after two more patterns are completed. MB encouraged everyone to review MN's proposal and pointed to the Slack channel/mailing list for ongoing discussion.  
> * **CCC Attestation SIG Update** — James Beaney (JB)  
  * JB (introduced as "Jim," co-chair of the Attestation SIG) gave a year-in-review update: the SIG tracks 13 open issues across six active tracks, including information/data models, secure channel establishment, and emerging standards, with CoRIM (Confidential Operating Environment Reference Information Model) highlighted as a converging industry standard.  
  * MB asked the SIG to consider writing a blog post on the past year's work for the CCC blog; JB agreed to take it back to the SIG.  
> * **VirTEE Project Update** — Tyler Fanelli (TF)  
  * TF gave an update on the VirTEE (Verdi) Project, maintained by TF for several years: the underlying tooling remains functional and is still used by other projects (e.g., Confidential Containers, Coconut SVSM), but active stewardship has dropped significantly as maintainers moved to other work — particularly affecting TDX-related tooling updates.  
  * AMD continues to provide support; Intel engagement has decreased. TF indicated openness to more Intel engagement or additional contributors. MB offered to follow up with TF on vulnerability-management options for the project.

## **Work in Progress**

> * PQC SIG proposal: awaiting 1-3 concrete deliverables from Rachel Wan (Google) via Rene Kolga (RKo) before a formal SIG proposal.  
> * Chandra Nelogal's (CN) storage confidential-compute requirements discussion to resume in two weeks.

## **Future Business**

> * Next meeting will be November 12, 2026\.  
> * Rotating chair(s): Simon Gallagher, as Nathaniel McCallum may be unavailable.  
> * Edward Boggis-Rolfe (EBR) to present on a high-performance RPC solution that also supports confidential computing.  
> * Tech talk: Dan Middleton or an NVIDIA colleague, on a new "Confidential Bare Metal" computing mode.

## **Action Items**

> * Rene Kolga: Follow up with Rachel Wan (Google) to get 1-3 concrete PQC SIG deliverables.  
> * Chandra Nelogal: Share email for offline input/feedback on storage CC requirements.  
> * Daniel Masny: Reach out to Ahmed Magdy (Meta) to review Mark Novak's GRC SIG PR on confidential inferencing governance.  
> * Mark Novak: Email confidential-inferencing governance slides to the TAC mailing list.  
> * Mark Novak: Bring the TACRA / trustworthy workload identity discussion to the Attestation SIG.  
> * James Beaney: Take request back to Attestation SIG to consider a blog post on the past year's work.  
> * Dan Middleton: Post VirTEE project repo link and Intel-engagement ask to the TAC chat.  
> * Tyler Fanelli: Provide email in chat for offline VirTEE/Intel-engagement follow-up.  
> * Mike Bursell: Follow up with Tyler Fanelli on vulnerability-management options for VirTEE.  
> * Dan Middleton: Coordinate with Simon Gallagher to chair the November 12, 2026 meeting.

> 