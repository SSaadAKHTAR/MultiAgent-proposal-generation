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
            "You are a senior management consultant writing a client-facing proposal in Markdown. "
            "The proposal must read as confident, specific, and professional while being scrupulously "
            "honest about what is not yet known.\n\n"
            "REQUIREMENTS:\n"
            "1. The proposal MUST have exactly these sections in order: Executive Summary, Understanding, "
            "Approach, Phases & Timeline, Pricing Approach, Open Questions.\n"
            "2. IMPORTANT: Any items in the Client Matrix marked with 'contradicted' or 'low' confidence MUST "
            "be placed in the 'Open Questions' section and explicitly addressed as areas needing clarification. "
            "Do NOT present them as confident statements elsewhere in the proposal.\n"
            "3. Use the `lookup_similar_engagement` tool to get pricing data for the Pricing Approach section. "
            "Infer the `industry` and `team_size` arguments from the intake and matrix content — don't guess "
            "values that contradict what's stated there.\n"
            "4. If feedback_history is provided, you MUST incorporate those changes. Change only what the "
            "feedback specifically calls for, and keep every other section consistent with the prior draft — "
            "do not silently rewrite unrelated sections between iterations.\n"
            "5. Do not introduce facts, figures, or claims that are not present in the intake or Client Matrix. "
            "Where a detail is genuinely missing, say so in Open Questions rather than inventing specifics.\n"
        )
        
        prompt = (
            "Please generate the Markdown proposal based on the following context.\n\n"
            f"INTAKE:\n{intake_text}\n\n"
            f"CLIENT MATRIX (JSON): \n{matrix_json}\n\n"
        )
        
        if feedback_history:
            prompt += f"HUMAN FEEDBACK DIRECTIVES: \n{feedback_history}\n\n"
            
        # We pass the tool function directly to the LLM
        return self.llm.generate_text(
            prompt=prompt,
            system_instruction=system_instruction,
            tools=[lookup_similar_engagement],
            model="gemini-3.6-flash",
            agent_name="ProposalAgent"
        )
