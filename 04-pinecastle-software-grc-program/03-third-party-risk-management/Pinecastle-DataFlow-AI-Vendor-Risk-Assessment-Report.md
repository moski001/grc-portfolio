# Pinecastle DataFlow AI Vendor Risk Assessment Report

*Fictional organization. Created for portfolio demonstration purposes.*

## Executive Summary

Pinecastle Software assessed DataFlow AI as a prospective critical SaaS vendor because the service would process confidential customer business data and integrate with production customer-support workflows.

The assessment resulted in a **Conditional Approval** recommendation. DataFlow AI demonstrates a reasonable security foundation, including SOC 2 evidence, encryption, vulnerability scanning, security policies, access controls, and cloud-hosting controls. Several gaps need remediation before full production use.

## Vendor Profile

| Field | Assessment Detail |
|---|---|
| Vendor | DataFlow AI |
| Service | AI-assisted customer-support analytics |
| Data processed | Confidential customer business data, support metadata, limited user identifiers |
| Integration | API integration with Pinecastle application and Salesforce |
| Hosting model | Cloud SaaS |
| Inherent risk tier | Critical |
| Assessment outcome | Conditional Approval |

## Methodology

The questionnaire has 27 questions across eleven topic areas, which the scorecard rolls up into seven weighted domains. Two questions cover AI data use: Pinecastle data is contractually excluded from model training, and the vendor gives no advance notice of model changes. Domain scores (1 to 5) are weighted in the scorecard below; the weighted total is 71%, inside the 65-79% Conditional Approval band. Findings were rated High, Medium, or Low based on likelihood, business impact, compensating controls, and whether the issue needed contractual or technical remediation.

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
| Breach notification terms not contractually specific | High | Pinecastle may not receive timely notification of vendor incidents |
| Penetration testing occurs every two years | Medium | Application weaknesses may persist longer than Pinecastle's target risk tolerance |
| Incident-response tabletop evidence not provided | Medium | Vendor readiness is less proven during a customer-impacting event |
| Contractor security training evidence incomplete | Low | Human-risk controls may not fully cover all workforce populations |

## Decision

**Conditional Approval**

DataFlow AI may proceed to limited implementation only after Pinecastle receives and approves:

1. Evidence that privileged administrative access requires MFA.
2. Contract language requiring timely incident and breach notification.
3. A commitment to annual penetration testing or a documented compensating control.
4. Incident-response tabletop evidence or scheduled exercise date.

## Management Rationale

The gaps appear remediable and the service has business value, so the vendor is not rejected. Two issues directly affect customer-data risk and incident-response obligations, so approval is conditional. The tabletop item (F-004) is recorded as unable to test because no exercise report was provided.

## Follow-up

Limited implementation can start once the four conditions are met. The missing advance notice of model changes is not a finding yet; it goes into the annual review as a question for the next contract renewal.

Scenario assessment date: **2026-08-27**. Next annual review: **2027-08-27**. These authored dates are part of the [shared scenario chronology](../00-company-profile/Pinecastle-Company-and-GRC-Scope.md#scenario-chronology-and-rating-definitions); remediation commitments remain unchanged.
