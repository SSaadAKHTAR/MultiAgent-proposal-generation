# Executive Summary

Northwind Logistics has experienced impressive growth, expanding 40% in 2024 through acquisition. However, incomplete technology integration and legacy systems have created significant operational bottlenecks. Manual double-entry between the custom Ruby on Rails dispatch tool and Salesforce has caused dispatch workflows to stall and driven a three-week delay in billing—trapping $1.4M in working capital and overburdening dispatchers. Additionally, upcoming federal Electronic Logging Device (ELD) compliance mandates require prompt technical alignment.

To resolve these challenges, we propose a fixed-fee, outcome-based engagement designed to deliver immediate operational relief and measurable financial returns. Drawing on our direct experience executing a similar transformation for peer brokerage **Cascade Freight**, our solution will automate data flows between Salesforce, dispatch, and NetSuite accounting, eliminate manual entry, and establish a clean integration layer.

### Key Expected Outcomes
* **$1.4M Working Capital Unlocked:** Accelerate invoicing to achieve the 5-day industry DSO standard.
* **$320k Annual Cost Avoidance:** Streamline dispatcher workflows to reduce handling time per load by 30%, absorbing business growth without adding headcount.
* **Architecture Flexibility:** Ensure 60%–70% of technical assets developed remain fully reusable regardless of future platform decisions.
* **Fixed-Fee Governance:** Deliver complete budget predictability with milestone payments tied directly to verifiable business outcomes.

---

# Understanding

### Current Operational & Technical Challenges
* **Billing Delays & Working Capital Friction:** Discrepancies between Salesforce and the custom Rails dispatch tool leave finance 3 weeks behind on invoicing, trapping $1.4M in unbilled receivables.
* **Dispatcher Workflow Bottlenecks:** 40 dispatchers execute repetitive manual entries across disconnected tools, severely constraining load capacity.
* **Driver Mobile Experience & Compliance:** Drivers report friction with the legacy mobile application, while upcoming November federal ELD compliance requirements create pressing operational risk.
* **Acquisition Debt:** Rapid growth via two recent acquisitions has left backend systems and workflows partially integrated.

### Core Objectives
1. **Financial Velocity:** Return invoicing to a 5-day DSO benchmark by automating data flows between Salesforce, dispatching, and NetSuite accounting.
2. **Dispatcher Efficiency:** Reduce handling time per load by 30%, freeing capacity and saving $320k in fully-loaded annual compensation costs.
3. **Future-Proof Engineering:** Construct clean integration APIs and workflow abstractions over existing systems to protect software investments and allow modular system updates.

---

# Approach

Our approach emphasizes rapid time-to-value, risk reduction, and architectural decoupling. Building on our experience with Cascade Freight, we will introduce a modular integration layer that directly addresses operational bottlenecks without disrupting live freight operations.

```
+-------------------+       +-------------------------------+       +--------------------+
|   Salesforce CRM  | <---> |   Workflow & Integration Layer | <---> |  NetSuite Billing  |
+-------------------+       +---------------+---------------+       +--------------------+
                                            |
                                            v
                               +--------------------------+
                               | Legacy Rails Dispatch App |
                               +--------------------------+
```

### 1. Integration & Workflow Abstraction Layer
* **Automated Sync:** Build secure, real-time API integrations connecting Salesforce, the Rails dispatch tool, and NetSuite to eliminate double-entry and prevent billing discrepancies.
* **Dispatcher Operations:** Streamline load creation, assignment, and status tracking into a single workflow.

### 2. Architecture Decoupling & Risk Mitigation
* **60–70% Code Reusability:** Design workflow logic in an abstraction layer external to core dispatch logic. This ensures that the investments made during this engagement remain intact even if core dispatch infrastructure evolves later.
* **Data Verification:** Execute schema and access pattern reviews during initial setup to validate data integrity across all endpoints.

### 3. Accountable Governance
* **Fixed-Fee Milestones:** Structured milestone deliverables guarantee transparency and address past vendor performance concerns, providing CFO-level visibility into progress and quality.

---

# Phases & Timeline

The proposed timeline spans a 16-week delivery roadmap structured to yield rapid functionality and risk-managed execution:

