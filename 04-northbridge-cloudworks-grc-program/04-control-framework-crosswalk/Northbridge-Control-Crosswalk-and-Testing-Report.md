# Northbridge Control Crosswalk and Testing Report

## Executive Summary

Northbridge Cloudworks needs a control model that supports security governance, customer assurance, and future SOC 2 readiness without creating duplicate work for every framework. This project creates a unified internal control library, maps the controls across major frameworks, and demonstrates control testing for selected controls.

The strongest lesson from this project is that frameworks are not the work product by themselves. The work product is the control, the evidence, the test procedure, the exception, the remediation plan, and the business decision that follows from testing it. Translating overlapping framework language into that concrete set of deliverables is where a GRC analyst adds value.

## Control Library Scope

The control library includes 15 practical controls across:

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

## Crosswalk Approach

Each internal control is mapped to:

- NIST CSF 2.0 function or outcome area
- NIST SP 800-53 Rev. 5 control family/reference
- CIS Controls v8.1 safeguard area
- ISO/IEC 27001:2022/Amd 1:2024 and ISO/IEC 27002:2022 control language
- AICPA Trust Services Criteria where SOC 2 relevance exists
- Optional ISO/IEC 27017:2026 cloud reference where applicable

## Control Testing Approach

Five controls were selected for test workpapers:

| Control | Test Focus | Result |
|---|---|---|
| AC-01 MFA Enforcement | Inspect identity-provider configuration and user sample | Exception noted |
| AC-02 Quarterly Access Review | Inspect access review evidence | Exception noted |
| VM-01 Vulnerability Scanning | Inspect scan cadence and remediation aging | Pass with improvement |
| IR-02 Incident Response Tabletop | Inspect exercise evidence | Exception noted |
| TPRM-01 Critical Vendor Review | Inspect vendor review evidence | Pass with observation |

## Key Findings

| Finding | Severity | Summary |
|---|---|---|
| Two contractor accounts lacked MFA evidence | High | MFA control is designed appropriately but not operating fully effectively |
| Q2 access review missing approval timestamp | Medium | Review occurred, but evidence quality is incomplete |
| Incident-response tabletop not completed in current year | Medium | IR plan exists, but readiness has not been exercised |

## Management Recommendation

Northbridge should maintain the unified control library as the source of truth, assign control owners, define evidence requirements, and use the testing workpapers as the foundation for SOC 2 readiness.

Scenario assessment date: **2026-09-02**. [Shared rating definitions](../00-company-profile/Northbridge-Company-and-GRC-Scope.md#distinct-rating-purposes) distinguish Control Criticality from SOC 2 Evidence Review Priority.
