# Frictionlessness Report — corrections and authorized scenario decisions

Repository: `/Users/cmorrissey/Documents/Codex/grc-portfolio-frictionlessness-20260914`
Branch: `agent/frictionlessness-review-20260914`
Predecessor: `d507c62fb5047b00092a75349ab8332ab9e59ab0`
Review date: 2026-09-14

The governing Frictionlessness criteria and source attachment provenance are recorded in [the historical first pass](report.md). This follow-up supersedes its five listed error deferrals and the named-accepter gap. All 16 matched workbooks were read with openpyxl; nine were edited. No duplicate primary IDs were found. Fictional effectiveness, chronology and acceptance decisions are explicitly labeled as scenario authorship authorized by the owner, not actual executed tests or real executive approval.

## Corrections and scenario decisions

All five requested defects are corrected: Cascade V-003 severity, V-008/AC-2 coverage, Meridian rubric and R-009 wording, and the SOC 2 category arithmetic. Crosswalk Control Criticality and SOC 2 Evidence Review Priority now have distinct definitions in [Northbridge company scope](../../04-northbridge-cloudworks-grc-program/00-company-profile/Northbridge-Company-and-GRC-Scope.md); its reconciliation table explains AC-02, VM-01, VM-02, LOG-01 and SEC-01 differences. Numeric labels were not normalized across different meanings.

R-014 acceptance ACC-014 names fictional COO Elena Voss, dated 2026-03-12. Public directory data and Low residual score 2 support retaining rate limiting in the Q3 backlog while higher-priority PHI/access work proceeds. Delegated authority, monitoring conditions, escalation, scheduled review and expiry are recorded. The acceptance does not establish remediation closure or a completed later review.

## All matched workbooks

### Meridian control mapping

File: `01-meridian-health-grc-program/artifacts/control_mapping_spreadsheet.xlsx`

Unchanged this pass. 20 controls retain partial/not-implemented states and valid risk links; no unsupported N/A or test result added.

### Meridian CSF gap assessment

File: `01-meridian-health-grc-program/artifacts/nist_csf_gap_assessment.xlsx`

Unchanged this pass. Prior action/owner alignment correction retained; missing GV.RR maturity inputs and evidence remain blank.

### Meridian risk register

File: `01-meridian-health-grc-program/artifacts/risk_register.xlsx`

Fixed Critical 15–25 / High 10–14 legend to match existing formulas; R-009 now says Medium at score 6. Added ACC-014: fictional Elena Voss, COO, accepts R-014 on 2026-03-12 with authority, public-data/cost rationale, monitoring, scheduled review 2026-07-31 and expiry 2026-12-31. No completed July review is claimed. Existing score-12 tie and R-015 zero reduction retained.

### Meridian vendor assessment

File: `01-meridian-health-grc-program/artifacts/vendor_risk_assessment.xlsx`

Ten assessment dates now span 2025-08-21 through 2026-02-04, explicitly fictional. V-008 remains unassessed with blank date. Scores unchanged; ClaimLink narrative-versus-inventory rating semantics remain unresolved.

### Cascade customer responsibility matrix

File: `02-cascade-civic-rev5-ato/artifacts/customer_responsibility_matrix.xlsx`

Unchanged this pass. Prior summary corrections retained; inherited controls still have agency duties. Actual onboarding completion fields remain blank.

### Cascade POA&M

File: `02-cascade-civic-rev5-ato/artifacts/poam.xlsx`

V-003 J7 now Moderate, matching SAR FIND-003. Eight finding IDs remain unique. V-006 retains the original June 15 target plus the later AAR June 30/July 15 corrective-action dates and delayed-classification reason; no approved replacement closure date is claimed.

### Cascade SCTM

File: `02-cascade-civic-rev5-ato/artifacts/sctm_control_matrix.xlsx`

AC-2 changed to Partially Implemented / Other Than Satisfied with V-008 and the existing shared-account facts. All eight POA&M findings now have backlinks; 21 Satisfied and 9 Other Than Satisfied. SAR DOCX/PDF counts synchronized.

### Northgate KSI validation

File: `03-northgate-signal-fedramp-20x/artifacts/ksi_validation_register.xlsx`

Unchanged this pass. 12 KSIs and 24 methods reconcile with source JSON; two false results remain. Existing Class-A-only N/A rationale retained. DRIFT-002 closure remains unproved.

### Northbridge enterprise risk

File: `04-northbridge-cloudworks-grc-program/01-enterprise-risk-assessment/artifacts/Northbridge-Enterprise-Risk-Assessment.xlsx`

