from schemas import ReviewCritique, TranslatedFeedback, ClientMatrix
from llm_provider import LLMProvider

class ReviewAgent:
    def __init__(self):
        self.llm = LLMProvider()
        
    def critique(self, proposal_text: str, matrix: ClientMatrix) -> ReviewCritique:
        matrix_json = matrix.model_dump_json(indent=2)
        
        system_instruction = (
            "You are an expert Review Agent. Your job is to critique a draft client proposal.\n"
            "You must produce a structured critique, identifying any issues (with severity, location, description, and suggested fix), "
            "overarching risks, and a final recommendation (approve, revise, or escalate_to_human).\n\n"
            "Pay special attention to whether the proposal adhered to the Client Matrix. Specifically, check if "
            "items marked as 'contradicted' or 'low' confidence were properly placed in the 'Open Questions' section "
            "and not stated as confident facts."
        )
        
        prompt = (
            "Please critique the following proposal.\n\n"
            f"=== CLIENT MATRIX ===\n{matrix_json}\n\n"
            f"=== PROPOSAL DRAFT ===\n{proposal_text}\n"
        )
        
        return self.llm.generate_structured(
            prompt=prompt,
            schema=ReviewCritique,
            system_instruction=system_instruction,
            model_tier="simple",
            agent_name="ReviewAgent_Critique"
        )
        
    def translate(self, human_feedback: str, proposal_text: str, matrix: ClientMatrix) -> TranslatedFeedback:
        matrix_json = matrix.model_dump_json(indent=2)
        
        prompt = (
            f"=== HUMAN FEEDBACK ===\n{human_feedback}\n\n"
            f"=== PROPOSAL DRAFT ===\n{proposal_text}\n\n"
            f"=== CLIENT MATRIX ===\n{matrix_json}\n\n"
            "Translate the human feedback into actionable directives."
        )
        
        system_instruction = (
            "You are an expert Translation Agent. The human reviewer has provided free-text feedback on the current proposal.\n"
            "Your job is to translate this raw human feedback into a structured list of clear, actionable directives "
            "for the Proposal Agent to follow on the next iteration. Do NOT just pass the feedback through verbatim. "
            "Interpret what it means in the context of the proposal and formulate explicit instructions."
        )

        return self.llm.generate_structured(
            prompt=prompt,
            schema=TranslatedFeedback,
            system_instruction=system_instruction,
            model_tier="complex",
            agent_name="ReviewAgent_Translate"
        )
