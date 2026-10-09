# Project 9: Rockledge Benefits Administrators, AI Governance Program

**AI governance for a fictional employee-benefits administrator that deployed AI first and asked questions later.**

> ⚠️ **Fictional organization. Created for portfolio demonstration purposes.** Rockledge Benefits Administrators does not exist. No AI system, vendor, or decision described here is real. Regulatory citations are for demonstration and are not legal advice. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

Rockledge administers health and retirement benefits for mid-market employers, including three EU-based client plans and a Dublin office. Over thirty months, business units deployed eight AI systems (a claims adjudication recommender, a member chatbot, a resume screener, an OCR pipeline, Microsoft Copilot, and others) with no governance function, no inventory, and nobody accountable for asking whether each system should exist. This project starts at the point someone did ask.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [AI System Inventory](pdf/ai_system_inventory.pdf) | [xlsx](artifacts/ai_system_inventory.xlsx) | 8 AI systems plus 1 shadow-AI governance finding, with EU AI Act tier, applicable deadline, NIST AI RMF profile, oversight mode, and governance status |
| [AI Risk Assessment](pdf/ai_risk_assessment.pdf) | [xlsx](artifacts/ai_risk_assessment.xlsx) | 13 risks tagged to NIST AI RMF trustworthiness characteristics and AI 600-1 GenAI categories, with inherent/residual scoring |
| [AI Control Crosswalk](pdf/ai_control_crosswalk.pdf) | [xlsx](artifacts/ai_control_crosswalk.xlsx) | 16 control objectives mapped across NIST AI RMF, ISO/IEC 42001, the EU AI Act, and the existing NIST CSF program |
| [AI Governance Decision Memo](pdf/ai_governance_decision_memo.pdf) | [docx](artifacts/ai_governance_decision_memo.docx) | Three decisions for leadership: two high-risk systems and the governance function itself |

---

## The sequence

**Inventory first.** Every AI governance framework assumes an inventory exists, and most organizations do not have one. Discovery here used procurement records, cloud consoles, CASB telemetry, and interviews. The CASB data produced the unexpected result: 214 unique users reached consumer AI endpoints in thirty days. That is row AI-009. It is an enterprise governance finding, not an AI system, and it cannot be classified under the AI Act, but leaving known unmanaged use out of the inventory would understate the exposure. The count is eight systems plus one finding, and the summary tab keeps the two separate.

**Classify by use.** The same LLM is Minimal-risk when it drafts marketing copy and Limited-risk in a member-facing chatbot. EU AI Act tiering depends on what the system is for and who it affects.

Two systems raised high-risk questions, and they are not equally clear. The resume screener is: Annex III(4)(a) names recruitment and candidate evaluation. ClaimDesk is contested. Annex III(5)(a) covers essential public assistance benefits administered by public authorities, and (5)(c) covers risk assessment and pricing for life and health insurance. A private administrator adjudicating employer-sponsored claims sits between them, so the inventory records it as High-Risk (contested), states the reasoning, and refers the question to counsel. A confident classification here would produce plans built on an answer nobody has.

**Assess against the framework's structure.** Every risk is tagged to the NIST AI RMF trustworthiness characteristic it threatens, and the Trustworthiness Coverage tab counts them. It shows no risks under Safe and four under Accountable & Transparent, which says something about where the assessment looked as well as where the exposure is.

**Map controls once.** One fairness-testing program can close an AI RMF subcategory, an ISO 42001 Annex A control, an EU AI Act article, and a risk register item. Where an AI control has no NIST CSF equivalent, the crosswalk leaves the cell as a dash; the existing security program was not built for these risks. The newest objective covers reassessment when a system's use changes, prompted by AIR-013: the actuarial model would fall under Annex III(5)(c) if anyone reused it to price individual members.

**Then decide.** Three risks stayed Critical after every planned control was applied. Controls cannot reduce those; they need a business decision, and the memo records it.

---

## The finding worth reading

ClaimDesk's adjuster override rate is 3%.

The system was designed with a human in the loop: an adjuster confirms every recommendation before it takes effect, and that was the control everyone pointed to. At a 3% override rate the adjuster is ratifying the model's output. Automation bias has turned the review step into a formality, and it went unnoticed because the presence of a human sounded like enough. The EU AI Act requires effective human oversight for high-risk systems, so this one number changed the ClaimDesk discussion.

## The decision worth reading

The obvious answer for ClaimDesk is to build full EU conformity. The memo recommends carving the EU plans out to manual adjudication first, running fairness testing on the US deployment, and deciding at 90 days whether to commit to conformity.

The reasoning is reversibility. Carving out is cheap and can be undone; a year of conformity work cannot. If fairness testing shows the model needs rebuilding, that year would have been spent on the wrong model.

The memo does not recommend halting AI adoption. Six of the nine inventory entries are appropriately governed or on track.

---

## On the timeline

The Digital Omnibus on AI (Regulation (EU) 2026/1744) was published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026, six days before the AI Act's original high-risk deadline. Standalone Annex III high-risk obligations now apply from 2 December 2027, and embedded high-risk systems under Annex I from 2 August 2028.

The deferral is selective. Article 50 transparency duties were not deferred and applied from 2 August 2026, and neither were the Article 5 prohibitions or the GPAI provider obligations.

The obligation Rockledge has actually missed is the cheapest one in the register: telling members they are talking to a chatbot. AIR-007 is a small UX change, and its legal deadline and remediation target are different dates. As of this review on 2026-09-14, the register shows passed remediation targets for AIR-005 and AIR-007 (2026-08-15) and for AIR-010 and AIR-012 (2026-08-31), with no closure evidence or reason for the miss recorded. The expensive work got sixteen more months; the easy fix was already due.

Section 2 of the memo makes the broader point. A deadline determines when enforcement can begin, not whether harm is occurring. AIR-001 (whether ClaimDesk encodes historical bias into denial recommendations) has no compliance date, and nobody yet knows whether the model discriminates. A member denied benefits in 2026 is not helped by a 2027 deadline.

---

## Frameworks applied

NIST AI RMF 1.0 · NIST AI 600-1 (Generative AI Profile) · ISO/IEC 42001:2023 · EU AI Act (Regulation 2024/1689) · NYC Local Law 144 · NIST CSF 2.0 (existing program) · OWASP LLM Top 10 · MITRE ATLAS

## Accuracy note

Regulatory articles, ISO clause numbers, and NIST subcategory references were current as of August 2026, reflect the AI Act as amended by Regulation (EU) 2026/1744, and should be checked against the published texts before reliance. This is a portfolio artifact, not legal advice; real EU AI Act classification requires counsel.

---

## Companion projects

This project extends the commercial GRC work (Tavares, Pinecastle) into AI-specific risk, using the same sequence as the federal packages (Tailspin, Salgado): define the scope, assess against a stated framework, and trace controls to evidence.

## Open review note

AI-009's inventory entry describes its data inputs as unknown or likely, while AIR-010 states member-data entry more firmly. Both are kept: the inventory records what discovery could confirm, and the risk assessment states the exposure scenario being evaluated. AIR-010 is not evidence that the inventory's uncertainty has been resolved; that would take evidence of the data actually submitted.

## Resolved review notes

The inventory's Classification Method B8 previously described the Digital Omnibus deferral as proposed, while the inventory header, the Applicable Deadline column, and this README described it as enacted. B8 now states the enacted position: Regulation (EU) 2026/1744 in force 27 July 2026, standalone Annex III obligations deferred to 2 December 2027, and the Article 50, Article 5, and GPAI obligations that were not deferred.
