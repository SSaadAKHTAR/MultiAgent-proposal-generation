# Executive Summary

Northwind Logistics has experienced impressive growth, expanding by 40% in 2024 through strategic acquisitions. However, this rapid scale has strained existing operational systems, particularly the dispatcher workflow and the data alignment between Routemaster and Salesforce. This proposal outlines a 6-month Phase 1 engagement designed to resolve these critical bottlenecks. By streamlining these workflows, our goal is to reduce dispatch time per load by 30%—avoiding the need to hire four additional dispatchers—and return Northwind to a five-day Days Sales Outstanding (DSO), thereby freeing up approximately $1.4M in working capital.

# Understanding

Northwind Logistics is managing significant operational pain stemming from fragmented systems and incomplete technology integration following recent acquisitions. 

*   **Operational & Financial Pain:** Dispatcher workflows are highly inefficient, causing significant operational strain. Furthermore, Finance is currently three weeks behind on invoicing due to manual entry requirements and data discrepancies between Routemaster and Salesforce.
*   **Driver Experience:** Drivers are highly dissatisfied with the current custom React Native mobile application.
*   **Technical Context:** Routemaster suffers from severe technical debt, preventing new feature development. Internal attempts to resolve these workflow issues have failed twice previously.
*   **Strategic Constraints:** Any changes made, particularly to the driver app, must not interfere with the upcoming federal ELD mandate update scheduled for November. Missing this deadline carries severe risks, including fines and the potential loss of operating authority.
*   **Success Criteria:** Success for this phase includes freeing up working capital via a five-day DSO, reducing dispatch time by 30%, and ensuring that 60-70% of the workflow logic built during Phase 1 remains portable in the event of a future platform change. Additionally, the CTO must review and approve the proposed architecture.

# Approach

Our approach centers on mitigating Northwind's immediate operational friction while laying a stable foundation for future technical decisions. We will begin by mapping the exact data discrepancies between Routemaster and Salesforce that are delaying the finance team. From there, we will design a robust integration and workflow optimization plan. To satisfy the requirement for future portability, we will decouple the core workflow logic from Routemaster wherever possible, ensuring a high survival rate of the code if the underlying platform changes.

Given the strict regulatory environment, we will coordinate all driver-facing mobile app enhancements with the compliance team to ensure zero interference with the ELD mandate workstream. Finally, no development will commence until the proposed architecture has been thoroughly reviewed and approved by the CTO.

# Phases & Timeline

This Phase 1 engagement is structured over a 6-month period. *(Note: The exact target date for the production pilot is pending internal alignment—see Open Questions).*

*   **Phase 1: Discovery & Architecture Design:** Deep dive into Routemaster and Salesforce data models. Define portable workflow logic. Concludes with CTO architectural review and sign-off.
*   **Phase 2: Workflow & Integration Development:** Implementation of data synchronization between Routemaster and Salesforce to unblock the Finance team and streamline dispatcher manual entry.
*   **Phase 3: Driver App Enhancements:** Targeted updates to the React Native driver app to improve user experience, executed in strict coordination with ELD compliance efforts.
*   **Phase 4: Pilot & Stabilization:** Deployment of the optimized workflow to a pilot group of dispatchers and drivers, followed by monitoring, bug fixing, and transition.

# Pricing Approach

Based on our experience delivering similar workflow optimizations and MVP builds for peer freight brokerages (such as our 2024 engagement with Cascade Freight, where a comparable initial 3-month scope fell into the $150,000–$250,000 range), we have structured a comprehensive 6-month Phase 1 engagement. 

To align with Northwind’s financial requirements and provide absolute predictability, we are proposing a fixed-fee structure with milestone-based payments tied to specific outcomes. The total fixed fee for this engagement is **$295,000**, which sits safely below the maximum budget threshold.

*   **Milestone 1 (20%):** CTO Approval of Architecture & Technical Design ($59,000)
*   **Milestone 2 (30%):** Completion of Routemaster/Salesforce Integration ($88,500)
*   **Milestone 3 (30%):** Deployment of the Production Pilot ($88,500)
*   **Milestone 4 (20%):** Final Handoff & Project Completion ($59,000)

# Open Questions

To ensure complete alignment before project kickoff, we need to resolve the following areas where internal perspectives at Northwind currently differ or where we lack critical details:

*   **Budget Cap:** There are conflicting signals regarding the maximum budget. The CFO has indicated a strict $300,000 cap for this phase, while Operations discussed a potential range of $250,000 to $400,000. We have priced this proposal under the $300,000 cap, but we must confirm the final approved budget limits before proceeding.
*   **Core Technical Approach:** We need to align on the long-term vision for Routemaster. The CTO has expressed a strong desire to replace Routemaster entirely with a SaaS platform, whereas Operations prefers to incrementally fix workflows on the existing system. This decision fundamentally impacts our architectural approach.
*   **Pilot Timeline:** There is a discrepancy regarding the pilot launch date. Operations and Finance require a pilot in production by the end of Q3 (September 30) to secure funding, while the CTO believes Q4 is a more realistic timeline and has not committed to Q3. We must agree on a feasible and fully supported launch date.
*   **ELD Compliance Details:** We currently lack the specific technical and regulatory details of the upcoming federal ELD mandate update. We need to review these requirements with the Head of Compliance to ensure our work on the driver mobile app does not cause conflicts or risk Northwind's operating authority.