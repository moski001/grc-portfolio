# Cybersecurity GRC Portfolio

**Chris Morrissey** · Governance, Risk & Compliance · Washington, DC area

CompTIA A+, Network+, Security+, Project+ · CompTIA CIOS & CSIS stacked credentials · ITIL Foundation v4 · Cisco AI Technical Practitioner

---

> ### ⚠️ All organizations and systems in this repository are fictional
>
> Every company, system, assessment, finding, and incident described here was created for demonstration purposes. No real client, employer, system, or security assessment is depicted. No confidential or proprietary information appears anywhere in this repository.
>
> These are original work products built to demonstrate methodology and reasoning. See [DISCLAIMER.md](DISCLAIMER.md).

---

## Why this repository exists

Certifications prove you studied. They don't show a hiring manager how you think.

A real risk register or authorization package is the property of the employer who paid for it — it can never be shown. So this repository contains the only version of that evidence I can legitimately put in front of you: complete, working GRC deliverables built end to end, with the reasoning visible.

Three projects, deliberately sequenced. Each proves something the others can't.

| # | Project | Domain | What it demonstrates |
|---|---|---|---|
| 1 | [Meridian Health Analytics](01-meridian-health-grc-program/) | Commercial healthcare | Building a risk program from nothing |
| 2 | [Cascade Civic Systems](02-cascade-civic-rev5-ato/) | Federal / FedRAMP Rev5 | Operating inside a defined authorization process |
| 3 | [Northgate Signal](03-northgate-signal-fedramp-20x/) | Federal / FedRAMP 20x | Tracking a standard change and acting on it early |

---

## Project 1 — Meridian Health Analytics
**A complete GRC program for a fictional healthcare claims analytics company.**

Not six disconnected templates. One coherent program where every artifact feeds the next: the risk register drives the gap assessment, the gap assessment drives the control roadmap, and the vendor and continuity work feed findings back into the register.

- Enterprise Risk Register — 15 risks, live inherent/residual scoring formulas
- NIST CSF 2.0 Gap Assessment — all six Functions including Govern, with maturity rollup
- Control Mapping — 20 controls across NIST CSF, CIS v8, ISO 27001:2022 Annex A, SOC 2 TSC
- Third-Party Risk Assessment — 11 vendors tiered, full sample security questionnaire
- Information Security Policy
- Business Impact Analysis — RTO/RPO/MTD by process

**The thread worth following:** risk IDs appear across four separate documents. `R-004` shows up in the register, the gap assessment, the BIA, and the control mapping. Pull any thread and it holds.

→ [Open project](01-meridian-health-grc-program/)

---

## Project 2 — Cascade Civic Systems / GrantBridge
**A FedRAMP Moderate (Rev5) authorization package for a fictional grants management SaaS.**

The RMF process is a chain of custody: a control deficiency must be traceable from the SSP through the assessment to a remediation plan with a date and an owner. If that chain breaks anywhere, the Authorizing Official cannot make a risk decision.

- System Security Plan — FIPS 199 categorization, authorization boundary, control origination model
- Security Controls Traceability Matrix — 30 controls, 15 families, assessment method and result per control
- Security Assessment Report — 8 findings in condition / criteria / cause / effect structure
- Plan of Action & Milestones — live status-date cell recalculating overdue status
- Customer Responsibility Matrix — CSP / Shared / Customer / Inherited, with agency onboarding checklist
- Incident Response Tabletop After-Action Report

**The judgment call worth reading:** the tabletop was run specifically to close a POA&M item. The exercise *failed* its primary objective — notification at 64 minutes against a 60-minute requirement. The milestone said "conduct a tabletop," so it could technically have been closed. The report recommends it stay open, because closing on the basis that an exercise occurred rather than succeeded would misrepresent posture to the AO.

→ [Open project](02-cascade-civic-rev5-ato/)

---

## Project 3 — Northgate Signal / Caseline
**A FedRAMP 20x Class C certification package — built after the standard changed.**

On June 25, 2026, FedRAMP published the Consolidated Rules for 2026 and made FedRAMP 20x a widely available certification path. "Authorization" became "Certification," impact levels became Classes A–D, and narrative control descriptions were replaced by Key Security Indicators validated automatically against the running system.

I had just finished Project 2 under the old standard. This is what I did about it.

- **KSI Validation Engine** (Python) — evaluates 12 KSIs using two independent automated methods each
- **Machine-readable evidence** — Security Decision Record and Ongoing Certification Report as JSON, plus SHA-256 integrity manifest
- KSI Validation Register — human-readable rendering of the JSON, plus drift findings
- Rev5 → 20x Migration Assessment — gap analysis and transition plan

**The design decision:** Class C requires at least two automated validation methods per KSI. Two checks reading the same API is one assertion counted twice. So every KSI pairs a **control-plane** method (what config declares) with a **data-plane or telemetry** method (what the system actually did). Where they disagree, observed behavior wins.

**What that produced:** 10 of 12 KSIs pass. Two fail on drift — network policy declares default-deny while flow logs show 1,317 unmatched permitted flows; encryption config declares TLS 1.3 minimum while one listener still accepts TLS 1.0. **Both would report `true` under configuration review alone.** That is the entire argument for continuous validation.

→ [Open project](03-northgate-signal-fedramp-20x/)

---

## Reading this repository

Every artifact is provided twice:

- **`/artifacts/`** — the working files (`.xlsx` with live formulas, `.docx`)
- **`/pdf/`** — PDF exports that preview directly in your browser, no download needed

If you're evaluating quickly, browse the PDFs. If you want to see the formulas and conditional logic, open the spreadsheets.

**Fastest path if you have five minutes:**
1. [Security Assessment Report](02-cascade-civic-rev5-ato/pdf/security_assessment_report.pdf) — read FIND-001 for how I write a finding
2. [KSI Validator source](03-northgate-signal-fedramp-20x/src/ksi_validator.py) — read the module docstring for the design reasoning
3. [Risk Register](01-meridian-health-grc-program/pdf/risk_register.pdf) — inherent vs. residual scoring in practice

---

## Frameworks and standards applied

NIST SP 800-53 Rev 5 · NIST SP 800-53A Rev 5 · NIST SP 800-37 Rev 2 (RMF) · NIST SP 800-30 Rev 1 · NIST SP 800-60 · FIPS 199 · NIST CSF 2.0 · FedRAMP Rev5 Moderate · FedRAMP 20x / Consolidated Rules for 2026 · ISO/IEC 27001:2022 · CIS Controls v8 · SOC 2 Trust Services Criteria · HIPAA/HITECH

---

## Accuracy and currency

FedRAMP's 2026 rules are new and revising frequently, with a public changelog. Project 3 reflects the rules as published; rule identifiers and KSI text should be verified against [fedramp.gov/2026](https://www.fedramp.gov/2026/) before being relied on.

The JSON in Project 3 is **modeled on** CR26 rule requirements. It is not claimed to validate against FedRAMP's official published schemas at fedramp.gov/schemas, which are authoritative. That limitation is stated in the project README rather than left for a reader to discover.

---

## Contact

**Chris Morrissey** — Morrissey Ventures LLC
[LinkedIn](#) · [morrisseyventuresllc.com](https://morrisseyventuresllc.com) · [Email](#)

*Open to GRC Analyst, Risk Analyst, ISSO, Security Control Assessor, and IT Specialist (INFOSEC) roles.*
