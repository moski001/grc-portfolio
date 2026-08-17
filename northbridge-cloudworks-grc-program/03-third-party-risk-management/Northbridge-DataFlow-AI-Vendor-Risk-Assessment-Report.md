# Northbridge DataFlow AI Vendor Risk Assessment Report

## Executive Summary

Northbridge Cloudworks assessed DataFlow AI as a prospective critical SaaS vendor because the service would process confidential customer business data and integrate with production customer-support workflows.

The assessment resulted in a **Conditional Approval** recommendation. DataFlow AI demonstrates a reasonable security foundation, including SOC 2 evidence, encryption, vulnerability scanning, security policies, access controls, and cloud-hosting controls. However, several gaps should be remediated before full production use.

## Vendor Profile

| Field | Assessment Detail |
|---|---|
| Vendor | DataFlow AI |
| Service | AI-assisted customer-support analytics |
| Data processed | Confidential customer business data, support metadata, limited user identifiers |
| Integration | API integration with Northbridge application and Salesforce |
| Hosting model | Cloud SaaS |
| Inherent risk tier | Critical |
| Assessment outcome | Conditional Approval |

## Methodology

The assessment used a weighted domain scorecard and evidence-review model. Each domain was scored from 1 to 5 and multiplied by its assigned weight. Findings were rated High, Medium, or Low based on likelihood, business impact, compensating controls, and whether the issue needed contractual or technical remediation.

## Domain Score Summary

| Domain | Weight | Score | Summary |
|---|---:|---:|---|
| Governance | 10% | 4 | Policies and ownership exist, but risk-review cadence could be clearer |
| IAM | 20% | 3 | MFA exists, but privileged MFA evidence is incomplete |
| Data Security | 20% | 4 | Encryption and retention controls are documented |
| Infrastructure Security | 15% | 4 | Cloud security controls exist, but configuration evidence is limited |
| Application Security | 15% | 3 | SDLC exists, but penetration testing cadence needs improvement |
| Incident Response and BCP | 10% | 3 | IR/BCP plans exist, but tabletop and notification evidence need improvement |
| Compliance and Assurance | 10% | 4 | SOC 2 evidence provided, with follow-up needed on exceptions |

## Key Findings

| Finding | Severity | Risk |
|---|---|---|
| Privileged MFA evidence incomplete | High | Unauthorized administrative access could affect customer data |
| Breach notification terms not contractually specific | High | Northbridge may not receive timely notification of vendor incidents |
| Penetration testing occurs every two years | Medium | Application weaknesses may persist longer than Northbridge's target risk tolerance |
| Incident-response tabletop evidence not provided | Medium | Vendor readiness is less proven during a customer-impacting event |
| Contractor security training evidence incomplete | Low | Human-risk controls may not fully cover all workforce populations |

## Decision

**Conditional Approval**

DataFlow AI may proceed to limited implementation only after Northbridge receives and approves:

1. Evidence that privileged administrative access requires MFA.
2. Contract language requiring timely incident and breach notification.
3. A commitment to annual penetration testing or a documented compensating control.
4. Incident-response tabletop evidence or scheduled exercise date.

## Management Rationale

The vendor is not rejected because the gaps appear remediable and the service provides business value. However, unconditional approval would be inappropriate because two issues directly affect customer-data risk and incident-response obligations.

## Interview-Ready Conclusion

The key judgment in this project is that vendor risk is not binary. A vendor can be usable if the risks are understood, documented, contractually managed, and tracked through remediation. Conditional approval is appropriate when the business wants the service, the risk is not outside tolerance, and specific gaps can be closed before full production use.
