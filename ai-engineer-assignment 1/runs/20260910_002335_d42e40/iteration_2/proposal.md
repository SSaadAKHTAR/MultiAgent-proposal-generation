# Proposal for Northwind Logistics: Operations & Workflow Transformation

## Executive Summary

Northwind Logistics has achieved impressive growth, expanding 40% in 2024 through acquisition to reach ~$85M in annual revenue. However, rapid expansion has strained operational systems. Disconnects between custom core tools, Salesforce, and finance platforms have created significant operational drag: finance currently operates 3 weeks behind on invoicing, leaving $1.4M in working capital locked in unbilled receivables, while 40 dispatchers face continuous manual data re-entry.

To unlock this capital and support scalable growth, Northwind requires targeted operational streamlining and system integration. This engagement delivers an immediate, pilot-tested integration solution designed to:
* **Eliminate Invoicing Delays:** Streamline data flows to move from a 3-week invoicing lag back to an industry-standard 5-day Days Sales Outstanding (DSO), unlocking $1.4M in working capital.
* **Boost Dispatcher Efficiency:** Reduce dispatch time per load by 30%, enabling existing teams to handle increased volume and avoiding $320,000 in planned headcount expansion (4 dispatchers).
* **Deliver Fast Risk-Mitigated Value:** Deploy a operational production pilot by September 30 (end of Q3) to maintain operational momentum, while aligning system updates with the upcoming November federal ELD compliance mandate.

Drawing on our direct experience delivering similar operational transformations for peer freight brokerages (such as Cascade Freight), we propose a modular, fixed-fee engagement structured around strict milestone deliverables.

---

## Understanding

Following Northwind's 2024 acquisitions, incomplete technology integration has created critical bottlenecks across financial, operational, and technical functions:

* **Financial Bottlenecks & Working Capital Friction:**
  * **Invoicing Lag:** Data misalignment between dispatch and billing creates a 3-week backlog in invoice processing.
  * **Working Capital Lockup:** $1.4M in working capital is currently tied up in unbilled receivables.
  * **DSO Target:** The business requires a structural return to an industry-standard 5-day DSO.

* **Operational & Dispatch Inefficiencies:**
  * **Manual Double-Entry:** 40 dispatchers must manually re-key data between the primary dispatch system and Salesforce (Sales Cloud).
  * **Capacity Constraints:** Rapid growth threatens to require 4 additional dispatcher hires ($320k in annual operating expense) unless efficiency is increased by 30% per load.
  * **Driver Experience:** ~600 contracted drivers report friction with the custom React Native mobile app (last significantly updated in 2023).

* **System & Regulatory Landscape:**
  * **Core Systems:** Core dispatch runs on a custom Rails 5 app maintained by a lean two-person team, integrated with Salesforce and NetSuite (accounting), with no centralized data warehouse.
  * **Regulatory Compliance:** A federal Electronic Logging Device (ELD) mandate update takes effect in November, requiring coordinated updates to driver-facing workflows.
  * **Previous Internal Initiatives:** Two previous internal attempts to resolve these workflow and integration challenges have failed. The proposed decoupled architecture, combined with dedicated external engineering and domain expertise, directly addresses the root causes of those past failures by insulating business logic from legacy constraints and providing hands-on execution bandwidth.

---

## Approach

Our technical and operational approach focuses on decoupling business workflows from underlying legacy code, delivering fast operational relief while maintaining technical flexibility.

```
+-----------------------------------------------------------------------+
|                         APPLICATION LAYER                             |
|   Salesforce (CRM)   |   Driver Mobile App   |   NetSuite (ERP)       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                      DECOUPLED INTEGRATION LAYER                      |
|        - Automated Data Validation & Sync                            |
|        - Portable Workflow Logic & Rules                             |
|        - Standardized API Gateway                                    |
+-----------------------------------------------------------------------+
                                   ^
                                   |
+-----------------------------------------------------------------------+
|                          DISPATCH SYSTEM                              |
|                    Custom Dispatch Tool (Rails)                       |
+-----------------------------------------------------------------------+
```

1. **Decoupled Workflow & Integration Layer:**
   Instead of modifying legacy codebase monoliths directly, we introduce a lightweight, decoupled middleware/integration approach. Workflows between dispatch, Salesforce, and NetSuite are automated externally, ensuring data synchronization without introducing fragility to existing software.

2. **Dispatcher Automated Data Synchronization:**
   We eliminate manual double-entry by establishing direct automated integration between dispatch logs and Salesforce load records. Invoicing triggers automatically upon load completion, eliminating the 3-week billing queue.

3. **Driver Mobile & ELD Coordination:**
   Mobile workflow updates will be strictly coordinated with compliance requirements, establishing a clean interface for driver load updates while ensuring full compliance with the November federal ELD mandate.

4. **Architecture Portability:**
   All workflow automation and business logic implemented in Phase 1 will be built as modular services. This guarantees that business logic developed today remains fully portable to any future infrastructure or software platform Northwind adopts.

---

## Phases & Timeline

The proposed 6-month Phase 1 engagement is structured into clear sub-phases, specifically ensuring the production pilot is operational prior to the Q3 deadline.

