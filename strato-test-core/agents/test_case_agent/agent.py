import os
import json
import requests
import re
from dotenv import load_dotenv
# from .models import UserStoryInput, MultiTestScriptResponse, TestCase

load_dotenv(dotenv_path="/Users/krkaushikkumar/Desktop/kwest-ai/.env")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def slugify(title):
    return "test_" + re.sub(r"[^a-zA-Z0-9]+", "_", title.strip().lower()) + ".spec.js"

def ensure_import(script: str) -> str:
    import_line = "import { test, expect } from '@playwright/test';"
    video_line = "test.use({ video: 'on' });"
    lines = script.strip().splitlines()
    if not lines or lines[0] != import_line:
        lines.insert(0, import_line)
    if len(lines) < 2 or lines[1] != video_line:
        lines.insert(1, video_line)
    return "\n".join(lines)

def generate_test_script(user_story: str):
    prompt_template = f"""
You are a QA automation engineer.

From the following user story, generate 3–5 **different** JavaScript Playwright test cases that include:

- Valid scenario (happy path)
- At least one invalid input
- An edge case (e.g., empty input, mobile constraints)
- A test with incorrect credentials

**Important Playwright guidelines:**
- Always start each script with: import {{ test, expect }} from '@playwright/test';
- For mobile emulation, use Playwright's context emulation, NOT page.setViewport. Example:
    const context = await browser.newContext({{ viewport: {{ width: 375, height: 812 }} }});
    const page = await context.newPage();
- Use robust selectors (prefer id, aria-label, or data-testid over tag or class).
- Only use selectors that actually exist on the real Wikipedia homepage (e.g., #searchInput for the search box).
- Return ONLY the raw JSON array, no markdown.

User Story:
'{user_story}'
"""

    messages = [
        {"role": "system", "content": "You write Playwright tests for QA automation."},
        {"role": "user", "content": prompt_template},
    ]
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemma2-9b-it",
        "messages": messages,
        "max_tokens": 1024,
        "temperature": 0.3
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code != 200:
        print("GROQ API error:", response.status_code, response.text)
        return {"tests": []}
    result = response.json()
    try:
        content = result["choices"][0]["message"]["content"].strip()
        # Remove Markdown code block if present
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", content, re.DOTALL)
        if match:
            raw_json = match.group(1).strip()
        else:
            raw_json = content
        parsed_cases = json.loads(raw_json)
        tests = []
        for tc in parsed_cases:
            filename = slugify(tc["title"]) if "title" in tc else "test_case.spec.js"
            script = ensure_import(tc["script"])
            tests.append({
                "filename": filename,
                "script": script
            })
        return {"tests": tests}
    except Exception as e:
        print("Error parsing LLM output:", e)
        return {"tests": []} 