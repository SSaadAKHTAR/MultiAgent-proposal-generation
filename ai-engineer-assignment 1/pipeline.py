import os
import sys
import time
import json
import argparse

from logger import current_logger
from debrief_agent import DebriefAgent
from proposal_agent import ProposalAgent
from review_agent import ReviewAgent
from schemas import ClientMatrix

def run_pipeline(intake_file: str, transcript_file: str, resume_file: str = None):
    print(f"--- Starting Pipeline (Run ID: {current_logger.run_id}) ---")
    
    debrief = DebriefAgent()
    proposal = ProposalAgent()
    review = ReviewAgent()
    
    max_iterations = 5
    
    if resume_file:
        print(f"\n[BRANCHING] Resuming from checkpoint: {resume_file}")
        with open(resume_file, 'r') as f:
            state = json.load(f)
        
        matrix = ClientMatrix.model_validate(state['matrix'])
        proposal_text = state['proposal_text']
        translated_feedback_text = state['translated_feedback_text']
        previous_issues = set(state['previous_issues'])
        start_iteration = state['iteration']
        
        with open(intake_file, 'r') as f:
            intake_text = f.read()
            
        print(f"\n--- Restored to Iteration {start_iteration} Human Gate ---")
        human_input = input(f"Feedback for Iteration {start_iteration} (or 'approve'): ").strip()
        current_logger.log_artifact("human_feedback", human_input)
        
        if human_input.lower() == 'approve':
            print("\n*** Proposal approved by Human! ***")
            print(f"\nPipeline Finished. Run summary and complete logs saved in {current_logger.run_dir}")
            return
            
        print("\nRunning Review Agent (Translate Feedback)...")
        translated = review.translate(human_input, proposal_text, matrix)
        current_logger.log_artifact("translated_feedback", translated)
        translated_feedback_text = "\n".join(f"- {d}" for d in translated.directives)
        print("-> Feedback translated into structured directives for next iteration.")
        
        start_iteration += 1
    else:
        with open(intake_file, 'r') as f:
            intake_text = f.read()
        with open(transcript_file, 'r') as f:
            transcript_text = f.read()
            
        # 1. Debrief
        print("\nRunning Debrief Agent (Extracting Client Matrix)...")
        current_logger.set_iteration(0)
        matrix = debrief.generate_matrix(intake_text, transcript_text)
        current_logger.log_artifact("client_matrix", matrix)
        print("-> Client Matrix Generated.")
        
        translated_feedback_text = ""
        previous_issues = set()
        start_iteration = 1

    for iteration in range(start_iteration, max_iterations + 1):
        print(f"\n{'='*40}")
        print(f" ITERATION {iteration}")
        print(f"{'='*40}")
        
        current_logger.set_iteration(iteration)
        
        # 2. Proposal
        print("\nRunning Proposal Agent (Synthesizing Proposal)...")
        proposal_text = proposal.generate_proposal(intake_text, matrix, translated_feedback_text)
        current_logger.log_artifact("proposal", proposal_text)
        print("-> Proposal Drafted.")
        
        # 3. Review Critique
        print("\nRunning Review Agent (Critique)...")
        critique = review.critique(proposal_text, matrix)
        current_logger.log_artifact("critique", critique)
        print("-> Review Complete.")
        
        # Display critique in simple CLI
        print(f"\n[ Recommendation: {critique.recommendation.upper()} ]")
        if critique.risks:
            print("\nOverarching Risks:")
            for risk in critique.risks: 
                print(f" - {risk}")
                
        current_issues = set()
        if critique.issues:
            print("\nCritique Issues:")
            for issue in critique.issues:
                issue_key = f"{issue.location}:{issue.description}"
                current_issues.add(issue_key)
                print(f"  [{issue.severity.upper()}] {issue.location}: {issue.description}")
                print(f"  Suggested Fix: {issue.suggested_fix}\n")
        
        # Termination checks
        if critique.recommendation == "approve":
            print("\n*** Proposal approved by Review Agent! ***")
            break
            
        # Repeat-issue detection (Termination logic)
        repeated = current_issues.intersection(previous_issues)
        if repeated and iteration > 1:
            print("\n*** TERMINATING: Repeat-issue detected across iterations (Divergence). ***")
            for r in repeated:
                print(f" - {r}")
            break
        previous_issues = current_issues
        
        # Human in the loop
        print("\n--- Human Review ---")
        
        # [STRETCH GOAL] Checkpoint dump
        checkpoint_path = os.path.join(current_logger.run_dir, f"checkpoint_iter_{iteration}.json")
        with open(checkpoint_path, 'w') as f:
            json.dump({
                "iteration": iteration,
                "matrix": matrix.model_dump(),
                "proposal_text": proposal_text,
                "translated_feedback_text": translated_feedback_text,
                "previous_issues": list(previous_issues)
            }, f, indent=2)
        print(f"[*] State checkpoint saved to: {checkpoint_path}")
        print("    (You can branch from here using --resume <file>)")
        
        print("Please review the critique and proposal.")
        print("You can type 'approve' to accept it, or provide free-text feedback for the next iteration.")
        human_input = input("Feedback (or 'approve'): ").strip()
        
        current_logger.log_artifact("human_feedback", human_input)
        
        if human_input.lower() == 'approve':
            print("\n*** Proposal approved by Human! ***")
            break
            
        # 4. Review Translate
        print("\nRunning Review Agent (Translate Feedback)...")
        translated = review.translate(human_input, proposal_text, matrix)
        current_logger.log_artifact("translated_feedback", translated)
        
        translated_feedback_text = "\n".join(f"- {d}" for d in translated.directives)
        print("-> Feedback translated into structured directives for next iteration.")
        
    print(f"\nPipeline Finished. Run summary and complete logs saved in {current_logger.run_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Agent Client Proposal Pipeline")
    parser.add_argument("intake_file", help="Path to the intake markdown file")
    parser.add_argument("transcript_file", help="Path to the transcript markdown file (not needed if resuming, but required by positional arg format for now)")
    parser.add_argument("--resume", dest="resume_file", help="Path to a checkpoint JSON file to resume/branch from", default=None)
    
    args = parser.parse_args()
    
    run_pipeline(args.intake_file, args.transcript_file, args.resume_file)