```
2025 Timeline
Month        |  Month 1  |  Month 2  |  Month 3  |  Month 4  |  Month 5  |  Month 6  |
-------------+-----------+-----------+-----------+-----------+-----------+-----------+
Phase 1A     |=======>   |           |           |           |           |           |
Discovery    |           |           |           |           |           |           |
-------------+-----------+-----------+-----------+-----------+-----------+-----------+
Phase 1B     |           |==========>|           |           |           |           |
Core Build   |           |           |           |           |           |           |
-------------+-----------+-----------+-----------+-----------+-----------+-----------+
Phase 1C     |           |           |==========>| (Sept 30) |           |           |
Pilot Deploy |           |           |           |  PILOT    |           |           |
-------------+-----------+-----------+-----------+-----------+-----------+-----------+
Phase 1D     |           |           |           |==========>|==========>|=======>   |
Stabilize/ELD|           |           |           |           |           | (Nov ELD) |
```

* **Phase 1A: Discovery, Integration Architecture & ELD Alignment (Weeks 1–4)**
  * Audit current data flows across Salesforce, NetSuite, and dispatch software.
  * Map precise billing bottleneck validation rules to enable immediate invoicing.
  * Define technical specifications in partnership with compliance leadership for the ELD update.

* **Phase 1B: Core Integration & Workflow Automation Build (Weeks 5–10)**
  * Construct decoupled integration pipeline between dispatch records, Salesforce, and NetSuite.
  * Implement automated load status sync to eliminate dispatcher double-entry.
  * Refactor mobile data upload workflows for driver efficiency.

* **Phase 1C: Production Pilot Deployment & Operational Rollout (Weeks 11–14)**
  * **Target Completion Date: By end of Q3 (September 30)**
  * Deploy production pilot across a select subset of dispatchers and driver groups to achieve immediate operational validation and secure funding alignment.
  * Validate reduction in billing lag and dispatch handling duration in live operations.

* **Phase 1D: Post-Pilot Stabilization & November ELD Final Integration Support (Weeks 15–24)**
  * Scale pilot functionality across all 40 dispatchers and full contracted driver base.
  * Finalize and deploy ELD compliance updates ahead of the federal November deadline.
  * Measure working capital release and present Phase 1 ROI audit to executive leadership.

---

## Pricing Approach

In accordance with Northwind's procurement preference, this engagement is structured under a **Fixed-Fee Model with Milestone-Based Payments** tied strictly to verified deliverable completions.

* **Budget Commitment:** The total fixed fee for this 6-month engagement will be scoped to fit strictly within the **$300,000 budget cap** approved by CFO Rita Donovan, while acknowledging the $250k–$400k exploratory range discussed with VP of Operations Sarah Chen. Scope details will be tailored to ensure complete delivery within the authorized $300k ceiling.

* **Proposed Milestone Schedule:**
  * **Milestone 1 (15%):** Completion of Phase 1A Discovery & Architecture Sign-off.
  * **Milestone 2 (35%):** Delivery of Core Integration Middleware and User Acceptance Testing (UAT) Completion.
  * **Milestone 3 (30%):** Phase 1C Production Pilot Deployment (Completed by September 30 / End of Q3).
  * **Milestone 4 (20%):** Full Deployment, November ELD Final Integration, and Final Phase 1 Sign-off.

---

## Open Questions

To ensure total clarity and executive alignment before contract finalization, the following items require formal internal clarification and joint resolution during kick-off:

1. **Phase 1 Approved Budget Cap:**
   * *Context:* Dialogue indicates a variance between CFO Rita Donovan ($300k strict budget cap) and VP of Operations Sarah Chen ($250k–$400k range).
   * *Clarification Needed:* We will baseline final contract scope against the formal $300,000 approved cap to align with executive expectations.

2. **Core Platform Direction (Routemaster vs. SaaS):**
   * *Context:* CTO Marcus Patel favors replacing the existing Rails application with a SaaS platform, whereas Sarah Chen advocates for incremental workflow fixes directly on the current system.
   * *Clarification Needed:* Confirming consensus on deploying our decoupled integration architecture, which satisfies immediate operational requirements while keeping long-term platform migration options open.

3. **Pilot Timeline Alignment & Feasibility:**
   * *Context:* Executive leadership requires a production pilot live by end of Q3 (September 30) to protect project funding, while technical leadership has expressed that Q4 may be a more realistic delivery target.
   * *Clarification Needed:* Formal agreement on Phase 1C pilot scope boundary to ensure a meaningful, production-grade pilot can be safely shipped by September 30.

4. **Codebase Reusability & Survival Rate:**
   * *Context:* Current estimates target that 60–70% of Phase 1 architecture work will survive any future TMS or platform transition.
   * *Clarification Needed:* Validation of specific technical architectural patterns with CTO Marcus Patel to maximize code reusability in the event of a future SaaS migration.

5. **Federal ELD Mandate Requirements:**
   * *Context:* Specific technical dependencies regarding the November federal ELD mandate update remain to be detailed.
   * *Clarification Needed:* Direct engagement with Head of Compliance Rajiv Mehta in Week 1 to detail compliance inputs and dependency schedules.