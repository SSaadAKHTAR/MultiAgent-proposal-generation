# Executive Summary

Northwind Logistics has experienced impressive growth following recent acquisitions. However, operational infrastructure has not kept pace with business scaling. Core operational workflows currently suffer from manual friction between a custom legacy dispatch application ("Routemaster") and Salesforce, driver dissatisfaction with the legacy mobile application, and severe invoicing bottlenecks that delay working capital realization.

To resolve these immediate operational challenges while safeguarding future technical strategy, we propose a modular, outcome-focused engagement centered on a portable logic layer. This architecture serves as the definitive strategy for Northwind: it delivers immediate workflow relief and automation on top of Routemaster while guaranteeing that all business logic and integration pipelines remain fully portable to any future platform replacement.

By addressing key friction points, Northwind will release approximately $1.4M in working capital tied up in unbilled receivables, avoid an estimated $320,000 in additional dispatcher hiring costs, and achieve a 30% reduction in dispatch processing time per load—all while targeting a Q3 pilot deployment (September 30) and ensuring total alignment with the critical November ELD compliance mandate.

---

# Understanding

### Business & Financial Impact
* **Invoicing Delays & Working Capital:** Delays in reconciling operational data between systems leave finance up to 3 weeks behind on invoicing. Approximately $1.4M in working capital is currently locked in unbilled receivables. Restoring billing efficiency to a 5-day Days Sales Outstanding (DSO) will directly release this capital.
* **Operational Scalability:** Manual data entry across disconnected systems creates a significant operational bottleneck. Optimizing workflow productivity will achieve a 30% reduction in dispatch time per load and avoid the near-term need to hire four additional dispatchers (representing ~$320k in annual cost avoidance).

### Technical & Systems Landscape
* **Dispatch System (Routemaster):** A custom dispatch application built ~7 years ago, currently maintained internally by two engineers. Technical debt and codebase fragility limit rapid feature delivery and hinder operational efficiency.
* **CRM & Financial Systems:** Salesforce is utilized for CRM, and NetSuite for accounting. Data exchange between Routemaster and Salesforce relies on heavy manual re-entry, creating data discrepancies that delay customer invoicing.
* **Driver Mobile Experience:** Drivers utilize a custom React Native mobile application that suffers from high driver dissatisfaction and usability friction.
* **M&A Tech Integration:** Technology integration from recent acquisitions remains incomplete, adding operational complexity across systems.
* **Regulatory Compliance:** A federal ELD compliance mandate deadline occurs in November; missing this deadline could result in fines or losing operating authority. All technical modifications, particularly those touching the custom driver mobile application, must seamlessly coordinate with and avoid disturbing this compliance workstream.
* **Internal Project History:** Previous internal attempts to fix these exact workflow issues have failed twice, highlighting the need for an external approach that decouples workflow logic from underlying codebase fragility.

### Core Success Criteria
* Achieve a **30% reduction in dispatch time per load**.
* Re-establish a **5-day DSO**, unlocking ~$1.4M in working capital.
* Target production pilot deployment by **September 30 (Q3)**.
* Ensure **60–70% of built workflow logic remains portable**, providing full flexibility for future core platform evolution.
* Zero disruption to internal ELD compliance milestones.

---

# Approach

