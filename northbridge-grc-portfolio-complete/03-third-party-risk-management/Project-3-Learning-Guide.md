# Project 3 Learning Guide

## What You Need To Understand

This project is about evaluating third-party risk before Northbridge allows a vendor to process customer data or connect to production workflows. Vendor risk is not just a questionnaire. It is classification, evidence review, findings, remediation, contract requirements, and a business decision.

## The Secret Sauce

Many candidates say:

> I can review vendor questionnaires.

A stronger answer is:

> I classified vendor inherent risk, reviewed evidence, scored control domains, documented findings, and recommended conditional approval with specific remediation requirements.

That answer sounds much more job-ready because it shows judgment.

## Core Concepts

### Inherent Vendor Risk

Inherent vendor risk is the risk before considering the vendor's controls. You classify it based on what the vendor does for the company.

DataFlow AI is critical because it:

- Processes confidential customer business data.
- Integrates with production customer-support workflows.
- Could affect customer trust if compromised.
- Depends on cloud and SaaS security controls.

Strong answer:

> I classified the vendor as critical because of data sensitivity, production integration, business dependency, and potential customer impact.

### Residual Vendor Risk

Residual vendor risk is what remains after reviewing the vendor's controls and evidence.

Example:

> The vendor has MFA, SOC 2 evidence, encryption, and policies, but residual risk remains because privileged MFA evidence and breach-notification terms are incomplete.

### Questionnaire vs. Assessment

A questionnaire collects answers. An assessment evaluates whether those answers are supported by evidence and whether the remaining risk is acceptable.

Strong answer:

> I would not approve a vendor based only on yes/no answers. I would review evidence and document findings, conditions, and remediation.

### Conditional Approval

Conditional approval means the vendor can move forward only if specific conditions are met.

This is often more realistic than simply approve or reject.

Strong answer:

> I recommended conditional approval because the vendor had a reasonable security foundation, but unresolved high-risk items needed closure before full production use.

## Where You Should Learn Deeply

### 1. Contract Risk Is Security Risk

Breach notification language is not just legal paperwork. If the vendor does not notify Northbridge quickly, Northbridge may fail customer, legal, or operational obligations.

Strong answer:

> I treated breach-notification language as a security and operational risk because delayed notice can weaken incident response and customer communication.

### 2. SOC 2 Evidence Is Useful But Not Enough

A SOC 2 report can help, but it does not automatically answer every risk question.

Strong answer:

> I would use SOC 2 evidence as one input, then still review scope, exceptions, complementary user entity controls, subservice organizations, and whether the report covers the service being used.

### 3. Vendor Risk Requires Business Judgment

Rejecting every imperfect vendor is not realistic. Approving every vendor is not responsible.

Strong answer:

> The GRC role is to help the business make an informed risk decision, document conditions, and track remediation.

## How To Explain The Workbook

Use this structure:

> The workbook includes a vendor profile, questionnaire, weighted scorecard, findings register, remediation tracker, and decision memo. The scorecard gives a structured view of domain maturity, while the findings register explains the actual risks and conditions for approval.

## Smart Interview Phrases

- "A vendor questionnaire is the input, not the decision."
- "I separate inherent vendor risk from residual vendor risk."
- "Conditional approval is useful when the business need is real and the gaps are specific and remediable."
- "For critical vendors, I would track findings through closure, not just store the questionnaire."
- "Contract terms like breach notification, audit rights, and subprocessors are part of third-party risk."

## Practice Exercise

Pick one vendor finding and answer:

1. What domain does it affect?
2. What evidence was reviewed?
3. Why is the finding a risk to Northbridge?
4. Is it technical, contractual, procedural, or evidence-related?
5. What remediation is required?
6. Who owns the remediation?
7. What evidence would prove closure?
8. Would you approve, reject, or conditionally approve the vendor?
