# Executive Summary

Northwind Logistics has experienced impressive growth, expanding to $85M in annual revenue following recent acquisitions. However, operational infrastructure has not kept pace with business scaling. Core operational workflows currently suffer from manual friction between a custom legacy dispatch application ("Routemaster") and Salesforce, driver dissatisfaction with the legacy mobile application, and severe invoicing bottlenecks that delay working capital realization.

To resolve these immediate operational challenges while safeguarding future flexibility, we propose a modular, outcome-focused engagement. Our objective is to streamline dispatcher workflows, automate data synchronization into accounting, and establish portable integration architecture. By addressing key friction points, Northwind can release approximately $1.4M in working capital tied up in unbilled receivables, avoid an estimated $320,000 in additional dispatcher hiring costs, and achieve a 30% reduction in dispatch processing time per load.

Our proposed approach focuses on delivering high-impact, incremental workflow improvements that complement internal technology initiatives—specifically respecting the critical, non-negotiable November ELD compliance workstream—while ensuring that the majority of solution logic remains portable to any future platform architecture.

---

# Understanding

### Business & Financial Impact
* **Invoicing Delays & Working Capital:** Delays in reconciling operational data between systems leave finance up to 3 weeks behind on invoicing. Approximately $1.4M in working capital is currently locked in unbilled receivables. Restoring billing efficiency to a 5-day Days Sales Outstanding (DSO) will directly release this capital.
* **Operational Scalability:** With 40 dispatchers managing ~600 contracted drivers across ~200 total employees, manual data entry creates a significant operational bottleneck. Optimizing workflow productivity can achieve a 30% reduction in dispatch time per load and avoid the near-term need to hire four additional dispatchers (representing ~$320k in annual cost avoidance).

### Technical & Systems Landscape
* **Dispatch System (Routemaster):** A custom Rails 5 application built ~7 years ago, currently maintained by two internal engineers. Technical debt and codebase fragility limit rapid feature delivery.
* **CRM & Financial Systems:** Salesforce (Sales Cloud) is utilized for CRM, and NetSuite serves as the core accounting platform. Data exchange between Routemaster, Salesforce, and NetSuite relies on heavy manual re-entry. Business intelligence currently depends on manual Excel exports.
* **Driver Mobile Experience:** Drivers utilize a custom React Native application (last major update in 2023) that suffers from low driver satisfaction.
* **M&A Tech Integration:** Technology integration from the 2024 acquisitions of two smaller brokerages remains incomplete, adding operational complexity.
* **Regulatory Compliance:** A federal ELD compliance mandate deadline occurs in November. All technical modifications, particularly those touching the driver mobile application, must seamlessly coordinate with and avoid disturbing this compliance workstream.

### Core Success Criteria
* Achieve a **30% reduction in dispatch time per load**.
* Re-establish a **5-day DSO**, unlocking ~$1.4M in working capital.
* Ensure **60–70% of built workflow logic remains portable**, ensuring long-term value preservation regardless of future core platform decisions.
* Zero disruption to internal ELD compliance milestones.

---

# Approach

Our approach emphasizes targeted operational relief, system integration, and modular engineering to deliver immediate financial return while preserving future technical flexibility.

```
       +-------------------------------------------------------+
       |             Dispatcher & Driver Interfaces            |
       +---------------------------+---------------------------+
                                   |
                                   v
       +-------------------------------------------------------+
       |             Portable Workflow Logic Layer             |
       |      (Isolated Business Rules & Validation Engine)     |
       +---------------------------+---------------------------+
                                   |
            +----------------------+----------------------+
            |                                             |
            v                                             v
+-----------------------+                     +-----------------------+
|  Routemaster (Rails)  | <--- Sync Engine -> | Salesforce & NetSuite |
+-----------------------+                     +-----------------------+
```

### 1. Workflow Optimization & Manual Data Elimination
We will analyze the core dispatcher journey to eliminate redundant data entry between Routemaster and Salesforce. By implementing automated data synchronization pipelines and streamlined UI workflows, dispatchers can process loads faster and eliminate the manual errors currently delaying financial invoicing.

### 2. Portable Integration Architecture
To protect Northwind's investment, business rules and validation logic will be designed within a decoupled, portable orchestration layer. This ensures that 60–70% of the workflow automation developed during this engagement can be directly migrated should Northwind transition platforms in the future.

### 3. Driver Experience & ELD Coordination
We will execute surgical enhancements to the React Native driver mobile app to address key usability pain points and ensure accurate load updates. All mobile development will be closely synchronized with the Head of Compliance (Rajiv Mehta) to ensure absolute alignment with the November ELD compliance mandate.

### 4. Financial Pipeline Acceleration
By automating load completion validation and bridging data directly into NetSuite, we will remove the 3-week invoicing lag, enabling the finance team to accelerate billing cycles and normalize DSO.

---

# Phases & Timeline

The engagement is structured into distinct workstreams designed to balance rapid operational wins with thorough technical validation.

