# Pinecastle Control Crosswalk and Testing Report

*Fictional organization. Created for portfolio demonstration purposes.*

## Executive Summary

Pinecastle Software needs a control model that supports security governance, customer assurance, and future SOC 2 readiness without creating duplicate work for every framework. The library below maps each internal control across the major frameworks once, so a single piece of evidence can answer all of them. Six controls were tested this cycle; three passed and three produced exceptions.

## Control Library Scope

The control library includes 17 controls across:

- Access control
- Vulnerability management
- Logging and monitoring
- Incident response
- Business continuity
- Vendor risk
- Change management
- Security awareness
- Data protection
- Cloud configuration
- Governance (policy review and risk register review)

## Crosswalk Approach

Each internal control is mapped to:

- NIST CSF 2.0 function or outcome area
- NIST SP 800-53 Rev. 5 control family/reference
- CIS Controls v8.1 safeguard area
- ISO/IEC 27001:2022/Amd 1:2024 and ISO/IEC 27002:2022 control language
- AICPA Trust Services Criteria where SOC 2 relevance exists
- Optional ISO/IEC 27017:2026 cloud reference where applicable

## Control Testing Approach

Six controls were selected for test workpapers:

| Control | Test Focus | Result |
|---|---|---|
| AC-01 MFA Enforcement | Inspect identity-provider configuration and user sample | Exception noted |
| AC-02 Quarterly Access Review | Inspect access review evidence | Exception noted |
| VM-01 Vulnerability Scanning | Inspect scan cadence and remediation aging | Pass with improvement |
| IR-02 Incident Response Tabletop | Inspect exercise evidence | Exception noted |
| TPRM-01 Critical Vendor Review | Inspect vendor review evidence | Pass with observation |
| CHG-01 Production Change Approval | Inspect 22 production changes, including both emergency changes | Pass |

## Key Findings

| Finding | Severity | Summary |
|---|---|---|
| Two contractor accounts lacked MFA evidence | High | MFA control is designed appropriately but not operating fully effectively |
| Q2 access review missing approval timestamp | Medium | Review occurred, but evidence quality is incomplete |
| Incident-response tabletop not completed in current year | Medium | IR plan exists, but readiness has not been exercised |

## Management Recommendation

Keep the control library as the single source of truth, confirm an owner for each of the 17 controls, and carry the testing workpapers into SOC 2 readiness. LOG-01 and the two governance controls were not tested this cycle and should be in the next one.

Scenario assessment date: **2026-09-03**. [Shared rating definitions](../00-company-profile/Pinecastle-Company-and-GRC-Scope.md#distinct-rating-purposes) distinguish Control Criticality from SOC 2 Evidence Review Priority.
