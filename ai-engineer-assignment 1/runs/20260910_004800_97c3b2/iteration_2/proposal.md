# Proposal for Northwind Logistics

## Executive Summary

Northwind Logistics has experienced rapid growth, expanding 40% in 2024 through two strategic acquisitions. However, operational and technical friction now hinders continued scaling. Dispatchers face severe manual overhead copying data between Routemaster and Salesforce, while finance is three weeks behind on invoicing due to persistent data misalignment across systems—leaving approximately $1.4M stuck in unbilled receivables. Simultaneously, drivers report high friction with the current mobile application, and upcoming regulatory changes require careful coordination.

To address these challenges, we propose a targeted engagement designed to deliver rapid operational relief while establishing a durable architectural foundation. Our primary objectives are to streamline dispatcher workflows to achieve a 30% reduction in dispatch time (avoiding the need to hire four additional dispatchers) and restore invoicing velocity to a 5-day DSO, unlocking $1.4M in working capital.

We will execute this work under a fixed-fee model capped at $300,000 with milestone-based payments, ensuring complete budget predictability for leadership. Crucially, our architecture will ensure that 60–70% of the workflow logic developed in Phase 1 remains platform-agnostic and fully reusable should Northwind choose to transition to a new platform in the future.

---

## Understanding

Based on our intake and stakeholder discussions, Northwind Logistics requires a balanced strategy that addresses immediate operational friction while respecting technical constraints and budget limits:

* **Dispatcher & System Friction:** Dispatchers routinely perform manual double-entry between Routemaster (a Rails 5 application maintained by two internal engineers) and Salesforce Sales Cloud. This manual overhead creates operational bottlenecks across the 40-person dispatch team.
* **Financial Delay & Working Capital Impact:** Invoicing processes lag by three weeks because operational data in Routemaster does not align seamlessly with Salesforce and NetSuite. This delay ties up approximately $1.4M in unbilled receivables. Returning to a 5-day DSO target is a core business priority.
* **Driver Experience:** The 600 contracted drivers experience significant friction using the custom React Native mobile app (last updated in 2023), contributing to operational delay and dissatisfaction.
* **Incomplete Acquisition Integration:** Technology integration from Northwind’s 2024 acquisitions remains incomplete, contributing to system fragility and data silos.
* **Regulatory Compliance:** The federal ELD compliance update in November represents a firm regulatory deadline. Missing this mandate carries severe business risks, including potential fines and the possible loss of operating authority in some states.
* **Vendor Governance & Budget Guardrails:** Following an unsatisfactory vendor experience in 2023, CFO Rita Donovan requires strict financial governance, a fixed-fee structure capped at $300,000, and clear milestone deliverables before releasing payments.

---

## Approach

Our approach focuses on tactical, high-impact fixes that deliver immediate operational value without trapping Northwind in technical debt:

1. **Workflow & Integration Automation:**
   * Establish automated, reliable data synchronisation between Routemaster, Salesforce, and NetSuite.
   * Eliminate duplicate data entry for dispatchers and standardize load data to eliminate the 3-week invoicing backlog.
2. **Mobile App Refactoring:**
   * Remediate top friction points in the React Native driver app to streamline load acceptance, status updates, and paperwork capture for contracted drivers.
3. **Decoupled Architectural Strategy:**
   * Design the integration and workflow logic to be modular so that 60–70% of the solution survives intact whether Northwind retains Routemaster or transitions to a SaaS platform down the road.
4. **ELD & Compliance Coordination:**
   * Align all mobile and backend modifications with Head of Compliance Rajiv Mehta to ensure full compliance with the November federal mandate without disrupting ongoing operations.

---

## Phases & Timeline

