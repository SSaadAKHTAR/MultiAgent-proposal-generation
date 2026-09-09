# Proposal: Operational Workflow Optimization & Integration

**Prepared for:** Sarah Chen, VP Operations | Northwind Logistics  
**Prepared by:** Senior Management Consulting Team  
**Date:** March 2025  

---

## Executive Summary

Northwind Logistics has achieved impressive growth, expanding revenue to ~$85M in 2025 and increasing operations by 40% in 2024 following two acquisitions. However, this rapid scaling has exposed operational bottlenecks across your 40 dispatchers, ~600 contracted drivers, and finance team. Disconnected systems—specifically double-entry between your custom Rails dispatch application and Salesforce—have delayed invoicing by three weeks, locking up **$1.4M in working capital** and stretching Days Sales Outstanding (DSO).

Building on our experience delivering similar integration and workflow transformations for peer freight brokerages such as Cascade Freight, we propose a targeted Phase 1 engagement. Our objective is to streamline dispatcher workflows, eliminate manual re-entry, integrate invoicing with NetSuite, and improve the driver experience—all while ensuring strict coordination with upcoming federal regulatory mandates.

By modernizing core workflows and establishing clean system integrations, this initiative aims to unlock $1.4M in tied-up working capital, achieve a 30% reduction in dispatch time per load, and avoid $320k in recurring annual dispatch headcount costs, establishing a scalable foundation for Northwind’s continued expansion.

---

## Understanding

Based on our discussions and technical reviews, Northwind Logistics operates in a fast-paced mid-market freight brokerage environment with specific operational and technical realities:

### Key Operational & Financial Bottlenecks
* **Invoicing Delays & Working Capital:** Finance is currently 3 weeks behind on invoicing due to manual data misalignment between core systems. This delay ties up $1.4M in working capital in unbilled receivables and elevates DSO beyond industry standards (targeting a return to a 5-day DSO).
* **Dispatcher Overhead:** 40 dispatchers perform repetitive manual re-entry between the custom dispatch tool and Salesforce. Eliminating this double-entry will reduce dispatch time per load by 30% and eliminate the need to hire four additional dispatchers (saving ~$320k annually).
* **Driver Experience & Compliance:** ~600 contracted drivers use a custom React Native mobile app (last updated in 2023) that experiences friction. Furthermore, an upcoming federal ELD compliance update in November represents a critical regulatory deadline requiring technical coordination.
* **M&A Integration Debt:** Operational systems reflect unintegrated tech components following two 2024 brokerage acquisitions.

### Existing Architecture & Technical Environment
* **Dispatch System:** Custom Rails 5 application ("Routemaster"), maintained internally by 2 engineers, carrying technical debt that slows feature velocity.
* **CRM & Accounting:** Salesforce (Sales Cloud) for CRM; NetSuite for accounting. Data exchange currently relies on manual transfer and Excel exports for BI reporting.
* **TMS Evaluation:** TMS vendor evaluation is underway, meaning any integration architecture built today must be modular and decoupled to protect investments against future platform decisions.

---

## Approach

Our approach emphasizes incremental operational improvement, tight technical execution, and modular architecture designed to solve immediate pain points without locking Northwind into a single technical path.

```
+-----------------------------------------------------------------------------------+
|                            Northwind Workflow Layer                               |
|   +--------------------------+  +--------------------------+  +-----------------+ |
|   | Dispatcher Single-Entry  |  | Automated Billing Bridge |  | Driver App & ELD| |
|   +------------+-------------+  +------------+-------------+  +--------+--------+ |
+----------------|-----------------------------|-------------------------|----------+
                 |                             |                         |
                 v                             v                         v
+-----------------------------------------------------------------------------------+
|                         Decoupled Integration Services                            |
+-------------------+--------------------------+-------------------------+----------+
                    |                          |                         |
                    v                          v                         v
        +-----------------------+   +--------------------+    +---------------------+
        | Rails / Routemaster   |   | Salesforce CRM     |    | NetSuite Accounting |
        +-----------------------+   +--------------------+    +---------------------+
```

### Core Solution Pillars

1. **Dispatcher Workflow Automation & Single-Entry Sync**
   * Establish automated, bi-directional API synchronization between Salesforce and the dispatch system.
   * Eliminate manual double-entry for load creation, status updates, and rate confirmations.

2. **Automated Billing & NetSuite Invoicing Bridge**
   * Audit field mappings and data validation rules required by NetSuite to automate invoice creation upon load completion.
   * Bridge the 3-week invoicing gap to release $1.4M in unbilled receivables and accelerate DSO toward the 5-day baseline.

3. **Driver Mobile App & Regulatory Alignment**
   * Perform targeted updates to the React Native driver app to fix driver usability pain points.
   * Coordinate driver workflow updates with the November federal ELD compliance mandate to prevent disruption to operating authority.

4. **Modular Integration Architecture**
   * Build clean, documented API contracts and middleware logic separate from legacy Rails core code, ensuring business logic remains portable for any future platform transitions.

---

## Phases & Timeline

We structure this Phase 1 initiative across a 6-month roadmap designed to deliver early operational wins while preparing for regulatory milestones.

