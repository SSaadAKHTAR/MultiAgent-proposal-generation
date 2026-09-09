# Executive Summary

Northwind Logistics ("Northwind"), an $85M mid-market freight brokerage with 40 dispatchers and 600 contracted drivers, has achieved rapid growth—including a 40% expansion in 2024 via acquisitions. However, operational bottlenecks and legacy technical debt threaten continued growth and financial health. Dispatchers face heavy manual re-keying between custom tools and Salesforce, drivers struggle with an outdated mobile app, and finance experiences a three-week delay in invoicing that currently traps **$1.4M in working capital** in unbilled receivables.

To resolve these challenges, we propose a 6-month Phase 1 engagement structured as a fixed-fee agreement of **$300,000**, aligning with CFO Rita Donovan's strict budget cap. Drawing on our proven track record with peer freight brokerages (such as Cascade Freight), our objective is to eliminate workflow friction, compress the billing cycle, and establish operational scalability.

### Core Objectives & Projected Business Impact
* **Working Capital Liberation:** Eliminate the 3-week invoicing lag to return to an industry-standard 5-day DSO, unlocking **$1.4M in working capital**.
* **Dispatcher Efficiency:** Reduce dispatch processing time per load by **30%**, improving productivity and avoiding **$320,000** in planned hiring costs for four additional dispatchers next year.
* **Production Pilot Delivery:** Target a production-ready pilot deployment by end of Q3 (September 30), dependent on resolving stakeholder alignment on timeline and scope.
* **Regulatory & System Stability:** Secure compliance ahead of the November federal ELD mandate while building portable, modular integration logic to protect future software investments.

---

# Understanding

Northwind’s operational pain points stem from high growth, incomplete post-acquisition system integration, and fragmented data workflows across dispatch, sales, and accounting.

### Operational Pain Points
* **Manual Data Entry:** Dispatchers continuously double-enter load and carrier information between Routemaster (custom dispatch software) and Salesforce, driving operational latency and human error.
* **Driver App Friction:** Contracted drivers find the current custom React Native mobile app difficult to use, leading to delayed load status updates and administrative friction.
* **Scaling Bottlenecks:** Without workflow automation, scaling operations would require hiring four additional dispatchers at an estimated cost of $320,000 annually.

### Financial & Strategic Impact
* **Invoicing Delays:** Finance operates three weeks behind on invoicing due to persistent data misalignment between dispatch records and NetSuite.
* **Capital Lockup:** The invoicing back-log leaves **$1.4M** in working capital tied up in unbilled receivables.
* **DSO Compression:** Achieving an industry-standard 5-day DSO is critical to restoring cash flow predictability.

### System & Regulatory Landscape
* **Dispatch System ("Routemaster"):** A 7-year-old custom Ruby on Rails 5 monolith maintained internally by two engineers. The codebase suffers from technical debt, making feature development fragile and slow.
* **Core Stack:** Salesforce (Sales Cloud) for CRM, NetSuite for accounting, custom React Native driver mobile app (last updated in 2023), and no centralized data warehouse (BI relies on Excel exports from Salesforce).
* **Evaluation Status:** Northwind is currently evaluating commercial TMS vendors; no final selection has been made.
* **Regulatory Compliance Risk:** An updated federal Electronic Logging Device (ELD) mandate takes effect in November. Missing this deadline presents severe business risks, including **substantial regulatory fines and the potential loss of operating authority in certain states**.

---

# Approach

Our approach delivers immediate operational relief on Northwind's existing software stack while establishing clean, modular integration layers that ensure long-term architectural flexibility.

```
+------------------+      +-------------------+      +------------------+
|   Salesforce     | <--> |  Integration Layer| <--> |    Routemaster   |
|  (Sales Cloud)   |      |  & Workflow Engine|      |  (Rails 5 App)   |
+------------------+      +-------------------+      +------------------+
                                    |
                                    v
                          +-------------------+
                          | NetSuite Invoicing|
                          | (Automated Billing|
                          +-------------------+
```

### 1. Automated Data Synchronization & Dispatch Streamlining
* Develop targeted API middleware to synchronize load data in real time between Routemaster and Salesforce, eliminating double-entry for dispatchers.
* Standardize load status triggers to achieve a **30% reduction in dispatch time per load**.

### 2. Streamlined Billing & Invoicing Pipeline
* Establish automated data validation triggers between Routemaster, Salesforce, and NetSuite.
* Automate proof-of-delivery (POD) matching to eliminate the 3-week invoicing delay, unlocking **$1.4M in working capital** and targeting a 5-day DSO.

### 3. Driver App & ELD Compliance Integration
* Refactor the React Native driver app to simplify core load-acceptance and status-reporting workflows.
* Coordinate mobile updates directly with the November federal ELD mandate to ensure zero disruption to operating authority or compliance standing.

### 4. Portable Architecture
* Build workflow and integration logic using decoupled API layers. This ensures that any business logic created during Phase 1 remains portable and reusable if Northwind replaces Routemaster with a commercial SaaS TMS in the future.

---

# Phases & Timeline

The proposed Phase 1 engagement spans six months, structured into three distinct two-month phases. 

