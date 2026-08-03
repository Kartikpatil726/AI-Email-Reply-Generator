import os
from dotenv import load_dotenv
from google import genai
from prompts import build_prompt

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_replies(email_text, tone):
    prompt = build_prompt(email_text, tone)
    response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)
  # Extract text from response candidates
    if response.candidates and response.candidates[0].content.parts:
        text_parts = [
            part.text for part in response.candidates[0].content.parts
            if hasattr(part, "text") and part.text
        ]
        return "\n".join(text_parts)
    return "No response generated."

