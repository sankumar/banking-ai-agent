from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def classify_message(message: str) -> str:
    prompt = f"""
You are a banking support classifier.
Classify the message into ONE category only:
- Positive Feedback
- Negative Feedback
- Query

Message: "{message}"

Return only the category name.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()