*Note: The end-of-Q3 pilot deployment is framed as a target date dependent on executive scope and schedule resolution.*

```
2026 Timeline
+------------------------------------+------------------------------------+------------------------------------+
| Month 1                   Month 2  | Month 3                   Month 4  | Month 5                   Month 6  |
| Phase 1A: Discovery & Architecture | Phase 1B: Core Workflow & Billing  | Phase 1C: Pilot & Compliance Rollout|
+------------------------------------+------------------------------------+------------------------------------+
                                                                            ^ Target Pilot: Sept 30 (Q3)
                                                                            ^ ELD Mandate: November
```

### Phase 1A: Discovery, Integration Architecture & Compliance Planning (Months 1–2)
* Audit Routemaster codebase, Salesforce data models, and NetSuite billing schemas.
* Finalize integration specifications between Routemaster, Salesforce, and NetSuite.
* Engage Head of Compliance (Rajiv Mehta) to define full technical requirements for the November ELD mandate.
* **Deliverables:** Architectural Blueprint, Data Mapping Matrix, ELD Technical Compliance Plan.

### Phase 1B: Core Workflow Automation & Invoicing Pipeline (Months 3–4)
* Build automated bi-directional data sync between Routemaster and Salesforce.
* Implement automated proof-of-delivery validation and NetSuite invoicing queue triggers.
* Initiate driver mobile app workflow refactoring.
* **Deliverables:** Automated Invoicing Pipeline, Operational Dispatch Sync, Beta Mobile App Build.

### Phase 1C: Pilot Deployment, Mobile Refactoring & Production Rollout (Months 5–6)
* Launch controlled pilot deployment with select dispatchers and driver groups (**Target: September 30 / Q3 End**, subject to alignment).
* Complete final ELD compliance deployment ahead of the November deadline.
* Validate DSO compression and dispatcher efficiency metrics against success criteria.
* **Deliverables:** Production Pilot Release, ELD Mandate Compliance Package, Phase 1 Value Realization Report.

---

# Pricing Approach

Grounded in our experience with similar mid-market freight brokerage transformations (where 3-month discovery and MVP engagements typically benchmark between $150,000 and $250,000), we propose a fixed fee of **$300,000** for this comprehensive 6-month Phase 1 engagement. This structure aligns strictly with CFO Rita Donovan's approved budget cap and preference for outcome-based milestone billing.

### Milestone Billing Schedule

| Milestone | Deliverable / Phase Target | Timing | Fee Percentage | Payment Amount |
| :--- | :--- | :--- | :---: | :---: |
| **Milestone 1** | Discovery, Integration Architecture Blueprint & ELD Compliance Plan | End of Month 1 | 20% | $60,000 |
| **Milestone 2** | Invoicing Pipeline & Salesforce-Routemaster Integration Build | End of Month 3 | 35% | $105,000 |
| **Milestone 3** | Driver App Refactoring & ELD Integration Release | End of Month 5 | 25% | $75,000 |
| **Milestone 4** | Q3 Production Pilot Deployment & Operational Handoff | End of Month 6 | 20% | $60,000 |
| **Total Fixed Fee** | | | **100%** | **$300,000** |

---

# Open Questions

To ensure full operational alignment prior to project kickoff, the following open questions and stakeholder alignment points must be formally resolved:

1. **Target Pilot Schedule Conflict (Sarah Chen & Rita Donovan vs. Marcus Patel):**
   * *Context:* VP of Operations Sarah Chen and CFO Rita Donovan require a production pilot in hand by the end of Q3 (September 30) to secure ongoing operational funding. Conversely, CTO Marcus Patel assesses that Q4 is a more realistic timeline to deliver a stable solution without introducing technical risk.
   * *Clarification Needed:* We need to establish an agreed-upon scope baseline for the Q3 target or formalize a phased feature-rollout plan that satisfies both funding requirements and engineering stability.

2. **Long-Term Systems Strategy: Incremental Fix vs. SaaS Replacement (Sarah Chen vs. Marcus Patel):**
   * *Context:* CTO Marcus Patel favors replacing Routemaster entirely with a commercial SaaS TMS platform, whereas VP of Operations Sarah Chen prefers incrementally resolving workflow pain points directly on the existing Rails system.
   * *Clarification Needed:* Alignment is required on whether Phase 1 logic should be designed purely as an incremental enhancement to Routemaster or explicitly structured as a decoupled bridge layer for an impending SaaS migration.

3. **Codebase Reusability Requirements:**
   * *Context:* To protect engineering investments against future platform changes, integration logic should be designed with portability in mind.
   * *Clarification Needed:* We request that CTO Marcus Patel define the technical architecture standards and required reusability targets for Phase 1 work in the event of a future SaaS migration.

4. **ELD Mandate & Mobile Driver App Coordination:**
   * *Context:* Missing the November ELD compliance deadline risks severe regulatory penalties and loss of operating authority in specific states.
   * *Clarification Needed:* Formal engagement with Head of Compliance Rajiv Mehta is required during Phase 1A to review technical specs and ensure driver mobile app updates fully satisfy federal compliance requirements without disrupting active driver workflows.