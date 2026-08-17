# Project 3 Interview Discussion Guide

## Your 60-Second Explanation

> I built a third-party risk assessment for DataFlow AI, a fictional critical SaaS vendor for Northbridge Cloudworks. I classified the vendor's inherent risk, reviewed simulated evidence, scored domains such as governance, IAM, data security, infrastructure, AppSec, incident response, business continuity, and compliance, documented findings, and recommended conditional approval. I used NIST SP 800-161 Rev. 1 Update 1 as the backbone for supply-chain risk thinking and mapped the work to NIST CSF 2.0, CIS Controls, ISO 27001/27002, ISO 27017, NIST 800-53, and SOC 2 evidence concepts.

## Deep-Dive Talking Points

### Why Vendor Risk Matters

> A company can have strong internal controls and still be exposed through a third party. If a vendor processes customer data, integrates with production, or supports a critical process, its security posture becomes part of the company's risk posture.

### Why This Vendor Was Critical

> DataFlow AI was classified as critical because it processed confidential customer data, integrated with production workflows, and could affect customer trust if compromised or unavailable.

### Conditional Approval

> Conditional approval means the vendor is not automatically rejected, but approval depends on closing specific security or contractual gaps. It is a practical risk decision when the business benefit is real and the risk can be reduced to an acceptable level.

### Evidence Review

> I did not rely only on questionnaire answers. I looked for evidence such as SOC 2 reports, policy excerpts, architecture summaries, penetration-test summaries, MFA evidence, IR plans, BCP/DR documentation, and contractual terms.

## Likely Interview Questions and Strong Answer Frames

### Question: How do you classify vendor risk?

Answer:

> I look at the data the vendor handles, system connectivity, business criticality, regulatory or contractual obligations, substitutability, and incident impact. A vendor processing confidential customer data and integrating with production would usually be high or critical risk.

### Question: Why did you conditionally approve instead of reject?

Answer:

> The vendor had a reasonable security foundation, and the gaps were specific and remediable. Rejection would be appropriate if the vendor lacked fundamental controls or refused remediation. Conditional approval allowed the business to move forward while requiring privileged MFA evidence, breach-notification language, annual testing, and IR exercise evidence.

### Question: What evidence would you request from a critical SaaS vendor?

Answer:

> I would request a SOC 2 report or security assurance report, information-security policy, access-control evidence, MFA evidence, penetration-test summary, vulnerability-management process, encryption details, incident-response plan, BCP/DR evidence, subprocessors list, data-retention terms, and breach-notification language.

### Question: What is the difference between a questionnaire and an assessment?

Answer:

> A questionnaire collects vendor answers. An assessment evaluates those answers against evidence, risk context, business impact, and company requirements. The assessment should lead to a decision and remediation plan.

### Question: How would you track vendor findings?

Answer:

> I would document severity, risk, evidence reviewed, recommendation, owner, due date, status, and validation method. For critical vendors, I would track findings through closure and escalate overdue high-risk items.

## STAR Story Frameworks

### STAR 1 - Vendor Assessment

Situation: Northbridge wanted to onboard a vendor that would process customer data.

Task: Determine whether the vendor could be approved safely.

Action: Classified inherent risk, reviewed evidence, scored security domains, documented findings, and built a remediation tracker.

Result: Recommended conditional approval tied to specific remediation requirements.

### STAR 2 - Contractual Risk

Situation: The vendor had security controls but unclear breach-notification terms.

Task: Identify whether this created material risk for Northbridge.

Action: Treated breach notification as both a legal and operational risk because delayed notice could affect customer obligations and incident response.

Result: Required contract language before full approval.

## Role-Play Scenarios

### Role-Play 1 - Business Owner Pushback

Interviewer: "The business needs this vendor now. Why are you slowing it down?"

Your response:

> My goal is not to block the business. It is to make sure the risk is understood and managed before customer data is exposed. I recommended conditional approval, which allows progress while requiring specific controls and contract terms before full production use.

### Role-Play 2 - Vendor Pushback

Interviewer: "The vendor says they cannot share their full penetration test."

Your response:

> I would not require the full sensitive report if that is inappropriate. I would request an executive summary, scope, test date, methodology, severity summary, remediation status, and attestation that critical/high findings were resolved or risk accepted.

### Role-Play 3 - CISO Escalation

Interviewer: "What are the two issues you would escalate?"

Your response:

> I would escalate incomplete privileged MFA evidence and weak breach-notification terms. Those directly affect unauthorized access risk and Northbridge's ability to respond to a customer-impacting incident.

## Questions You Can Ask The Interviewer

- How does your team classify vendors by inherent risk?
- Do you use a GRC platform for vendor reviews or track assessments manually?
- Who owns vendor remediation follow-up: procurement, security, legal, or GRC?
- What evidence do you require from critical SaaS vendors?
- How do you handle business pressure when a vendor has unresolved findings?
