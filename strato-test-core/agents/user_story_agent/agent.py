import os
import requests
import json
import re
from dotenv import load_dotenv
from .models import IntentInput, UserStoryResponse

load_dotenv(dotenv_path="/Users/krkaushikkumar/Desktop/kwest-ai/.env")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

prompt_template = '''
You are a user story generator. Given the following intent, generate a BDD-style user story with 'Given', 'When', and 'Then' clauses.
Intent:
Goal: {goal}
Entities: {entities}
Constraints: {constraints}
Respond with only the user story in plain text.
'''

def generate_user_story(intent: IntentInput) -> UserStoryResponse:
    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY environment variable not set.")
    prompt = prompt_template.format(
        goal=intent.goal,
        entities=", ".join(intent.entities),
        constraints=", ".join(intent.constraints)
    )
    messages = [
        {"role": "system", "content": prompt}
    ]
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemma2-9b-it",
        "messages": messages,
        "max_tokens": 256,
        "temperature": 0.2
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code != 200:
        raise RuntimeError(f"GROQ API error: {response.status_code} {response.text}")
    result = response.json()
    try:
        content = result["choices"][0]["message"]["content"].strip()
        # Remove Markdown code block if present
        match = re.search(r"```(?:[a-zA-Z]+)?\s*(.*?)\s*```", content, re.DOTALL)
        if match:
            user_story = match.group(1).strip()
        else:
            user_story = content
        return UserStoryResponse(user_story=user_story)
    except Exception as e:
        raise RuntimeError(f"Failed to parse GROQ response: {e}\nRaw response: {result}") 