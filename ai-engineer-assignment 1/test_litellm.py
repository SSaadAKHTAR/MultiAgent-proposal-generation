import os
from dotenv import load_dotenv
import litellm
import instructor
from pydantic import BaseModel

load_dotenv()

class TestResponse(BaseModel):
    message: str

def test_model(model_name: str):
    print(f"\n--- Testing LiteLLM model: {model_name} ---")
    try:
        # LiteLLM native
        print("1. Testing raw litellm.completion...")
        response = litellm.completion(
            model=model_name,
            messages=[{"role": "user", "content": "Say hello in one word."}]
        )
        print(f"Success! Response: {response.choices[0].message.content}")
        
        # Instructor patch over litellm
        print("2. Testing structured output (Instructor + LiteLLM)...")
        # For litellm, instructor.from_litellm takes litellm.completion
        patched_client = instructor.from_litellm(litellm.completion, mode=instructor.Mode.JSON)
        resp_obj = patched_client.chat.completions.create(
            model=model_name,
            response_model=TestResponse,
            messages=[{"role": "user", "content": "Say hello in one word."}]
        )
        print(f"Success! Structured Response: {resp_obj.model_dump_json()}")
        
    except Exception as e:
        print(f"FAILED: {type(e).__name__} - {e}")

if __name__ == "__main__":
    # Test with standard litellm syntax for Groq models
    test_model("groq/openai/gpt-oss-20b")
