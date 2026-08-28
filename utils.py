import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError, ClientError
from prompts import build_prompt

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = ["gemini-flash-latest", "gemini-flash-lite-latest", "gemini-pro-latest"]

def generate_replies(email_text, tone, max_retries=2):
    prompt = build_prompt(email_text, tone)

    for model in MODELS:
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model=model, contents=prompt
                )
                if response.candidates and response.candidates[0].content.parts:
                    text_parts = [
                        p.text for p in response.candidates[0].content.parts
                        if hasattr(p, "text") and p.text
                    ]
                    if text_parts:
                        return "\n".join(text_parts)
                break  # empty response, try next model
            except ServerError:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                # else: fall through to next model
            except ClientError:
                break  # this model unavailable, move to next model immediately

    return "⚠️ All models are currently unavailable. Please try again in a minute."
