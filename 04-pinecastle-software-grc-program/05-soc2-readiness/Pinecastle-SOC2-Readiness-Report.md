# Pinecastle SOC 2 Readiness Report

*Fictional organization. Created for portfolio demonstration purposes.*

## Executive Summary

Pinecastle Software has several foundational security controls that support SOC 2 readiness, including MFA, vulnerability scanning, backups, security policies, vendor reviews, and incident-response documentation. It is not yet audit-ready because some controls lack complete evidence, defined review cadence, or documented operating effectiveness.

The readiness result is **Partially Ready**. Pinecastle should complete remediation before beginning a formal SOC 2 examination period.

## Readiness Themes

| Theme | Status | Summary |
|---|---|---|
| Access Control | Partial | MFA and access processes exist, but exceptions and review evidence need cleanup |
| Vulnerability Management | Partial | Scanning exists, but SLA evidence and aging reports need formalization |
| Incident Response | Not Ready | IR plan exists, but tabletop exercise evidence is missing |
| Business Continuity | Partial | Backups exist, but restoration and DR test evidence need improvement |
| Vendor Risk | Partial | Critical vendor review process is emerging but not fully mature |
| Logging and Monitoring | Partial | Logs are enabled, but there is no source inventory or named alert owner |
| Evidence Management | Partial | Evidence exists across teams but is not centrally governed |

## Highest Priority Readiness Gaps

| Gap | Severity | Why It Matters |
|---|---|---|
| MFA exception evidence incomplete | High | Access control is a core SOC 2 security concern |
| Q2 access review lacks approval evidence | Medium | An auditor needs a dated approval to accept that the review happened |
| Incident-response tabletop not completed | Medium | The plan has never been exercised, so its readiness is unproven |
| Critical vulnerability SLA exceptions not formally approved | Medium | Audit reviewers will expect evidence of tracking and exception handling |
| Evidence ownership is decentralized | Medium | Missing evidence creates audit friction and weakens control confidence |
| No log source inventory or alert owners (SOCF-006) | Medium | Auditors test CC7 by asking which sources are monitored and who responds |

## Readiness Recommendation

Pinecastle should not start a formal SOC 2 examination period until high-priority evidence gaps are closed. The company should complete a 60-90 day readiness sprint focused on:

1. Finalizing evidence owners.
2. Closing high-risk access-control evidence gaps.
3. Completing incident-response tabletop testing.
4. Performing backup restoration evidence collection.
5. Formalizing vulnerability SLA exception approval.
6. Building the log source inventory and alert routing matrix.
7. Reviewing all 13 PBC requests for completeness.

## Report type

The first report should be a Type I. The Type II observation window should start only after an internal readiness retest passes, and no audit date should be promised to customers before then.

Scenario assessment date: **2026-09-10**. Dashboard areas are mutually exclusive and derived from Control Matrix column J: 22 controls total, comprising 6 Ready, 15 Partial and 1 Not Ready. [Shared rating definitions](../00-company-profile/Pinecastle-Company-and-GRC-Scope.md#distinct-rating-purposes) explain Evidence Review Priority and its differences from Control Criticality.
