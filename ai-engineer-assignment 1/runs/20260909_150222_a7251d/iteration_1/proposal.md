# Proposal for Operations & Dispatch Workflow Transformation

**Prepared for:** Northwind Logistics  
**Attention:** Sarah Chen (VP Operations), Marcus Patel (CTO), Rita Donovan (CFO)  
**Date:** March 2025  

---

## Executive Summary

Northwind Logistics has experienced remarkable growth, expanding 40% in 2024 through acquisition to reach ~$85M in revenue. However, operational systems have not kept pace. Dispatchers are burdened with manual double-entry between the custom dispatch tool ("Routemaster") and Salesforce, drivers face friction with the legacy mobile application, and finance operates three weeks behind on invoicing due to cross-system data discrepancies. 

This proposal outlines a focused, high-impact Phase 1 engagement designed to eliminate dispatcher friction, automate invoicing data alignment, and establish a modern, scalable integration layer. By addressing these root causes, Northwind can achieve a **30% reduction in dispatch handling time**—avoiding $320,000 in additional dispatcher hiring costs—and return to a **5-day Days Sales Outstanding (DSO)**, unlocking approximately **$1.4M in working capital**.

To protect Northwind’s investment and address prior vendor concerns, we propose a **fixed-fee, milestone-based structure** tied strictly to verifiable operational deliverables. Furthermore, all integration logic and workflow automation will be architected to be highly portable (60–70% survival rate), ensuring long-term value regardless of future core platform evolution.

---

## Understanding

### Business & Operational Context
Following rapid expansion, Northwind operates with 40 dispatchers and over 600 contracted drivers. Operational efficiency is currently constrained by fragmented systems:
* **Invoicing Delays:** Finance spends significant manual effort reconciling load and operational data across Routemaster, Salesforce, and NetSuite, resulting in a 3-week invoicing backlog that threatens cash flow.
* **Dispatcher Overhead:** Dispatchers spend excessive hours manually transferring load data between Salesforce Sales Cloud and Routemaster, limiting capacity and increasing error rates.
* **Driver Experience:** Contracted drivers report high dissatisfaction with the legacy custom React Native mobile app, leading to compliance tracking and status update delays.

### Technical Environment
* **Dispatch Core ("Routemaster"):** A 7-year-old custom Ruby on Rails 5 application maintained by two internal engineers. While functional, technical debt makes new feature delivery slow and fragile.
* **CRM & Financials:** Salesforce Sales Cloud serves as the primary CRM, while NetSuite handles accounting. No central data warehouse currently exists; reporting relies on manual Excel exports.
* **Acquisition Integration:** Technical integration from the 2024 acquisitions remains incomplete, contributing to operational friction across business units.

### Strategic Objectives & Success Metrics
1. **Financial Impact:** Lower DSO to 5 days to release ~$1.4M in working capital.
2. **Operational Efficiency:** Reduce dispatch processing time per load by 30%, absorbing growth without adding 4 new dispatcher headcount ($320k annual savings).
3. **Risk Mitigation:** Re-establish executive trust through a transparent, milestone-gated delivery model with modular, portable software assets.

---

## Approach

Our approach focuses on building a lightweight, highly resilient **Workflow Automation & Integration Layer** rather than forcing intrusive changes on day one. This isolates system complexity and delivers immediate operational relief while safeguarding future flexibility.

```
+-------------------+      +--------------------------------+      +-------------------+
|  Salesforce CRM   | <--> |  Workflow & Integration Layer  | <--> |  NetSuite (ERP)   |
+-------------------+      +---------------+----------------+      +-------------------+
                                           |
                                           v
                           +--------------------------------+
                           |   Routemaster / Future TMS     |
                           +--------------------------------+
```

### Key Principles

1. **Decoupled Workflow Orchestration:** We will build integration services that handle load creation, status updates, and invoicing triggers outside the monolith. This ensures that 60–70% of the workflow logic survives intact even if underlying core systems are updated or migrated in the future.
2. **Automated Invoicing Reconciliation:** Establish real-time data validation rules between load execution events and NetSuite billing entries, eliminating manual data matching and cutting invoicing cycle time from weeks to days.
3. **Dispatcher Double-Entry Elimination:** Implement bidirectional API synchronization between Salesforce and the dispatch system, enabling single-touch load management for dispatchers.
4. **Mobile Experience Optimization:** Targeted fixes to the React Native driver application to streamline driver check-ins, load status updates, and compliance reporting.

---

## Phases & Timeline

We structure the engagement into clear, sequential milestones designed to manage delivery risk and deliver early operational utility.

