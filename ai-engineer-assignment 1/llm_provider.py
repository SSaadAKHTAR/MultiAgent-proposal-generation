import os
import json
import time
from typing import Type, TypeVar, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

from google import genai
from google.genai import types
from tenacity import retry, stop_after_attempt, retry_if_exception_type, wait_fixed
from logger import current_logger

load_dotenv()

def print_retry_sleep(retry_state):
    print(f"\n[API Rate Limit / Temporary Error] Waiting {retry_state.next_action.sleep} seconds before retrying (Attempt {retry_state.attempt_number})...")

T = TypeVar('T', bound=BaseModel)

class LLMProvider:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set in .env")
        self.client = genai.Client(api_key=api_key)
        self.model_complex = "gemini-3.1-pro-preview"
        self.model_simple = "gemini-3.6-flash"

    def get_model_for_tier(self, tier: str, override: Optional[str] = None) -> str:
        if override:
            return override
        if tier == "complex":
            return self.model_complex
        return self.model_simple

    @retry(
        wait=wait_fixed(65),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type(Exception),
        before_sleep=print_retry_sleep
    )
    def generate_structured(self, prompt: str, schema: Type[T], system_instruction: str = "",
        model_tier: str = "complex",
        model: Optional[str] = None,
        agent_name: str = "UnknownAgent"
    ) -> T:
        _model = self.get_model_for_tier(model_tier, model)
        current_prompt = prompt
        max_retries = 3
        
        for attempt in range(max_retries):
            start_time = time.time()
            
            response = self.client.models.generate_content(
                model=_model,
                contents=current_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=0.2,
                )
            )
            
            latency = time.time() - start_time
            if response.usage_metadata:
                current_logger.log_llm_call(
                    agent_name,
                    _model,
                    response.usage_metadata.prompt_token_count,
                    response.usage_metadata.candidates_token_count,
                    latency
                )
            current_logger.log_raw_payload(agent_name, current_prompt, response.text)
            
            try:
                data = json.loads(response.text)
                return schema.model_validate(data)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise ValueError(f"Schema validation failed after {max_retries} attempts: {e}\nRaw response: {response.text}")
                
                print(f"[{agent_name}] Schema validation failed, feeding error back to LLM (Attempt {attempt+1}/{max_retries})...")
                current_prompt += f"\n\n[SYSTEM NOTIFICATION: Your previous response failed schema validation. Error: {e}. Please provide a corrected JSON response.]"

    @retry(
        wait=wait_fixed(65),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type(Exception),
        before_sleep=print_retry_sleep
    )
    def generate_text(
        self, 
        prompt: str, 
        system_instruction: str = "", 
        model_tier: str = "complex",
        model: Optional[str] = None,
        tools: Optional[list] = None,
        agent_name: str = "UnknownAgent"
    ) -> str:
        _model = self.get_model_for_tier(model_tier, model)
        start_time = time.time()
        
        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7,
        )
        if tools:
            config.tools = tools

        response = self.client.models.generate_content(
            model=_model,
            contents=prompt,
            config=config
        )
        latency = time.time() - start_time
        if response.usage_metadata:
            current_logger.log_llm_call(
                agent_name,
                _model,
                response.usage_metadata.prompt_token_count,
                response.usage_metadata.candidates_token_count,
                latency
            )
        current_logger.log_raw_payload(agent_name, prompt, response.text)
            
        if response.function_calls:
            fn_call = response.function_calls[0]
            fn_name = fn_call.name
            
            fn_args = {}
            if fn_call.args:
                for k, v in fn_call.args.items():
                    fn_args[k] = v

            tool_func = next((t for t in tools if t.__name__ == fn_name), None)
            if tool_func:
                tool_result = tool_func(**fn_args)
                
                chat = self.client.chats.create(model=_model, config=config)
                chat.send_message(prompt)
                tool_resp = types.Part.from_function_response(
                    name=fn_name,
                    response={"result": tool_result}
                )
                
                final_start_time = time.time()
                final_response = chat.send_message(tool_resp)
                final_latency = time.time() - final_start_time
                
                if final_response.usage_metadata:
                    current_logger.log_llm_call(
                        agent_name + "_tool_response",
                        _model,
                        final_response.usage_metadata.prompt_token_count,
                        final_response.usage_metadata.candidates_token_count,
                        final_latency
                    )
                current_logger.log_raw_payload(agent_name + "_tool_response", f"Tool output: {tool_result}", final_response.text)
                return final_response.text
            
        return response.text