```
+-----------------------------------------------------------------------------------+
| Phase 1A: Discovery & Architecture (Weeks 1–4)                                    |
| - Process mapping, integration design between Routemaster & Salesforce/NetSuite   |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 1B: Core Integration & App Refactoring (Weeks 5–10)                        |
| - Automated data sync, driver app friction fixes, ELD alignment design            |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 1C: Pilot Deployment & Operations Validation (Weeks 11–14)                  |
| - Controlled pilot rollout, dispatcher time reduction & DSO velocity tracking     |
| * Note: Addresses stakeholder launch alignment (Q3 vs Q4 target)                  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| Phase 1D: Transition, Documentation & ELD Readiness (Weeks 15–18)                |
| - Knowledge transfer to internal engineering team, final ELD validation           |
+-----------------------------------------------------------------------------------+
```

### Phase Details

* **Phase 1A: Discovery & Architecture (Weeks 1–4)**
  * Audit existing Routemaster API endpoints, Salesforce schema, and NetSuite billing workflows.
  * Establish precise technical specifications for automated integration and mobile app enhancements.
* **Phase 1B: Core Integration & Mobile Refactoring (Weeks 5–10)**
  * Build and test automated integration pipelines connecting Routemaster, Salesforce, and NetSuite.
  * Execute priority fixes on the React Native mobile app and prepare interface hooks for ELD compliance work.
* **Phase 1C: Pilot Deployment & Operations Validation (Weeks 11–14)**
  * Deploy solutions to a pilot group of dispatchers and drivers to measure dispatch time savings and invoice reconciliation speed.
  * *Note on Stakeholder Alignment:* There is an active internal stakeholder conflict regarding the pilot launch date. Operations (Sarah Chen) and Finance (Rita Donovan) mandate a Q3 (Sept 30) pilot launch for operational and budget reasons, whereas Engineering (Marcus Patel) expects a Q4 timeline given Routemaster's fragile codebase. Final alignment on this target date will be established in Phase 1A.
* **Phase 1D: Transition, Documentation & ELD Readiness (Weeks 15–18)**
  * Complete full documentation and hand off maintenance procedures to Northwind's two internal engineers.
  * Validate system readiness ahead of the November federal ELD deadline.

---

## Pricing Approach

To align with CFO Rita Donovan's explicitly approved budget cap and vendor governance requirements, we propose a fixed-fee engagement capped at **$300,000**. Payments are tied directly to milestone sign-offs:

| Milestone | Deliverable / Outcome | Fee Percentage | Amount |
| :--- | :--- | :--- | :--- |
| **Milestone 1** | Completion of Phase 1A Discovery, Integration Architecture, and Alignment Sign-off | 25% | $75,000 |
| **Milestone 2** | Completion of Phase 1B Core Development (Routemaster/Salesforce sync & Mobile Refactor) | 35% | $105,000 |
| **Milestone 3** | Completion of Phase 1C Pilot Deployment & Operational Validation | 25% | $75,000 |
| **Milestone 4** | Final Handover, Engineering Documentation, and Phase 1 Closure | 15% | $45,000 |
| **Total** | | **100%** | **$300,000** |

This fixed-fee structure eliminates cost overrun risks for Northwind Logistics and ensures that capital is deployed against verifiable deliverables.

---

## Open Questions

The following areas represent internal stakeholder alignment items or technical parameters requiring explicit clarification during the initial project kickoff:

1. **Long-Term Platform Vision Alignment (SaaS Platform vs. Routemaster Enhancement):**
   * *Issue needing clarification:* Stakeholders hold conflicting views regarding long-term technical strategy. CTO Marcus Patel favors replacing Routemaster with a commercial SaaS platform, whereas VP of Operations Sarah Chen prefers incremental workflow improvements on the existing codebase. 
   * *Action:* In Phase 1A, we must clarify the long-term roadmap to ensure that our architectural decoupling isolates 60–70% of core workflow logic, enabling a seamless transition if a SaaS replacement is selected later.

2. **Pilot Launch Schedule Alignment:**
   * *Issue needing clarification:* Operations and Finance mandate a production pilot launch by the end of Q3 (September 30), whereas Engineering considers Q4 a more realistic timeline due to codebase fragility.
   * *Action:* During Phase 1A discovery, we will work with Sarah Chen, Rita Donovan, and Marcus Patel to review scope trade-offs and formally commit to a baseline pilot release schedule that meets operational targets without compromising system stability.