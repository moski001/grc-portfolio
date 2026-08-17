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