```
Month 1           Month 2           Month 3           Month 4           Month 5           Month 6
[--- Phase 1A ---][-------- Phase 1B --------][-------- Phase 1C --------][-------- Phase 1D --------]
  Discovery &       Invoicing & Dispatch        Driver App & Pilot        Hardening & ELD
  Architecture      Integration Build           Deployment                Mandate Rollout
```

### Phase Breakdown

* **Phase 1A: Discovery, Integration Design & ELD Alignment (Weeks 1–4)**
  * Map end-to-end data flows across Salesforce, Routemaster, and NetSuite.
  * Define field-level mapping and API specs to resolve invoicing data gaps.
  * Review compliance requirements for the November ELD mandate with internal technical and compliance leads.

* **Phase 1B: Core Invoicing & Dispatch Workflow Integration (Weeks 5–12)**
  * Develop bi-directional sync between Salesforce and dispatch tooling.
  * Implement automated invoicing data bridge to NetSuite.
  * Deploy automated validation checks to stop bad data before billing.

* **Phase 1C: Driver App Refinement & Production Pilot Deployment (Weeks 13–18)**
  * Implement targeted React Native driver app fixes for dispatch confirmation and load tracking.
  * Launch production pilot with a select group of dispatchers and drivers.
  * Monitor billing cycle improvement and measure reduction in dispatch handling time.

* **Phase 1D: Hardening, Full Rollout & ELD Finalization (Weeks 19–24)**
  * Roll out single-entry dispatch workflows across all 40 dispatchers.
  * Finalize driver app updates and verify federal ELD mandate compliance ahead of the November deadline.
  * Transition documentation and integration maintenance to internal engineering.

---

## Pricing Approach

To provide budget predictability and align directly with executive financial priorities, we propose a **Fixed-Fee Model with Milestone-Based Payments** tied directly to tangible operational outcomes.

Based on benchmark pricing for similar peer engagements (such as a 4-person consulting team delivering a 3-month discovery and MVP build in the $150k–$250k range), our fixed-fee engagement structure ensures complete transparency without the uncertainty of Time & Materials billing.

### Proposed Milestone Payment Structure

| Milestone | Deliverable / Outcome | Payment % |
| :--- | :--- | :--- |
| **Milestone 1: Project Initiation & Architecture** | Delivery of validated field mapping, API specifications, and ELD compliance integration plan. | 25% |
| **Milestone 2: Invoicing Bridge Deployment** | Completion and validation of NetSuite automated invoicing integration in staging environment. | 25% |
| **Milestone 3: Production Pilot Launch** | Successful release of dispatch integration and mobile app updates to pilot group. | 25% |
| **Milestone 4: Full Rollout & Compliance Handover** | Full deployment across all 40 dispatchers, complete NetSuite automated billing, and ELD verification. | 25% |

*Note: Specific fixed-fee cap alignment is referenced in Open Questions below to ensure full alignment across executive stakeholders.*

---

## Open Questions

To ensure total alignment before signing, the following items require explicit joint review and clarification:

1. **Phase 1 Budget Cap Alignment**
   * *Context:* Internal discussions indicate a variance between the strict $300,000 budget cap requested by CFO Rita Donovan and the $250,000–$400,000 range discussed with VP Operations Sarah Chen.  
   * *Clarification Needed:* We need to formalize the agreed-upon fixed-fee contract ceiling and ensure milestone scope aligns directly with CFO sign-off.

2. **Long-Term System Strategy (SaaS Replacement vs. Incremental Rails Refactoring)**
   * *Context:* Operational leadership focuses on incremental workflow fixes within the current custom Rails application, while technical leadership leans toward replacing legacy tooling with an off-the-shelf SaaS platform.
   * *Clarification Needed:* We must confirm that our proposed decoupled integration design satisfies immediate dispatcher needs while preserving complete flexibility for any future SaaS TMS transition.

3. **Phase 1 Code Survival Target (60–70% Portability)**
   * *Context:* Stakeholders have referenced a target where 60–70% of Phase 1 integration work survives a potential future TMS or dispatch platform change.
   * *Clarification Needed:* We need to review technical boundaries and define specific architectural standards for middleware to validate what components qualify as portable across future platform shifts.

4. **Target Delivery Timeline (End of Q3 Pilot vs. Q4 Execution)**
   * *Context:* Operational leadership requires a production pilot by the end of Q3 (Sept 30) to secure Phase 1 funding, whereas technical leadership has raised concerns regarding technical debt risk and favors a Q4 delivery target.
   * *Clarification Needed:* We need to align executive consensus on the precise scope boundaries required to ensure a safe, high-impact Q3 pilot rollout without compromising technical stability.

5. **Federal ELD Mandate Scope & Compliance Leadership**
   * *Context:* An update to the federal ELD compliance mandate takes effect in November, which carries potential operational authority risk if missed. Head of Compliance Rajiv Mehta has not yet been directly engaged.
   * *Clarification Needed:* We need to schedule a dedicated technical discovery session with Rajiv Mehta to confirm exact functional requirements for the driver mobile app prior to finalizing Phase 1C/1D scope.