# Northbridge Program, Phase 2: NIST CSF 2.0 Gap Assessment

## Purpose

I built this project to assess a company's cybersecurity program against NIST CSF 2.0: comparing current and target states, identifying gaps, prioritizing remediation, and communicating results to leadership.

## Scenario

Northbridge Cloudworks completed an enterprise cybersecurity risk assessment and now wants to understand how its current cybersecurity program aligns to NIST CSF 2.0. Leadership wants a practical roadmap, not a fake certification score.

## The judgment call

Phase 1 ranked ransomware disruption as the third-highest residual risk, driven partly by untested backups. I still pushed the disaster-recovery exercise to the 6-12 month window here, behind governance owners, a risk tracker, and vendor tiering. That's a trade-off, not an oversight: running a DR test before anyone owns the results just produces another undocumented finding. A different analyst weighting the risk score more heavily than the ownership gap could reasonably have pulled the DR exercise into the first 90 days and treated the accountability gap as a problem to solve afterward.

## Dashboard Preview

![Northbridge NIST CSF 2.0 gap assessment dashboard](../../assets/dashboard-previews/northbridge-nist-csf-gap-dashboard.png)

## Standards Used

- NIST CSF 2.0 as the primary framework.
- NIST SP 1308 for governance, enterprise-risk, and workforce alignment.
- NIST IR 8286 Rev. 1 series for enterprise-risk reporting context.
- NIST SP 800-53 Rev. 5 Release 5.2.0 and NIST SP 800-53A Rev. 5 for control and assessment references.
- CIS Controls v8.1, ISO/IEC 27001:2022/Amd 1:2024, ISO/IEC 27002:2022, AICPA TSC revised points of focus 2022, and ISO/IEC 27017:2026 where control-language alignment is useful.
- NIST SP 800-61 Rev. 3 where incident response is relevant.

## Deliverables

- `Northbridge-NIST-CSF-2.0-Gap-Assessment.xlsx`
- [CSF 2.0 Gap Assessment Report](Northbridge-CSF-2.0-Gap-Assessment-Report.md)

## Scope and approach

In this phase, I:

- Interpreted NIST CSF 2.0 outcomes in a realistic business context.
- Built current and target profiles.
- Identified implementation gaps.
- Avoided claiming NIST CSF "certification."
- Prioritized remediation by risk, business impact, and effort.
- Translated assessment results into a 12-month roadmap.

## Files

| Artifact | Browse | Working file |
|---|---|---|
| Northbridge NIST CSF 2.0 Gap Assessment | [PDF](pdf/Northbridge-NIST-CSF-2.0-Gap-Assessment.pdf) | [xlsx](artifacts/Northbridge-NIST-CSF-2.0-Gap-Assessment.xlsx) |
