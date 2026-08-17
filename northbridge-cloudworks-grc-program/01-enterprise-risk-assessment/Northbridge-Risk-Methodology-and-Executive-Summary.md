# Northbridge Risk Methodology and Executive Summary

## Objective

The objective of this assessment is to identify, estimate, prioritize, and communicate cybersecurity risks that could affect Northbridge Cloudworks' business objectives. The output is a management-ready risk register, not a technical vulnerability list.

## Methodology

The assessment follows a qualitative 1-5 likelihood by 1-5 impact model. Risk score equals likelihood multiplied by impact.

| Score Range | Rating | Management Meaning |
|---:|---|---|
| 1-4 | Low | Monitor through normal operations |
| 5-9 | Medium | Track with named owner and reasonable remediation plan |
| 10-16 | High | Prioritize remediation and report to leadership |
| 17-25 | Critical | Immediate leadership visibility and risk-treatment decision required |

## Likelihood Scale

| Score | Label | Definition |
|---:|---|---|
| 1 | Rare | Not expected, but possible under unusual circumstances |
| 2 | Unlikely | Could occur, but not expected annually |
| 3 | Possible | Could occur within the next year |
| 4 | Likely | Expected to occur or has occurred in similar environments |
| 5 | Almost Certain | Expected repeatedly or already occurring |

## Impact Scale

Impact considers confidentiality, integrity, availability, legal/regulatory exposure, customer trust, financial loss, operational disruption, and executive visibility.

| Score | Label | Definition |
|---:|---|---|
| 1 | Minimal | Limited internal inconvenience |
| 2 | Minor | Some operational disruption or limited data exposure |
| 3 | Moderate | Material process disruption, customer impact, or audit finding |
| 4 | Major | Significant customer, legal, financial, or operational impact |
| 5 | Severe | Major breach, prolonged outage, regulatory exposure, or board-level impact |

## Control Effectiveness

| Rating | Meaning |
|---|---|
| Effective | Control is designed appropriately and appears consistently operating |
| Partially Effective | Control exists but is inconsistent, incomplete, manual, or not fully evidenced |
| Ineffective | Control does not address the risk or is not operating |
| Not Implemented | No meaningful control is in place |

## Risk Treatment Options

- Mitigate: reduce likelihood or impact through improved controls.
- Transfer: shift some risk through insurance or contractual provisions.
- Accept: leadership accepts residual risk within defined tolerance.
- Avoid: stop the activity causing the risk.

## Executive Summary

The assessment identified 20 cybersecurity risks across identity, cloud security, vulnerability management, vendor risk, incident response, business continuity, data governance, and change management. The highest residual risks relate to privileged access compromise, AWS misconfiguration, ransomware readiness, third-party breach exposure, and incomplete incident-response testing.

The most urgent pattern is not a single missing tool. It is inconsistent governance: several controls exist but lack formal ownership, evidence, review cadence, or executive-level reporting. This is why the assessment uses the NIST IR 8286 Rev. 1 series and NIST SP 1308 in addition to NIST SP 800-30. The goal is to make cybersecurity risk comparable to other enterprise risks and usable for leadership decisions.

## Top Five Risks

| Rank | Risk | Residual Rating | Why It Matters |
|---:|---|---|---|
| 1 | Privileged account compromise | High | Could lead to broad system access and customer data exposure |
| 2 | AWS misconfiguration exposes customer data | High | Direct confidentiality and customer-trust impact |
| 3 | Ransomware disrupts operations | High | Could interrupt SaaS availability and support operations |
| 4 | Third-party vendor breach | High | Northbridge depends on critical SaaS vendors and integrations |
| 5 | Inadequate incident-response testing | High | Plans are weaker if roles and decision paths have not been exercised |

## 90-Day Management Priorities

1. Enforce phishing-resistant MFA for privileged accounts where technically supported.
2. Implement cloud configuration monitoring and monthly control-owner review.
3. Establish vulnerability remediation SLAs with executive exception reporting.
4. Complete a tabletop exercise using NIST SP 800-61 Rev. 3 incident-response concepts.
5. Formalize third-party risk tiering and critical vendor review cadence.

## How This Connects to ERM

Cybersecurity risk should be presented in terms that leadership can compare with financial, operational, legal, and strategic risks. The risk register therefore includes business process, asset, risk owner, treatment plan, target date, residual risk rating, and executive escalation status. This structure supports the risk-register and enterprise-risk integration concepts in the NIST IR 8286 Rev. 1 series.
