# CCC TAC Bi-Weekly Meeting Minutes: July 09, 2026

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

* Dan Middleton (DM) opened the call at 7:05 am PT and introduced Rene Kolga (RK) as the rotating chair.   
* RK welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* Michelle Roth (MR) recorded the meeting minutes.  
* RK reviewed the agenda.

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

* AMD \- **Nathaniel McCallum+**  / David Kaplan  
* Google \-  **Rene Kolga+** / Keith Moyer  
* Huawei \- Wu Yongzheng  
* Intel \- Scott Raynor  / Simon Johnson  
* Meta \- **Ahmed Magdy+**   
* Microsoft \- **Alec Fernandez+** / Simon Gallagher+  
* Nvidia \- **Fritz Alder+** / **Dan Middleton+**  
* TikTok \-  Mingshen Sun   
* Shielded Technologies \- Bob Blessing-Hartley

   " \+ " indicates attending

### Project Staff

* Michelle Roth (LF PMO)  
* John Mertic (LF PMO)

### Other Attendees

* Eric Hibbard (Samsung)  
* Gauthier Jolly (Canonical)   
* Ijlal loutfi (Canonical Group Limited)  
* Jordi Guijarro (OpenNebula Systems)  
* Julian Stephen (IBM)  
* Kevin Jones (1Claw)   
* Manu Fontaine (Hushmesh)   
* Marek Mahut (Input Output)   
* Mark Novak (JPMorgan Chase & Co)  
* Mary Lee (Microsoft)   
* Muhammad Usama Sarder (TU Dresden)   
* Ram Pai (IBM)   
* Rithikha Rajamohan (EQTY Lab)   
* Sakul Gupta (Micron)   
* Simon Frost (Arm)   
* Syama Poluri (Dell)   
* Yogesh Deshpande (Arm) 

## **Welcome New Community Members**

* Gauthier Jolly from Canonical introduced himself, noting his team works on Ubuntu image building for public clouds. Kevin Jones introduced himself as the founder of One Claw, an AI startup using Google Cloud confidential compute for accessing secrets from HSM modules and providing zero-trust architectures and guardrails for agentic workflows.

## **Old Business**

* RK reviewed the major points from the last TAC meeting, highlighting the vote for Blueprint C and the tech talk from AMD on portable machine imaging. 

## **Announcements**

* RK noted that the NIST IR 8320E (Initial Public Draft) is currently open for comment, with a fast-approaching deadline of July 13, 2026\.

## **CC Summit Takeaways**

* RK opened the floor for feedback on the recent Confidential Computing Summit. RK noted key themes included Agentic AI and Sovereign AI, as well as a notable presentation from Apple on Apple PC. Alec Fernandez (AF) noted the Linux Foundation is taking over the summit entirely from Opaque, and suggested setting up informal, in-person meetings for TAC members at future summits. Dan Middleton (DM) supported this and proposed scheduling a joint meeting with the outreach committee in January or February to influence the agenda early. Fritz Alder (FA) and Muhammad Usama Sardar (MUS) suggested structuring future summits to better balance marketing-focused talks with technical, problem-solving, and developer-oriented content.

## **New Business**

* Work on Blueprints A & B  
* TAC whitepaper

## **Annual Project Review: Veraison**

* Yogesh Deshpande (YD) presented an update on Project Veraison, noting the project remains in the incubation stage and recently hired a part-time project manager from the Linux Foundation to oversee governance. Over the last 12 months, the project added five new Rust repositories, achieved a fully functional CoServe demo with support from Linaro, Arm, and Oracle, and integrated with standards including CMW and EAT Media Types. Mark Novak (MN) emphasized that broad commercial adoption requires overcoming performance bottlenecks by shifting crypto processing to SmartNICs (which Nathaniel McCallum confirmed AMD is shipping in the second half of the year) and prioritizing multi-verifier support in software.  
* YD and Simon Frost (SF) addressed team updates, announcing that Thomas Fossati is changing organizations but intends to remain involved in the open source and standards community. SF announced his retirement from the core group, with Paul Howard taking over his team at Arm and YD inheriting leadership of the Veraison project.  
* Simon Frost (SF) noted that although there are some core team changes, Arm has a continued commitment to maintain the project. 

## **RATS Specification Implementation Discussion** 

* Nathaniel McCallum (NM) raised foundational questions regarding the RATS (Remote Attestation for Trust and Security) specification and CoRIM, asking whether attestation should provide supply chain transparency to the tenant or shift liability by asserting which firmware should be run. FA and DM agreed this philosophical discussion is highly relevant to the TAC. NM took an action item to create an architectural diagram independent of RATS terminology and schedule a long-form discussion with the group to map it back to RATS concepts.

## **Work in Progress**

* RK shared links to Blueprints A and B, requesting the community review them. DM requested that companies with real-world implementations contribute their specific patterns to the documents rather than repeating existing RATS language. AF reported having a solid start on the TAC white paper and requested a shared Google Doc for moderated review. Michelle Roth (MR) took the action to create the doc in the CCC space. DM also encouraged voting members to review a new GitHub issue regarding tying confidential computing with Agentic AI.

## **Additional Business**

* SIG Issue Appeal: MUS raised an appeal regarding the Attestation SIG chairs not creating a repository for an accepted formal analysis project. DM and FA responded that their understanding was the underlying project draft had been abandoned two years ago and was considered closed. MUS refuted this, citing a recent SIG meeting where the project scope was officially expanded. RK noted that time had expired for the meeting and the issue would require offline follow-up.

## **Future Business**

* Next meeting will be July 23, 2026  
* Rotating chair(s): Wu Yongzheng  
* Agenda: Occlum annual project review and Kernel SIG annual review

## **Action Items**

* Yogesh Deshpande to share the composite attester draft link and RATSD documentation.  
* Alec Fernandez to work with the PM to schedule a tech talk for Muhammad Usama Sardar.  
* Nathaniel McCallum to create an attestation model diagram and schedule a long-form discussion with the TAC to map it to RATS terminology.  
* Michelle Roth to create a shared Google Doc in the CCC space for the TAC white paper and share the link with Alec Fernandez.  
* TAC voting members to review the [GitHub issue](https://github.com/confidential-computing/governance/issues/380) on tying confidential computing with Agentic AI and provide input.  
* TAC members to review and contribute real-world implementation patterns to Blueprints A \[[link](https://docs.google.com/document/d/1yUhUqtXkyVYYRr5QGHGI2Wfz8O9HJy--Xf97zAX2ZKg/edit?tab=t.0)\] and B \[[link](https://docs.google.com/document/d/1dle-5JjgoIIsyrFvhbLD9rSh3ZWFEaN4Dbr7TFRbn9w/edit?tab=t.0)\].


---

