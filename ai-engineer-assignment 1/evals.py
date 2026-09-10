import sys
from rich.console import Console
from debrief_agent import DebriefAgent
from proposal_agent import ProposalAgent
from llm_provider import LLMProvider

console = Console()

def eval_contradiction_recall():
    console.print("[bold yellow]Running Eval 1: Contradiction Recall on Transcript B[/bold yellow]")
    
    with open("data/intake.md", "r") as f:
        intake_text = f.read()
    with open("data/transcript_b.md", "r") as f:
        transcript_text = f.read()
        
    debrief = DebriefAgent()
    matrix = debrief.generate_matrix(intake_text, transcript_text)

    contradictions_found = []
    
    # helper to check all items
    def check_items(category_items, category_name):
        for item in category_items:
            if item.confidence == "contradicted":
                contradictions_found.append(f"[{category_name}] {item.statement} (Note: {item.contradiction_note})")
                
    for row_name, category in [("business", matrix.business), ("technical", matrix.technical), ("operational", matrix.operational), ("strategic", matrix.strategic)]:
        check_items(category.pain_points, f"{row_name}.pain_points")
        check_items(category.desired_state, f"{row_name}.desired_state")
        check_items(category.success_criteria, f"{row_name}.success_criteria")
        check_items(category.risks_unknowns, f"{row_name}.risks_unknowns")
        
    if contradictions_found:
        console.print("[bold green]PASS[/bold green]: The Debrief Agent correctly preserved contradictions.")
        for c in contradictions_found:
            console.print(f" - {c}")
    else:
        console.print("[bold red]FAIL[/bold red]: The Debrief Agent flattened or averaged out the contradictions!")

def eval_loop_regression():
    console.print("\n[bold yellow]Running Eval 2: Loop Regression[/bold yellow]")
    
    intake_text = "Standard intake for a software project."
    matrix_json = '{"business": {"pain_points": []}, "technical": {"pain_points": []}, "operational": {"pain_points": []}, "strategic": {"pain_points": []}}'
    
    from schemas import ClientMatrix
    import json
    matrix = ClientMatrix.model_validate(json.loads(matrix_json))
    
    v1_proposal = (
        "# Executive Summary\nWe will build this using Agile methodology.\n\n"
        "# Understanding\nThe client needs a new system.\n\n"
        "# Approach\nStandard two-week sprints.\n\n"
        "# Phases & Timeline\n3 months total.\n\n"
        "# Pricing Approach\n$100k fixed.\n\n"
        "# Open Questions\nNone."
    )
    
    feedback = "- Remove any mention of 'Agile' and use 'Waterfall' instead.\n- Add a section on 'Risk Mitigation'."
    
    proposal = ProposalAgent()
    # Pass v1_proposal as the prior_draft
    v2_proposal = proposal.generate_proposal(intake_text, matrix, feedback_history=feedback, prior_draft=v1_proposal)
    
    # LLM-as-a-judge to check if it complied AND didn't rewrite unrelated sections
    llm = LLMProvider()
    judge_prompt = (
        f"Compare the V1 Proposal and V2 Proposal.\n\n"
        f"V1 Proposal:\n{v1_proposal}\n\n"
        f"Feedback Directives given to create V2:\n{feedback}\n\n"
        f"V2 Proposal:\n{v2_proposal}\n\n"
        "Check two things:\n"
        "1. Did V2 successfully apply the directives (removed Agile/added Waterfall, and added a Risk Mitigation section)?\n"
        "2. Did V2 keep the rest of the unrelated sections (Pricing, Timeline, Understanding) largely identical to V1 without silently rewriting them?\n\n"
        "Answer PASS if both are true, or FAIL if it ignored feedback or unnecessarily rewrote unrelated sections. Provide a brief explanation."
    )
    
    judgment = llm.generate_text(judge_prompt, system_instruction="You are an expert evaluator.")
    
    console.print(f"Judgment Result:\n{judgment}")
    if "PASS" in judgment.upper():
        console.print("[bold green]PASS[/bold green]: Proposal Agent addressed feedback AND preserved unrelated sections.")
    else:
        console.print("[bold red]FAIL[/bold red]: Proposal Agent failed the regression test.")

def eval_proposal_coherence():
    console.print("\n[bold yellow]Running Eval 3: Proposal Coherence[/bold yellow]")
    
    with open("data/intake.md", "r") as f:
        intake_text = f.read()
    with open("data/transcript_b.md", "r") as f:
        transcript_text = f.read()
        
    debrief = DebriefAgent()
    matrix = debrief.generate_matrix(intake_text, transcript_text)
    
    proposal = ProposalAgent()
    proposal_text = proposal.generate_proposal(intake_text, matrix)
    
    llm = LLMProvider()
    judge_prompt = (
        "Evaluate the following Proposal based on the provided Client Matrix.\n\n"
        f"CLIENT MATRIX: \n{matrix.model_dump_json(indent=2)}\n\n"
        f"PROPOSAL: \n{proposal_text}\n\n"
        "Check three things:\n"
        "1. Are the required sections present? (Executive Summary, Understanding, Approach, Phases & Timeline, Pricing Approach, Open Questions)\n"
        "2. Does the proposal address every 'high' confidence matrix item somewhere?\n"
        "3. Are all 'contradicted' or 'low' confidence items placed explicitly in the 'Open Questions' section?\n\n"
        "Output 'PASS' if all three are met, or 'FAIL' if any are violated, followed by a brief explanation."
    )
    
    judgment = llm.generate_text(judge_prompt, system_instruction="You are an expert evaluator.")
    
    console.print(f"Judgment Result:\n{judgment}")
    if "PASS" in judgment.upper():
        console.print("[bold green]PASS[/bold green]: Proposal coherence checks passed.")
    else:
        console.print("[bold red]FAIL[/bold red]: Proposal coherence checks failed.")

if __name__ == "__main__":
    eval_contradiction_recall()
    eval_loop_regression()
    eval_proposal_coherence()
