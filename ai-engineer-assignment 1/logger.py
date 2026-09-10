import os
import json
import uuid
from datetime import datetime
from pydantic import BaseModel

class PipelineLogger:
    def __init__(self, run_id=None):
        self.run_id = run_id or datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + str(uuid.uuid4())[:6]
        self.run_dir = os.path.join("runs", self.run_id)
        os.makedirs(self.run_dir, exist_ok=True)
        self.iteration = 0
        self.total_cost = 0.0
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        
        self.summary_file = os.path.join(self.run_dir, "run_summary.json")
        self._init_summary()

    def _init_summary(self):
        summary = {
            "run_id": self.run_id,
            "start_time": datetime.now().isoformat(),
            "iterations": 0,
            "total_cost": 0.0,
            "metrics": {}
        }
        self._write_summary(summary)

    def _write_summary(self, data):
        with open(self.summary_file, 'w') as f:
            json.dump(data, f, indent=2)

    def set_iteration(self, iter_num):
        self.iteration = iter_num
        iter_dir = os.path.join(self.run_dir, f"iteration_{iter_num}")
        os.makedirs(iter_dir, exist_ok=True)

    def log_artifact(self, name: str, content: str | BaseModel):
        """Saves a string or Pydantic model to the current iteration directory."""
        iter_dir = os.path.join(self.run_dir, f"iteration_{self.iteration}")
        os.makedirs(iter_dir, exist_ok=True)
        
        ext = "json" if isinstance(content, BaseModel) else "md"
        filepath = os.path.join(iter_dir, f"{name}.{ext}")
        
        with open(filepath, 'w') as f:
            if isinstance(content, BaseModel):
                f.write(content.model_dump_json(indent=2))
            else:
                f.write(content)
                
    def log_raw_payload(self, agent_name: str, prompt: str, response_text: str):
        iter_dir = os.path.join(self.run_dir, f"iteration_{self.iteration}")
        os.makedirs(iter_dir, exist_ok=True)
        
        # Append to a raw log file for this iteration
        raw_log_file = os.path.join(iter_dir, f"raw_{agent_name}.log")
        with open(raw_log_file, "w") as f:
            f.write(f"=== PROMPT ===\n{prompt}\n\n=== RESPONSE ===\n{response_text}\n")
            
    def log_llm_call(self, agent_name: str, model_name: str, prompt_tokens: int, completion_tokens: int, latency: float):
        if "flash" in model_name.lower():
            # Approximate Flash pricing
            cost = (prompt_tokens / 1_000_000) * 0.075 + (completion_tokens / 1_000_000) * 0.30
        else:
            # Approximate Pro pricing
            cost = (prompt_tokens / 1_000_000) * 1.25 + (completion_tokens / 1_000_000) * 5.00
        
        self.total_prompt_tokens += prompt_tokens
        self.total_completion_tokens += completion_tokens
        self.total_cost += cost
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "iteration": self.iteration,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "latency_seconds": round(latency, 2),
            "cost": cost
        }
        
        log_file = os.path.join(self.run_dir, "llm_calls.jsonl")
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        # Update summary
        with open(self.summary_file, 'r') as f:
            summary = json.load(f)
            
        summary["iterations"] = max(summary["iterations"], self.iteration)
        summary["total_cost"] = self.total_cost
        summary["total_prompt_tokens"] = self.total_prompt_tokens
        summary["total_completion_tokens"] = self.total_completion_tokens
        
        if agent_name not in summary["metrics"]:
            summary["metrics"][agent_name] = {"calls": 0, "cost": 0.0}
            
        summary["metrics"][agent_name]["calls"] += 1
        summary["metrics"][agent_name]["cost"] += cost
        
        self._write_summary(summary)

# A global logger for the current run
current_logger = PipelineLogger()
