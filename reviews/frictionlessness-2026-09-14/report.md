# Frictionlessness Report — 2026-09-14

Historical first pass. For current resolutions and authorized scenario decisions, see [the follow-up](scenario-follow-up.md). The original findings and validation hashes below are retained as the record of commit d507c62.

Repository: `/Users/cmorrissey/Documents/Codex/grc-portfolio-frictionlessness-20260914`
Branch: `agent/frictionlessness-review-20260914`
Base: `e51513e8f191d9809c99e3744b475961699c90ab`
Source conversation: `chatgpt-conversation://6aa79ada-c700-83ea-a6a9-dd36f4b38954`
Governing criteria: REVIEW-BRIEF_1.md, “Frictionlessness (highest value, hardest to fix)”. The requested `/mnt/data/REVIEW-BRIEF_1.md` was recovered from the conversation attachment at `/var/folders/lx/9k15r6l12nv74tl9c193wjlr0000gn/T/codex-file-preview-2Hhmjl/REVIEW-BRIEF_1.md`; SHA-256 `db178589f3b69b024896b91158bc437097a6f668b57ccb63ea626e7d29c871d8`. The brief itself is not added to the published repository.

## Outcome and evidence boundary

Read all 16 `.xlsx` files matching `*/artifacts/*.xlsx` and `*/*/artifacts/*.xlsx` with openpyxl 3.1.5. The earlier preview counted 15 and contains distributions that do not match this revision. Eight workbooks were edited with openpyxl. These are fictional scenario records, not evidence of real organizational operating effectiveness.

No true duplicate primary IDs were found within the inspected table namespaces. Reuse across separate companies is intentional. Corrected three omitted Northgate source-JSON reference lists, a wrong Halcyon worksheet locator, contradictory Cascade summary text, a Halcyon README date claim, and 19 misaligned Meridian action/owner rows. Substantive rating and applicability disputes remain open rather than being silently decided.

| Requested feature | Evidence-supported result |
|---|---|
| Explicit Not Applicable with rationale | Added in Halcyon inventory P13 for AI-009 system classification. This is a classification determination, not a fabricated control exclusion. Northgate already contains Class-A-only N/A determinations. |
| Unable to test — evidence not provided | Added verbatim in DataFlow Questionnaire D17 and Findings Register E5 for existing F-004. Other response/rating fields retained. |
| Accepted risk, named accepter, business rationale | **Partially supported only.** Meridian R-014 already says Accept; its README supplies the public-data/remediation-cost rationale, now in S18. API Platform Lead is a risk owner, not evidenced as the accepter. No personal name or acceptance authority was invented. A named acceptance record is still needed. |
| Scoring tie or explained same-score priority | Existing Meridian score-12 tie documented in S19: R-003/R-006/R-010/R-013/R-015. No scores or ordering changed. |
| Slipped date with reason | **Schedule conflict documented, not a newly approved rebaseline.** V-006 original 2026-06-15 completion conflicts with AAR corrective actions due June 30 and July 15. AAR §§8–11 attributes notification failure to delayed classification. N10 records those dates and the reason; original Q1 date/status retained. An approved replacement closure date is not recorded. |

## Workbook-by-workbook review

Score ties/disputes, N/A/missing evidence, acceptance/deferral, superseded decisions, remediation slippage, production chronology and template repetition were considered for each workbook. Risk-scoring and acceptance checks do not apply mechanically to inventories, mappings or blank onboarding templates. Absence of a feature is a review signal, not permission to manufacture it.

### Meridian control mapping

File: `01-meridian-health-grc-program/artifacts/control_mapping_spreadsheet.xlsx`

20 mapped controls; partial and not-implemented states, including overdue tabletop. Risk links resolve by topic. No control-level N/A or explicit unable-to-test result.

Unchanged.

### Meridian CSF gap assessment

File: `01-meridian-health-grc-program/artifacts/nist_csf_gap_assessment.xlsx`

20 categories; GV.RR has no maturity inputs, and its gap/priority formulas correctly remain blank. Nineteen other rows had actions and owners under the wrong headers; evidence for those rows is absent. No dated remediation tracker.

Moved existing actions I→J and owners J→K for rows 5–24 except 7; left missing evidence blank. Matched owner style to K7. Ratings unchanged.

