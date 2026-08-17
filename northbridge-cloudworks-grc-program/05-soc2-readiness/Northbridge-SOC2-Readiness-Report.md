# Northbridge SOC 2 Readiness Report

## Executive Summary

Northbridge Cloudworks has several foundational security controls that support SOC 2 readiness, including MFA, vulnerability scanning, backups, security policies, vendor reviews, and incident-response documentation. However, the company is not yet fully audit-ready because some controls lack complete evidence, defined review cadence, or documented operating effectiveness.

The readiness result is **Partially Ready**. Northbridge should complete remediation before beginning a formal SOC 2 examination period.

## Readiness Themes

| Theme | Status | Summary |
|---|---|---|
| Access Control | Partial | MFA and access processes exist, but exceptions and review evidence need cleanup |
| Vulnerability Management | Partial | Scanning exists, but SLA evidence and aging reports need formalization |
| Incident Response | Not Ready | IR plan exists, but tabletop exercise evidence is missing |
| Business Continuity | Partial | Backups exist, but restoration and DR test evidence need improvement |
| Vendor Risk | Partial | Critical vendor review process is emerging but not fully mature |
| Evidence Management | Partial | Evidence exists across teams but is not centrally governed |

## Highest Priority Readiness Gaps

| Gap | Severity | Why It Matters |
|---|---|---|
| MFA exception evidence incomplete | High | Access control is a core SOC 2 security concern |
| Q2 access review lacks approval evidence | Medium | Review performance must be evidenced, not only described |
| Incident-response tabletop not completed | Medium | A plan without testing is weaker evidence of readiness |
| Critical vulnerability SLA exceptions not formally approved | Medium | Audit reviewers will expect evidence of tracking and exception handling |
| Evidence ownership is decentralized | Medium | Missing evidence creates audit friction and weakens control confidence |

## Readiness Recommendation

Northbridge should not start a formal SOC 2 examination period until high-priority evidence gaps are closed. The company should complete a 60-90 day readiness sprint focused on:

1. Finalizing evidence owners.
2. Closing high-risk access-control evidence gaps.
3. Completing incident-response tabletop testing.
4. Performing backup restoration evidence collection.
5. Formalizing vulnerability SLA exception approval.
6. Reviewing all PBC requests for completeness.

## Interview-Ready Conclusion

SOC 2 readiness is not just having policies. It is proving that controls are designed, assigned, evidenced, and operating over time. A strong GRC analyst helps the company find gaps before the auditor does.
