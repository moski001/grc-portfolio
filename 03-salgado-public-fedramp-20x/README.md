# Project 3: FedRAMP 20x Class C Certification Package

**Salgado Public Systems, Inc. | CaseBoard Platform**
A cloud-native SaaS case management platform for state and local health and human services agencies.

> ⚠️ **Fictional organization. Created for portfolio demonstration purposes.** Salgado Public Systems and the CaseBoard platform do not exist. No certification, assessment, or drift finding described here occurred. See [DISCLAIMER](../DISCLAIMER.md) and "Accuracy and scope" below.

---

## Why this project exists

I built a Rev5-style FedRAMP authorization package first: SSP, SCTM, Security Assessment Report, POA&M, Customer Responsibility Matrix. That package shows control-by-control reasoning and audit-finding writing.

On June 25, 2026, FedRAMP published the **Consolidated Rules for 2026** and made **FedRAMP 20x** a widely available certification path. It is the first substantial redesign of the program since 2011: "Authorization" became "Certification," impact levels became certification Classes A–D, and narrative control descriptions were replaced by **Key Security Indicators** validated automatically against the running system. This project builds that model in code.

---

## What's here

| Artifact | What it is |
|---|---|
| [`src/ksi_validator.py`](src/ksi_validator.py) | The validation engine. Evaluates 13 KSIs with two independent automated methods each, writes machine-readable evidence, and verifies that evidence against its manifest. |
| [`src/render_register.py`](src/render_register.py) | Refreshes the register workbook's result columns from the Security Decision Record, so the spreadsheet cannot drift from the JSON. |
| [`evidence/security-decision-record.json`](evidence/security-decision-record.json) | The 20x replacement for a Rev5 SSP. Generated, not hand-written. |
| [`evidence/ongoing-certification-report.json`](evidence/ongoing-certification-report.json) | The 20x replacement for a monthly ConMon submission. |
| [`evidence/evidence-integrity-manifest.json`](evidence/evidence-integrity-manifest.json) | SHA-256 hash and byte count of each evidence file as written to disk. `sha256sum` on a published file reproduces its entry. |
| [`ksi_validation_register`](pdf/ksi_validation_register.pdf) ([xlsx](artifacts/ksi_validation_register.xlsx)) | Human-readable rendering of the SDR, plus drift findings, class requirements, and methodology. |
| [`rev5_to_20x_migration_assessment`](pdf/rev5_to_20x_migration_assessment.pdf) ([docx](artifacts/rev5_to_20x_migration_assessment.docx)) | Gap assessment and transition plan for a provider moving from Rev5 to 20x Class C. |
| [Interactive dashboard](https://claude.ai/artifact/7DrT2VsqkTfA3HZH695FQ3) | The same results drawn from the evidence files, with each number linked to the file and field it came from. |

---

## The design decision

CR26 rule **FRC-CSX-VVK** requires a Class C provider to run **at least two automated validation methods per KSI**. Two checks that read the same API are one assertion counted twice, so every KSI here pairs:

- a **control-plane** method, which reads what the configuration declares, with
- a **data-plane or telemetry** method, which measures what the running system did.

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
KSI-PIY-GIV     TRUE     2        -
KSI-INR-RIR     TRUE     2        -
----------------------------------------------------
11/13 KSIs true | 26 validation methods | Class C 2-method count met: True
```

Two KSIs fail, both because the configuration is correct and the system does not behave accordingly:

- **KSI-CNA-RNT**: network policy declares default-deny with 100% workload coverage. Flow logs show 1,317 permitted flows over 30 days that match no explicit allow rule.
- **KSI-SVC-SIN**: encryption config declares a TLS 1.3 minimum, but active protocol negotiation found one load balancer listener still accepting TLS 1.0.

Configuration review alone would have reported both as true. Both also name legacy reporting components (`legacy-reporting-subnet` and `lb-legacy-reporting-01`), so retiring or re-baselining the legacy reporting segment is likely to close both, and the drift findings are tracked together.

### Passing KSIs still carry exceptions

The eleven passing KSIs have the exceptions a running system has. Each method's pass logic states what makes an exception acceptable:

| KSI | What the data shows | Why it still passes |
|---|---|---|
| KSI-IAM-AAM | 415 of 417 accounts under automated lifecycle | The other 2 are sealed break-glass accounts under a documented exception |
| KSI-IAM-AAM / ELP | 5 accounts flagged for excess privilege, 4 remediated | The open one is 2 days old, inside its 5-day remediation window |
| KSI-IAM-JIT | 2 elevated sessions reached the 60-minute cap | The broker revoked both at the cap |
| KSI-IAM-SNU | Secret scanning raised 4 findings, 1 real (a test token) | Revoked and rotated the same afternoon |
| KSI-IAM-SUS | 11 risk signals, 9 auto-disabled accounts | The other 2 came from the authorized external scanner and were suppressed by a documented allowlist entry |
| KSI-CMT-RMV | 235 of 238 deployments had pre-merge peer review | The 3 without it were emergency changes, all reviewed afterward |
| KSI-CED-RAT | 88 of 91 staff completed awareness training | The other 3 were hired in the last 30 days |
| KSI-PIY-GIV | Cloud asset APIs found 147 resources against 143 in the inventory | The 4 extras sit outside the authorization boundary, each with a boundary decision on file |

The ongoing certification report has its own gaps: detection coverage is 98.6% (two new hosts awaiting scanner enrollment), and one high-severity finding in a vendor base image is past its response expectation, with a deviation request on file.

---

## Run it

```bash
python3 src/ksi_validator.py --summary   # evaluate and write evidence/
python3 src/ksi_validator.py --verify    # check evidence/ against the manifest
python3 src/render_register.py           # refresh the register workbook (needs openpyxl)
```

The validator needs only the standard library. The `FIXTURES` dict stands in for cloud provider, IdP, and SIEM API responses; in production each would be an API call. Two fixtures disagree with their configuration blocks on purpose to produce the drift results, and both are commented in the source.

### Evidence integrity

The manifest hashes the exact bytes written to disk, so the published evidence can be checked without running Python:

```bash
cd evidence && sha256sum security-decision-record.json ongoing-certification-report.json
```

Each digest should match the `sha256` value for that file in `evidence-integrity-manifest.json`. `--verify` runs the same check and exits non-zero on a mismatch or a missing file. An earlier version hashed a canonical re-serialization of the JSON rather than the file bytes, so the published files never matched their own manifest. That was corrected in October 2026.

---

## Accuracy and scope

- KSI identifiers are drawn from the **FedRAMP Consolidated Rules for 2026**, which changed the naming scheme (`KSI-IAM-AAM`, not the `KSI-IAM-01` format from the 2025 pilot). KSI-CMT-RMV quotes the official statement; the others are close paraphrases. Verify each against the published text, including KSI-PIY-GIV, which was added in October 2026.
- The JSON structures are **modeled on** CR26 rule requirements (`SDR-CSO-FRR`, `CCM-OCR-AVL`, `FRC-CSO-JSN`). They are not claimed to validate against FedRAMP's published schemas at `fedramp.gov/schemas`. A production implementation would validate against those schemas in CI.
- The 2026 rules are new and revised often. Check anything here against the current text at **fedramp.gov/2026** before relying on it.
- The 13 KSIs are a sample across seven families. A full Class C package addresses the complete KSI set across all ten families.

---

## Companion projects

1. [**Tavares Claims Services**](../01-tavares-claims-grc-program/), commercial GRC program: risk register, NIST CSF 2.0 gap assessment, control mapping, vendor risk, security policy, BIA.
2. [**Tailspin Civic Systems / AwardWorks**](../02-tailspin-civic-rev5-ato/), Rev5 federal authorization package: SSP, SCTM, SAR, POA&M, CRM, incident response tabletop AAR.
3. **This project**, the same work under the newer rules.
