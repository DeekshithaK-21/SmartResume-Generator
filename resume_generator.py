import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Create client (NEW SDK STYLE)
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Best free-tier, stable text model
MODEL_NAME = "models/gemini-flash-latest"

def generate_resume(prompt):
    for attempt in range(2):  # retry once
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )
            return response.text
        except Exception:
            time.sleep(2)

    return (
        "⚠️ AI service is currently overloaded (free-tier limit).\n\n"
        "Please try again later."
    )
