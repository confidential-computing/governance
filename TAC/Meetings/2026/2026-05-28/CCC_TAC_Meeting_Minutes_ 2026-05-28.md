# CCC TAC Bi-Weekly Meeting Minutes: May 28, 2026

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

* Dan Middleton (DM) opened the call at 7:05 am PT  
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* Michelle Roth (MR) created meeting minutes.  
* DM reviewed the agenda.

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

* AMD \- Nathaniel McCallum+  / David Kaplan  
* Google \-  Rene Kolga / Keith Moyer  
* Huawei \- Wu Yongzheng  
* Intel \- Scott Raynor+  / Simon Johnson  
* Meta \- Ahmed Magdy   
* Microsoft \- Alec Fernandez+ / Simon Gallagher+  
* Nvidia \- Fritz Alder+ / Dan Middleton+  
* TikTok \-  Mingshen Sun   
* Shielded Technologies \- Bob Blessing-Hartley

   " \+ " indicates attending

### Other Attendees

* Cameron Dennis (Near AI)  
* Catalin Sandu (Google)   
* Caroline Perez-Vargas (Microsoft)   
* Cedric Fournet (Unaffiliated)   
* Chris Ramming (Unaffiliated)  
* Eric Hibbard (Samsung)  
* Henk (Unaffiliated)   
* Ijlal loutfi (Canonical Group Limited)  
* Jens Albers (Fr0ntierX)  
* Jeremy Powell (AMD)  
* Jiewen Yao (Intel)  
* Jordi Guijarro (Unaffiliated)  
* Mark Novak (JPMorgan Chase & Co)  
* Michelle Roth (LF PMO)   
* Mike Bursell (Confidential Computing Consortium)  
* Ofir Azoulay-Rozanes (Anjuna)  
* Ram Pai (IBM)  
* Rithikha Rajamohan (EQTY Lab)   
* Sakul Gupta (Micron)   
* Tom Jones (VeriClouds)

## **Welcome New Community Members**

* Cédric Fournet introduced themselves, noting their work on CCF and co-authoring the Skit Architecture at the IETF.  
* Cameron Dennis introduced themselves, sharing their work at Near AI building private inference networks on GPUs and the Ironclaw secure agent framework.

## **Meeting Minute Approval & Old Business**

* Ijlal loutfi noted no progress or discussions have happened on the TAC white papers. Cédric Fournet will check with Alec regarding the status of the white paper.  
* Dan Middleton (DM) noted that the Attestation SIG needs to be rescheduled after missing their slot at the previous meeting.  
* Ming Shen is scheduled to be the next rotating chair.  
* The team discussed email communication issues causing some members to miss messages.  
* Simon agreed to serve as an alternate voting member for Alec. Michelle committed to updating meeting slides to reflect this and catching up on the minutes for the last three TAC meetings.

## **Announcements**

* DM mentioned the upcoming CC Summit is transitioning from being hosted by Opaque to being jointly owned with the Linux Foundation this year, and will be fully LF-owned going forward. Mike Bursell (MB) clarified that the LF ownership of the summit is not yet definitely confirmed.

## **Project Updates**

* **SPDM Core Project Annual Review**: Jiewen Yao (JY) presented an annual update on the pure Rust version of the SPDM Library (SPDM RS).  
* The project now successfully implements the DMTF SPDM 1.4 specification, notably adding support for Post-Quantum Cryptography (PQC) using the AWS LC crypto binding for ML-DSA and ML-KEM algorithms.  
* JY noted that SPDM key exchange is officially approved in the FIPS 140-3 implementation guide.  
* The project is transitioning to new formal verification tools (Kani and Verus) and is seeing new adoption use cases, including the Migration TD project for live migration.  
* JY requested budget for a third-party penetration test. DM explained that due to recent consortium deficit spending, TAC funding for this was not approved in the last fiscal cycle.

## **Collaborative Clean Room Blueprint Vote**

* DM initiated a call for votes on the Collaborative Clean Room blueprint (Blueprint C), co-authored by Renee and Ming Shen.  
* Current voting status: Google, TikTok, and NVIDIA have voted to approve.  
* Scott Raynor and Nathaniel McCallum noted they missed the email thread and will locate it to cast their votes.

## **GRC SIG Update**

* Mark Novak (MN) presented an update on the Governance, Risk, and Compliance (GRC) SIG, focusing on threat-model-informed governance to unblock enterprise adoption.  
* MN highlighted three published governance patterns and a newly submitted pull request for "proxies and gateways" (Trust Intermediaries).  
* MN noted that sparse attendance from end-user organizations has made progress challenging. He emphasized that the SIG's future work on confidential inferencing and training requires active engagement from deployers who face regulatory hurdles, rather than just technology suppliers.  
* Chris Ramming agreed on the need for targeted recruitment of end-user customers to participate in governance discussions.  
* Eric Hibbard, chair of the US Mirror Committee to ISO SC27, offered his standards expertise and noted NIST's involvement in related standards editing.  
* Tom Jones raised questions about tracking data access on edge devices for regulatory purposes. MN and Henk discussed the technical boundaries of preventing out-of-band data capture (e.g., screenshots) and how confidential computing handles device association.

## **Action Items**

* **Cédric Fournet**: Check with Alec regarding the status/update of the TAC white paper and report back.  
* **Michelle**: Update the TAC slides/records to reflect Simon as alternate voting member for Microsoft, and complete the minutes for the last three TAC meetings.  
* **Simon**: Review and, if appropriate, update the minutes for recent TAC meetings. Sync with Alec about alternate voting responsibilities.  
* **Voting members (Scott, Nathaniel, Simon, etc.)**: Review and vote on the Collaborative Clean Room blueprint (Blueprint C) via email or web interface.  
* **Mark Novak**: Monitor and respond to comments on the GRC SIG's "proxies and gateways" governance pattern pull request on GitHub.  
* **Ming Shen**: As next co-chair, add Mark Novak's GRC governance pattern review to the agenda for the next TAC session.  
* **All TAC members**: Review the GRC SIG's "proxies and gateways" governance pattern document and provide comments/questions on GitHub. Continue offline review of Blueprint documents A and B.  
* **Mike Bursell**: Continue/step up outreach to recruit end-user/adopter members (especially regulated industry representatives) to the CCC/TAC for GRC and related topics.  
* **Eric Hibbard**: Consider proposing dates for upcoming storage-related discussions (e.g., TDISP, TDS, device association) in TAC meetings and share relevant links/resources.

---

