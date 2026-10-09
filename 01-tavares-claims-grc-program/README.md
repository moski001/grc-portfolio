# Project 1: Tavares Claims Services, Inc.

**A cybersecurity GRC program for a fictional healthcare claims company: risk register, CSF 2.0 gap assessment, control mapping, vendor risk, policy, and business impact analysis.**

> ⚠️ **Fictional organization. Created for portfolio demonstration purposes.** Tavares Claims Services does not exist. All risks, vendors, findings, and personnel are invented. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

Tavares Claims Services is a mid-size company that processes claims data, eligibility verification, and billing for healthcare payers and providers. It handles PHI, is subject to HIPAA/HITECH, runs mostly on AWS with some legacy on-premises components, and has an engineering-led security culture: good technical controls, thin governance. That combination is common, and it is what the gap assessment ends up showing.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [Risk Register](pdf/risk_register.pdf) | [xlsx](artifacts/risk_register.xlsx) | 17 risks with live inherent/residual scoring and a formal acceptance record for R-014 |
| [NIST CSF 2.0 Gap Assessment](pdf/nist_csf_gap_assessment.pdf) | [xlsx](artifacts/nist_csf_gap_assessment.xlsx) | Current vs. target maturity for all 22 CSF 2.0 Categories |
| [Control Mapping](pdf/control_mapping_spreadsheet.pdf) | [xlsx](artifacts/control_mapping_spreadsheet.xlsx) | 21 controls mapped across four frameworks |
| [Vendor Risk Assessment](pdf/vendor_risk_assessment.pdf) | [xlsx](artifacts/vendor_risk_assessment.xlsx) | 11 vendors, tiering, and a sample questionnaire |
| [Information Security Policy](pdf/security_policy.pdf) | [docx](artifacts/security_policy.docx) | Governing policy, 16 sections, v1.3 |
| [Business Impact Analysis](pdf/business_impact_analysis.pdf) | [docx](artifacts/business_impact_analysis.docx) | RTO/RPO/MTD by business process |

---

## How to read this

### Start with the Risk Register

Seventeen risks across data protection, access control, third parties, business continuity, and application security. Each has an inherent score (likelihood × impact before controls), the existing controls, and a residual score. The formulas are live, so changing a likelihood rating recalculates the level.

R-001 is the one to look at first. Unencrypted PHI backups on a legacy NAS score Critical inherent (20 of 25) and Low residual, because the encrypted cloud backups and the three-person admin group work. The difference between those two numbers is what the security program is buying.

R-014 is one of two accepted risks, and the one with a full acceptance record. The provider directory API has no rate limiting, but the data is public by design and the remediation would displace PHI and access-control work. The Risk Acceptance sheet records ACC-014: Elena Voss, COO, accepted the Low residual risk on 2026-03-12 under delegated authority for public-data operational risks, with monitoring conditions, a July review, and a December expiry. Writing that record exposed a conflict in the policy, which named only the CISO as an approver of exceptions. Policy v1.3 now separates policy exceptions from risk acceptance.

R-016 and R-017 came out of the vendor review. ClaimLink's contract gives it five business days to report a breach, and DataVault, which stores archived paper PHI, scored 65 with no SOC 2 report and no recorded sign-off for a High-rated vendor.

### Then the Gap Assessment

The register says what could go wrong. The gap assessment says how mature the program is, scored at the Category level across all six CSF 2.0 Functions. GV.RR has no rating because the evidence to rate it was not supplied, and the sheet leaves it blank instead of guessing.

Technical areas (monitoring, platform security) score reasonably. Govern scores worst: policies exist, but there is no documented risk appetite and no board-level reporting. That is the usual profile of an engineering-led organization, and it tends to show up as an audit problem a couple of years later.

### Then Control Mapping

One control implementation can satisfy four frameworks. MFA on privileged accounts is `PR.AA-02` in CSF, `CIS 6.5`, `A.8.5` in ISO 27001:2022, and supports `CC6.1`/`CC6.6` in SOC 2. The fit is often partial, and one framework's control can span three of another's, so the mapping is many-to-many and says so where the match is loose.

### Then Vendor Risk, Policy, and BIA

Vendor risk tiers 11 vendors by data access and includes a SIG-Lite-style questionnaire for the highest-risk one: a claims clearinghouse with direct PHI access and no current SOC 2 Type II. The recommendation is conditional approval with a 90-day deadline. Replacing a clearinghouse mid-contract carries its own operational risk.

The BIA found that the stated 4-hour RTO for claims processing is not achievable with a single-region deployment and an untested DR runbook. That became `R-004` in the register.

---

## Cross-references

Risk IDs appear across four documents. `R-004` (single-region DR) is in the register, the gap assessment (RC.RP), the BIA findings, and the control mapping (business continuity row). `R-003` (the vendor SOC 2 gap) is in the register, the gap assessment (GV.SC), the vendor assessment, and the control mapping.

---

## Methodology notes

Risk scoring is qualitative 5×5: likelihood from Rare to Almost Certain, impact from Negligible to Severe, with Severe anchored to a regulatory, financial, or patient-safety consequence rather than a dollar figure.

5×5 scores are ordinal. A 12 is not twice as risky as a 6, and averaging scores across a register produces a number with no meaning. The method works for triage and communication; it does not support comparing investment options. A more mature program would model the top-tier risks quantitatively (FAIR) and keep qualitative screening for the rest. Six risks currently tie at an inherent score of 12, and the register notes the tie instead of inventing an order.

**Limitation of this project:** control statuses are asserted, not tested. There is no scan output, ticket export, or screenshot behind them. [Project 2](../02-tailspin-civic-rev5-ato/) addresses that, because a Security Assessment Report has to name the evidence reviewed for every finding.

---

## Resolved review notes

The ClaimLink (V-001) questionnaire findings previously described its risk as "Critical/High" and "Medium-High," which are not values on the Vendor Inventory's Risk Rating scale (Not Assessed/Low/Medium/High) and conflicted with that column's formula output of Medium for a score of 84. The findings now separate ClaimLink's static Inherent Risk Tier (Critical, from PHI and system access) from its calculated Risk Rating (Medium, under the documented logic: Critical tier + score < 80 = High, score 70-84 = Medium), and give the assessor's escalation rationale without overriding the calculated rating.

## Frameworks applied

NIST CSF 2.0 · NIST SP 800-30 Rev 1 · NIST SP 800-34 Rev 1 · CIS Controls v8 · ISO/IEC 27001:2022 · SOC 2 Trust Services Criteria · HIPAA/HITECH
