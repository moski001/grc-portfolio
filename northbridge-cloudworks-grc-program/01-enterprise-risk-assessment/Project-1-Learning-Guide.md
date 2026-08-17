# Project 1 Learning Guide

## What You Need To Understand

A risk assessment is not just a list of scary events. It is a decision-support process. You identify what could go wrong, why it could happen, how bad it could be, what controls already exist, what risk remains, and what management should do.

## Core Concepts

### Inherent Risk

Inherent risk is the level of risk before considering existing controls. Example: if privileged accounts can access production systems, the inherent impact of compromise is severe even if some controls exist.

### Residual Risk

Residual risk is what remains after existing controls are considered. If MFA exists but is not enforced for all administrators, residual risk may remain high because the control is only partially effective.

### Control Effectiveness

A control can exist and still be weak. In interviews, say:

> I separated control existence from control effectiveness. A policy or tool alone does not prove risk is managed; I looked for consistency, ownership, evidence, and whether the control actually reduced the scenario.

### Risk Treatment

Risk treatment is the management decision. The analyst can recommend, but leadership owns acceptance of material residual risk.

## Three Risks To Practice First

### R-001 Privileged Account Compromise

Explain it this way:

> The asset is privileged access to cloud, identity, and administrative systems. The threat is credential theft or session compromise. Existing controls include MFA and access logging, but the residual risk remains high if phishing-resistant MFA is not enforced for privileged users and access reviews are inconsistent.

### R-003 AWS Misconfiguration

Explain it this way:

> The issue is not simply cloud security in general. The risk scenario is customer data exposure because storage, IAM, network, or logging settings could be misconfigured. The treatment plan focuses on configuration monitoring, least privilege, security review of infrastructure changes, and evidence collection.

### R-015 Incident-Response Testing Gap

Explain it this way:

> Having an incident-response plan is not the same as being ready. A tabletop exercise tests roles, escalation paths, legal/customer notification decisions, and executive communication under pressure.

## How To Talk About Standards

Use this structure:

> I used NIST SP 800-30 for the risk-assessment method, then supplemented it with the NIST IR 8286 Rev. 1 series because the goal was not only to score technical risks but to make them usable in enterprise risk management. I used NIST CSF 2.0 to organize the work around governance, identification, protection, detection, response, and recovery.

## Common Mistakes To Avoid

- Do not say NIST CSF is a certification.
- Do not imply SOC 2 has a "2026 version."
- Do not describe risk scoring as objective math; it is a structured estimate.
- Do not say a control is effective just because a tool exists.
- Do not accept high residual risk without a business owner.

## Practice Exercise

Pick one risk and answer:

1. What business process is affected?
2. What asset or data is at risk?
3. What threat and vulnerability create the scenario?
4. What is the inherent risk?
5. What controls exist?
6. Why is residual risk lower, equal, or still high?
7. What treatment did you recommend?
8. What evidence would you request to validate the control?