### Meridian risk register

File: `01-meridian-health-grc-program/artifacts/risk_register.xlsx`

15 risks. Inherent 12 has five ties; R-015 stays 12 residual. R-009 and R-014 are accepted, with roles but no explicit acceptance record. Open/in-progress dates are historical; elapsed calendar time alone does not prove a new status.

S18 now includes the existing README business rationale and missing-accepter limitation. S19 documents the existing score tie. No scores, owners, statuses or dates changed.

### Meridian vendor assessment

File: `01-meridian-health-grc-program/artifacts/vendor_risk_assessment.xlsx`

11 vendors; V-008 has no score/date and evaluates to Not Assessed. ClaimLink has stale SOC 2 and BC/DR testing; R-003 reference resolves. Ten assessment dates repeat 2025-11-01. No documented acceptance or revised dates.

Unchanged. Conflicting rating narrative retained for owner resolution, below.

### Cascade customer responsibility matrix

File: `02-cascade-civic-rev5-ato/artifacts/customer_responsibility_matrix.xlsx`

20 controls; 17 real go-live actions plus a separately labelled example. Actual completion/owner/date fields remain blank. Inherited is not N/A. No evidence supports declaring a control not applicable.

Corrected Summary D5/D8 and Legend B4/B7: CSP/inherited labels do not erase agency duties explicitly listed in detail rows.

### Cascade POA&M

File: `02-cascade-civic-rev5-ato/artifacts/poam.xlsx`

Eight weaknesses; all target dates are future at the stated Q1 status date 2026-03-31. V-001 already documents 14 missed remediation windows and missing automated escalation. V-006 has later approved AAR evidence contradicting its original schedule.

N10 preserves original milestones and adds the dated later evidence: failed notification objective, corrective actions beyond June 15, and no recorded approved replacement closure date. Original dates/status snapshot preserved.

### Cascade SCTM

File: `02-cascade-civic-rev5-ato/artifacts/sctm_control_matrix.xlsx`

30 sampled controls: 8 Other Than Satisfied, 22 Satisfied. N/A and Planned exist in the legend but are unused; this is a subset, not full baseline coverage. Seven distinct POA&M IDs are linked because V-001 appears twice; V-008 has no backlink.

Unchanged: adding an adverse control determination to resolve V-008 would change a substantive conclusion. Coverage conflict remains flagged below.

### Northgate KSI validation register

File: `03-northgate-signal-fedramp-20x/artifacts/ksi_validation_register.xlsx`

12 KSIs × 2 methods; 10 true and 2 false with configuration/observed-behavior disagreement. Class Requirements C8:E8 already marks the Class-A-only requirement N/A. DRIFT-002 target 2026-08-29 has no closure/status evidence; source snapshot is 2026-08-10.

Restored missing source-JSON control references in E6:E8. All KSI identifiers, statements, method results, status and drift flags verified against security-decision-record.json. No simulated telemetry changed.

### Northbridge enterprise risk assessment

File: `04-northbridge-cloudworks-grc-program/01-enterprise-risk-assessment/artifacts/Northbridge-Enterprise-Risk-Assessment.xlsx`

20 risks, real ties, all residual scores below inherent, every control effectiveness Partially Effective, all treatments Mitigate or Transfer / Mitigate. No recorded acceptance or schedule slip. Assessment date 2026-08-13.

Unchanged. Treatment plan IDs/actions/owners/dates/statuses reconcile; do not invent accepted or non-improving risks to vary the pattern.

### Northbridge CSF gap assessment

File: `04-northbridge-cloudworks-grc-program/02-nist-csf-gap-assessment/artifacts/Northbridge-NIST-CSF-2.0-Gap-Assessment.xlsx`

18 outcomes: 1 Implemented, 16 Partially Implemented, 1 Not Implemented; 12 high priorities. No N/A/test-result taxonomy, acceptance record, or slipped date. Roadmap is phased rather than dated.

Unchanged. Dashboard claims and roadmap references inspected; comparable medium-risk outcomes have different priorities, but no new explanation was invented.

### Northbridge third-party assessment

File: `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/artifacts/Northbridge-Third-Party-Risk-Assessment.xlsx`