```
+-----------------------------------------------------------------------------------+
| Phase 1A: Discovery & Architecture (Weeks 1-4)                                   |
| - Process mapping, API specification, modular architecture design                 |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Phase 1B: Integration & Automation Build (Weeks 5-16)                             |
| - Salesforce <-> Routemaster <-> NetSuite sync, Invoicing rules engine            |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Phase 1C: Pilot Deployment & Optimization (Weeks 17-24)                           |
| - Production pilot roll-out, Driver app updates, Operational verification         |
+-----------------------------------------------------------------------------------+
```

### Detailed Breakdown

* **Phase 1A: Discovery & Integration Architecture (Weeks 1–4)**
  * Comprehensive mapping of dispatch-to-invoicing data flows.
  * API contract definition for Salesforce, Routemaster, and NetSuite.
  * Integration architecture sign-off focusing on portability and modularity.

* **Phase 1B: Core Integration & Invoicing Automation (Weeks 5–16)**
  * Development of automated load synchronization between CRM and dispatch.
  * Automated pre-invoicing validation engine to resolve data discrepancies.
  * Targeted driver app patch releases for check-in stability.

* **Phase 1C: Pilot Rollout & Refinement (Weeks 17–24)**
  * Deployment of operational pilot to a subset of dispatchers and driver fleets.
  * Performance tuning, user feedback iteration, and DSO metric verification.
  * Final operational handover and documentation.

---

## Pricing Approach

To ensure complete alignment with CFO expectations and mitigate historical vendor risk, we operate strictly on a **Fixed-Fee, Milestone-Based** structure. Payments are tied directly to verifiable delivery gates rather than hours logged.

### Historical Benchmark & Scope Calibration
Based on past engagements in the logistics and freight management sector for team structures of similar scale (4-person specialized delivery pod), comparable discovery and production MVP builds typically benchmark within a **$150,000 to $250,000** price band for core integration and pilot delivery.

### Proposed Milestone Structure

| Milestone | Deliverable Gate | Payment % | Value Delivered |
| :--- | :--- | :--- | :--- |
| **Milestone 1: Architecture & Integration Blueprint** | Approved data flow specs, API contracts, and portable architecture blueprint (End of Month 1) | 25% | Technical clarity & risk mitigation |
| **Milestone 2: Automated Sync & Invoicing Engine** | Functioning bidirectionally tested integration between CRM, Dispatch, and NetSuite (End of Month 4) | 40% | Elimination of manual double-entry |
| **Milestone 3: Production Pilot & Metric Verification** | Deployed production pilot, verified reduction in invoicing backlog, driver app patch release (End of Month 6) | 35% | Working capital release & DSO reduction |

*Note: The exact fixed fee within the benchmark range will be finalized upon alignment on the open items below.*

---

## Open Questions

To ensure full alignment across executive stakeholders before final execution, the following areas require explicit clarification during our kickoff alignment session:

### 1. Phase 1 Budget Cap Alignment (Contradicted Intake Data)
* **Context:** There is an internal difference in budget assumptions between leadership stakeholders (CFO Rita mandates a strict $300,000 budget cap, whereas VP of Operations Sarah identified a scope range between $250,000 and $400,000).
* **Clarification Needed:** We need to formally confirm the binding budget ceiling for Phase 1 so we can right-size the scope boundary within agreed financial parameters.

### 2. Long-Term Platform Strategy vs. Workflow Overlay (Contradicted Intake Data)
* **Context:** CTO Marcus advocates replacing Routemaster with a full SaaS TMS platform (~$600k/yr), while VP of Operations Sarah favors an incremental workflow overlay fix to address immediate pain points within current budget limits.
* **Clarification Needed:** We must align on whether Phase 1 should strictly treat Routemaster as a long-term core system or design the integration layer explicitly as a temporary abstraction layer to facilitate a future SaaS TMS migration.

### 3. Production Pilot Target Release Date (Contradicted Intake Data)
* **Context:** Operations and Finance target an end-of-Q3 (September 30) production pilot launch to retain executive funding, while Technical leadership views a Q4 release as a more realistic engineering timeframe.
* **Clarification Needed:** We need to establish a mutually agreed delivery schedule that balances rapid risk-free deployment with technical feasibility.

### 4. Federal ELD Compliance Mandate & Driver App Scope (Low/Medium Confidence)
* **Context:** A federal ELD compliance mandate update is noted for November 15, impacting driver hours logging and reporting requirements.
* **Clarification Needed:** We need to confirm the exact technical specifications required for the November 15 ELD mandate update and determine whether ELD compliance changes fall within Phase 1 scope or a subsequent track.