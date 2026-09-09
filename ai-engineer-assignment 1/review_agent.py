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
            "SEVERITY RUBRIC:\n"
            "- 'critical': a contradicted/low-confidence item is stated as fact, a required section is missing, "
            "or the pricing/approach directly conflicts with the Client Matrix.\n"
            "- 'high': a meaningful gap or inaccuracy that would embarrass the firm in front of the client.\n"
            "- 'medium': a clarity or completeness issue that should be fixed but isn't client-facing risky.\n"
            "- 'low': wording, formatting, or stylistic nitpicks.\n\n"
            "RECOMMENDATION RUBRIC:\n"
            "- 'approve': no issues of severity 'high' or 'critical' remain.\n"
            "- 'revise': there are 'high'/'critical' issues the Proposal Agent can reasonably fix next iteration.\n"
            "- 'escalate_to_human': a 'critical' issue has persisted across iterations, or resolving it requires "
            "a judgment call the Proposal Agent can't make alone (e.g., genuinely conflicting client feedback).\n\n"
            "COMPLETENESS CHECK: Verify all six required sections are present, in the required order, before "
            "evaluating content. A missing or reordered section is always at least a 'high' severity issue.\n\n"
            "Pay special attention to whether the proposal adhered to the Client Matrix. Specifically, check if "
            "items marked as 'contradicted' or 'low' confidence were properly placed in the 'Open Questions' section "
            "and not stated as confident facts. Do not recommend 'approve' simply because earlier issues were "
            "partially addressed — actively look for new problems, including ones not previously flagged."
        )
        
        prompt = (
            "Please critique the following proposal.\n\n"
            f"CLIENT MATRIX: \n{matrix_json}\n\n"
            f"PROPOSAL DRAFT: \n{proposal_text}\n"
        )
        
        return self.llm.generate_structured(
            prompt=prompt,
            schema=ReviewCritique,
            system_instruction=system_instruction,
            model="gemini-3.1-pro-preview",
            agent_name="ReviewAgent_Critique"
        )
        
    def translate(self, human_feedback: str, proposal_text: str, matrix: ClientMatrix) -> TranslatedFeedback:
        matrix_json = matrix.model_dump_json(indent=2)
        
        prompt = (
            f"HUMAN FEEDBACK: \n{human_feedback}\n\n"
            f"PROPOSAL DRAFT: \n{proposal_text}\n\n"
            f"CLIENT MATRIX: \n{matrix_json}\n\n"
            "Translate the human feedback into actionable directives."
        )
        
        system_instruction = (
            "You are an expert Translation Agent. The human reviewer has provided free-text feedback on the current proposal.\n"
            "Your job is to translate this raw human feedback into a structured list of clear, actionable directives "
            "for the Proposal Agent to follow on the next iteration. Do NOT just pass the feedback through verbatim. "
            "Interpret what it means in the context of the proposal and formulate explicit instructions.\n\n"
            "DIRECTIVE QUALITY BAR: Each directive must be specific enough that the Proposal Agent can act on it "
            "without re-reading the human's original wording. For example, 'fix the pricing' is not acceptable; "
            "'Replace the price range in Pricing Approach with a single fixed number, using the midpoint of the "
            "current range unless the Client Matrix or feedback specifies otherwise' is.\n\n"
            "CONFLICT HANDLING: If the feedback contradicts a 'high'-confidence item in the Client Matrix, or asks "
            "for something infeasible given the intake, do not silently comply. Write a directive that flags the "
            "conflict explicitly (e.g., 'Note in Open Questions that the client's ask for X conflicts with the "
            "confirmed budget of Y') rather than quietly overriding a confirmed fact."
        )

        return self.llm.generate_structured(
            prompt=prompt,
            schema=TranslatedFeedback,
            system_instruction=system_instruction,
            model="gemini-3.1-pro-preview",
            agent_name="ReviewAgent_Translate"
        )