DataFlow AI conditional approval; five findings with two High, two Medium, one Low. F-004 explicitly lacks an exercise report. No acceptance for unresolved high findings; due dates are future relative to 2026-08-13 assessment.

Questionnaire D17 and Findings Register E5 now explicitly state Unable to test — evidence not provided. Vendor response No, score 2, severity Medium, Open status, decision, dates and closure criteria preserved.

### Northbridge control crosswalk/testing

File: `04-northbridge-cloudworks-grc-program/04-control-framework-crosswalk/artifacts/Northbridge-Control-Framework-Crosswalk-and-Testing.xlsx`

15 controls; only five workpapers, two Pass and three Exception. IR-02 has no current-year tabletop evidence. N/A entries mean no extra cloud/supply-chain note, not control exclusion. Repeated mapping/evidence prose and fixed five-test sample remain visible.

Unchanged. Shared internal control IDs resolve across library, workpapers, evidence requests and SOC 2; different risk tiers between artifacts require semantic clarification, not invented normalization.

### Northbridge SOC 2 readiness

File: `04-northbridge-cloudworks-grc-program/05-soc2-readiness/artifacts/Northbridge-SOC2-Readiness-and-Evidence-Tracker.xlsx`

22 controls: 6 Ready, 15 Partial, 1 Not Ready. Missing tabletop PBC and incomplete contractor/access-review evidence are explicit. No accepted risk approval or recorded slipped completion date.

Unchanged. Finding/action/owner/date/status records agree with remediation tracker. Static dashboard area counts are inconsistent with the 22-control detail population; flagged below.

### Halcyon AI control crosswalk

File: `05-halcyon-ai-governance/artifacts/ai_control_crosswalk.xlsx`

15 objectives: 0 Implemented, 7 Partially Implemented, 8 Not Implemented. Missing CSF equivalents are mapping gaps, not N/A control determinations. All AIR references resolve.

Legend B7 now points to transparency at worksheet row 13 (AIR-002/AIR-007), not row 9 (impact assessment). No classification/rating changes.

### Halcyon AI risk assessment

File: `05-halcyon-ai-governance/artifacts/ai_risk_assessment.xlsx`

12 risks; six inherent scores of 20, two unchanged residual scores of 20; three residual Critical under this workbook’s ≥15 threshold. AIR-011 accepted with monitoring and human-review rationale, but no explicit accepter record. AIR-005/007/010/012 targets precede review date.

Workbook unchanged. README corrected to distinguish legal dates from the four past remediation targets and identify absent closure/delay evidence.

### Halcyon AI system inventory

File: `05-halcyon-ai-governance/artifacts/ai_system_inventory.xlsx`

Eight systems plus one governance finding; contested AI-001 classification and unknown AI-009 inputs are retained. AI-009 is not a discrete system. Inventory date 2026-08-05.

P13 explicitly records Not Applicable for AI Act system classification with existing rationale and limits. Original category and summary logic unchanged. Conflicting timeline caveat remains flagged below.

## Remaining contradictions requiring substantive decisions

- Meridian risk legend B4:B5 says Critical 20–25 / High 10–19; register K/Q formulas use Critical ≥15. Preserve existing formulas/ratings pending the owner's choice of rubric. R-009's “low residual risk” wording also conflicts with its score 6 / Medium band.
- Meridian vendor questionnaire A19/A22 calls ClaimLink Critical/High or Medium-High, while score 84 yields Medium under the inventory formula. Critical inherent tier and residual rating must be distinguished by the assessor; not silently rewritten here.
- Cascade V-003 is High in POA&M J7 but Moderate in SAR FIND-003. Cascade V-008 is recorded in the POA&M and SAR but absent from SCTM backlinks while AC-2 is Satisfied; resolving the coverage/conclusion conflict requires an assessor decision. No link points to a nonexistent ID, but the reverse coverage is incomplete.
- Northbridge SOC 2 Dashboard E4:G8 totals 24 memberships (6 Ready, 17 Partial, 1 Not Ready), while the detail has 22 controls (6, 15, 1). Area definitions overlap or counts are wrong; no control-to-area assignment is recorded to justify an unambiguous correction. Formula-driven overall totals are correct. Crosswalk Control Library risk tiers and SOC2 Control Matrix tiers differ for shared controls (including AC-02 and VM-01/02); their intended meanings are not defined as identical.
- Halcyon inventory Classification Method B8 still treats the deferral as proposed while the header, deadline cells and companion artifacts treat it as enacted. This is a substantive legal-status conflict. The brief forbids silently choosing or softening risky factual claims. Regulatory assertions were not verified in this workbook consistency pass; this report does not endorse them.
- Halcyon AI-009 inventory describes inputs as unknown/likely while AIR-010 treats member-data entry more firmly. No source proof was supplied to resolve that evidentiary difference. The 3% override-rate conclusion elsewhere also remains outside this targeted edit.
- Northgate DRIFT-002 and Halcyon past targets have no current closure evidence or recorded delay cause. Do not turn historical snapshots into newly asserted operational outcomes.

