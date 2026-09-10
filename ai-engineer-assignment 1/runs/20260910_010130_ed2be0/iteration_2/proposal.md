# Proposal: Operational Workflow & Integration Optimization

**Prepared for:** Sarah Chen, VP Operations — Northwind Logistics  
**Stakeholders:** Marcus Patel (CTO), Rita Donovan (CFO), Rajiv Mehta (Head of Compliance)  

---

## Executive Summary

Northwind Logistics has experienced rapid growth, expanding revenue to ~$85M following two strategic acquisitions in 2024. However, operational friction between dispatch, driver mobile applications, and financial operations is constraining cash flow and team productivity. Dispatchers face heavy manual double-entry between Northwind’s core dispatch system, **Routemaster**, and Salesforce. Meanwhile, finance remains three weeks behind on invoicing due to system data misalignments—leaving approximately $1.4M in working capital locked in unbilled receivables. Additionally, driver dissatisfaction with the mobile app poses retention and operational challenges.

To resolve these bottlenecks, we propose a targeted Phase 1 engagement designed to streamline dispatcher workflows, harmonize operational data across systems, and modernize the driver interface. Key outcome targets for Phase 1 include:
* **Unlocking $1.4M in Working Capital:** Reducing invoicing lag to return toward an industry-standard 5-day DSO.
* **Boosting Dispatcher Productivity:** Achieving a 30% reduction in dispatch time per load, avoiding $320k in planned dispatcher hires (4 FTEs).
* **Guaranteed Q3 Delivery:** Launching a production pilot by September 30 (end of Q3) while ensuring full compatibility with upcoming November ELD compliance mandates.

Our team brings direct experience from similar freight brokerage engagements, ensuring a portable, low-risk approach that delivers immediate financial value while protecting Northwind’s long-term technical options.

---

## Understanding

### Business & Operational Context
Northwind operates with 200 employees, 40 dispatchers, and ~600 contracted drivers out of Columbus, OH. Recent rapid expansion (40% growth in 2024) has exposed operational bottlenecks across three main operational pillars:
1. **Billing Delays & Working Capital:** Data misalignment between sales, dispatch, and accounting (NetSuite) forces finance into manual reconciliation, creating a 3-week invoicing delay that ties up $1.4M in unbilled receivables.
2. **Dispatcher Efficiency:** Dispatchers execute repetitive manual entry across **Routemaster** and Salesforce. Eliminating double-entry will reduce load dispatch time by 30% and eliminate the need to hire 4 additional dispatchers next year ($320k cost avoidance).
3. **Driver Experience & Compliance:** Drivers report low satisfaction with the custom React Native mobile app (last updated in 2023). Any driver app updates must carefully align with federal ELD compliance updates managed by Head of Compliance Rajiv Mehta ahead of the November deadline.

### Technical & Organizational Context
Northwind’s technical architecture consists of:
* **Routemaster:** A custom Rails 5 dispatch application (~7 years old, maintained by 2 internal engineers). **Routemaster** suffers from severe technical debt, which currently halts feature shipping and causes code changes to take three times longer than expected. Furthermore, two previous internal projects to fix these workflows failed, underscoring the need for an experienced external partner with proven execution playbooks.
* **Core Stack & Integration:** Salesforce (Sales Cloud) for CRM, NetSuite for accounting, and a custom React Native driver mobile app. Northwind currently lacks a central data warehouse, relying on Excel exports from Salesforce for business intelligence.
* **Acquisition Debt:** Systems from the two 2024 acquisitions remain incompletely integrated, adding operational complexity.

---

## Approach

Our technical approach prioritizes high-impact operational fixes without forcing an immediate, risky rewrite of **Routemaster**.

```
  +-------------------------------------------------------------------+
  |                      PORTABLE WORKFLOW LAYER                      |
  |  - Unified Load Entry   - Auto-Sync Logic   - Billing Validation    |
  +-------------------------------------------------------------------+
           |                                         |
           v                                         v
  +------------------+                      +------------------+
  |   ROUTEMASTER    | <--- API / Data ---> |    SALESFORCE    |
  | (Rails 5 Dispatch)                      |  (Sales Cloud)   |
  +------------------+                      +------------------+
           |                                         |
           +--------------------+--------------------+
                                |
                                v
                      +-------------------+
                      |     NETSUITE      |
                      |   (Accounting)    |
                      +-------------------+
```

