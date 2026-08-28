import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError
from prompts import build_prompt

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_replies(email_text, tone, max_retries=3):
    prompt = build_prompt(email_text, tone)

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )
            if response.candidates and response.candidates[0].content.parts:
                text_parts = [
                    part.text for part in response.candidates[0].content.parts
                    if hasattr(part, "text") and part.text
                ]
                return "\n".join(text_parts)
            return "No response generated."
        except ServerError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return "⚠️ Gemini is currently overloaded. Please try again in a minute."