Authored 2 Effective (R-005/R-018), 2 Ineffective (R-015/R-020), 16 Partially Effective. Ineffective controls receive no modeled reduction: residual 20/16. Treatment labels and top-five dashboard now formula-linked. Score ties use original register order for display only. Assessment date 2026-08-13 retained.

### Northbridge CSF gap assessment

File: `04-northbridge-cloudworks-grc-program/02-nist-csf-gap-assessment/artifacts/Northbridge-NIST-CSF-2.0-Gap-Assessment.xlsx`

Assessment date 2026-08-19; shared chronology linked. Existing 1 Implemented / 16 Partially Implemented / 1 Not Implemented retained. No new test conclusion or dated roadmap invented.

### Northbridge third-party risk

File: `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/artifacts/Northbridge-Third-Party-Risk-Assessment.xlsx`

Assessment date 2026-08-26; annual review 2027-08-26. Days-to-due formulas reference the assessment date and support negative overdue days. Existing F-004 Unable to test — evidence not provided retained; five findings and remediation dates unchanged.

### Northbridge crosswalk/testing

File: `04-northbridge-cloudworks-grc-program/04-control-framework-crosswalk/artifacts/Northbridge-Control-Framework-Crosswalk-and-Testing.xlsx`

Assessment date 2026-09-02. Renamed tier to Control Criticality; authoritative definitions reconcile five differing shared labels with SOC 2 evidence priority. Two Pass / three Exception results preserved. Companion tabletop reference corrected IR-01 to IR-02.

### Northbridge SOC 2 readiness

File: `04-northbridge-cloudworks-grc-program/05-soc2-readiness/artifacts/Northbridge-SOC2-Readiness-and-Evidence-Tracker.xlsx`

Assessment date 2026-09-10. Added one Readiness Area per control and formula-driven category counts: 22 total = 6 Ready + 15 Partial + 1 Not Ready. Renamed tier Evidence Review Priority and linked shared definitions; existing readiness/finding judgments retained.

### Halcyon AI control crosswalk

File: `05-halcyon-ai-governance/artifacts/ai_control_crosswalk.xlsx`

Unchanged this pass. Prior locator correction retained; 15 objectives include 7 partial and 8 not implemented, with valid AIR links.

### Halcyon AI risk assessment

File: `05-halcyon-ai-governance/artifacts/ai_risk_assessment.xlsx`

Unchanged this pass. Real ties and two unchanged residual scores remain. AIR-010 evidentiary tension with inventory AI-009 retained, with README note. Past targets do not establish closure.

### Halcyon AI system inventory

File: `05-halcyon-ai-governance/artifacts/ai_system_inventory.xlsx`

Unchanged this pass. Explicit AI-009 classification Not Applicable rationale retained. B8 proposed/enacted deferral conflict deferred to pass 5; no external legal-status conclusion made.

## Requested friction examples and limits

- **Not Applicable:** Halcyon inventory AI-009 classification includes a written rationale because the entry is a governance gap, not a discrete AI system; Northgate also retains structural Class-A-only determinations.
- **Unable to test — evidence not provided:** Northbridge third-party F-004 retains this explicit result and its missing exercise-report basis.
- **Accepted risk:** Meridian ACC-014 now supplies named authority, date and business rationale as authorized fiction.
- **Scoring tie:** Meridian inherent score 12 has five risks. Northbridge residual score 15 has four; dashboard ties use register order, without implying different business priority.
- **Slipped remediation evidence:** Cascade V-006 records later corrective actions beyond the original June 15 target and delayed classification as the reason. This supports a schedule-conflict/slippage example, **not an approved replacement closure date**; that record remains absent.

Halcyon B8 legal-status conflict is deferred to pass 5. AI-009/AIR-010 ambiguity remains with a note. Meridian ClaimLink narrative tier versus calculated inventory rating is also still a documented unresolved semantic issue. Neither elapsed time nor invented dates were used as evidence that remediation occurred.

## Validation evidence

All 16 final workbooks reopened with openpyxl 3.1.5 in formula and data-only modes. 5,629 low-level assertions passed: primary IDs, known downstream references, source JSON projections, intended cell values, retained formulas outside logged changes, original worksheets, tables, filters, panes, conditional formatting, charts and existing validations. Seven untouched workbooks remain byte-for-byte identical to the predecessor. The new acceptance sheet, SOC 2 area validation, ranking column and text-layout adjustments are intentional additions. Typed assessment and acceptance dates were verified; remediation target dates were retained.

LibreOffice recalculated disposable copies for 13 additional assertions, including top-five order, an increased risk moving to first place, Ready-to-Partial totals changing from 6/15/1 to 5/16/1, and a past due date producing -1 day. No recalculated error cells were found in these copies. The final XLSX files remain openpyxl-authored; formula caches may be blank until opened in a spreadsheet application. This is not a claim of testing in Microsoft Excel.

