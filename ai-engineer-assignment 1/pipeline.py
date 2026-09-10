import os
import sys
# import time
import json
import argparse

from logger import current_logger
from debrief_agent import DebriefAgent
from proposal_agent import ProposalAgent
from review_agent import ReviewAgent
from schemas import ClientMatrix, ReviewCritique

def run_pipeline(intake_file: str, transcript_file: str):
    print(f"--- Starting Pipeline (Run ID: {current_logger.run_id}) ---")
    
    debrief = DebriefAgent()
    proposal = ProposalAgent()
    review = ReviewAgent()
    
    max_iterations = 5
    
    with open(intake_file, 'r') as f:
        intake_text = f.read()
    with open(transcript_file, 'r') as f:
        transcript_text = f.read()
        
    # 1. Debrief
    print("\nRunning Debrief Agent (Extracting Client Matrix)")
    current_logger.set_iteration(0)
    matrix = debrief.generate_matrix(intake_text, transcript_text)
    current_logger.log_artifact("client_matrix", matrix)
    print("Client Matrix Generated.")
    
    translated_feedback_text = ""
    start_iteration = 1
    proposal_text = None

    for iteration in range(start_iteration, max_iterations + 1):
        print(f"\n{'='*40}")
        print(f" ITERATION {iteration}")
        print(f"{'='*40}")
        
        current_logger.set_iteration(iteration)
        
        # Proposal
        print("\nRunning Proposal Agent (Synthesizing Proposal)...")
        proposal_text = proposal.generate_proposal(intake_text, matrix, translated_feedback_text, proposal_text)
        current_logger.log_artifact("proposal", proposal_text)
        print("Proposal Drafted.")
        
        #Review 
        print("\nRunning Review Agent (Critique)...")
        critique = review.critique(proposal_text, matrix)
        current_logger.log_artifact("critique", critique)
        print("-> Review Complete.")
        
        # print critique 
        print(f"\n[ Recommendation: {critique.recommendation.upper()} ]")
        if critique.risks:
            print("\nOverarching Risks:")
            for risk in critique.risks: 
                print(f" - {risk}")
                
        if critique.issues:
            print("\nCritique Issues:")
            for issue in critique.issues:
                print(f"  [{issue.severity.upper()}] {issue.location}: {issue.description}")
                print(f"  Suggested Fix: {issue.suggested_fix}\n")
        
        # Termination checks
        if critique.recommendation == "approve":
            print("\n*** Proposal approved by Review Agent, but passing to Human for final sign-off! ***")
        
        # Human in the loop
        print("\n Human Review ")
        
        print("Please review the critique and proposal.")
        print("You can type 'approve' to accept it, or provide free text feedback for the next iteration.")
        human_input = input("Feedback (or 'approve'): ").strip()
        
        current_logger.log_artifact("human_feedback", human_input)
        
        if human_input.lower() == 'approve':
            print("\n Proposal approved by Human! ")
            break
            
        # Review Translate feedback, human feedback and aicritique
        print("\nRunning Review Agent (Translate Feedback)...")
        translated = review.translate(human_input, proposal_text, matrix, critique)
        current_logger.log_artifact("translated_feedback", translated)
        
        translated_feedback_text = ""
        if translated.directives:
            formatted_directives = [f"- {d}" for d in translated.directives]
            translated_feedback_text = "\n".join(formatted_directives)
        
        print("\n FINAL DIRECTIVES SENT TO PROPOSAL AGENT ")
        print(translated_feedback_text)
        print("================================================\n")
        
    print(f"\nPipeline Finished. Run summary and complete logs saved in {current_logger.run_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Agent Client Proposal Pipeline")
    parser.add_argument("intake_file", help="Path to the intake markdown file")
    parser.add_argument("transcript_file", help="Path to the transcript markdown file")
    
    args = parser.parse_args()
    
    run_pipeline(args.intake_file, args.transcript_file)
