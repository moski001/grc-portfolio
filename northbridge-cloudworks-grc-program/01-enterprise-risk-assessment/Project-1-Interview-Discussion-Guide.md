# Project 1 Interview Discussion Guide

## Your 60-Second Explanation

> I built an enterprise cybersecurity risk assessment for Northbridge Cloudworks, a fictional AWS-hosted SaaS company. I identified 20 realistic cyber risks, scored inherent and residual risk, documented existing controls, evaluated control effectiveness, assigned owners and treatment plans, and created an executive dashboard. I used NIST SP 800-30 for risk assessment, the NIST IR 8286 Rev. 1 series for enterprise-risk integration, NIST SP 1308 for CSF 2.0 and ERM alignment, and NIST CSF 2.0 to organize the risk themes.

## Deep-Dive Talking Points

### Why NIST SP 800-30?

Use this when asked about methodology:

> NIST SP 800-30 is useful because it frames risk assessment as a way to inform decision-makers. I used it to structure risk scenarios around threats, vulnerabilities, likelihood, impact, and response. I did not treat it as a compliance checklist.

### Why NIST IR 8286 Rev. 1?

Use this when asked about executive reporting:

> The IR 8286 series helped me think beyond technical risk. It emphasizes that cyber risk should feed enterprise risk management, so I included business process, owner, residual rating, treatment plan, escalation status, and due date.

### Why Residual Risk Matters

Use this when asked about control maturity:

> Inherent risk shows how bad the scenario could be before controls. Residual risk shows what remains after controls. That distinction matters because management should not assume a risk is solved just because a control exists.

## Likely Interview Questions and Strong Answer Frames

### Question: Walk me through your risk assessment process.

Structured answer:

1. Defined scope and business context.
2. Identified assets, threats, and vulnerabilities.
3. Wrote risk statements in cause-event-impact form.
4. Scored inherent likelihood and impact.
5. Documented existing controls.
6. Evaluated control effectiveness.
7. Scored residual risk.
8. Recommended treatment, owner, and due date.
9. Summarized top risks for leadership.

### Question: How did you decide whether a risk was high?

Answer:

> I used a 1-5 likelihood by 1-5 impact matrix. A high risk was not just a big number; it had a plausible scenario, meaningful business impact, and control gaps that left material residual exposure. I also considered whether the risk affected customer data, production availability, legal obligations, or executive commitments.

### Question: What is the difference between a vulnerability and a risk?

Answer:

> A vulnerability is a weakness, such as inconsistent MFA enforcement. A risk is the business-relevant scenario that could result, such as unauthorized access to customer data through a compromised privileged account.

### Question: How would you validate whether a control is operating effectively?

Answer:

> I would request evidence tied to the control objective. For MFA, I would inspect identity-provider policy configuration, review user enrollment exports, sample privileged accounts, and confirm exceptions are approved and time-bound.

### Question: What would you escalate to leadership?

Answer:

> I would escalate high residual risks where remediation requires funding, cross-functional ownership, risk acceptance, or policy enforcement. Examples include privileged access, ransomware readiness, cloud misconfiguration, critical vendor exposure, and incident-response preparedness.

## STAR Story Frameworks

### STAR 1 - Building a Risk Register

Situation: Northbridge lacked a formal enterprise cyber risk register.

Task: Build a register that leadership could use for prioritization.

Action: Defined scoring scales, identified 20 risks, mapped controls, calculated inherent and residual risk, and assigned owners and treatment plans.

Result: Created an executive-ready risk view that highlighted top residual risks and 90-day priorities.

### STAR 2 - Challenging Control Assumptions

Situation: MFA existed in the environment.

Task: Determine whether MFA sufficiently reduced privileged access risk.

Action: Treated MFA as partially effective because enforcement was inconsistent for privileged accounts and exceptions lacked formal review.

Result: Recommended phishing-resistant MFA for administrators, quarterly access reviews, and exception reporting.

## Role-Play Scenarios

### Role-Play 1 - CISO Pushback

Interviewer: "We already have MFA. Why is privileged access still high risk?"

Your response:

> MFA reduces risk, but only if it is consistently enforced and appropriate for the account type. For privileged users, I would look for phishing-resistant MFA where supported, no unmanaged exceptions, logs showing enforcement, and periodic access reviews. If those are incomplete, the control is only partially effective.

### Role-Play 2 - Executive Summary

Interviewer: "Explain your top risk to a nontechnical executive."

Your response:

> The biggest concern is that a compromised administrator account could give an attacker broad access to systems that support our product and customer data. The business impact is customer trust, outage potential, legal exposure, and response cost. The near-term fix is stronger admin authentication, access review, and monitoring.

### Role-Play 3 - Auditor Evidence Request

Interviewer: "What evidence would you request for access control?"

Your response:

> I would request identity-provider policy settings, privileged user lists, MFA enrollment reports, recent access-review evidence, exception approvals, and logs showing authentication events. Then I would compare the evidence to the control objective and note any exceptions.

## Questions You Can Ask The Interviewer

- How does your team decide when cyber risk should be escalated to enterprise risk leadership?
- Do analysts own risk-register maintenance, evidence collection, control testing, or all three?
- What frameworks are most important in your current GRC program?
- How are remediation owners held accountable after findings are opened?
