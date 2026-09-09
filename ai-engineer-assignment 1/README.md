# Multi-Agent Client Proposal Pipeline

## 1. Architecture Diagram

```mermaid
graph TD
    A[Intake Docs & Transcripts] --> B(Debrief Agent)
    B -->|Generates| C[4x4 Client Matrix]
    C --> D(Proposal Agent)
    D -->|Generates| E[Markdown Proposal]
    E --> F(Review Agent - Critique)
    F -->|Outputs| G[Structured Review]
    G --> H{Human Gate}
    H -->|Approve| I[Final Proposal]
    H -->|Reject w/ Feedback| J(Review Agent - Translate)
    J -->|Generates| K[Actionable Directives]
    K --> D
```

## 2. Framework Choice
**Framework:** Native `google-genai` SDK + `tenacity` + `pydantic`
* **Zero Magic:** Instead of abstracting away control with heavy agent frameworks (like LangChain or CrewAI), the native SDK provides precise control over function calling and strict schema adherence.
* **Deterministic Reliability:** Pydantic models paired with Google's native structured output configuration guarantee that agent boundaries are strongly typed and won't fail unpredictably in production.
* **Granular Error Handling:** Wrapping native API calls with `tenacity` allows us to implement deliberate, customized retry logic for transient API failures without framework interference.

## 3. Why three agents and not two or four?
Could the Debrief and Proposal agents be a single well-prompted call? In theory, yes, but in practice, doing so violates the Single Responsibility Principle and degrades output quality. 
The Debrief Agent is optimized for *analytical extraction* (identifying contradictions and mapping data). The Proposal Agent is optimized for *creative synthesis* (writing cohesive, persuasive copy). Merging them dilutes the prompt focus, risking hallucinated consensus over the contradictions we need to preserve. We don't need a fourth agent because the Review Agent cleanly handles both critiquing and translation (since they both rely on analyzing the delta between the proposal and the matrix).

## 4. State Design
**Data Flow:** The pipeline passes state forward via strongly-typed Pydantic schemas (e.g., `ClientMatrix`, `ReviewCritique`, `TranslatedFeedback`).
**Feedback History Strategy:** *Summarized / Translated Directives.* 
Instead of concatenating raw human feedback across iterations (which leads to bloated context windows and contradictory instructions over time), the Review Agent *translates* the human's free-text feedback into a structured list of actionable directives. This ensures the Proposal Agent only receives clear, synthesized instructions relevant to the current iteration.

## 5. Termination Logic
The pipeline terminates under three conditions:
1. **Human Approval:** The user inputs 'approve' at the Human Gate.
2. **Max Iterations:** The loop hits the default cap of 5 iterations.
3. **Divergence Detection (Repeat-Issue Detection):** The pipeline tracks the specific issues flagged by the Review Agent across iterations. If the Review Agent flags the exact same issue (location + description) in iteration *N* that it flagged in iteration *N-1*, the pipeline forcefully terminates. This prevents infinite loops where the Proposal Agent fails to fix a persistent issue.

## 6. Failure Modes Handled
1. **Transient API Errors / Rate Limits (Handled):** The `google-genai` API (especially on free tiers) frequently throws 429 Rate Limit and 503 Unavailable errors. I wrapped all LLM calls in a `tenacity` retry decorator with a fixed 65-second wait to cleanly bypass Google's aggressive 60-second quotas without crashing the pipeline.
2. **Schema Validation Failures (Handled):** If the LLM generates invalid JSON that violates the Pydantic schema, `pydantic` raises a validation error. While the native SDK handles this quite well, we explicitly catch `json.loads` and validation errors to raise clear, traceable exceptions.
3. **Prompt Injection (Handled):** Untrusted transcripts may contain malicious instructions (e.g., "ignore previous instructions"). The Debrief Agent wraps the transcript in `<untrusted_transcript>` XML tags and includes a strict `SECURITY DIRECTIVE` in its system prompt to treat the contents purely as passive data.

## 7. Stretch Goals Implemented
* **Mixed Model Tiers:** The Debrief and Proposal agents use `gemini-3.6-flash` (Complex Tier) for heavy synthesis, while the Review Agent's critique generation uses `gemini-3.5-flash-lite` (Simple Tier) for faster, cheaper classification.
* **Divergence Detection:** (See Termination Logic #3).
* **Prompt Injection Awareness:** (See Failure Modes #3).
* **Checkpoint / Branching:** At every Human Gate, the entire pipeline state is dumped to a `checkpoint_iter_{N}.json` file. The CLI supports a `--resume <file>` flag, allowing users to branch off from any previous iteration without restarting the pipeline!

## 8. What I'd do with another 4 hours
* Write comprehensive unit tests for the Pydantic boundary schemas to ensure edge-case transcripts don't break the JSON parsers.
* Implement a local LLM-as-a-Judge script (`evals.py`) to systematically grade the Proposal Agent on whether it accurately placed all 'contradicted' matrix items into the Open Questions section.
* Wire up a rich Terminal UI (using `rich` or `textual`) to make the Human Gate review process cleaner and more readable than standard `print()` statements.

## 9. What would change for a production deployment
* **State Persistence:** Move state from local `.json` checkpoint files to a proper database (e.g., PostgreSQL or MongoDB) for distributed, asynchronous access.
* **Queueing:** Decouple the agents using a message broker (like RabbitMQ or Redis) so that heavy Proposal Agent generation tasks don't block the main thread, allowing concurrent processing of multiple client pipelines.
* **Observability:** Replace the local `logger.py` with Datadog or LangSmith for centralized tracing, cost monitoring, and alerting on LLM failure rates.
