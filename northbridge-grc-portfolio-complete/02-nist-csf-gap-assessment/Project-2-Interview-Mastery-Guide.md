# Project 2 Interview Mastery Guide

## Your 60-Second Explanation

> I built a NIST CSF 2.0 gap assessment for Northbridge Cloudworks, the same fictional SaaS company from my risk assessment project. I assessed selected outcomes across GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, and RECOVER. For each outcome, I documented current state, target state, evidence, gap, risk, recommendation, owner, priority, and roadmap timing. I intentionally avoided calling it a certification score because NIST CSF is a voluntary framework for managing and communicating cybersecurity risk.

## Deep-Dive Talking Points

### Current Profile vs. Target Profile

> The current profile describes what the organization does today. The target profile describes the intended cybersecurity outcomes based on risk, business needs, and maturity goals. The gap is the difference between the two.

### Why GOVERN Matters

> NIST CSF 2.0 added GOVERN as a core function, which is important for GRC work because it connects cybersecurity outcomes to accountability, policy, oversight, risk management strategy, supply chain, and executive decision-making.

### Why This Is Not a Checklist

> I treated CSF 2.0 as a framework for outcomes and communication. The point was not to mark boxes, but to identify where Northbridge's current practices were below the target state and then build a prioritized roadmap.

## Likely Interview Questions and Strong Answer Frames

### Question: How did you perform the CSF gap assessment?

Answer:

> I selected relevant CSF 2.0 outcomes for a SaaS company, documented the current state and available evidence, defined a reasonable target state, identified the gap, assessed the business risk, and created prioritized remediation actions with owners and timeframes.

### Question: What is the difference between NIST CSF and NIST 800-53?

Answer:

> NIST CSF is an outcome-oriented cybersecurity framework used to organize and communicate risk-management outcomes. NIST SP 800-53 is a detailed catalog of security and privacy controls. In my project, CSF 2.0 structures the gap assessment, while 800-53 can support more detailed control selection and testing.

### Question: How would you prioritize gaps?

Answer:

> I would prioritize based on business impact, risk reduction, regulatory or customer commitments, control dependencies, and effort. For example, privileged access and incident response are high priorities because failure in those areas can amplify many other risks.

### Question: What evidence would you expect for a CSF outcome?

Answer:

> It depends on the outcome. For policy governance, I would expect approved policies, review dates, ownership, and approval records. For access control, I would expect identity-provider configuration, user exports, MFA reports, access reviews, and exception records.

### Question: How would you explain the results to executives?

Answer:

> I would avoid framework jargon first. I would explain the top business risks, the most important gaps, the decisions needed from leadership, the 90-day priorities, and how progress will be measured. The detailed CSF mapping supports the analysis, but the executive message should be risk and action oriented.

## STAR Story Frameworks

### STAR 1 - Building a CSF Gap Assessment

Situation: Northbridge needed to understand cybersecurity maturity against NIST CSF 2.0.

Task: Build a current-versus-target assessment and remediation roadmap.

Action: Assessed outcomes across six CSF functions, documented evidence and gaps, assigned owners, and prioritized remediation.

Result: Produced a roadmap that leadership could use for governance, audit readiness, and security planning.

### STAR 2 - Turning Findings Into Roadmap Actions

Situation: Several controls existed but were inconsistently governed.

Task: Convert assessment gaps into practical remediation.

Action: Grouped actions into 0-30, 31-90, 3-6 month, and 6-12 month phases based on risk and dependency.

Result: Made the assessment actionable instead of leaving it as a static checklist.

## Role-Play Scenarios

### Role-Play 1 - Hiring Manager Challenge

Interviewer: "Why shouldn't we just use a percentage score for NIST CSF?"

Your response:

> A percentage can be useful internally if the scoring method is clear, but I would be careful not to imply NIST certification or precision that does not exist. I prefer current state, target state, gap, risk, and roadmap because that better supports decisions.

### Role-Play 2 - Executive Briefing

Interviewer: "You have two minutes with the CEO. What do you say?"

Your response:

> Northbridge has a reasonable security foundation, but the program is not yet consistently governed or evidenced. The highest priorities are privileged access, vendor risk, incident-response testing, recovery testing, and executive security metrics. The recommended plan focuses first on reducing risks that could affect customer trust, service availability, and future audit readiness.

### Role-Play 3 - Auditor Conversation

Interviewer: "How do you prove a CSF outcome is implemented?"

Your response:

> I would translate the outcome into control expectations and request evidence. Then I would inspect whether the evidence proves design and operating effectiveness. For example, a policy outcome needs an approved policy, owner, review cadence, and evidence that people actually follow it.

## Questions You Can Ask The Interviewer

- How does your team use NIST CSF: assessment, reporting, roadmap planning, or customer assurance?
- Do you maintain current and target profiles?
- How do you track remediation after a framework assessment?
- What evidence systems or GRC tools do analysts use day to day?
