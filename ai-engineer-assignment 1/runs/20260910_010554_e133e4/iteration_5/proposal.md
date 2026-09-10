# Executive Summary
Northwind Logistics is facing critical operational bottlenecks stemming from inefficient dispatcher workflows, disjointed systems, and a driver mobile app that suffers from low adoption. These friction points require extensive manual data entry between custom tools and Salesforce, ultimately causing a three-week delay in invoicing. Northwind is seeking a partner to modernize these workflows, integrate core systems, and accelerate the invoicing cycle. We propose a focused, six-month Phase 1 engagement to streamline operations, reduce dispatch time, and return Northwind to a five-day Days Sales Outstanding (DSO), freeing up significant working capital.

# Understanding
Our understanding of Northwind Logistics' current environment and objectives is rooted in the following realities:

*   **Business Impact:** Delayed invoicing is currently locking up approximately $1.4M in working capital. Returning to a five-day DSO is a primary financial success metric for this initiative.
*   **Operational Friction:** The dispatcher workflow is highly inefficient, requiring manual data entry between Routemaster (a custom Rails 5 app) and Salesforce. Addressing this and reducing dispatch time by 30% will negate the need to hire four additional dispatchers. Furthermore, previous internal attempts to resolve these workflow issues have failed twice.
*   **System Landscape:** The technology stack includes Salesforce, NetSuite, a custom React Native driver app (which drivers currently dislike), and Routemaster. The dispatch tool suffers from severe technical debt that hinders new feature development. Additionally, technology integration from recent company acquisitions remains incomplete. 
*   **Strategic & Compliance Imperatives:** Missing the upcoming November federal ELD mandate update carries severe risks, including fines and the potential loss of operating authority in certain states. Any workflow improvements must be carefully coordinated to avoid interfering with this compliance work.

# Approach
To achieve Northwind's operational and financial goals, our approach will center on:

*   **Targeted Workflow Automation:** We will focus on eliminating manual data entry between dispatch and CRM/accounting systems to directly accelerate the invoicing cycle.
*   **Portable Architecture:** Recognizing the technical debt in the current ecosystem, we will design workflow logic to be portable, ensuring that 60-70% of the Phase 1 work will survive any potential future platform changes.
*   **Coordinated Driver App Enhancements:** We will address high-friction areas in the driver mobile app to improve satisfaction, ensuring all changes are tightly coordinated with the separate ELD compliance workstream.
*   **Technical Governance:** The proposed architecture will be submitted to the CTO for comprehensive review and sign-off prior to implementation.

# Phases & Timeline
*   **Phase 1 Duration:** 6 months.
*   **Delivery Model:** The engagement will be structured around fixed-fee milestone payments tied to specific, measurable outcomes, culminating in a production pilot. *(Note: Alignment on the exact delivery target date for this pilot is required; see Open Questions).*

# Pricing Approach
Based on our experience with similar mid-market freight brokerages (including our 2024 engagement with Cascade Freight, where a comparable but shorter 3-month MVP scope required a $150,000 – $250,000 investment), we have structured a fixed-fee model for this 6-month engagement. 

Per our recent discussions, we are proposing a **$295,000 fixed fee**. This figure explicitly references the 'Budget Cap' outlined in the Open Questions section below; it is based on the conservative $300,000 cap and is pending final internal budget alignment among Northwind stakeholders. Payments will be scheduled upon the completion of agreed-upon milestones to align with the CFO's requirements.

# Open Questions
To ensure a successful engagement, we must resolve the following areas where we have identified conflicting internal requirements or require further clarification:

*   **Budget Cap:** There is a discrepancy regarding the total budget for this engagement. The CFO has stated a strict $300,000 cap, whereas Operations indicated a potential range of $250,000 to $400,000. We need to confirm the final approved budget.
*   **Core Technical Approach:** There are differing technical visions for the dispatch tool. The CTO prefers replacing the legacy Routemaster system with a SaaS platform, while Operations prefers incrementally fixing workflows on the existing system. We must align on the architectural direction before finalizing the scope.
*   **Pilot Timeline:** There is a misalignment regarding the production pilot timeline. Operations and Finance require a Q3 (end of September) pilot to maintain funding, but the CTO believes Q4 is more realistic and has not committed to the Q3 date.
*   **ELD Compliance Details:** We currently lack specific details regarding the November ELD mandate requirements. We need to engage with the Head of Compliance, Rajiv Mehta, to ensure our proposed driver app updates do not conflict with these critical compliance efforts.