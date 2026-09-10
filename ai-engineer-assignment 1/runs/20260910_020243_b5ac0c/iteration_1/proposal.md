# Executive Summary

Northwind Logistics has experienced impressive growth, expanding revenue to ~$85M and absorbing two recent acquisitions. However, this rapid scaling has outpaced the current technical infrastructure. Today, operational friction between your custom dispatch tool and Salesforce is forcing manual double-entry, frustrating your 40 dispatchers, and alienating your 600 contracted drivers. More critically, data discrepancies have left Finance three weeks behind on invoicing. 

We propose a targeted, 6-month Phase 1 engagement to streamline these workflows. By bridging the gaps between your legacy systems, our goal is to return Northwind to a five-day Days Sales Outstanding (DSO)—freeing up approximately $1.4M in trapped working capital—and generate $320k in operational savings by avoiding the need for additional dispatcher headcount. We will deliver this while ensuring that all technical interventions strictly coordinate with your critical November ELD compliance mandate.

# Understanding

Based on our conversations with Northwind leadership, we understand the current landscape and your strategic objectives:

*   **Operational & Financial Pain:** Dispatchers are losing significant time to manual data entry between Routemaster (your custom Rails 5 app) and Salesforce CRM. Because this data frequently fails to align, Finance is severely delayed in invoicing through NetSuite. 
*   **Technical Context:** The legacy Routemaster platform carries severe technical debt, making feature development fragile and slow. Furthermore, the custom React Native driver app is currently highly unpopular with drivers. Internal attempts to resolve these workflow issues have been tried twice previously and failed, underscoring the complexity of the challenge.
*   **Compliance Imperative:** A federal ELD mandate update is due in November. Failure to meet this deadline risks severe regulatory penalties, including fines and the potential loss of operating authority in certain states. Any changes to the driver app must be carefully coordinated with this compliance effort.
*   **Success Criteria:** The engagement must achieve a 30% reduction in dispatch time per load, return the business to a five-day DSO, and ensure that 60–70% of the workflow logic built during Phase 1 remains portable to any future platform architecture. Finally, a pilot must be in production by the end of Q3 to prevent the reallocation of project funding.

# Approach

Our approach is designed to deliver rapid operational relief while safeguarding your long-term technical investments and regulatory standing.

1.  **Workflow & Data Synchronization:** We will focus strictly on eliminating the manual double-entry between Salesforce and Routemaster. By establishing reliable data pipelines, we will ensure that Finance receives accurate, timely data for NetSuite invoicing.
2.  **Portable Architecture:** Recognizing the fragility of the current codebase, we will build integration logic externally wherever possible. This guarantees that 60–70% of our Phase 1 deliverables will survive and provide value even if Northwind transitions to a new Transportation Management System (TMS) in the future.
3.  **Compliance-First Driver App Updates:** We will ring-fence the ELD compliance work. Any workflow improvements touching the driver mobile app will be mapped explicitly against the requirements of the Head of Compliance to ensure zero interference with the November mandate.
4.  **Milestone-Driven Delivery:** Given the history of internal project stalls, we will structure our delivery around concrete, verifiable milestones. This de-risks the engagement and provides transparent progress tracking for the CFO and executive sponsors.

# Phases & Timeline

We propose a 6-month Phase 1 engagement, structured to target the critical Q3 funding deadline and November compliance mandate:

*   **Phase 1A: Discovery & Alignment (Weeks 1–4)**
    *   Map data discrepancies between Routemaster, Salesforce, and NetSuite.
    *   Audit the driver app architecture to isolate ELD compliance dependencies.
*   **Phase 1B: Workflow MVP & Integration (Weeks 5–12)**
    *   Deploy automated data synchronization between dispatch and CRM.
    *   Target the 30% reduction in dispatch time through UI/workflow adjustments.
*   **Phase 1C: Target Pilot Launch (End of Q3)**
    *   Release the initial workflow improvements into production to satisfy funding requirements.
*   **Phase 1D: Financial Reconciliation & ELD Readiness (Weeks 13–24)**
    *   Stabilize the invoicing data pipeline to drive toward the five-day DSO target.
    *   Finalize coordination with the November ELD compliance rollout.

# Pricing Approach

Northwind has expressed a strong preference for a fixed-fee structure with milestone-based payments. We fully support this model, as it aligns our financial incentives with your operational outcomes. 

To provide context on our pricing, we recently completed a similar engagement for a peer freight brokerage (Cascade Freight). For a comparable cross-functional team (approx. 4 members), a 3-month discovery and MVP build typically falls within a price band of **$150,000 to $250,000**. 

Because Northwind requires a comprehensive 6-month Phase 1 engagement, we anticipate the total investment will scale accordingly. However, rather than billing time and materials, we will structure the final proposal as a hard fixed fee tied to the specific deliverables outlined in the Phases & Timeline section. We will finalize the exact pricing once we have resolved the open questions below.

# Open Questions

To finalize the scope and provide a binding fixed-fee quote, we must first address three areas where we have identified internal misalignment among Northwind stakeholders:

1.  **Budget Cap Clarification:** There is currently disagreement regarding the approved budget for this Phase 1 engagement. We need to confirm whether there is a strict hard cap of $300,000 (as indicated by Finance) or if the budget extends up to a $400,000 range (as indicated by Operations).
2.  **Long-Term Platform Strategy:** Stakeholders are fundamentally misaligned on the root cause of the operational issues. Specifically, we need a unified decision on whether the ultimate goal is to replace the legacy Routemaster platform entirely with a SaaS product, or to permanently fix the workflows within the existing proprietary system.
3.  **Q3 Timeline Feasibility:** While Operations and Finance have mandated that a pilot must be in production by the end of Q3 to secure funding, Engineering has indicated that Q3 may be unrealistic and prefers a Q4 target. We must align on a unified, realistic release date before finalizing the project schedule.