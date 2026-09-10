# Proposal for Northwind Logistics

## Executive Summary

Northwind Logistics has achieved rapid expansion, growing 40% in 2024 through acquisition to reach ~$85M in annual revenue. However, this growth has strained operational infrastructure. Dispatchers face heavy manual entry between the custom Rails dispatch system and Salesforce, driver mobile app adoption is lagging, and finance is delayed three weeks on invoicing, leaving approximately $1.4M in working capital locked in unbilled receivables.

To unlock this capital and support scalable growth, Northwind Logistics requires a modern, streamlined workflow that integrates dispatch, CRM, and accounting systems while preparing for critical regulatory milestones. Building on our successful engagement with peer freight brokerage Cascade Freight, we propose a structured, fixed-fee Phase 1 engagement focused on automated data synchronization, dispatcher workflow reduction, and driver mobile app enhancements. 

Our approach delivers immediate operational relief—targeting a 30% reduction in dispatch time and a return to a 5-day Days Sales Outstanding (DSO)—while establishing a resilient integration architecture that protects your technology investment through future platform evaluations.

---

## Understanding

### Current Operational & Technical Landscape
Northwind’s operations depend on a 7-year-old custom Ruby on Rails dispatch application maintained by an internal team of two engineers, alongside Salesforce Sales Cloud and NetSuite. Recent acquisitions have left technical integration incomplete across these platforms, resulting in fragmented workflows:
* **Dispatcher Workflow Friction:** 40 dispatchers perform repetitive manual double-entry between the custom dispatch tool and Salesforce. Reducing dispatch time per load by 30% is critical to scale without adding four headcount positions.
* **Financial Delays:** Invoicing lags by three weeks due to cross-system data misalignment between dispatch and NetSuite, locking ~$1.4M in unbilled receivables. Restoring a 5-day DSO will immediately free this working capital.
* **Driver Mobile Experience:** Approximately 600 contracted drivers utilize a custom React Native app (last updated in 2023) that suffers from poor driver satisfaction and adoption.

### Critical Risks & Context
* **Failed Internal Attempts:** Two prior internal initiatives to resolve these exact workflow inefficiencies ended in failure. The custom dispatch codebase has become fragile, making feature delivery difficult and risky for internal teams working in isolation. This history reinforces the necessity of an experienced external partner bringing proven integration patterns, rigorous project governance, and specialized execution capacity.
* **Regulatory Deadlines:** Upcoming federal Electronic Logging Device (ELD) mandate updates in November require close alignment with Head of Compliance Rajiv Mehta to ensure driver mobile app modifications do not disrupt compliance or risk operating authority.
* **Acquisition & System Transition:** The technical architecture must account for incomplete legacy integrations while remaining flexible as Northwind evaluates new Transportation Management System (TMS) vendors.

---

## Approach

Our proposed approach balances immediate operational impact with long-term architectural stability:

1. **Decoupled Workflow & Integration Layer:**
   We will design and implement automated data synchronization between the custom Rails app, Salesforce, and NetSuite. By decoupling business logic from the fragile Rails monolith, we ensure that 60% to 70% of the integration and workflow logic created in Phase 1 will survive any future platform migration or TMS adoption.

2. **Dispatcher Workflow Automation:**
   Eliminate redundant manual entry by establishing real-time data flows between Salesforce load records and dispatch queues, directly cutting dispatch processing time.

3. **Driver Mobile App Modernization & Compliance Alignment:**
   Refactor the React Native driver application to improve user experience, field data capture, and proof-of-delivery uploads. All mobile app updates will be strictly coordinated with the ELD compliance requirements to ensure zero disruption to regulatory mandates.

4. **Milestone-Based Delivery Governance:**
   In recognition of prior vendor experiences and internal project hurdles, our team will utilize outcome-based milestones, clear acceptance criteria, and weekly steering updates to maintain full visibility and risk control.

---

## Phases & Timeline

The proposed Phase 1 engagement spans a structured execution roadmap designed to mitigate technical debt and deliver incremental value:

