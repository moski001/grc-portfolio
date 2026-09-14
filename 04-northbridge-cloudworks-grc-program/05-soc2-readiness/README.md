# Northbridge Program, Phase 5: SOC 2 Readiness and Evidence Management

## Purpose

I built this project to prepare a company for SOC 2 readiness: organizing controls, evidence requests, exceptions, remediation, owners, due dates, and executive readiness reporting.

## Scenario

Northbridge Cloudworks is not yet undergoing a real SOC 2 examination, but customer security reviews are increasing. Leadership wants to understand what evidence exists, what is missing, where control exceptions exist, and what must be remediated before engaging an auditor.

## The judgment call

Incident Response is the only theme rated fully Not Ready, worse than every Partial rating elsewhere, but I put MFA exception evidence at the top of the 60-90 day sprint instead. IR readiness needs an actual tabletop exercise scheduled and run, which takes longer than any evidence-collection task on this list. Sequencing the sprint by severity alone would have opened with the worst-rated theme and produced no closed gap by the deadline. A different analyst could reasonably have led with IR anyway, on the logic that the worst-rated control deserves executive attention first regardless of how long the fix takes.

## Dashboard Preview

![Northbridge SOC 2 readiness dashboard](../../assets/dashboard-previews/northbridge-soc2-readiness-dashboard.png)

## Standards Used

- AICPA Trust Services Criteria with revised points of focus 2022 for SOC 2 readiness language.
- NIST CSF 2.0 for program structure and risk communication.
- NIST SP 800-53 Rev. 5 Release 5.2.0 and NIST SP 800-53A Rev. 5 for control and evidence testing concepts.
- CIS Controls v8.1 for practical control expectations.
- ISO/IEC 27001:2022/Amd 1:2024 and ISO/IEC 27002:2022 for ISMS control alignment.
- ISO/IEC 27017:2026 for cloud-specific control considerations.
- NIST SP 800-61 Rev. 3 for incident-response readiness.
- NIST SP 800-161 Rev. 1 Update 1 for vendor-control readiness.

## Deliverables

- `Northbridge-SOC2-Readiness-and-Evidence-Tracker.xlsx`
- [SOC 2 Readiness Report](Northbridge-SOC2-Readiness-Report.md)

## Scope and approach

In this phase, I:

- Built a SOC 2 readiness control matrix.
- Created a PBC evidence request tracker.
- Tracked evidence status, owners, due dates, and auditor-style comments.
- Documented audit findings and remediation actions.
- Explained why evidence quality matters.
- Communicated readiness status to leadership.

## Files

| Artifact | Browse | Working file |
|---|---|---|
| Northbridge SOC2 Readiness and Evidence Tracker | [PDF](pdf/Northbridge-SOC2-Readiness-and-Evidence-Tracker.pdf) | [xlsx](artifacts/Northbridge-SOC2-Readiness-and-Evidence-Tracker.xlsx) |
