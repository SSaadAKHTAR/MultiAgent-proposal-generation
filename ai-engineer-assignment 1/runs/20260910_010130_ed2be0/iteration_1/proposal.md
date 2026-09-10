# Executive Summary

Northwind Logistics has experienced impressive growth, expanding 40% in 2024 to ~$85M in annual revenue. However, rapid expansion—including the acquisition of two smaller freight brokerages—has strained the company’s operational and technical infrastructure. Today, core operations face severe friction: 40 dispatchers struggle with manual data entry across disconnected systems, drivers express frustration with the mobile application, and finance lags three weeks behind on invoicing due to cross-system data misalignment.

To resolve these challenges without disrupting day-to-day operations, Northwind requires a targeted, outcome-driven consulting engagement. Leveraging our deep experience with peer freight brokerages (such as Cascade Freight), we propose a structured Phase 1 initiative designed to streamline load workflows, automate data reconciliation between dispatch, CRM, and accounting, and improve driver mobile interactions. 

Our approach emphasizes financial predictability through a fixed-fee model tied to tangible operational outcomes, including a targeted 30% reduction in dispatch time per load, freeing up $1.4M in working capital tied up in unbilled receivables, and avoiding $320k in planned dispatcher head count. By establishing a clean, portable workflow layer, we will deliver rapid operational relief while preserving Northwind's long-term technical flexibility.

---

# Understanding

Based on our discussions and intake analysis, Northwind Logistics' current operational and technical environment presents several distinct challenges and objectives:

### Operational & Financial Pain Points
* **Invoicing Delays & Working Capital Bottlenecks:** Finance is currently three weeks behind on invoicing because load and billing data do not align between systems. This delay locks up approximately $1.4M in working capital in unbilled receivables. The goal is to return to an industry-standard five-day Days Sales Outstanding (DSO).
* **Dispatcher Workload & Manual Data Entry:** Dispatchers perform redundant double-entry across the custom Rails dispatch tool and Salesforce. Achieving a 30% reduction in dispatch time per load will eliminate this inefficiency and allow Northwind to avoid hiring four additional dispatchers next year (saving approximately $320k).
* **Driver Mobile App Friction:** Contracted drivers (~600 drivers) report severe dissatisfaction with the custom React Native mobile app, which has not received a major update since 2023.

### Technical & Organizational Context
* **Core Application Stack:** The technical ecosystem relies on a custom Rails 5 dispatch application maintained internally by two engineers, Salesforce (Sales Cloud) for CRM, NetSuite for accounting, and Excel exports for reporting. Systems integration from recent acquisitions remains incomplete.
* **TMS Evaluation:** Management is currently evaluating commercial Transportation Management System (TMS) vendors, though no selection has been made.
* **Compliance Requirements:** Federal Electronic Logging Device (ELD) compliance mandates require updates by November, led by Head of Compliance Rajiv Mehta. Any operational or mobile app updates must strictly avoid interfering with ELD compliance.
* **Stakeholder Expectations:** Key leadership stakeholders—VP of Operations Sarah Chen, CTO Marcus Patel, CFO Rita Donovan, and Head of Compliance Rajiv Mehta—require a collaborative approach that respects budget limits, prevents past vendor pitfalls through fixed-fee milestone payments, and aligns operational needs with technical reality.

---

# Approach

We propose a four-pillar approach tailored to resolve immediate operational pain points while maintaining adaptability for Northwind’s technical future.

```
+-----------------------------------------------------------------------------------+
|                                 OUR APPROACH                                      |
+-----------------------------------------------------------------------------------+
|  1. Workflow & Data Synchronization Layer                                         |
|     Automate data flow between Salesforce, Rails dispatch tool, and NetSuite.     |
+-----------------------------------------------------------------------------------+
|  2. Revenue Cycle & Invoicing Streamlining                                        |
|     Eliminate 3-week billing lag to recover $1.4M in unbilled receivables.        |
+-----------------------------------------------------------------------------------+
|  3. Driver Experience & Compliance Coordination                                   |
|     Refine React Native mobile workflows while supporting ELD mandates.           |
+-----------------------------------------------------------------------------------+
|  4. Fixed-Fee Governance & Stakeholder Alignment                                  |
|     Ensure outcome-based milestone delivery and active executive alignment.       |
+-----------------------------------------------------------------------------------+
```

### Pillar 1: Workflow & Data Synchronization Layer
Rather than attempting a high-risk overhaul of legacy systems, we will introduce a portable workflow layer that bridges Salesforce, the custom Rails dispatch tool, and NetSuite. This layer will validate and synchronize load data automatically, eliminating dispatcher double-entry and reducing load dispatch time by 30%.

### Pillar 2: Revenue Cycle & Invoicing Streamlining
We will establish automated data reconciliation rules between dispatch completions and NetSuite billing. By ensuring load documents, rate confirmations, and pod data match before reaching finance, we will eliminate the three-week billing delay and accelerate progress toward a five-day DSO, releasing $1.4M in trapped working capital.

### Pillar 3: Driver Mobile Experience & Compliance Coordination
We will perform targeted updates to the React Native driver app to simplify load status updates and document capture. All driver-facing changes will be closely coordinated with Rajiv Mehta to guarantee seamless integration with upcoming November ELD compliance updates.

