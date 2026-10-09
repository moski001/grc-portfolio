# Pinecastle Software GRC Program (Projects 4-8)

Pinecastle Software, Inc. is a fictional B2B SaaS company. The five projects in this folder follow one security program from risk identification to a SOC 2 readiness decision, with each phase using the results of the one before it.

> **Fictional organization. Created for portfolio demonstration purposes.** See [DISCLAIMER](../DISCLAIMER.md).

## Company scenario

Pinecastle Software is a remote-first SaaS provider with roughly 120 employees. It hosts its product in AWS; uses Microsoft 365, Okta, GitHub, Slack, Salesforce, Stripe, and other SaaS vendors; and processes confidential customer business data. Leadership wants to mature the security program, align with NIST CSF 2.0, prepare for SOC 2, and see cyber risk in terms it can act on. Shared scenario dates, rating definitions, and control-effectiveness assumptions are in the [company profile](00-company-profile/Pinecastle-Company-and-GRC-Scope.md).

## Standards baseline

Checked as of August 13, 2026:

| Area | Standard / Framework | Used for |
|---|---|---|
| Cybersecurity framework | NIST CSF 2.0 | Program structure, current and target profiles, gap assessment |
| Risk assessment | NIST SP 800-30 Rev. 1 | Risk scenarios, likelihood, impact, and response |
| Cyber risk to ERM | NIST IR 8286 Rev. 1 series | Register design, enterprise roll-up, governance reporting |
| CSF/ERM/workforce | NIST SP 1308 | Tying risk decisions to business and workforce priorities |
| Security/privacy controls | NIST SP 800-53 Rev. 5 Release 5.2.0 | Control references |
| Control assessment | NIST SP 800-53A Rev. 5 | Evidence and testing logic |
| Supply chain risk | NIST SP 800-161 Rev. 1 Update 1 | Vendor and supply-chain risk |
| Prioritized safeguards | CIS Controls v8.1 | Safeguard mapping |
| ISMS requirements | ISO/IEC 27001:2022 + Amd 1:2024 | Governance and ISMS alignment |
| Security controls | ISO/IEC 27002:2022 | Control language |
| SOC 2 | AICPA TSC with revised points of focus 2022 | Readiness and audit-facing control language |
| Incident response | NIST SP 800-61 Rev. 3 | IR gap and risk treatment references |
| CUI / federal context | NIST SP 800-171 Rev. 3 | Conditional reference only; Pinecastle handles no CUI |
| Cloud controls | ISO/IEC 27017:2026 | Cloud-specific control references |
| Payment card scope | PCI DSS v4.0.1 | Scope check for the Stripe-hosted payment flow (R-021) |

## The five projects

### Project 4: Enterprise cybersecurity risk assessment

22 risks with inherent and residual scoring, control-effectiveness ratings (two Effective, two Ineffective), treatment plans, and an executive dashboard.

- [Project 4 README](01-enterprise-risk-assessment/README.md)
- [Risk Methodology and Executive Summary](01-enterprise-risk-assessment/Pinecastle-Risk-Methodology-and-Executive-Summary.md)
- `Pinecastle-Enterprise-Risk-Assessment.xlsx`

### Project 5: NIST CSF 2.0 gap assessment

18 outcomes across all six Functions, current and target profiles, and a phased roadmap with dependencies between steps.

- [Project 5 README](02-nist-csf-gap-assessment/README.md)
- [CSF 2.0 Gap Assessment Report](02-nist-csf-gap-assessment/Pinecastle-CSF-2.0-Gap-Assessment-Report.md)
- `Pinecastle-NIST-CSF-2.0-Gap-Assessment.xlsx`

### Project 6: Third-party risk assessment

A 27-question review of DataFlow AI, an AI support-analytics vendor, with a weighted scorecard, five findings, one item that could not be tested, and a conditional approval.

- [Project 6 README](03-third-party-risk-management/README.md)
- [DataFlow AI Vendor Risk Assessment Report](03-third-party-risk-management/Pinecastle-DataFlow-AI-Vendor-Risk-Assessment-Report.md)
- `Pinecastle-Third-Party-Risk-Assessment.xlsx`

### Project 7: Control crosswalk and testing

A 17-control internal library mapped to NIST, CIS, ISO, and SOC 2, with six test workpapers (three passes, three exceptions) and the resulting findings.

- [Project 7 README](04-control-framework-crosswalk/README.md)
- [Control Crosswalk and Testing Report](04-control-framework-crosswalk/Pinecastle-Control-Crosswalk-and-Testing-Report.md)
- `Pinecastle-Control-Framework-Crosswalk-and-Testing.xlsx`

### Project 8: SOC 2 readiness and evidence management

A 22-control readiness matrix, a 13-item PBC tracker, six audit-style findings, and a readiness decision.

- [Project 8 README](05-soc2-readiness/README.md)
- [SOC 2 Readiness Report](05-soc2-readiness/Pinecastle-SOC2-Readiness-Report.md)
- `Pinecastle-SOC2-Readiness-and-Evidence-Tracker.xlsx`

## Source URLs

- NIST CSF 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-30 Rev. 1: https://csrc.nist.gov/pubs/sp/800/30/r1/final
- NIST IR 8286 Rev. 1: https://csrc.nist.gov/pubs/ir/8286/r1/final
- NIST IR 8286A Rev. 1: https://csrc.nist.gov/pubs/ir/8286/a/r1/final
- NIST IR 8286C Rev. 1: https://csrc.nist.gov/pubs/ir/8286/c/r1/final
- NIST SP 1308: https://csrc.nist.gov/pubs/sp/1308/final
- NIST SP 800-53 Rev. 5 / Release 5.2.0: https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls
- NIST SP 800-53A Rev. 5: https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
- NIST SP 800-161 Rev. 1 Update 1: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final
- CIS Controls v8.1: https://www.cisecurity.org/controls/v8-1
- ISO/IEC 27001:2022/Amd 1:2024: https://www.iso.org/standard/88435.html
- ISO/IEC 27002:2022: https://www.iso.org/standard/75652.html
- AICPA Trust Services Criteria with revised points of focus 2022: https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
- NIST SP 800-61 Rev. 3: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST SP 800-171 Rev. 3: https://csrc.nist.gov/pubs/sp/800/171/r3/final
- ISO/IEC 27017:2026: https://www.iso.org/standard/27017
- PCI DSS v4.0.1: https://www.pcisecuritystandards.org/document_library/