## Chronology and repeated structure

Five Northbridge workbooks share 2026-08-13 assessment dates and closely related dashboards/reference tabs. Meridian vendor assessments repeat 2025-11-01. These are production-pattern signals, but file/assessment dates cannot establish effort spent or prove an implausible production rate. No dates were changed for appearance. Uniform Partially Effective labels in Northbridge, repeated workpaper prose and round sample sizes remain visible. Cascade's later AAR supplies actual superseding scenario evidence; most other books have no decision history. No history was invented.

## Validation and limitations

All 16 workbooks were reopened with openpyxl in formula and data-only modes. All eight edited workbooks were compared against pre-edit copies. The checks verify unique primary IDs, known cross-workbook references, Northgate JSON projections, 71 intended cell changes, all existing formulas and dates, worksheet order, tables, merges, validations, filters, panes, conditional formatting and charts. Style changes are limited to longer-text row heights/wrapping and matching relocated owners to the existing Owner cell style. No score, severity, control determination or date was changed.

The assertion count is a collection of low-level checks, not 6,798 independent audit tests. See `validation.json` for results, per-file hashes, formula/cache counts and independently computed distributions. `cell-changes.json` records exact before/after values and reasons. Formula caches may be blank after openpyxl saves; they are not interpreted as zero. Formula text validation and render-engine recalculation do not establish Excel runtime behavior.

Changed ranges were rendered before and after for visual review. PDF companions were refreshed with LibreOffice; see `pdf-validation.json` for verification and limitations. Synced ChatGPT project references and canonical Control Room state were not edited. A separate SESSION_EVENT draft is prepared for the reconciler and not applied.

## Changed files

- `01-meridian-health-grc-program/artifacts/nist_csf_gap_assessment.xlsx`
- `01-meridian-health-grc-program/pdf/nist_csf_gap_assessment.pdf`
- `01-meridian-health-grc-program/artifacts/risk_register.xlsx`
- `01-meridian-health-grc-program/pdf/risk_register.pdf`
- `02-cascade-civic-rev5-ato/artifacts/customer_responsibility_matrix.xlsx`
- `02-cascade-civic-rev5-ato/pdf/customer_responsibility_matrix.pdf`
- `02-cascade-civic-rev5-ato/artifacts/poam.xlsx`
- `02-cascade-civic-rev5-ato/pdf/poam.pdf`
- `03-northgate-signal-fedramp-20x/artifacts/ksi_validation_register.xlsx`
- `03-northgate-signal-fedramp-20x/pdf/ksi_validation_register.pdf`
- `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/artifacts/Northbridge-Third-Party-Risk-Assessment.xlsx`
- `04-northbridge-cloudworks-grc-program/03-third-party-risk-management/pdf/Northbridge-Third-Party-Risk-Assessment.pdf`
- `05-halcyon-ai-governance/artifacts/ai_control_crosswalk.xlsx`
- `05-halcyon-ai-governance/pdf/ai_control_crosswalk.pdf`
- `05-halcyon-ai-governance/artifacts/ai_system_inventory.xlsx`
- `05-halcyon-ai-governance/pdf/ai_system_inventory.pdf`
- `05-halcyon-ai-governance/README.md`
- `reviews/frictionlessness-2026-09-14/report.md`
- `reviews/frictionlessness-2026-09-14/cell-changes.json`
- `reviews/frictionlessness-2026-09-14/validation.json`
- `reviews/frictionlessness-2026-09-14/pdf-validation.json`
