# Project 2 — Cascade Civic Systems, Inc. / GrantBridge

**A FedRAMP Moderate (Rev5) authorization package for a fictional government grants management SaaS.**

> ⚠️ **Fictional company and system.** Cascade Civic Systems and the GrantBridge platform do not exist. No FedRAMP authorization, 3PAO assessment, or incident described here occurred. Documents carry CUI markings only to demonstrate correct handling conventions — no actual CUI is present. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

GrantBridge is a multi-tenant SaaS platform for federal, state, and local agencies administering the grants lifecycle — opportunity publication, applicant intake, eligibility review, award issuance, subrecipient monitoring, disbursement, and closeout.

It handles applicant PII, taxpayer identification numbers, and financial disbursement data. It runs on AWS GovCloud under that provider's FedRAMP High P-ATO. It is pursuing an **agency ATO** at the **Moderate** baseline with a named sponsoring agency.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [System Security Plan](pdf/system_security_plan.pdf) | [docx](artifacts/system_security_plan.docx) | Categorization, boundary, control approach, ConMon strategy |
| [Security Controls Traceability Matrix](pdf/sctm_control_matrix.pdf) | [xlsx](artifacts/sctm_control_matrix.xlsx) | 30 controls, 15 families, method and result per control |
| [Security Assessment Report](pdf/security_assessment_report.pdf) | [docx](artifacts/security_assessment_report.docx) | 8 findings, condition/criteria/cause/effect |
| [Plan of Action & Milestones](pdf/poam.pdf) | [xlsx](artifacts/poam.xlsx) | 8 items, milestones, live overdue calculation |
| [Customer Responsibility Matrix](pdf/customer_responsibility_matrix.pdf) | [xlsx](artifacts/customer_responsibility_matrix.xlsx) | Shared responsibility, agency onboarding checklist |
| [IR Tabletop After-Action Report](pdf/ir_tabletop_after_action_report.pdf) | [docx](artifacts/ir_tabletop_after_action_report.docx) | Exercise design, timeline, findings, POA&M disposition |

---

## The chain of custody

The RMF process is a chain. A control deficiency has to be traceable from the SSP, through the independent assessment, to a remediation plan with a date and an owner. If that chain breaks anywhere, the Authorizing Official cannot make an informed risk decision.

Follow one deficiency all the way through:

```
SCTM          RA-5, SI-2 marked "Other Than Satisfied"
                    ↓
SAR           FIND-001 — 14 High vulns open past the 30-day window,
              longest at 94 days. Cause: no automated SLA escalation.
                    ↓
POA&M         V-001 — 3 milestones, owner, target 2026-06-30,
              risk rating High
```

Every "Other Than Satisfied" control in the SCTM carries a POA&M ID. Every POA&M item cites the same NIST controls. Every SAR finding names both. Eight deficiencies, eight POA&M items, no orphans.

---

## How to read this

### Start with the SSP — categorization and boundary

RMF starts by categorizing the system. Working through the information types in SP 800-60 and applying the **high water mark**, GrantBridge lands at Moderate for confidentiality, integrity, and availability. That single decision selects the entire control baseline, which is why the rationale is documented rather than just the result.

Then the **authorization boundary** — the part most people underestimate. The SSP documents what's inside, what's outside, and *why*. AWS GovCloud infrastructure is outside and inherited. Corporate IT is outside because no federal data touches it.

Draw the boundary too small and you're hiding scope, which an assessor will find. Too large and you're assessing components you don't control and can't remediate.

### Then the SAR — specifically FIND-001

Each finding follows **condition / criteria / cause / effect**, then evidence reviewed, recommendation, and management response.

The **cause** section is the one most people skip, and it's the one that determines whether the fix holds. FIND-001's condition is "14 High vulnerabilities open past 30 days." The cause isn't "they were slow" — it's that the vulnerability pipeline created tickets but had no automated escalation when an SLA was breaching, so security findings competed with feature work in sprint planning with nothing enforcing the deadline.

A finding that stops at "they were late" produces a remediation that fails again next quarter. A finding that identifies the missing enforcement mechanism produces a fix that holds. The recommendation follows from the cause: automated escalation at 15 and 25 days, not "remediate faster."

**Also read FIND-007.** The weekly log review probably *was* happening — but no artifact recorded it. Technically nothing was misconfigured. The control is still Other Than Satisfied, because a control you can't evidence is a control you can't assess.

### Then the Customer Responsibility Matrix

This is the one that matters most in practice. **FedRAMP authorizes the provider's controls. It does not make the customer agency compliant.**

Twenty controls split into CSP / Shared / Customer / Inherited. Nine are **Shared** — meaning neither party is compliant unless both do their part. Seventeen require agency action before go-live, extracted into a sign-off checklist.

The most common cloud security failure isn't a provider control failing. It's a customer assuming the provider handled something nobody handled. AWS provides encryption; whether you enabled it is on you.

### Then the Tabletop AAR

Read section 10 first.

The exercise was run specifically to close POA&M item V-006, about the one-hour US-CERT notification requirement never having been exercised. The exercise **failed** — notification draft at T+64 against a 60-minute requirement, severity classification at 22 minutes against a 15-minute objective, and the General Counsel's number in the roster was outdated.

The milestone said "conduct a tabletop." One was conducted. It could technically have been closed.

**The report recommends it stay open**, because closing a POA&M item on the basis that an exercise *occurred* rather than *succeeded* would misrepresent the organization's posture to the AO. The AO is accepting risk based on what the ISSO reports. If the POA&M is optimistic, their risk decision is wrong and they don't know it.

---

## Design notes

**Why 30 controls, not 323.** A production FedRAMP Moderate package addresses the full baseline. This documents a representative sample across 15 families to stay reviewable while demonstrating the method. The SCTM legend states this explicitly.

**Why some controls are Inherited.** PE-3 and MP-6 are fully inherited from AWS GovCloud's FedRAMP High P-ATO. Two cautions worth knowing: inheritance must be *verified*, not assumed, and most controls people call inherited are actually **shared**.

**On the POA&M.** Cell U1 is a live status date — change it and every overdue calculation recalculates. A POA&M that isn't current is worse than useless in front of an AO.

---

## Program context: this package is Rev5

On **June 25, 2026**, FedRAMP published the Consolidated Rules for 2026 and made **FedRAMP 20x** a widely available certification path. Under those rules "Authorization" became "Certification," impact levels became Classes A–D, and narrative control descriptions were replaced by Key Security Indicators validated automatically.

This package is built to **Rev5**, which remains valid — CR26 becomes mandatory for existing certifications on January 1, 2027, and new Rev5 applications stop being accepted June 11, 2027. Rev5 is also the better vehicle for demonstrating control-by-control reasoning.

[Project 3](../03-northgate-signal-fedramp-20x/) is the same discipline under the standard that replaced it.

---

## Frameworks applied

NIST SP 800-53 Rev 5 · NIST SP 800-53A Rev 5 · NIST SP 800-37 Rev 2 (RMF) · NIST SP 800-60 · FIPS 199 · FedRAMP Moderate baseline · FISMA · OMB Circular A-130
