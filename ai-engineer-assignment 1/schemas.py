from typing import List, Literal, Optional
from pydantic import BaseModel, Field

# --- Debrief Agent Schemas ---

class MatrixItem(BaseModel):
    statement: str = Field(..., description="The claim, 1-2 sentences.")
    confidence: Literal["high", "medium", "low", "contradicted"] = Field(
        ..., description="Confidence level of the statement."
    )
    source_excerpt: str = Field(
        ..., description="Short quote from the transcript or intake supporting the item."
    )
    contradiction_note: Optional[str] = Field(
        None, description="Required if confidence is 'contradicted'; describes the disagreement."
    )

class MatrixCategory(BaseModel):
    pain_points: List[MatrixItem] = Field(default_factory=list)
    desired_state: List[MatrixItem] = Field(default_factory=list)
    success_criteria: List[MatrixItem] = Field(default_factory=list)
    risks_unknowns: List[MatrixItem] = Field(default_factory=list)

class ClientMatrix(BaseModel):
    business: MatrixCategory
    technical: MatrixCategory
    operational: MatrixCategory
    strategic: MatrixCategory

# --- Review Agent Schemas ---

class Issue(BaseModel):
    severity: Literal["low", "medium", "high", "critical"]
    location: str = Field(..., description="Where in the proposal the issue is found (e.g., 'Pricing Approach', 'Paragraph 2')")
    description: str = Field(..., description="Description of the issue")
    suggested_fix: str = Field(..., description="Actionable fix for the issue")

class ReviewCritique(BaseModel):
    issues: List[Issue] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list, description="Any overarching risks with the current proposal.")
    recommendation: Literal["approve", "revise", "escalate_to_human"] = Field(
        ..., description="Final recommendation based on the critique."
    )

class TranslatedFeedback(BaseModel):
    directives: List[str] = Field(
        ..., description="A list of clear, structured directives for the Proposal Agent to follow on the next iteration."
    )
