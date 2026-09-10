# Proposal for Northwind Logistics

## Executive Summary

Northwind Logistics is poised to unlock significant operational efficiency and free up vital capital tied up in unbilled receivables. Rapid growth—including a 40% surge in 2024 driven by acquisitions—has stretched existing systems, creating operational bottlenecks for dispatchers, friction for drivers, and a three-week billing delay in finance that currently holds $1.4M in working capital stuck in unbilled receivables.

Our proposed engagement provides an immediate, structured path to resolve these challenges. By streamlining dispatcher workflows between Routemaster and Salesforce, optimizing the mobile driver experience, and ensuring financial data alignment with NetSuite, our target outcomes include reducing load dispatch times by 30%, returning to an industry-standard 5-day Days Sales Outstanding (DSO), and avoiding approximately $320,000 in additional dispatcher headcount next year.

We propose a targeted fixed-fee engagement of **$250,000**, structured around deliverable milestones. We target a production pilot in Q3 to meet operational funding constraints. **Note on Recommended Targets:** Both the proposed $250,000 budget and the Q3 target pilot timeline are recommended targets. They are contingent upon completing Phase 1A discovery and reaching formal alignment among Northwind’s executive stakeholders on the unresolved items detailed in the Open Questions section.

---

## Understanding

### Business Context
Northwind Logistics is an $85M (2025 revenue) mid-market freight brokerage based in Columbus, OH, with ~200 employees, 40 dispatchers, and ~600 contracted drivers. Following 40% growth in 2024 driven by two brokerage acquisitions, financial workflows have struggled to keep pace. Finance is currently 3 weeks behind on invoicing due to data discrepancies between systems, leaving $1.4M in working capital trapped in unbilled receivables. Key executive objectives include returning to a 5-day DSO, unlocking $1.4M in working capital, and saving $320k annually by avoiding the need to hire four additional dispatchers.

### Operational Context
Dispatchers experience significant manual double-entry between Routemaster and Salesforce. Meanwhile, Northwind’s ~600 contracted drivers express high dissatisfaction with the custom React Native mobile driver app (which has not had a major update since 2023). Operational goals focus on achieving a 30% reduction in dispatch processing time per load and improving driver app usability without disrupting daily operations.

### Technical Context
Northwind’s core technical stack includes:
* **Dispatch System:** Routemaster, a 7-year-old custom Ruby on Rails 5 application maintained internally by 2 engineers. The codebase suffers from technical debt, making feature delivery slow and fragile.
* **CRM:** Salesforce (Sales Cloud).
* **Accounting:** NetSuite.
* **TMS:** Transportation Management System selection is currently undergoing vendor evaluation.
* **Analytics/BI:** No centralized data warehouse; reporting relies on manual Excel exports from Salesforce.
* **Acquisition Debt:** Technical integration from the two 2024 acquisitions remains incomplete.

### Strategic Context & Stakeholders
* **Sarah Chen (VP Operations):** Project champion seeking immediate operational workflow relief and a production pilot by end of Q3.
* **Marcus Patel (CTO):** Technical owner of Routemaster requiring full architectural sign-off; advocates for replacing Routemaster long-term.
* **Rita Donovan (CFO):** Budget controller requiring fixed-fee milestone pricing; cautious due to past vendor performance in 2023 and enforcing a strict $300k budget cap.
* **Rajiv Mehta (Head of Compliance):** Responsible for a mandatory federal ELD compliance update in November, which cannot be jeopardized by driver app modifications.

---

## Approach

Our methodology focuses on delivering immediate operational relief while building modular, resilient components that protect Northwind’s long-term technical investments:

1. **Decoupled Architecture & Strategic Preservation:** Rather than forcing an abrupt replacement of Routemaster with a new SaaS platform or applying superficial patches, we will build clean, decoupled integration layers. This approach ensures that 60–70% of the workflow and integration logic developed during Phase 1 will survive any future transition to a commercial TMS platform.
2. **Collaborative Technical Governance:** We will partner directly with CTO Marcus Patel during architecture design sessions to review and sign off on data schemas, API contracts, and integration patterns, ensuring development velocity without overburdening the internal two-person engineering team.
3. **Dispatcher & Invoicing Streamlining:** Direct integration between Routemaster, Salesforce, and NetSuite will eliminate manual double-entry, standardize load data, resolve billing discrepancies, and reduce dispatch processing times by 30%.
4. **Mobile Experience & ELD Coordination:** Upgrades to the React Native driver app will focus on core driver pain points while maintaining strict technical separation from ongoing ELD compliance work, in direct alignment with Head of Compliance Rajiv Mehta.
5. **Fixed-Fee, Milestone-Gated Execution:** To address CFO Rita Donovan’s risk requirements, all work will be structured under a fixed-fee agreement tied to concrete operational and technical milestones.