Our approach emphasizes targeted operational relief, system integration, and modular engineering to deliver immediate financial return while preserving long-term technical flexibility.

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
|  Routemaster (Custom) | <--- Sync Engine -> |       Salesforce      |
+-----------------------+                     +-----------------------+
```

### 1. Workflow Optimization & Manual Data Elimination
We will analyze the core dispatcher journey to eliminate redundant data entry between Routemaster and Salesforce. By implementing automated data synchronization pipelines and streamlined UI workflows, dispatchers can process loads faster and eliminate the manual errors currently delaying financial invoicing.

### 2. Definitive Strategy: Portable Integration Architecture
To address historical technical debt and satisfy both immediate operational needs and future platform goals, business rules and validation logic will be established in a decoupled, portable orchestration layer built on top of Routemaster. This definitive architectural pattern isolates workflow improvements from underlying codebase fragility and guarantees that 60–70% of the workflow automation developed during Phase 1 will migrate seamlessly to any future SaaS platform replacement.

### 3. Driver Experience & ELD Coordination
We will execute surgical enhancements to the custom React Native driver mobile app to address key usability pain points and ensure accurate load updates. Mobile updates will be explicitly synchronized with the compliance workstream to protect the November ELD mandate.

### 4. Financial Pipeline Acceleration
By automating load completion validation and bridging data accurately between Routemaster, Salesforce, and NetSuite, we will remove the 3-week invoicing lag, enabling the finance team to accelerate billing cycles and normalize DSO to 5 days.

---

# Phases & Timeline

The engagement is structured to hit the target **Q3 production pilot deployment (September 30)** while explicitly evaluating technical debt early to manage implementation risk.

```
+-----------------------------------------------------------------------------------+
| Phase 1: Discovery, Technical Audit & Blueprint (Weeks 1 - 3)                    |
|   - Workflow mapping, Routemaster debt audit, ELD alignment with Rajiv Mehta      |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Phase 2: Core Workflow Automation & Integration Build (Weeks 4 - 9)              |
|   - Routemaster-Salesforce data sync, driver UX updates, ELD integration          |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Phase 3: Pilot Deployment & Outcome Validation (Weeks 10 - 13 / Target Sept 30)  |
|   - Q3 pilot launch, dispatch time benchmark verification, DSO acceleration       |
+-----------------------------------------------------------------------------------+
```

### Phase 1: Discovery, Technical Debt Audit & Integration Blueprint (Weeks 1–3)
* Conduct deep-dive workflow mapping with dispatchers to identify specific manual data entry touchpoints.
* Perform a thorough technical debt assessment of the Routemaster codebase and database schemas to evaluate platform stability and mitigate technical risks against the aggressive Q3 schedule.
* Conduct a dedicated alignment session with Rajiv Mehta (Head of Compliance) and internal technical leads to review ELD compliance requirements, establish technical boundaries, and safeguard the November regulatory deadline.
* Define portable integration architecture and business rule validation specs.
* **Deliverable:** Workflow Blueprint, Technical Debt & Architecture Assessment, and ELD Compliance Coordination Plan.

### Phase 2: Core Workflow & Integration Engineering (Weeks 4–9)
* Develop automated data synchronization between Routemaster, Salesforce, and financial interfaces.
* Implement optimized dispatcher load-entry UI components.
* Refactor targeted driver mobile app components to improve user adoption and operational data capture without affecting ELD code paths.
* Conduct joint end-to-end testing with internal engineering and compliance leads.
* **Deliverable:** Functional Integration Engine, Beta Driver App Update, End-to-End Invoicing Pipeline.

### Phase 3: Pilot Rollout & Handover (Weeks 10–13 / Q3 Target: September 30)
* Deploy production pilot to a representative cohort of dispatchers and drivers by September 30.
* Benchmark operational metrics against target KPIs (30% dispatch time reduction, return to 5-day DSO).
* Complete technical documentation and knowledge transfer to internal engineers.
* **Deliverable:** Q3 Production Pilot Launch, Operational KPI Validation Report, Engineering Knowledge Transfer Documentation.

---

# Pricing Approach

To provide complete budget certainty, this Phase 1 engagement is structured as a fixed-fee agreement with milestone-based payments tied to verifiable deliverables.

### Benchmark & Budget Alignment
Historical engagements of similar scope for mid-market freight brokerages (covering discovery, architecture, workflow automation, and MVP delivery with a 4-person team) benchmark between $150,000 and $250,000. To align strictly with leadership parameters, the total fixed fee for this Phase 1 engagement is capped at **$300,000**.

### Fixed-Fee Milestone Breakdown

| Milestone | Deliverable / Outcome | Fee Amount (% Total) |
| :--- | :--- | :--- |
| **Milestone 1: Architecture, Technical Audit & Compliance Alignment** | Workflow Blueprint, Routemaster Technical Debt Audit, Architecture Spec, and ELD Coordination Plan | $90,000 (30%) |
| **Milestone 2: Integration Engine & Beta Delivery** | Routemaster-Salesforce data sync engine, billing pipeline integration, and Beta driver mobile app updates | $120,000 (40%) |
| **Milestone 3: Q3 Pilot Deployment & Handover** | Successful Q3 pilot launch (by Sept 30), verification of KPI performance (30% dispatch efficiency, DSO reduction), and engineering handover | $90,000 (30%) |
| **Total Fixed Fee** | **Capped Maximum Engagement Fee** | **$300,000 (100%)** |

This structure ensures financial predictability while tying capital outlay directly to measurable business outcomes, unlocking $1.4M in working capital and realizing $320k in dispatcher operational efficiency.