```
+-----------------------------------------------------------------------------------+
|  Phase 1: Discovery, Architecture & Compliance Alignment (Weeks 1–3)              |
|  - System mapping (Rails, Salesforce, NetSuite) & compliance coordination         |
|  - Target integration architecture & survival layer definition                    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  Phase 2: Workflow Automation & Driver App Enhancement (Weeks 4–9)                |
|  - Bi-directional data synchronization build (Salesforce <-> Rails <-> NetSuite)   |
|  - Mobile app UX refactoring & automated invoicing payload validation             |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|  Phase 3: Pilot Deployment, Validation & Rollout (Weeks 10–12)                   |
|  - Operational pilot deployment with core dispatcher cohort                       |
|  - DSO reduction validation, user feedback iteration, and handover                |
+-----------------------------------------------------------------------------------+
```

* **Phase 1: Discovery, Architecture & Compliance Alignment (Weeks 1–3)**
  * Technical discovery across Rails codebase, Salesforce, NetSuite, and Excel BI routines.
  * Formal alignment with Compliance (Rajiv Mehta) on ELD regulatory requirements.
  * Architectural specification for the durable workflow integration layer.

* **Phase 2: Automated Workflow & Mobile Enhancement Build (Weeks 4–9)**
  * Core integration build automating load creation, status updates, and invoicing data synchronization.
  * Refactoring of driver mobile app interfaces for streamlined proof-of-delivery capture.
  * End-to-end integration testing between dispatch records and NetSuite billing.

* **Phase 3: Pilot Deployment & Outcome Validation (Weeks 10–12)**
  * Controlled pilot deployment with a representative dispatcher team and driver group.
  * Measurement of DSO impact, unbilled receivables reduction, and dispatch cycle times.
  * Handover documentation and transition support for internal engineering (2 Rails developers).

---

## Pricing Approach

To align with CFO Rita Donovan’s preference for budget predictability and risk mitigation, we propose a **Fixed-Fee, Milestone-Based Contract**. Based on our experience with similar mid-market freight brokerages requiring 3-month MVP builds with a 4-person consulting team, the typical price band ranges from **$150,000 to $250,000**.

### Proposed Payment Schedule

| Milestone | Deliverable / Outcome | Payment % |
| :--- | :--- | :--- |
| **Milestone 1: Project Initiation & Architecture Sign-off** | Completion of technical discovery, integrated architecture spec, and ELD compliance plan | 25% |
| **Milestone 2: Integration & Mobile App MVP Build** | Functional data synchronization between Rails, Salesforce, and NetSuite; updated driver mobile build | 40% |
| **Milestone 3: Pilot Deployment & Acceptance** | Successful production pilot rollout, dispatcher workflow verification, and operational sign-off | 35% |

---

## Open Questions

To ensure full alignment across all executive stakeholders before project launch, the following items require explicit resolution during project kickoff:

1. **Platform Strategy Alignment (Full SaaS Rebuild vs. Incremental Workflow Optimization)**
   * *Context:* CTO Marcus Patel favors replacing the existing custom Rails app ("Routemaster") with a complete SaaS TMS platform, whereas VP Operations Sarah Chen favors incremental workflow fixes on the existing infrastructure.
   * *Clarification Needed:* We need to confirm that our proposed decoupled integration layer—which ensures 60–70% of built logic survives a future SaaS transition—satisfies both immediate operational relief and long-term technical strategy.

2. **Target Pilot Deployment Timeline Alignment (Q3 vs. Q4)**
   * *Context:* Operations and Finance mandate a production pilot by end of Q3 (September 30), whereas Engineering views Q4 as a more technically realistic target given codebase constraints.
   * *Clarification Needed:* Stakeholders must agree on the exact MVP feature boundary for Phase 1 to guarantee a safe, reliable release that meets the September 30 target without compromising core system stability.

3. **Phase 1 Budget Authorization Cap**
   * *Context:* CFO Rita Donovan has stated a strict budget cap of $300,000 for the Phase 1 engagement, whereas VP Operations Sarah Chen previously discussed a budget range of $250,000 to $400,000.
   * *Clarification Needed:* Formal confirmation of the approved budget ceiling ($300,000 cap) prior to finalizing the fixed-fee milestone schedule.