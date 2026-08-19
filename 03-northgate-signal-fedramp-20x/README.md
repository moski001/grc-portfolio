# Project 3 — FedRAMP 20x Class C Certification Package

**Northgate Signal, Inc. | Caseline Platform**
A cloud-native SaaS case management platform for state and local health and human services agencies.

> ⚠️ **Fictional company and system.** Northgate Signal and the Caseline platform do not exist. No certification, assessment, or drift finding described here occurred. See [DISCLAIMER](../DISCLAIMER.md) and "Accuracy and scope" below.

---

## Why this project exists

I built a Rev5-style FedRAMP authorization package first — SSP, SCTM, Security Assessment Report, POA&M, Customer Responsibility Matrix. That package demonstrates control-by-control reasoning and the ability to write a defensible audit finding.

Then, on June 25, 2026, FedRAMP published the **Consolidated Rules for 2026** and made **FedRAMP 20x** a widely available certification path. It is the first substantial redesign of the program since 2011: "Authorization" became "Certification," impact levels became certification Classes A–D, and narrative control descriptions were replaced by **Key Security Indicators** validated automatically against the running system.

This project is my response to that change. It demonstrates the new model rather than describing it.

---

## What's here

| Artifact | What it demonstrates |
|---|---|
| [`src/ksi_validator.py`](src/ksi_validator.py) | The validation engine. Evaluates 12 KSIs against live system state using two independent automated methods each, and emits machine-readable evidence. |
| [`evidence/security-decision-record.json`](evidence/security-decision-record.json) | The 20x replacement for a Rev5 SSP. Structured, generated, not hand-authored. |
| [`evidence/ongoing-certification-report.json`](evidence/ongoing-certification-report.json) | The 20x replacement for a monthly ConMon submission. |
| [`evidence/evidence-integrity-manifest.json`](evidence/evidence-integrity-manifest.json) | SHA-256 hashes of each artifact, so tampering between generation and submission is detectable. |
| [`ksi_validation_register`](pdf/ksi_validation_register.pdf) ([xlsx](artifacts/ksi_validation_register.xlsx)) | Human-readable rendering of the SDR, plus drift findings, class requirements comparison, and methodology. |
| [`rev5_to_20x_migration_assessment`](pdf/rev5_to_20x_migration_assessment.pdf) ([docx](artifacts/rev5_to_20x_migration_assessment.docx)) | Gap assessment and transition plan for a provider moving from Rev5 to 20x Class C. |

---

## The design decision that matters

CR26 rule **FRC-CSX-VVK** requires a Class C provider to implement **at least two automated validation methods per KSI**. The obvious way to satisfy that is to write two checks. The useful way is to ask what two methods are *for*.

The answer is corroboration from independent sources. Two methods reading the same API is one assertion counted twice.

So every KSI here pairs:

- a **control-plane** method — what the configuration declares should be true, and
- a **data-plane or telemetry** method — what the running system actually did.

Where they disagree, the KSI reports `false` and the observed behavior is treated as authoritative.

## What that produced

```
KSI             Status   Methods  Drift
----------------------------------------------------
KSI-IAM-AAM     TRUE     2        -
KSI-IAM-APM     TRUE     2        -
KSI-IAM-ELP     TRUE     2        -
KSI-IAM-JIT     TRUE     2        -
KSI-IAM-SNU     TRUE     2        -
KSI-IAM-SUS     TRUE     2        -
KSI-CMT-LMC     TRUE     2        -
KSI-CMT-RMV     TRUE     2        -
KSI-CNA-RNT     FALSE    2        DRIFT
KSI-SVC-SIN     FALSE    2        DRIFT
KSI-CED-RAT     TRUE     2        -
KSI-INR-RIR     TRUE     2        -
----------------------------------------------------
10/12 KSIs true | 24 validation methods | Class C 2-method count met: True
```

**Two KSIs fail, and both fail for the same reason: the configuration is correct and the system is not behaving accordingly.**

- **KSI-CNA-RNT** — network policy declares default-deny with 100% workload coverage. Flow logs show 1,317 permitted flows over 30 days matching no explicit allow rule.
- **KSI-SVC-SIN** — encryption config declares a TLS 1.3 minimum. Active protocol negotiation testing found one load balancer listener still accepting TLS 1.0.

Both would have reported `true` under configuration review alone. That is the entire argument for continuous validation, and the reason FedRAMP moved away from point-in-time document assessment.

---

## Run it

```bash
python3 src/ksi_validator.py --summary
```

No dependencies beyond the standard library. The `FIXTURES` dict at the top stands in for cloud provider, IdP, and SIEM API responses; in production each is an API call. Two fixtures intentionally disagree with their corresponding configuration blocks to produce the drift scenario above — those are commented in the source.

---

## Accuracy and scope

- KSI identifiers and statements are drawn from the **FedRAMP Consolidated Rules for 2026**. The KSI naming scheme changed under CR26 (e.g. `KSI-IAM-AAM`, not the `KSI-IAM-01` format used in the 2025 pilot).
- The JSON structures are **modeled on** CR26 rule requirements (`SDR-CSO-FRR`, `CCM-OCR-AVL`, `FRC-CSO-JSN`). They are **not** claimed to validate against FedRAMP's official published JSON schemas at `fedramp.gov/schemas`, which are authoritative. A production implementation would validate against those schemas in CI.
- The 2026 rules are new and revising frequently. Verify anything here against the current text at **fedramp.gov/2026** before relying on it.
- Twelve KSIs are implemented as a representative sample across six families. A full Class C package addresses the complete KSI set across all ten families.

---

## Companion projects

1. [**Meridian Health Analytics**](../01-meridian-health-grc-program/) — commercial GRC program: risk register, NIST CSF 2.0 gap assessment, control mapping, vendor risk, security policy, BIA.
2. [**Cascade Civic Systems / GrantBridge**](../02-cascade-civic-rev5-ato/) — Rev5 federal authorization package: SSP, SCTM, SAR, POA&M, CRM, incident response tabletop AAR.
3. **This project** — the same discipline under the standard that replaced it.
