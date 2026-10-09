# Project 2: Tailspin Civic Systems, Inc. / AwardWorks

**A FedRAMP Moderate (Rev5) authorization package for a fictional government grants management SaaS.**

> ⚠️ **Fictional organization. Created for portfolio demonstration purposes.** Tailspin Civic Systems and the AwardWorks platform do not exist. No FedRAMP authorization, 3PAO assessment, or incident described here occurred. Documents carry CUI markings only to demonstrate handling conventions; no actual CUI is present. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

AwardWorks is a multi-tenant SaaS platform for federal, state, and local agencies that administer grants: opportunity publication, applicant intake, eligibility review, award issuance, subrecipient monitoring, disbursement, and closeout.

It handles applicant PII, taxpayer identification numbers, and disbursement data. It runs on AWS GovCloud under that provider's FedRAMP High P-ATO, and it is pursuing an agency ATO at the Moderate baseline with a named sponsoring agency.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [System Security Plan](pdf/system_security_plan.pdf) | [docx](artifacts/system_security_plan.docx) | Categorization, boundary, control approach, ConMon strategy |
| [Security Controls Traceability Matrix](pdf/sctm_control_matrix.pdf) | [xlsx](artifacts/sctm_control_matrix.xlsx) | 33 controls in 16 families, with method and result per control |
| [Security Assessment Report](pdf/security_assessment_report.pdf) | [docx](artifacts/security_assessment_report.docx) | 8 findings in condition/criteria/cause/effect form |
| [Plan of Action & Milestones](pdf/poam.pdf) | [xlsx](artifacts/poam.xlsx) | 8 items, milestones, live overdue calculation |
| [Customer Responsibility Matrix](pdf/customer_responsibility_matrix.pdf) | [xlsx](artifacts/customer_responsibility_matrix.xlsx) | 23 controls by responsibility model, plus the agency onboarding checklist |
| [IR Tabletop After-Action Report](pdf/ir_tabletop_after_action_report.pdf) | [docx](artifacts/ir_tabletop_after_action_report.docx) | Exercise design, timeline, findings, POA&M disposition |

---

## Tracing a deficiency

A control deficiency has to be traceable from the SSP, through the independent assessment, to a remediation plan with a date and an owner. If the trail breaks, the Authorizing Official is making a risk decision without the facts. Here is one deficiency end to end:

```
SCTM          RA-5, SI-2 marked "Other Than Satisfied"
                    ↓
SAR           FIND-001: 14 High vulns open past the 30-day window,
              longest at 94 days. Cause: no automated SLA escalation.
                    ↓
POA&M         V-001: 3 milestones, owner, target 2026-06-25,
              risk rating High
```

Every "Other Than Satisfied" control in the SCTM carries a POA&M ID, every POA&M item cites the same NIST controls, and every SAR finding names both. Nine controls are Other Than Satisfied; RA-5 and SI-2 share V-001, so they produce eight findings and eight POA&M items.

---

## How to read this

### Start with the SSP: categorization and boundary

RMF starts by categorizing the system. Working through the SP 800-60 information types and applying the high water mark puts AwardWorks at Moderate for confidentiality, integrity, and availability. That decision selects the control baseline, so the SSP records the reasoning along with the result.

Then the authorization boundary. The SSP documents what is inside, what is outside, and why. AWS GovCloud infrastructure is outside and inherited. Corporate IT is outside because no federal data touches it. A boundary drawn too small hides scope an assessor will find; one drawn too large pulls in components the provider cannot control or remediate.

### Then the SAR, starting with FIND-001

Each finding is written as condition, criteria, cause, and effect, followed by evidence reviewed, recommendation, and management response.

The cause section decides whether the fix holds. FIND-001's condition is 14 High vulnerabilities open past 30 days. The cause is that the pipeline created tickets but had no automated escalation when an SLA was close to breaching, so security work competed with feature work in sprint planning with nothing enforcing the deadline. The recommendation follows from that cause: automated escalation at 15 and 25 days.

FIND-007 is worth reading too. The weekly log review was probably happening, but no artifact recorded it. Nothing was misconfigured, and the control is still Other Than Satisfied because it could not be evidenced.

The sample also includes one Not Applicable determination. SC-15 (collaborative computing devices) does not apply because nothing of that kind sits inside the boundary; the assessor examined the boundary inventory and accepted the determination.

### Then the Customer Responsibility Matrix

FedRAMP authorizes the provider's controls. It does not make the customer agency compliant. Of the 23 controls, 11 are Shared, which means neither party is compliant unless both do their part. Nineteen go-live actions for the agency are pulled into a sign-off checklist.

A common cloud failure is a customer assuming the provider handled something nobody handled. AC-20 is the example here: AwardWorks can allowlist IP ranges, but only the agency can decide whether staff may use personal devices.

### Then the Tabletop AAR

Read section 10 first. The exercise was run to close POA&M item V-006, which concerns a one-hour CISA notification requirement that had never been exercised. The exercise failed: the notification draft came in at T+64 against a 60-minute requirement, severity classification took 22 minutes against a 15-minute objective, and the General Counsel's number in the roster was out of date.

The milestone said "conduct a tabletop," and one was conducted, so the item could have been closed on paper. The report recommends keeping it open. The AO accepts risk based on what the ISSO reports, and closing V-006 because an exercise occurred, when it did not succeed, would give the AO the wrong picture.

---

## Design notes

**Sample size.** A production FedRAMP Moderate package addresses the full 323-control baseline. This one documents 33 controls across 16 families so it stays reviewable, and the SCTM legend says so.

**Inherited controls.** PE-3 and MP-6 are fully inherited from AWS GovCloud's FedRAMP High P-ATO. Inheritance claims still need verification, and many controls described as inherited are actually shared.

**The POA&M.** Cell U1 holds the status date. Change it and every overdue calculation updates.

---

## Program context: this package is Rev5

On June 25, 2026, FedRAMP published the Consolidated Rules for 2026 and made FedRAMP 20x a widely available certification path. Under those rules "Authorization" became "Certification," impact levels became Classes A–D, and narrative control descriptions were replaced by Key Security Indicators validated automatically.

This package is built to Rev5, which remains valid. CR26 becomes mandatory for existing certifications on January 1, 2027, and new Rev5 applications stop being accepted June 11, 2027. [Project 3](../03-salgado-public-fedramp-20x/) applies the same discipline under the newer rules.

---

## Frameworks applied

NIST SP 800-53 Rev 5 · NIST SP 800-53A Rev 5 · NIST SP 800-37 Rev 2 (RMF) · NIST SP 800-60 · FIPS 199 · FedRAMP Moderate baseline · FISMA · OMB Circular A-130