```
Weeks 01 - 04: Phase 1 — Discovery, Architecture & Schema Validation
Weeks 05 - 10: Phase 2 — Integration Layer & Automated Invoicing Build
Weeks 11 - 14: Phase 3 — Pilot Rollout & Workflow Optimization
Weeks 15 - 16: Phase 4 — Final Production Deployment & Handoff
```

### Phase 1: Discovery, Architecture & Schema Validation (Weeks 1–4)
* Conduct schema review and access analysis for the Rails dispatch tool and Salesforce.
* Finalize API mapping specifications for automated NetSuite billing integration.
* Establish baseline metrics for DSO and dispatcher load handling times.

### Phase 2: Integration Layer & Automated Invoicing Build (Weeks 5–10)
* Develop the workflow abstraction layer and automated bidirectional data sync between Salesforce and dispatch.
* Construct automated invoicing data validation pipelines to eliminate billing discrepancies.
* Conduct end-to-end integration testing with finance and dispatch leads.

### Phase 3: Pilot Rollout & Workflow Optimization (Weeks 11–14)
* Deploy the streamlined workflow to a designated pilot group of dispatchers.
* Measure and refine dispatch handling times toward the target 30% reduction goal.
* Validate automated invoicing flows to ensure DSO reduction toward the 5-day target.

### Phase 4: Final Production Deployment & Handoff (Weeks 15–16)
* Roll out integrations across all 40 dispatchers.
* Deliver technical documentation and operational runbooks to internal engineering teams.
* Complete project sign-off and transition to operational maintenance.

---

# Pricing Approach

Based on benchmark data from similar logistics and freight brokerage engagements involving a specialized team of 4–5 engineering and integration experts, typical scopes range between **$150,000 and $250,000**.

We propose a fixed-fee engagement model totaling **$225,000**, structured around concrete deliverable milestones to eliminate financial risk and ensure complete budget alignment.

### Proposed Fixed-Fee Structure

| Milestone | Deliverable / Outcome | Payment |
| :--- | :--- | :--- |
| **Milestone 1: Discovery & Integration Blueprint** | System schema review completed, integration architecture finalized, and data sync specs approved. | **$50,000** |
| **Milestone 2: Integration & Invoicing Engine** | Abstraction layer built, bidirectional Salesforce/dispatch sync live in staging, NetSuite billing automation verified. | **$100,000** |
| **Milestone 3: Pilot Deployment & Validation** | Pilot rollout completed, verification of dispatch efficiency metrics and 5-day DSO target enablement. | **$75,000** |
| **Total Fixed Fee** | | **$225,000** |

* **Model Benefits:** 100% fixed fee with zero time-and-materials uncertainty. Fees are tied directly to sign-off on concrete business deliverables.

---

# Open Questions

To ensure total alignment across leadership, the following items require formal clarification prior to project initiation:

1. **Phase 1 Budget Limit Alignment:** Internal discussions reflect differing budget expectations, ranging from a strict $300,000 cap enforced by CFO Rita Donovan to a $250,000–$400,000 range noted by VP of Operations Sarah Chen. *Area needing clarification:* Confirmation that our proposed fixed-fee total of $225,000 satisfies all internal governance constraints.
2. **Platform Strategy Direction:** Stakeholders hold differing views on platform direction—VP of Operations Sarah Chen favors resolving workflow pain points on top of the current dispatch tool, whereas CTO Marcus Patel advocates evaluating a full $600,000/year SaaS replacement. *Area needing clarification:* Formal alignment on using our proposed abstraction layer design to solve immediate operational pain while preserving 60–70% reusability if a platform replacement is pursued in the future.
3. **Pilot Target Release Schedule:** Target timeline expectations differ between executive stakeholders, with Sarah Chen and Rita Donovan targeting an end-of-Q3 production pilot, while Marcus Patel estimates a Q4 timeline as more realistic. *Area needing clarification:* Agreement on a finalized pilot deployment date within the 16-week delivery roadmap.
4. **Driver App Scope & Federal ELD Compliance Mandate:** The upcoming November 15 federal ELD compliance mandate impacts driver mobile workflows. *Area needing clarification:* Decoupling strategy and timing for mobile driver app updates relative to the ELD compliance work stream to guarantee uninterrupted operating authority.