### Key Principles:
1. **Decoupled Workflow & Integration Layer:** Build portable workflow and data-validation logic on top of **Routemaster** and Salesforce. This immediately automates data flows into NetSuite, eliminating the 3-week invoicing gap while ensuring that logic remains reusable regardless of future core platform decisions.
2. **Targeted Driver App Refinement:** Refactor essential driver workflows in the React Native application to improve driver satisfaction and load status visibility. All mobile updates will be strictly coordinated with compliance to ensure no disruption to ELD compliance work.
3. **Data Harmonization for Automated Invoicing:** Implement automated validation rules between **Routemaster**, Salesforce, and NetSuite to ensure load records auto-reconcile upon completion, directly attacking the $1.4M in unbilled receivables.

---

## Phases & Timeline

We commit to delivering a production pilot by **September 30 (end of Q3)**, providing immediate operational impact ahead of the November federal ELD deadline.

| Phase | Core Deliverables & Milestones | Target Schedule |
| :--- | :--- | :--- |
| **Phase 1A: Discovery & Architecture Validation** | Complete data mapping between **Routemaster**, Salesforce, and NetSuite. Define decoupled workflow integration specs. Map ELD compliance requirements with Compliance leadership. | Weeks 1–3 |
| **Phase 1B: Workflow Automation & Integration** | Build decoupled integration logic to eliminate dispatcher manual double-entry. Implement billing auto-validation routines to accelerate NetSuite invoicing. | Weeks 4–8 |
| **Phase 1C: Driver App Optimization & Testing** | Release targeted updates to the React Native driver app. Perform end-to-end user acceptance testing with dispatchers and drivers. | Weeks 9–11 |
| **Phase 1D: Q3 Pilot Production Launch** | **Deploy production pilot by September 30.** Measure dispatch time reduction and unbilled receivable drawdowns. Handover documentation and transition to Phase 2 planning. | Weeks 12–13 (By Sept 30) |

---

## Pricing Approach

Based on past engagements with peer freight brokerages (such as Cascade Freight) involving similar team size and scope, we propose a **fixed-fee structure with outcome-based milestone payments**. This structure ensures full alignment on deliverables and protects Northwind against cost overruns.

* **Estimated Engagement Range:** $150,000 – $250,000 (Fixed Fee)
* **Budget Alignment Note:** The proposed $150,000 – $250,000 fixed-fee range safely complies with the CFO's strict $300,000 budget cap, which addresses the internal disagreement over the budget ceiling and provides a comfortable financial buffer.

### Proposed Milestone Structure

```
+-----------------------------------------------------------------+
| Milestone 1: Discovery & Technical Architecture (25%)           |
+-----------------------------------------------------------------+
                                 |
                                 v
+-----------------------------------------------------------------+
| Milestone 2: Integration & Automation Buildout (35%)             |
+-----------------------------------------------------------------+
                                 |
                                 v
+-----------------------------------------------------------------+
| Milestone 3: Q3 Pilot Production Deployment (30%)                |
+-----------------------------------------------------------------+
                                 |
                                 v
+-----------------------------------------------------------------+
| Milestone 4: Post-Pilot Operational Validation (10%)             |
+-----------------------------------------------------------------+
```

---

## Open Questions

To ensure full alignment before formal contract execution, the following open questions and internal discrepancies must be clarified during alignment discussions:

1. **Long-Term Platform Strategy (SaaS Replacement vs. Incremental Fixes):**  
   * *Context & Clarification Needed:* Internal stakeholders currently hold differing views regarding long-term technical direction. The CTO favors a full replacement of **Routemaster** with a commercial SaaS platform, whereas the VP of Operations favors incremental workflow updates on top of **Routemaster**. We need to formalize alignment on using a portable workflow layer in Phase 1 so that current investments remain intact regardless of future platform decisions.

2. **Code Reusability & Survival Rate:**  
   * *Context & Clarification Needed:* Preliminary estimates suggest that 60–70% of the workflow logic built in Phase 1 can survive a future core platform migration. We need to conduct initial discovery in Phase 1A to formally baseline and confirm this survival rate requirement with engineering leadership.

3. **Federal ELD Mandate Scope & Schedule Coordination:**  
   * *Context & Clarification Needed:* Details regarding the specific technical updates required for the November federal ELD compliance mandate remain unconfirmed. We require a dedicated discovery session with Rajiv Mehta (Head of Compliance) to confirm technical specifications and ensure driver mobile app updates avoid any overlap or conflict with ELD compliance code path.