Nine workbook PDF companions and the SAR PDF were refreshed. Changed ranges, dashboard previews, acceptance page and all eight SAR pages were visually inspected. The nine workbook PDFs contain no detected formula-error text. Existing wide register layouts remain dense; editable workbooks are the detailed review surface.

Evidence files:

- [Exact cell changes](scenario-cell-changes.json)
- [All-workbook validation and hashes](scenario-validation.json)
- [Calculation tests](scenario-calculation-validation.json)
- [PDF checks](scenario-pdf-validation.json)

The first-pass evidence files remain historical. A separate SESSION_EVENT draft is prepared outside the repository and is not applied to canonical Control Room state. No push is performed.

## Exact changed paths in this follow-up

- `01-meridian-health-grc-program/README.md`
- `01-meridian-health-grc-program/artifacts/risk_register.xlsx`
- `01-meridian-health-grc-program/artifacts/vendor_risk_assessment.xlsx`
- `01-meridian-health-grc-program/pdf/risk_register.pdf`
- `01-meridian-health-grc-program/pdf/vendor_risk_assessment.pdf`
- `02-cascade-civic-rev5-ato/artifacts/poam.xlsx`
- `02-cascade-civic-rev5-ato/artifacts/sctm_control_matrix.xlsx`
- `02-cascade-civic-rev5-ato/artifacts/security_assessment_report.docx`
- `02-cascade-civic-rev5-ato/pdf/poam.pdf`
- `02-cascade-civic-rev5-ato/pdf/sctm_control_matrix.pdf`
- `02-cascade-civic-rev5-ato/pdf/security_assessment_report.pdf`
- `04-northbridge-cloudworks-grc-program/00-company-profile/Northbridge-Company-and-GRC-Scope.md`
- `04-northbridge-cloudworks-grc-program/01-enterprise-risk-assessment/Northbridge-Risk-Methodology-and-Executive-Summary.md`
- `04-northbridge-cloudworks-grc-program/01-enterprise-risk-assessment/artifacts/Northbridge-Enterprise-Risk-Assessment.xlsx`
- `04-northbridge-cloudworks-grc-program/01-enterprise-risk-assessment/pdf/Northbridge-Enterprise-Risk-Assessment.pdf`
- `04-northbridge-cloudworks-grc-program/02-nist-csf-gap-assessment/Northbridge-CSF-2.0-Gap-Assessment-Report.md`
- `04-northbridge-cloudworks-grc-program/02-nist-csf-gap-assessment/artifacts/Northbridge-NIST-CSF-2.0-Gap-Assessment.xlsx`
- `04-northbridge-cloudworks-grc-program/02-nist-csf-gap-assessment/pdf/Northbridge-NIST-CSF-2.0-Gap-Assessment.pdf`
- `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/Northbridge-DataFlow-AI-Vendor-Risk-Assessment-Report.md`
- `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/artifacts/Northbridge-Third-Party-Risk-Assessment.xlsx`
- `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/pdf/Northbridge-Third-Party-Risk-Assessment.pdf`
- `04-northbridge-cloudworks-grc-program/04-control-framework-crosswalk/Northbridge-Control-Crosswalk-and-Testing-Report.md`
- `04-northbridge-cloudworks-grc-program/04-control-framework-crosswalk/artifacts/Northbridge-Control-Framework-Crosswalk-and-Testing.xlsx`
- `04-northbridge-cloudworks-grc-program/04-control-framework-crosswalk/pdf/Northbridge-Control-Framework-Crosswalk-and-Testing.pdf`
- `04-northbridge-cloudworks-grc-program/05-soc2-readiness/Northbridge-SOC2-Readiness-Report.md`
- `04-northbridge-cloudworks-grc-program/05-soc2-readiness/artifacts/Northbridge-SOC2-Readiness-and-Evidence-Tracker.xlsx`
- `04-northbridge-cloudworks-grc-program/05-soc2-readiness/pdf/Northbridge-SOC2-Readiness-and-Evidence-Tracker.pdf`
- `05-halcyon-ai-governance/README.md`
- `reviews/frictionlessness-2026-09-14/report.md`
- `reviews/frictionlessness-2026-09-14/scenario-calculation-validation.json`
- `reviews/frictionlessness-2026-09-14/scenario-cell-changes.json`
- `reviews/frictionlessness-2026-09-14/scenario-follow-up.md`
- `reviews/frictionlessness-2026-09-14/scenario-pdf-validation.json`
- `reviews/frictionlessness-2026-09-14/scenario-validation.json`
