# CCC TAC Bi-Weekly Meeting Minutes: July 23, 2026

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

* Dan Middleton (DM) opened the call at 7:05 am PT.  
* DM welcomed the members of the TAC and reviewed the values of the CCC and the antitrust policy of the Linux Foundation  
* Michelle Roth (MR) recorded the meeting minutes.  
* DM reviewed the agenda.

## **Attendance**

Per the \[charter\](https://charter.confidentialcomputing.io), all \[CCC Premier members\]([https://confidentialcomputing.io/members/)](https://confidentialcomputing.io/members/\)) receive one vote on the TAC. Quorum for votes is at least 50% of voting members present.

### Voting Members of the TAC

- [ ] Ahmed Magdy (Meta)  
- [x] Alec Fernandez (Microsoft)  
- [ ] Bob Blessing-Hartley (Shielded Technologies)   
- [ ] Fritz Alder (NVIDIA)   
- [ ] Mingshen Sun (TikTok)   
- [ ] Nathaniel McCallum (AMD)  
- [x] Rene Kolga (Google)  
- [x] Scott Raynor (Intel)  
- [x] Yongzheng Wu (Huawei) 

### Alternate Voting Members

- [x] Dan Middleton (NVIDIA, TAC Chair)   
- [ ] David Kaplan (AMD)   
- [ ] Keith Moyer (Google)   
- [x] Simon Gallagher (Microsoft)   
- [ ] Simon Johnson (Intel) 

### Project Staff

- [ ] Ben Sternthal (LF PMO)   
- [x] Michelle Roth (LF PMO)  
- [x] Mike Bursell (CCC ED) 

### Other Attendees

* Hongliang Tian Tate (Occlum Project)   
* Ijlal Ioutfi (Canonical)   
* Jens Alberts (FrOntierX)   
* Jeremy Powell (AMD)  
* Julian Stephen (IBM)   
* Manu Fontaine (Hushmesh)   
* Mona Vij (Intel)   
* Ofir Azoulay-Rozanes (Anjuna Security)   
* Ram Pai (IBM)   
* Rithikha Rajamohan (EQTY Lab)   
* Syama Poluri (Dell) 


## **Welcome New Community Members**

* There were no new community member announcements.

## **Old Business**

* DM reviewed the major points from the last TAC meeting, highlighting the Veraison project update and takeaways from the Confidential Computing Summit.

## **Announcements**

* Rene Kolga (RK) brought up a request for public review of a MITRE continuous attestation paper. Jens Albers (JA) noted the framework is open for a 7-week public review and offered to coordinate a presentation with Dr. Spina from MITRE and Jason from Invari for the next TAC meeting.  
* Request for public review of Mitre continuous attestation paper: [https://www.mitre.org/news-insights/news-release/mitre-and-industry-collaborators-release-draft-framework-continuous](https://www.mitre.org/news-insights/news-release/mitre-and-industry-collaborators-release-draft-framework-continuous) 

## **New Business**

* Occlum Project Update: Hongliang Tian (HT)  
  * Hongliang Tian (HT) presented the annual review for the Occlum project. HT noted that the project is nearing its end of life due to decreasing developer interest in enclave libraries. HT introduced its successor, the Asterinas kernel, a new general-purpose OS kernel written in Rust that supports over 240 Linux syscalls and is designed to provide greater memory safety. Mona Vij (MV) questioned the differences in threat models between normal VMs and CVMs, pointing out that Linux was originally designed by trusting the host and might not be ideal for CVM environments. HT explained that Asterinas uses a frame kernel architecture that only trusts the OS framework, compiler, CPU, and memory, and explicitly distrusts peripheral devices to prevent Iago attacks. DM invited HT to consider proposing Asterinas as a sponsored project within the CCC for broader visibility, and HT agreed to consider it.  
  * DM made a motion to move Occlum to Emeritus. All TAC members present were in favor, so the motion passed.   
* Blueprint Papers Status: Alec Fernandez (AF) asked for a status update on the blueprint papers. DM confirmed that the "3 degrees" paper is approved and online. MR noted that the Blueprint C paper has been approved but is waiting on final author attribution approval from Mingshen Sun before it can be published.  
* TAC whitepaper update: Alec Fernandez (AF)  
  * Alec Fernandez (AF) reviewed the primary TAC white paper, noting it has aged well over 5 years but requires consistency updates. AF proposed explicitly listing "attestability" as a required property of a TEE, amending older language that considered it optional. AF also presented proposed diagrams to represent stack architecture in public cloud environments, including multiple hardware components. Syama Poluri (SP) and Ram Pai (RP) suggested focusing the text on functional capabilities—specifically components that have DMA access to T-memory or perform computations on behalf of the TEE—rather than specific device categories like GPUs or NICs. AF agreed to incorporate this functional definition. AF will apply his changes to version 1.3 of the document and circulate a shared link for the TAC to review over the next two weeks.

## **Work in Progress**

* Covered above. 

## **Future Business**

* Next meeting will be August 6, 2026  
* Rotating chair(s): Scott Raynor

## **Action Items**

* Jens Albers: Coordinate a presentation of the MITRE continuous attestation framework with Dr. Spina and Jason for the next TAC meeting (August 6).  
* Hongliang Tian: Consider proposing the Asterinas kernel as a Confidential Computing Consortium project and follow up with Dan Middleton.  
* Michelle Roth: Verify the final author attribution approval from Mingshen Sun for the Blueprint C paper so it can be published.  
* Alec Fernandez: Merge proposed white paper edits into version 1.3, create a shared document, and email the link to the TAC for review.  
* All TAC members: Review Alec's updated draft of the primary TAC white paper and provide comments before the August 6 meeting.


---

