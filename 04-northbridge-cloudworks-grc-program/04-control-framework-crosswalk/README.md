# Northbridge Program, Phase 4: Control Framework Crosswalk and Control Testing

## Purpose

I built this project to translate multiple frameworks into a practical internal control library: mapping controls across standards, requesting evidence, performing control testing, documenting exceptions, and tracking remediation.

## Scenario

Northbridge Cloudworks is preparing for stronger customer security reviews and future SOC 2 readiness work. Leadership wants a unified control library instead of separate, duplicated checklists for NIST, CIS, ISO, and SOC 2.

## The judgment call

Fifteen controls exist in the library; only five got test workpapers this cycle, and access control got two of them while business continuity and change management got none. That's not neutral. I weighted testing coverage toward access control because Phase 1's risk register ranked privileged account compromise as Northbridge's top residual risk, and testing effort should follow risk rather than chase even coverage across categories. A different analyst optimizing for breadth across all ten control areas could reasonably have spread the five test slots differently, and would have caught problems in categories this cycle didn't touch at all.

## Dashboard Preview

![Northbridge control crosswalk and testing dashboard](../../assets/dashboard-previews/northbridge-control-testing-dashboard.png)

## Standards Used

- NIST CSF 2.0 for outcome-oriented program structure.
- NIST SP 800-53 Rev. 5 Release 5.2.0 for detailed control references.
- NIST SP 800-53A Rev. 5 for control assessment procedures and evidence logic.
- CIS Controls v8.1 for practical prioritized safeguards.
- ISO/IEC 27001:2022/Amd 1:2024 and ISO/IEC 27002:2022 for ISMS and control guidance.
- ISO/IEC 27017:2026 for cloud-specific controls.
- AICPA Trust Services Criteria with revised points of focus 2022 for SOC 2 readiness language.
- NIST SP 800-61 Rev. 3 for incident-response controls.
- NIST SP 800-161 Rev. 1 Update 1 for vendor and supply-chain controls.

## Deliverables

- `Northbridge-Control-Framework-Crosswalk-and-Testing.xlsx`
- [Control Crosswalk and Testing Report](Northbridge-Control-Crosswalk-and-Testing-Report.md)

## Scope and approach

In this phase, I:

- Built an internal control library.
- Mapped one internal control to multiple frameworks.
- Distinguished framework mapping from actual control testing.
- Requested evidence that supports a control objective.
- Evaluated design and operating effectiveness.
- Documented exceptions and remediation actions.
- Explained control work in language auditors and managers understand.

## Files

| Artifact | Browse | Working file |
|---|---|---|
| Northbridge Control Framework Crosswalk and Testing | [PDF](pdf/Northbridge-Control-Framework-Crosswalk-and-Testing.pdf) | [xlsx](artifacts/Northbridge-Control-Framework-Crosswalk-and-Testing.xlsx) |