```
+-----------------------------------------------------------------------------------+
| Phase 1: Discovery & Integration Blueprint (Weeks 1 - 4)                         |
|   - Workflow mapping, API audit, validation logic isolation architecture          |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Phase 2: Core Workflow Automation & Billing Integration Build (Weeks 5 - 12)    |
|   - Routemaster-Salesforce-NetSuite sync, driver UX updates, ELD alignment        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Phase 3: Pilot Deployment & Outcome Validation (Weeks 13 - 16)                    |
|   - Controlled rollout, dispatch time benchmark verification, DSO monitoring     |
+-----------------------------------------------------------------------------------+
```

### Phase 1: Discovery & Integration Architecture Blueprint (Weeks 1–4)
* Conduct deep-dive workflow mapping with 40 dispatchers to identify specific manual data entry touchpoints.
* Audit Routemaster (Rails 5) codebase, Salesforce, and NetSuite data schemas.
* Define portable integration architecture and business rule validation specs.
* Coordinate touchpoints with Compliance to establish clear boundaries for ELD updates.
* **Deliverable:** Workflow Blueprint, Technical Architecture Specification, and Compliance Coordination Plan.

### Phase 2: Core Workflow & Integration Engineering (Weeks 5–12)
* Develop automated data synchronization between Routemaster, Salesforce, and NetSuite.
* Implement optimized dispatcher load-entry UI components.
* Refactor targeted React Native driver app components to improve user adoption and data capture.
* Conduct joint testing with internal Rails engineers and Compliance.
* **Deliverable:** Functional Integration Engine, Beta Driver App Update, End-to-End Billing Data Pipeline.

### Phase 3: Pilot Rollout & Handover (Weeks 13–16)
* Launch pilot deployment with a representative cohort of dispatchers and contracted drivers.
* Benchmark operational metrics against target KPIs (30% dispatch time reduction, invoicing lag reduction).
* Complete technical documentation and knowledge transfer to internal engineers.
* **Deliverable:** Final Deployment Package, Operational KPI Validation Report, Engineering Knowledge Transfer Documentation.

---

# Pricing Approach

To ensure complete alignment with leadership expectations, we propose a **fixed-fee structure with milestone-based payments** tied directly to key project deliverables.

### Benchmark & Structure
Based on benchmark data from similar past engagements in freight brokerage and logistics (involving mid-market team structures and discovery-to-pilot delivery), comparable scope engagements typically map to a benchmark band of **$150,000 – $250,000**.

### Proposed Milestone Structure

| Milestone | Key Objective / Deliverable | Payment (% Fee) |
| :--- | :--- | :--- |
| **Milestone 1: Architecture & Alignment** | Delivery of Workflow Blueprint, Integration Architecture, and ELD Compliance Synchronization Plan | 30% |
| **Milestone 2: Integration & Beta Delivery** | Completion of Routemaster-Salesforce-NetSuite sync engine and Beta driver workflow updates | 40% |
| **Milestone 3: Pilot Rollout & Handover** | Deployment of pilot, confirmation of operational metrics, and full handover to internal engineering | 30% |

This fixed-fee model provides budget predictability for finance while tying investment directly to verifiable operational outcomes, including unlocking $1.4M in unbilled receivables and achieving $320k in operational cost avoidance.

---

# Open Questions

To ensure total alignment across Northwind Logistics' leadership team before kickoff, the following open questions and stakeholder alignment items must be formally addressed:

1. **Phase 1 Budget Cap Alignment:**
   * *Context:* Feedback reflects differing internal assumptions regarding the approved Phase 1 budget ceiling (a strict $300,000 cap versus a $250,000–$400,000 target range).
   * *Action Needed:* Confirm the binding fixed-fee budget threshold across the VP of Operations and CFO prior to final contract execution.

2. **Long-Term Platform Strategy (Fix vs. Replace):**
   * *Context:* Stakeholders hold varying views on whether Phase 1 should focus on incremental workflow enhancements over Routemaster or prepare for a broader legacy platform replacement/SaaS TMS selection.
   * *Action Needed:* Confirm leadership consensus on our proposed architecture—building a portable workflow/integration layer that solves immediate operational pain while ensuring 60–70% of built logic remains reusable if Routemaster is replaced in the future.

3. **Target Pilot Timeline & Production Readiness:**
   * *Context:* Target timeline expectations vary regarding pilot production readiness (end of Q3 versus Q4 execution window).
   * *Action Needed:* Review engineering dependencies during Phase 1 discovery to establish a mutually agreed deployment calendar that balances rapid operational relief with strict quality assurance.

4. **ELD Compliance Mandate Specifics:**
   * *Context:* Specific technical dependencies regarding the November federal ELD mandate update require formal review.
   * *Action Needed:* Schedule a dedicated technical alignment session with Rajiv Mehta (Head of Compliance) to review ELD requirements and map driver mobile app touchpoints.