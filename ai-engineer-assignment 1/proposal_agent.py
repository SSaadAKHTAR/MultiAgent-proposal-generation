from schemas import ClientMatrix
from llm_provider import LLMProvider

def lookup_similar_engagement(industry: str, team_size: int) -> str:
    """
    Looks up pricing and scope data for a similar past engagement.
    Call this tool when drafting the Pricing Approach section.
    
    Args:
        industry: The client's industry (e.g., 'healthcare', 'finance')
        team_size: Approximate team size required.
    """
    # Mock data to satisfy the tool call requirement
    return (
        f"Similar past engagement in {industry} for team size {team_size}:\n"
        "Scope: 3-month discovery and MVP build.\n"
        "Price band: $150k - $250k.\n"
        "Outcome: Delivered on time, client upsold to retainer."
    )

class ProposalAgent:
    def __init__(self):
        self.llm = LLMProvider()
        
    def generate_proposal(self, intake_text: str, matrix: ClientMatrix, feedback_history: str = "") -> str:
        # Convert matrix to json for context
        matrix_json = matrix.model_dump_json(indent=2)
        
        system_instruction = (
            "You are an expert Proposal Agent. Write a polished client proposal in Markdown.\n\n"
            "REQUIREMENTS:\n"
            "1. The proposal MUST have exactly these sections in order: Executive Summary, Understanding, "
            "Approach, Phases & Timeline, Pricing Approach, Open Questions.\n"
            "2. IMPORTANT: Any items in the Client Matrix marked with 'contradicted' or 'low' confidence MUST "
            "be placed in the 'Open Questions' section and explicitly addressed as areas needing clarification. "
            "Do NOT present them as confident statements elsewhere in the proposal.\n"
            "3. Use the `lookup_similar_engagement` tool to get pricing data for the Pricing Approach section.\n"
            "4. If there is feedback_history provided from a human, you MUST incorporate those changes into the proposal.\n"
        )
        
        prompt = (
            "Please generate the Markdown proposal based on the following context.\n\n"
            f"=== INTAKE ===\n{intake_text}\n\n"
            f"=== CLIENT MATRIX (JSON) ===\n{matrix_json}\n\n"
        )
        
        if feedback_history:
            prompt += f"=== HUMAN FEEDBACK DIRECTIVES ===\n{feedback_history}\n\n"
            
        # We pass the tool function directly to the LLM
        return self.llm.generate_text(
            prompt=prompt,
            system_instruction=system_instruction,
            tools=[lookup_similar_engagement],
            model_tier="complex",
            agent_name="ProposalAgent"
        )
