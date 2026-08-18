# Project 9 — Halcyon Benefits Group: AI Governance Program

**Building AI governance for a fictional employee-benefits administrator that deployed AI first and asked questions later.**

> ⚠️ **Fictional company and systems.** Halcyon Benefits Group does not exist. No AI system, vendor, or decision described here is real. Regulatory citations are for demonstration and are not legal advice. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

Halcyon administers health and retirement benefits for mid-market employers, including three EU-based client plans and a Dublin office. Over thirty months, business units deployed eight AI systems — a claims adjudication recommender, a member chatbot, a resume screener, an OCR pipeline, Microsoft Copilot, and others — with no governance function, no inventory, and no one accountable for asking whether each system should exist.

Then someone asked. This project is what the answer looked like.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [AI System Inventory](pdf/ai_system_inventory.pdf) | [xlsx](artifacts/ai_system_inventory.xlsx) | 8 AI systems plus 1 shadow-AI governance finding — EU AI Act tier, applicable deadline, NIST AI RMF profile, oversight mode, governance status |
| [AI Risk Assessment](pdf/ai_risk_assessment.pdf) | [xlsx](artifacts/ai_risk_assessment.xlsx) | 12 risks tagged to NIST AI RMF trustworthiness characteristics and AI 600-1 GenAI categories; inherent/residual scoring |
| [AI Control Crosswalk](pdf/ai_control_crosswalk.pdf) | [xlsx](artifacts/ai_control_crosswalk.xlsx) | 15 control objectives mapped across NIST AI RMF, ISO/IEC 42001, EU AI Act, and the existing NIST CSF program |
| [AI Governance Decision Memo](pdf/ai_governance_decision_memo.pdf) | [docx](artifacts/ai_governance_decision_memo.docx) | Three decisions for leadership: two high-risk systems and the governance function itself |

---

## The sequence, and why it's this order

**Inventory first.** You cannot govern what you haven't enumerated, and every AI governance framework presumes an inventory exists. Most organizations don't have one. Discovery here used procurement records, cloud consoles, CASB telemetry, and interviews — and the CASB data surfaced the finding nobody expected: 214 unique users hitting consumer AI endpoints in thirty days. That's row AI-009. It is deliberately **not** an AI system, and it is not classifiable under the AI Act. It's an enterprise governance finding, and an inventory that omits known unmanaged use isn't an inventory. So the count is eight systems plus one finding — a distinction the summary tab preserves rather than papering over.

**Classify by use, not by technology.** The same LLM is Minimal-risk drafting marketing copy and Limited-risk in a member-facing chatbot. EU AI Act tiering depends on what the system is *for* and who it affects.

Two systems raised high-risk questions, and they are not equally clear. The resume screener is unambiguous — Annex III(4)(a) names recruitment and candidate evaluation explicitly. ClaimSight is genuinely contested: Annex III(5)(a) covers essential public assistance benefits administered by *public authorities*, and (5)(c) covers risk assessment and pricing for life and health *insurance*. A private administrator adjudicating employer-sponsored claims sits between them. The inventory records it as **High-Risk (contested)** with the reasoning stated, pending a counsel determination.

Recording it that way is the point. Manufacturing false certainty about an unsettled classification is the more common failure, and it is worse — it produces confident plans built on an answer nobody actually has.

**Assess against the framework's own structure.** Every risk is tagged to the NIST AI RMF trustworthiness characteristic it threatens. That's not decoration: the Trustworthiness Coverage tab shows *which characteristics have no risks* — and a register with zero Safety risks and four Transparency risks tells you where the assessors looked, which is different from where the exposure is.

**Map controls once, evidence four ways.** One fairness-testing program closes an AI RMF subcategory, an ISO 42001 Annex A control, an EU AI Act article, and a risk register item. The crosswalk also has an honest column: where the AI control has no NIST CSF equivalent, it says so. The existing security program was not designed for these risks, and pretending otherwise is how gaps persist.

**Then decide.** Three risks stayed Critical after every planned control was applied. That's the signal that a control can't fix them — a business decision has to. The memo is that decision.

---

## The finding worth reading

**ClaimSight's adjuster override rate is 3%.**

The system was designed with a human-in-the-loop: an adjuster confirms every recommendation before it takes effect. That's the control everyone pointed to. But at a 3% override rate, the human is ratifying, not reviewing. Automation bias has converted a human-in-the-loop into a rubber stamp, and nobody noticed because "there's a human" sounded like enough.

The EU AI Act treats human oversight as a required control for high-risk systems, not a classification-reducing factor. Nominal oversight doesn't satisfy it. That single metric reframed the entire ClaimSight discussion.

## The decision worth reading

**Option B, not Option A.** The obvious answer for ClaimSight is "build full EU conformity." The memo recommends carving the EU plans out to manual adjudication first, running fairness testing on the US deployment, and deciding at 90 days whether to commit to conformity.

The reasoning is about reversibility. Carving out is cheap and undoable. A year of conformity work is neither — and if the fairness testing reveals the model needs rebuilding, that year was wasted. Take the reversible action, learn, then commit.

Also worth noting: **the memo explicitly does not recommend halting AI adoption.** Six of nine systems are fine. The purpose of governance is to say yes with confidence, not no by default.

---

## On the timeline — and why the deferral is not relief

The Digital Omnibus on AI (Regulation (EU) 2026/1744) was published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026, six days before the AI Act's original high-risk deadline. Standalone Annex III high-risk obligations now apply from 2 December 2027; embedded high-risk systems under Annex I from 2 August 2028.

**The deferral is selective, and that turns out to be the interesting part.** Article 50 transparency duties were expressly *not* deferred and applied from 2 August 2026. Neither were the Article 5 prohibitions or the GPAI provider obligations.

So the obligation Halcyon has actually missed is the cheapest one in the entire register — telling members they're talking to a chatbot. AIR-007 is a low-effort UX change, and it's the only item with a deadline in the past. Everything expensive got sixteen more months; the one thing that was trivially fixable was already due.

The deeper point is in Section 2 of the memo: deadlines govern *enforcement*, not *harm*. AIR-001 — whether ClaimSight encodes historical bias into denial recommendations — has no compliance date attached. The model either discriminates or it doesn't, and nobody currently knows. A member denied benefits in 2026 is not helped by a 2027 deadline.

Writing governance plans against a regulatory target that moved mid-project is the actual job in 2026. This project is built to show that.

---

## Frameworks applied

NIST AI RMF 1.0 · NIST AI 600-1 (Generative AI Profile) · ISO/IEC 42001:2023 · EU AI Act (Regulation 2024/1689) · NYC Local Law 144 · NIST CSF 2.0 (existing program) · OWASP LLM Top 10 · MITRE ATLAS

## Accuracy note

Regulatory articles, ISO clause numbers, and NIST subcategory references were current as of August 2026 and reflect the AI Act as amended by Regulation (EU) 2026/1744 and should be verified against published texts before reliance. This is a portfolio artifact, not legal advice, and real EU AI Act classification requires counsel.

---

## Companion projects

This project extends the portfolio's commercial GRC work (Meridian, Northbridge) into AI-specific risk, and applies the same discipline as the federal packages (Cascade, Northgate): inventory the scope, assess against a defined framework, trace controls to evidence, and make a defensible decision.
