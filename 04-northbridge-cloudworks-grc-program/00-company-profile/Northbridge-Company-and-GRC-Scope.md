# Northbridge Cloudworks Company and GRC Scope

## Company Profile

Northbridge Cloudworks, Inc. is a fictional B2B SaaS company that provides workflow automation and customer operations software to mid-market clients. It has approximately 120 employees, operates remote-first, and hosts its production application in AWS.

## Business Objectives

- Protect customer confidential business data.
- Mature cybersecurity governance and risk management.
- Align security practices with NIST CSF 2.0.
- Prepare the company for future SOC 2 readiness work.
- Improve vendor-risk visibility.
- Communicate cyber risk in business terms that leadership can act on.

## Technology Environment

| Area | In-Scope Systems |
|---|---|
| Cloud hosting | AWS production and development accounts |
| Identity | Okta, Microsoft Entra ID / Microsoft 365 |
| Code and CI/CD | GitHub, GitHub Actions |
| Customer operations | Salesforce, support tooling |
| Collaboration | Slack, Microsoft 365 |
| Payments | Stripe, with cardholder data intentionally limited to Stripe-hosted flows |
| Monitoring | Cloud logging, endpoint telemetry, SaaS audit logs |
| Vendors | AWS, Okta, GitHub, Microsoft, Salesforce, Slack, Stripe, endpoint security provider |

## Data Types

- Customer business data
- User account data
- Employee HR data
- Security logs
- Vendor due-diligence records
- Contract and customer support records

## GRC Scope

The portfolio focuses on practical GRC analyst work:

- Risk assessment and risk-register development
- NIST CSF 2.0 gap analysis
- Control mapping and control testing
- Vendor and supply-chain risk review
- SOC 2 readiness and evidence tracking
- Executive reporting and remediation tracking

## Assumptions

- Northbridge is not directly storing full payment card data because payment processing is outsourced to Stripe-hosted payment flows.
- Northbridge is not currently handling CUI, so NIST SP 800-171 Rev. 3 is treated as a conditional reference only.
- Northbridge is not yet pursuing ISO certification, but ISO/IEC 27001:2022/Amd 1:2024 and ISO/IEC 27002:2022 are used for control-language maturity.
- Northbridge is a cloud SaaS company, so ISO/IEC 27017:2026 is relevant for cloud-specific control considerations.

## Portfolio Message

The purpose of this company profile is to give each project a realistic business context. In an interview, this prevents the work from sounding theoretical. Each artifact should answer:

- What business process is affected?
- What system or data is at risk?
- What framework or standard guided the work?
- What evidence would prove the control exists?
- What decision should leadership make?


## Scenario chronology and rating definitions

These are fictional assessment dates and decision assumptions authored for the portfolio. They do not describe real operating tests or the time spent producing the files. The framework-reference baseline remains August 13, 2026.

| Phase | Scenario assessment date | Dependency |
|---|---|---|
| Enterprise risk assessment | 2026-08-13 | Establish risks and treatment ownership |
| CSF gap assessment | 2026-08-19 | Use enterprise risks to prioritize gaps |
| DataFlow AI vendor assessment | 2026-08-26 | Assess the vendor before the control-testing workpaper |
| Control crosswalk and testing | 2026-09-02 | Use the vendor assessment as TPRM-01 evidence |
| SOC 2 readiness | 2026-09-10 | Consolidate earlier work into evidence requests and readiness actions |

DataFlow AI's next annual assessment is 2027-08-26. Existing remediation commitments are retained. Dates are assessment checkpoints, not assertions that every activity happened on that one day.

### Distinct rating purposes

This section owns the definitions used by the Northbridge workbooks. An identical control ID keeps the same control objective; the rating columns answer different questions.

| Field and authoritative location | Meaning | Tier interpretation |
|---|---|---|
| Control Criticality — crosswalk Control Library column L | Business importance of the control objective if it fails; independent of whether current evidence is complete. | High: broad access, exposure or service-protection consequence. Medium: narrower or supporting control objective. Low: limited consequence. |
| Evidence Review Priority — SOC 2 Control Matrix column I | Relative attention for the readiness evidence review, considering the documented evidence gap and follow-up needed. It is not a new business-risk rating. | High: production-sensitive evidence or important incomplete vendor/cloud assurance. Medium: routine control evidence or a bounded review/workflow gap. Low: administrative evidence follow-up. A Ready control may retain a review priority for continued monitoring. |
| Finding Severity — workpapers and findings registers | Severity of the particular observed or assumed exception described in that finding. | The finding's stated consequence and evidence determine its severity. It need not equal the control's criticality. |
| Residual Risk — enterprise Risk Register | Likelihood × impact remaining for the business-risk scenario after crediting effective controls. | Low 1–4; Medium 5–9; High 10–16; Critical 17–25. These bands apply to Northbridge only. |

The shared controls below retain different values deliberately. They are reconciled by purpose and the existing finding, not silently treated as one scale.

| Control | Criticality | Evidence review priority | Reconciliation |
|---|---|---|---|
| AC-02 Access Review | High | Medium | Access is consequential; the documented exception is a missing approval timestamp on a review that occurred. |
| VM-01 Scanning | High | Medium | Scanning is important; three monthly scans passed the workpaper test, with an aging-summary follow-up. |
| VM-02 Vulnerability Remediation | High | Medium | Unremediated vulnerabilities can be serious; SOCF-004 specifically concerns undocumented SLA exceptions and is rated Medium. |
| LOG-01 Logging | High | Medium | Detection coverage is important; readiness work requires the source inventory and documented ownership. |
| SEC-01 Training | Medium | Low | Workforce awareness is a supporting control; the PBC follow-up is contractor completion evidence, not a newly discovered security incident. |

All other shared controls have matching tier labels. PBC request priority and finding severity remain separately scoped fields.

### Control effectiveness assumptions

Effective means the described control operates consistently within its scope; it does not mean zero residual risk. Ineffective means the control does not meet the assessed objective, and this assessment credits no reduction for it. Partial controls have limited or incomplete operation.

| Risk | Effectiveness | Fictional scenario decision and scoring consequence |
|---|---|---|
| R-005 Former employee access | Effective | Deactivation and retained records operate after timely HR notice. The remaining risk is a delayed upstream notification. Residual score remains 8. |
| R-018 Unauthorized change | Effective | Approvals and five-business-day emergency review operate consistently. Unauthorized bypass can still cause harm before detection. Residual score remains 8. |
| R-015 Untested response | Ineffective | A plan and rota do not demonstrate coordinated response without an exercise. No reduction is credited: 20 inherent and 20 residual, Critical. |
| R-020 Missing evidence | Ineffective | Shared folders without evidence owners do not establish evidence governance. No reduction is credited: 16 inherent and 16 residual, High. |

The other sixteen risks retain Partially Effective. These are scenario assumptions, not newly executed tests. The dashboard ranks residual scores dynamically; tied scores keep register order for display only.