---

## Phases & Timeline

*Disclaimer: The schedule below outlines a Targeted Q3 Pilot contingent upon Phase 1A discovery and executive alignment on timeline and architectural direction as outlined in Open Questions.*

```
+-----------------------------------------------------------------------------------+
| PHASE 1A: Discovery, Architecture Alignment & ELD Mapping (Weeks 1-4)              |
| - Process mapping across Routemaster, Salesforce & NetSuite                      |
| - Technical architecture sign-off with CTO Marcus Patel                          |
| - Alignment on ELD mandate scope with Head of Compliance Rajiv Mehta             |
| - Finalizing target pilot scope and milestone agreement                          |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| PHASE 1B: Integration & Driver App Optimization (Weeks 5-12)                     |
| - Automated data sync between Routemaster and Salesforce                         |
| - Refactoring dispatcher load entry workflows (Target: 30% time savings)          |
| - Driver mobile app UX improvements (React Native)                               |
| - Financial data validation with NetSuite to resolve unbilled receivables        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| PHASE 1C: Targeted Q3 Pilot & Operational Rollout (Weeks 13-16)                  |
| - Targeted pilot deployment with subset of dispatchers and drivers                |
| - Validation of invoicing speed and DSO progress towards 5-day goal              |
| - Final handoff & documentation for internal engineering team                    |
+-----------------------------------------------------------------------------------+
```

---

## Pricing Approach

Based on past engagements of similar scale and complexity in mid-market freight brokerage (requiring a 4-person senior engagement team over a 3-to-4 month build), pricing typically ranges between $150,000 and $250,000. 

We propose a target fixed fee of **$250,000**, structured into outcome-based milestone payments.

*Note: This pricing structure and budget figure represent recommended targets contingent upon resolving the stakeholder budget and scope open questions during Phase 1A.*

### Milestone Payment Schedule

| Milestone | Deliverable / Outcome | Associated Fee | Percentage |
| :--- | :--- | :--- | :--- |
| **Milestone 1: Architecture Blueprint & Discovery** | Completion of Phase 1A discovery, architecture review and formal sign-off by CTO Marcus Patel, and ELD compliance alignment. | $62,500 | 25% |
| **Milestone 2: Integration & Workflow Build** | Delivery of Routemaster–Salesforce bi-directional sync, refactored dispatcher load entry, and updated driver mobile app build. | $112,500 | 45% |
| **Milestone 3: Pilot Deployment & Hand-Off** | Successful deployment of the production pilot, verification of invoicing data alignment with NetSuite, and technical operational transition. | $75,000 | 30% |
| **Total** | | **$250,000** | **100%** |

---

## Open Questions

To ensure full alignment before finalizing scope and commitments, the following contradicted points and risks identified during intake must be explicitly clarified and resolved during Phase 1A:

1. **Budget Range Alignment:** CFO Rita Donovan has indicated a strict budget cap of $300,000, whereas VP of Operations Sarah Chen previously discussed an anticipated range of $250,000 to $400,000. We need to confirm that our proposed $250,000 scope fully satisfies Sarah's operational goals while remaining comfortably within Rita's financial cap.
2. **Long-Term System Architecture Vision:** Stakeholders hold differing views regarding Routemaster's future: CTO Marcus Patel favors replacing Routemaster with a commercial SaaS platform, while VP Ops Sarah Chen favors incremental workflow fixes on Routemaster. We need to formalize alignment in Phase 1A that our build will focus on a decoupled integration layer where 60–70% of the logic survives a potential future SaaS transition.
3. **Pilot Schedule Feasibility:** VP Ops Sarah Chen and CFO Rita Donovan require a pilot in production by the end of Q3 (September 30) to secure internal budget allocation. However, CTO Marcus Patel considers Q4 to be a more realistic timeline for stable delivery. We must establish a mutually agreed, phased pilot scope during Phase 1A that satisfies operational deadlines without compromising technical quality.
4. **ELD Mandate Scope & Technical Requirements:** The precise technical requirements and scope of the federal ELD compliance update in November under Rajiv Mehta (Head of Compliance) remain unconfirmed. We need to review the ELD code and compliance specifications to ensure planned updates to the driver mobile app do not cause conflicts or compliance risks.