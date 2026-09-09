# Executive Summary

Northwind Logistics has experienced rapid growth, expanding 40% in 2024 to ~$85M in annual revenue across 200 employees, 40 dispatchers, and ~600 contracted drivers. However, this growth—driven in part by recent acquisitions—has introduced severe operational friction and technical debt. The operational workflow between Northwind's legacy custom dispatch app ("Routemaster") and Salesforce requires extensive manual re-entry, while finance remains 3 weeks behind on invoicing due to system-wide data discrepancies. Furthermore, driver dissatisfaction with the mobile app poses risks to fleet operations.

To address these challenges, we propose a targeted Phase 1 engagement focused on two critical priorities: automated invoicing data reconciliation and dispatcher workflow optimization. By deploying a modular integration layer between Routemaster, Salesforce, and NetSuite, Northwind can:
* **Unlock $1.4M in working capital** currently trapped in unbilled receivables by restoring invoicing velocity to industry standards.
* **Reduce load dispatch time by 30%**, saving approximately $320k in avoided dispatcher hiring costs.
* **Future-proof technical investments** by ensuring 60–70% of the integration architecture survives any potential future transition to a commercial SaaS Transportation Management System (TMS).

To ensure complete financial predictability and alignment with Northwind's governance requirements, this project will be structured under a **fixed-fee model with outcome-based milestone payments**.

---

# Understanding

### Current Environment & Operational Friction
Northwind’s operating model relies on a blend of legacy custom applications and enterprise SaaS platforms:
* **Core Dispatch:** "Routemaster," a 7-year-old custom Ruby on Rails 5 application maintained by an internal team of two engineers. Codebase fragility currently slows feature delivery and operational adjustments.
* **CRM & Commercial Management:** Salesforce Sales Cloud, operating with significant manual data entry gaps relative to Routemaster.
* **Accounting:** NetSuite, where invoicing is delayed by 3 weeks due to data mismatch across dispatch records and customer profiles.
* **Driver Experience:** A custom React Native mobile app last updated in 2023, which drivers find difficult to use.
* **Analytics & Integration Status:** No central data warehouse (BI is managed through manual Excel exports), and technical integration from the 2024 acquisitions remains incomplete.

### Strategic Priorities & Stakeholder Dynamics
Key stakeholders across Northwind share a commitment to resolving operational bottlenecks, but bring distinct perspectives:
* **Operations (Sarah Chen, VP Operations):** Focused on reducing manual dispatcher effort, resolving invoicing delays to free up working capital, and maintaining operational momentum.
* **Technology (Marcus Patel, CTO):** Focused on mitigating technical debt in Routemaster, evaluating third-party SaaS TMS platforms, and ensuring technical work is built with high architectural standards.
* **Finance (Rita Donovan, CFO):** Focused on tight budget control, risk mitigation following previous vendor challenges in 2023, and strict adherence to a fixed-fee milestone schedule.
* **Compliance (Rajiv Mehta, Head of Compliance):** Focused on upcoming federal ELD mandate updates taking effect in November.

### Financial & Operational Value Drivers
* **Working Capital Recovery:** Reconciling data discrepancies between dispatch and billing will return Days Sales Outstanding (DSO) to standard levels, releasing approximately $1.4M in working capital.
* **Dispatcher Efficiency:** Achieving a 30% reduction in per-load dispatch time will allow the current 40-person dispatcher team to handle increased load volume without adding $320k in new headcount costs.
* **Architecture Preservation:** Designing modular workflows and middleware ensures that 60–70% of the integration logic remains fully functional even if Routemaster is eventually replaced with a third-party SaaS platform.

---

# Approach

Our approach emphasizes targeted, low-risk architectural interventions that deliver immediate cash-flow relief while building reusable integration patterns.

```
+-------------------+        +---------------------------------+        +--------------------+
|  Salesforce CRM   | <----> |   Modular Integration Layer     | <----> |  NetSuite Billing  |
+-------------------+        |  (Decoupled Sync & Rules Engine)|        +--------------------+
                             +---------------------------------+
                                              ^
                                              |
                                              v
                             +---------------------------------+
                             | Custom Rails App (Routemaster)  |
                             +---------------------------------+
```

### 1. Decoupled Integration Architecture
Instead of modifying Routemaster’s core Rails codebase extensively, we will implement an external, lightweight integration layer. This layer will manage data synchronization between Salesforce, Routemaster, and NetSuite. By decoupling validation rules and data transformations from the legacy core, Northwind preserves 60–70% of this investment should leadership decide to transition to a SaaS TMS in the future.

### 2. Automated Invoicing & Data Reconciliation
We will deploy automated reconciliation workflows to cross-verify dispatch logs, rate sheets, and billing profiles between Routemaster, Salesforce, and NetSuite. Eliminating manual cross-referencing will resolve the 3-week billing lag and normalize DSO.

### 3. Dispatcher Workflow Optimization & Mobile Remediation
* **Workflow Automation:** Re-engineer the load-booking and assignment workflows to eliminate duplicate manual entries between Salesforce and Routemaster.
* **Mobile App Stability:** Conduct targeted remediation on the React Native driver app to fix high-friction workflows and improve driver load status updates.