### Pillar 4: Fixed-Fee Governance & Stakeholder Alignment
To address CFO Rita Donovan’s emphasis on accountability and predictable costs, our engagement will be executed under a fixed-fee structure with payments tied strictly to tangible delivery milestones.

---

# Phases & Timeline

We structure Phase 1 into three sequential stages designed to deliver fast operational impact while maintaining rigorous quality control.

```
+-----------------------------------------------------------------------------------+
| PHASE 1A: Discovery, Mapping & Compliance Alignment (Weeks 1–4)                  |
| - Map load flows across Salesforce, dispatch tool, NetSuite, and driver app.      |
| - Establish data validation rules for invoicing & partner with ELD compliance.    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| PHASE 1B: Core Integration & Workflow Engine (Weeks 5–10)                         |
| - Implement portable workflow synchronization layer.                              |
| - Deliver targeted driver app updates and automated invoicing checks.             |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| PHASE 1C: Pilot Deployment & Operational Validation (Weeks 11–14+)               |
| - Roll out pilot to dispatcher cohort and select driver group.                    |
| - Measure reduction in dispatch time and validate DSO/invoicing acceleration.     |
+-----------------------------------------------------------------------------------+
```

* **Phase 1A: Discovery, Workflow Mapping & Architectural Alignment (Weeks 1–4)**
  * Audit load processing workflows across Salesforce, the dispatch tool, and NetSuite.
  * Define data reconciliation logic required to fix billing delays.
  * Partner with Rajiv Mehta on ELD compliance constraints.
* **Phase 1B: Core Integration & Portable Workflow Build (Weeks 5–10)**
  * Construct automated data synchronization logic between systems.
  * Implement driver app workflow updates for load tracking and document submission.
  * Build automated billing audit checks prior to NetSuite invoice creation.
* **Phase 1C: Pilot Deployment & Operational Validation (Weeks 11–14+)**
  * Launch pilot rollout with a dedicated group of dispatchers and drivers.
  * Measure time savings against the 30% dispatch reduction benchmark.
  * Track unbilled receivables reduction toward the five-day DSO goal.

---

# Pricing Approach

In alignment with CFO Rita Donovan’s requirements, we propose a **Fixed-Fee Structure with Outcome-Based Milestone Payments**. This eliminates financial uncertainty and ensures investment is tied directly to verified progress.

Based on historical data from similar past engagements in mid-market freight brokerage (utilizing a 4-person consulting team for discovery, integration build, and pilot deployment), typical investment levels fall within the following price band:

* **Estimated Investment Range:** $150,000 – $250,000 (Fixed Fee)

### Proposed Milestone Payment Schedule
1. **Milestone 1 (25%):** Completion of Phase 1A Discovery, Data Mapping & Compliance Strategy Approval.
2. **Milestone 2 (35%):** Delivery & Integration Testing of Core Portable Workflow Layer and Driver App Refinements.
3. **Milestone 3 (40%):** Successful Pilot Deployment, Dispatcher Efficiency Sign-off, and Invoicing Validation.

*Note: The exact fixed fee within this range will be finalized upon joint resolution of the scope open questions outlined below.*

---

# Open Questions

To ensure total transparency and alignment across the executive leadership team, the following items represent areas where stakeholder opinions currently differ or where confidence is low. These points require explicit clarification during alignment discussions:

1. **Phase 1 Budget Ceiling Alignment**
   * *Context / Disagreement:* There is an internal difference regarding the authorized Phase 1 budget limit. CFO Rita Donovan has indicated a strict $300,000 budget cap, whereas VP of Operations Sarah Chen has noted potential flexibility up to $400,000.
   * *Clarification Needed:* We require formal confirmation of the approved budget cap so we can finalize scope boundaries and resource allocation within agreed financial limits.

2. **Long-Term Dispatch System Strategy (SaaS Replacement vs. Incremental Fixes)**
   * *Context / Disagreement:* Leadership holds differing views on the technical path forward for the dispatch tool. CTO Marcus Patel advocates for a complete replacement with a third-party SaaS platform, while VP of Operations Sarah Chen prefers incremental workflow fixes on the existing custom Rails app (Routemaster).
   * *Clarification Needed:* We need consensus on whether Phase 1 should focus exclusively on building a portable workflow layer over the existing app or begin preparing integrations for an incoming SaaS TMS platform.

3. **Phase 1 Work Survivability Rate**
   * *Context / Low Confidence:* Current estimates suggest that 60–70% of the workflow logic and integration work built during Phase 1 will survive a future full platform or TMS replacement, but this estimate carries low confidence.
   * *Clarification Needed:* A technical architectural audit during Phase 1A is needed to establish precise technical dependencies and maximize long-term code portability.

4. **Pilot Target Timeline Alignment (Q3 vs. Q4)**
   * *Context / Disagreement:* Stakeholders differ on the target delivery date for the pilot release. VP of Operations Sarah Chen and CFO Rita Donovan mandate a Q3 pilot release (by September 30), whereas CTO Marcus Patel considers a Q4 timeline more realistic given code debt and engineering capacity.
   * *Clarification Needed:* We must establish a mutually agreed deployment schedule during Phase 1A that satisfies business urgency without compromising technical stability or ELD compliance work.