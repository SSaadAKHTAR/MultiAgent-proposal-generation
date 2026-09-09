import os
from dotenv import load_dotenv
import groq
import instructor
from pydantic import BaseModel

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

class TestResponse(BaseModel):
    message: str

def test_model(model_name: str):
    print(f"\n--- Testing model: {model_name} ---")
    try:
        # 1. Raw Text Test
        print("1. Testing raw text generation...")
        client = groq.Groq(api_key=API_KEY)
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Say hello in one word."}]
        )
        print(f"Success! Response: {response.choices[0].message.content}")
        
        # 2. Structured Output Test
        print("2. Testing structured output (Instructor)...")
        patched_client = instructor.from_groq(client, mode=instructor.Mode.JSON)
        resp_obj = patched_client.chat.completions.create(
            model=model_name,
            response_model=TestResponse,
            messages=[{"role": "user", "content": "Say hello in one word."}]
        )
        print(f"Success! Structured Response: {resp_obj.model_dump_json()}")
        
    except Exception as e:
        print(f"FAILED: {type(e).__name__} - {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("GROQ_API_KEY not found in .env")
    else:
        test_model("openai/gpt-oss-20b")
        test_model("openai/gpt-oss-120b")
