# Northbridge NIST CSF 2.0 Gap Assessment Report

## Executive Summary

Northbridge Cloudworks has several foundational cybersecurity practices in place, including MFA, cloud hosting controls, endpoint security, vulnerability scanning, and incident-response documentation. However, many practices are inconsistent, not fully evidenced, or not formally governed. The largest gaps are in governance cadence, policy lifecycle management, third-party risk, security metrics, incident-response exercising, recovery testing, and control-owner accountability.

The assessment uses NIST CSF 2.0's six functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, and RECOVER. It compares Northbridge's current profile against a realistic target profile for a 120-person B2B SaaS company preparing for stronger customer security reviews and future SOC 2 readiness.

## Assessment Method

Each selected CSF outcome was assessed using:

- Current implementation status
- Evidence available
- Target state
- Gap description
- Business risk
- Recommended action
- Owner
- Priority
- Target date

Implementation status categories:

- Implemented
- Partially Implemented
- Not Implemented
- Not Applicable

## Key Findings by Function

| Function | Summary Finding | Overall Maturity |
|---|---|---|
| GOVERN | Security responsibilities exist informally, but policy review, risk appetite, and metrics need formalization | Partial |
| IDENTIFY | Assets and vendors are known, but inventories and risk ownership need stronger governance | Partial |
| PROTECT | MFA, endpoint protection, and access controls exist, but privileged access and training evidence need improvement | Partial |
| DETECT | Logs exist across key systems, but centralized alerting and detection coverage need stronger ownership | Partial |
| RESPOND | Incident-response plan exists, but tabletop testing and communication playbooks need improvement | Partial |
| RECOVER | Backups exist, but recovery testing and executive recovery metrics are immature | Partial |

## Highest Priority Gaps

| Priority | Gap | Recommended Action |
|---:|---|---|
| 1 | No formal cybersecurity governance cadence | Establish quarterly security risk review with executive reporting |
| 2 | Privileged access controls inconsistent | Enforce phishing-resistant MFA and quarterly privileged access reviews |
| 3 | Vendor risk tiering incomplete | Implement critical vendor classification and annual reviews |
| 4 | Incident-response plan not exercised | Conduct tabletop exercise aligned to NIST SP 800-61 Rev. 3 |
| 5 | Recovery testing incomplete | Conduct backup restoration and disaster-recovery test |

## 12-Month Roadmap

### 0-30 Days

- Confirm security governance owners.
- Approve policy review calendar.
- Create risk and gap remediation tracker.
- Identify critical systems and critical vendors.
- Enforce no unmanaged exceptions for privileged MFA.

### 31-90 Days

- Complete privileged access review.
- Establish vulnerability remediation SLAs.
- Implement vendor risk tiering.
- Define core security metrics and KRIs.
- Build evidence folders for key controls.

### 3-6 Months

- Conduct incident-response tabletop exercise.
- Test backup restoration.
- Complete critical vendor assessments.
- Formalize security awareness evidence.
- Review cloud configuration monitoring results.

### 6-12 Months

- Conduct disaster-recovery exercise.
- Mature control testing using NIST SP 800-53A concepts.
- Prepare SOC 2 readiness evidence list.
- Implement continuous control monitoring for highest-risk controls.
- Present cybersecurity risk posture to executive leadership.

## Interview-Ready Conclusion

Northbridge does not need a theoretical framework score. It needs a practical, risk-based roadmap. The CSF 2.0 gap assessment shows how governance, risk, controls, evidence, incident response, recovery, and vendor risk connect to business objectives. The most important message for leadership is that many controls exist, but maturity depends on ownership, evidence, cadence, testing, and remediation follow-through.
