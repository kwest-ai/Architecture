import os
import requests
import json
import re
from dotenv import load_dotenv
from .models import ParsePromptResponse

load_dotenv(dotenv_path="/Users/krkaushikkumar/Desktop/kwest-ai/.env")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

prompt_template = """
You are an intelligent test planning agent. Given a user request, extract:
- goal (the main action or feature)
- entities (apps, components, URLs, etc.)
- constraints (like browser, platform, etc.)

Respond in this format:
{{
  "goal": "...",
  "entities": ["..."],
  "constraints": ["..."]
}}

User prompt:
'{user_prompt}'
"""

def parse_prompt(prompt: str) -> ParsePromptResponse:
    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY environment variable not set.")

    user_prompt = prompt
    system_prompt = prompt_template.format(user_prompt=user_prompt)
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemma2-9b-it",  # Change to your preferred model
        "messages": messages,
        "max_tokens": 256,
        "temperature": 0.2
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code != 200:
        raise RuntimeError(f"GROQ API error: {response.status_code} {response.text}")
    result = response.json()
    try:
        content = result["choices"][0]["message"]["content"]
        # Robustly extract JSON from Markdown code block if present
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", content, re.DOTALL)
        if match:
            json_str = match.group(1).strip()
        else:
            json_str = content.strip()
        parsed = json.loads(json_str)
        # Ensure entities and constraints are lists
        entities = parsed.get("entities", [])
        constraints = parsed.get("constraints", [])
        if isinstance(entities, str):
            entities = [entities] if entities else []
        if isinstance(constraints, str):
            constraints = [constraints] if constraints else []
        return ParsePromptResponse(
            goal=parsed.get("goal", ""),
            entities=entities,
            constraints=constraints
        )
    except Exception as e:
        raise RuntimeError(f"Failed to parse GROQ response: {e}\nRaw response: {result}") 