### 4. Governance & Risk Mitigation
To address past negative experiences with external vendors, our engagement operates under a strict fixed-fee milestone framework. Each milestone is tied to verifiable operational outcomes and technical deliverables.

---

# Phases & Timeline

The proposed 6-month Phase 1 roadmap is structured across four structured stages. *(Note: Alignment on specific milestone target dates relative to internal stakeholder preferences is detailed in the Open Questions section).*

```
2025 Roadmap
Month 1           Month 2           Month 3           Month 4           Month 5           Month 6
[--- Phase 1A ---][--- Phase 1B ---][--- Phase 1C ---][-------------- Phase 1D --------------]
 Discovery &       Invoicing MVP     Dispatcher &      ELD & Platform Transition
 Data Architecture Sync Engine       Driver App Opt.   Readiness
```

### Phase 1A: Discovery & Data Architecture (Weeks 1–4)
* Process mapping of dispatcher workflows across all 40 dispatchers and acquired business units.
* Audit data discrepancies across Routemaster, Salesforce, and NetSuite.
* Finalize the modular integration layer architecture and data contracts.

### Phase 1B: Invoicing Reconciliation MVP & Sync Engine (Weeks 5–12)
* Implement automated data synchronization between Routemaster, Salesforce, and NetSuite.
* Deploy automated billing reconciliation tools to clear the 3-week invoicing backlog.
* Pilot initial workflow updates with a core subgroup of dispatchers.

### Phase 1C: Dispatcher Workflow & Driver Mobile Remediation (Weeks 13–20)
* Eliminate manual dual-entry points between Salesforce and Routemaster for the broader dispatcher team.
* Release targeted stability and usability fixes for the React Native driver app.
* Evaluate operational metrics against the target 30% reduction in load dispatch time.

### Phase 1D: ELD Compliance & Platform Transition Readiness (Weeks 21–24)
* Coordinate with compliance leadership regarding the November ELD mandate integration touchpoints.
* Document integration contracts to ensure compatibility with ongoing SaaS TMS evaluations.
* Final handoff and operational stabilization.

---

# Pricing Approach

### Structure
In accordance with Northwind's risk-mitigation priorities and CFO guidance, this engagement is offered on a **Fixed-Fee basis with outcome-based milestone payments**. Payments are released only upon successful completion and sign-off of specific operational and technical deliverables.

### Benchmark & Price Band
Based on peer engagements in the logistics and freight brokerage sector involving discovery, workflow optimization, and custom integration MVP builds (team size 4–5), typical investments fall within the **$150,000 to $250,000** price band for initial production deployment.

### Proposed Milestone Schedule

| Milestone | Deliverable / Outcome | Payment % |
| :--- | :--- | :--- |
| **Milestone 1: Architecture & Data Mapping** | Finalized integration architecture, completed data audit across Salesforce/Routemaster/NetSuite, and signed-off test plan. | 20% |
| **Milestone 2: Automated Invoicing Sync MVP** | Production deployment of invoicing reconciliation engine, resolving data lag between dispatch and NetSuite. | 40% |
| **Milestone 3: Dispatcher Workflow & Driver Fixes** | Rollout of stream-lined load entry tools to dispatchers and deployment of updated React Native driver app fixes. | 30% |
| **Milestone 4: Compliance Alignment & Handover** | Integration documentation sign-off, ELD mandate alignment, and transition guide for TMS evaluation. | 10% |

---

# Open Questions

To ensure total alignment across Northwind's executive leadership team before final contracting, the following items require explicit clarification and agreement:

1. **Phase 1 Budget Cap Alignment (Contradiction Needing Resolution)**
   * *Issue:* Executive leadership holds differing understandings of the approved Phase 1 budget. CFO Rita Donovan explicitly states the approved budget is capped at **$300,000**, whereas VP of Operations Sarah Chen understood the approved range to be **$250,000 to $400,000**.
   * *Clarification Needed:* We need to formalize the strict upper budget bound during alignment discussions so the final statement of work remains within agreed parameters.

2. **Production Pilot Delivery Schedule (Contradiction Needing Resolution)**
   * *Issue:* There is an internal timeline mismatch regarding the production pilot target date. Sarah Chen and Rita Donovan require a production pilot in deployment by **end of Q3 (September 30)** to protect allocated funding. Conversely, CTO Marcus Patel explicitly rejects the end-of-Q3 deadline as high-risk, targeting a **Q4 completion date** to account for Routemaster codebase fragility.
   * *Clarification Needed:* We must align stakeholders on a phased MVP scope (e.g., scoping Phase 1B specifically to hit the September 30 date for invoicing reconciliation) while allowing core technical stabilization work to extend into Q4 as necessary.

3. **ELD Compliance Scope (November Mandate)**
   * *Details Needed:* Specific operational and technical requirements for the November 15 federal ELD compliance update have not yet been detailed. We need to schedule a technical discovery session with Rajiv Mehta (Head of Compliance) to determine if ELD data flows impact the Phase 1 integration layer.

4. **TMS Evaluation Strategy & Long-Term System Selection**
   * *Details Needed:* Northwind is currently evaluating third-party SaaS TMS vendors. We require visibility into candidate platforms to ensure our Phase 1 middleware interface specifications align directly with potential future SaaS replacement candidates.