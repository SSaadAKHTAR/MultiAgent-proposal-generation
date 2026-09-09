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
    
    # We are looking for at least one 'contradicted' item in the matrix.
    # Specifically, they disagreed on budget, timeline, and scope.
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
    
    # Mock V1 proposal and translated feedback
    intake_text = "Standard intake."
    matrix_json = '{"business": {"pain_points": []}, "technical": {"pain_points": []}, "operational": {"pain_points": []}, "strategic": {"pain_points": []}}'
    
    from schemas import ClientMatrix
    import json
    matrix = ClientMatrix.model_validate(json.loads(matrix_json))
    
    feedback = "- Remove any mention of 'Agile' and use 'Waterfall' instead.\n- Add a section on 'Risk Mitigation'."
    
    proposal = ProposalAgent()
    v2_proposal = proposal.generate_proposal(intake_text, matrix, feedback)
    
    # LLM-as-a-judge to check if it actually complied
    llm = LLMProvider()
    judge_prompt = (
        f"Does the following proposal strictly follow these directives?\n"
        f"Directives: {feedback}\n\n"
        f"Proposal:\n{v2_proposal}\n\n"
        "Answer YES or NO and briefly explain why."
    )
    
    judgment = llm.generate_text(judge_prompt, system_instruction="You are an evaluator.")
    
    console.print(f"Judgment Result:\n{judgment}")
    if "YES" in judgment.upper():
        console.print("[bold green]PASS[/bold green]: Proposal Agent addressed the feedback.")
    else:
        console.print("[bold red]FAIL[/bold red]: Proposal Agent ignored the feedback.")

if __name__ == "__main__":
    eval_contradiction_recall()
    eval_loop_regression()
