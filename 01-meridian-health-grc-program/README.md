# Project 1 — Meridian Health Analytics, Inc.

**A complete cybersecurity GRC program for a fictional healthcare claims analytics company.**

> ⚠️ **Fictional company.** Meridian Health Analytics does not exist. All risks, vendors, findings, and personnel are invented for demonstration. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

Meridian Health Analytics is a mid-size company processing claims data, eligibility verification, and billing for healthcare payers and providers. It handles PHI, is subject to HIPAA/HITECH, runs primarily on AWS with legacy on-premises components, and has an engineering-led security culture — good technical controls, thin governance.

That last detail is deliberate. It's a very common real-world shape, and it's what the gap assessment surfaces.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [Risk Register](pdf/risk_register.pdf) | [xlsx](artifacts/risk_register.xlsx) | 15 risks with live inherent/residual scoring |
| [NIST CSF 2.0 Gap Assessment](pdf/nist_csf_gap_assessment.pdf) | [xlsx](artifacts/nist_csf_gap_assessment.xlsx) | Current vs. target maturity, all six Functions |
| [Control Mapping](pdf/control_mapping_spreadsheet.pdf) | [xlsx](artifacts/control_mapping_spreadsheet.xlsx) | 20 controls across four frameworks |
| [Vendor Risk Assessment](pdf/vendor_risk_assessment.pdf) | [xlsx](artifacts/vendor_risk_assessment.xlsx) | 11 vendors, tiering + sample questionnaire |
| [Information Security Policy](pdf/security_policy.pdf) | [docx](artifacts/security_policy.docx) | Governing policy, 15 sections |
| [Business Impact Analysis](pdf/business_impact_analysis.pdf) | [docx](artifacts/business_impact_analysis.docx) | RTO/RPO/MTD by business process |

---

## How to read this

### Start with the Risk Register
Everything else is downstream of knowing what the organization is actually worried about. Fifteen risks across data protection, access control, third-party, business continuity, and application security.

Each carries an **inherent** score (likelihood × impact, before controls), the existing controls, then a **residual** score. The formulas are live — change a likelihood rating and the risk level recalculates.

**Look at R-001.** Unencrypted PHI backups on a legacy NAS. Inherent risk is Critical (20/25). Residual is Low, because the controls actually work. That gap is the measurable value the security program produces. A register showing only inherent risk tells leadership nothing about whether their spend is doing anything.

**Look at R-014.** No rate limiting on the public provider directory API — deliberately **accepted**, not mitigated. The data is public by design and the exposure doesn't justify the remediation cost. Accepting risk isn't failure; refusing to accept any risk means spending money in the wrong places.

### Then the Gap Assessment
The register says what could go wrong. The gap assessment says how mature the program is against a recognized framework.

CSF 2.0, so all six Functions including **Govern** (new in 2.0) — which is where this organization scores worst. Policies exist, but there's no documented risk appetite and no board-level reporting.

**The pattern matters more than any single score.** Technical controls (monitoring, platform security) score reasonably. Governance controls score worst. That's the signature of an engineering-led organization, and it usually surfaces as an audit problem about two years later.

### Then Control Mapping
One control implementation, four frameworks satisfied. MFA on privileged accounts is `PR.AA-02` in CSF, `CIS 6.5`, `A.8.5` in ISO 27001:2022, and supports `CC6.1`/`CC6.6` in SOC 2.

The trap is assuming the mapping is one-to-one. It isn't — one framework's control often spans three of another's, so the mapping has to be many-to-many and honest where the fit is partial.

### Then Vendor Risk, Policy, and BIA
Vendor risk tiers 11 vendors by data access and includes a full SIG-Lite-style questionnaire for the highest-risk one — a claims clearinghouse with direct PHI access and **no current SOC 2 Type II**. The right answer isn't automatic termination; it's conditional approval with a hard deadline, because ripping out a clearinghouse mid-contract carries its own operational risk.

The BIA is where the loop closes: analysis showed the stated 4-hour RTO for claims processing isn't achievable with single-region deployment and an untested DR runbook. That became `R-004` in the register.

---

## The thing to notice

Risk IDs appear across four separate documents.

`R-004` — the single-region DR gap — appears in the risk register, the CSF gap assessment (RC.RP), the BIA findings, and the control mapping (business continuity row). `R-003` — the vendor SOC 2 gap — appears in the register, the gap assessment (GV.SC), the vendor assessment, and the control mapping.

Pull any thread and it holds. That's what this project was actually practicing: not producing documents, but producing a program where the documents agree with each other.

---

## Methodology notes

**Risk scoring** is qualitative 5×5 — likelihood Rare to Almost Certain, impact Negligible to Severe, with Severe anchored to a regulatory, financial, or patient-safety consequence rather than a dollar figure.

The honest limitation: 5×5 is **ordinal, not cardinal**. A 12 isn't twice as risky as a 6, and averaging those scores across a register is meaningless arithmetic. It's defensible as a triage and communication tool for a large register, and indefensible as a basis for comparing investment options. A more mature program would move toward quantitative modeling (FAIR) for the top-tier risks while keeping qualitative screening for the rest.

**Known limitation of this project:** every control status is *asserted*, not tested. There's no scan output, ticket export, or screenshot backing it. In a real engagement that's the whole job — the assertion is worthless without the artifact. [Project 2](../02-cascade-civic-rev5-ato/) is where I addressed that, because a Security Assessment Report forces you to name the evidence reviewed for every finding.

---

## Frameworks applied

NIST CSF 2.0 · NIST SP 800-30 Rev 1 · NIST SP 800-34 Rev 1 · CIS Controls v8 · ISO/IEC 27001:2022 · SOC 2 Trust Services Criteria · HIPAA/HITECH
