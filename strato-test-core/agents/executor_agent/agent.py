import os
import subprocess
import glob
import requests
import re
import json
from dotenv import load_dotenv
from .models import TestScriptInput, TestRunResult

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(BASE_DIR, "test_runs")
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")

os.makedirs(TEST_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

load_dotenv(dotenv_path="/Users/krkaushikkumar/Desktop/kwest-ai/.env")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LOGGER_AGENT_URL = "http://localhost:8001/v1/log"  # Adjust port if needed

# Eye LLM: Extractor
def call_groq_llm_eye(script: str, error_log: str, dom_snapshot: str = "") -> dict:
    # Further limit DOM snapshot to first 2000 characters
    dom_snippet = dom_snapshot[:2000] if dom_snapshot else ""
    prompt = f"""
You are an expert Playwright test debugger. Given the error log, test script, and DOM snapshot, extract:
- The selector that failed (if any)
- The expected value (if any)
- The actual value found (if any)
- Any other relevant facts (e.g., timeout, number of elements matched, etc.)

Return your answer as a JSON object with keys: failed_selector, expected_value, actual_value, notes.
If you cannot find the facts, return an empty JSON object: {{}}

Test Script:
{script}

Error Log:
{error_log}

DOM Snapshot (first 2000 chars):
{dom_snippet}
"""
    messages = [
        {"role": "system", "content": "You extract facts from Playwright test failures."},
        {"role": "user", "content": prompt},
    ]
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemma2-9b-it",
        "messages": messages,
        "max_tokens": 1024,
        "temperature": 0.1
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code != 200:
        return {}
    result = response.json()
    try:
        content = result["choices"][0]["message"]["content"].strip()
        print("[Eye LLM raw output]:", content)  # Debug log
        # Use raw string and single backslashes for regex
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
        if match:
            json_str = match.group(1).strip()
        else:
            json_str = content
        return json.loads(json_str)
    except Exception as e:
        print("[Eye LLM parse error]:", e)
        return {}

# Brain LLM: Fixer
def call_groq_llm_brain(script: str, facts: dict) -> str:
    prompt = f"""
You are a Senior QA Automation Engineer. Your job is to review and fix Playwright tests so they are robust, maintainable, and reliable.

Here are the facts about the failure:
{json.dumps(facts, indent=2)}

**Playwright best practices:**
- Always start the script with: import {{ test, expect }} from '@playwright/test';
- For mobile emulation, use browser.newContext with viewport, NOT page.setViewport.
- Use robust, unique selectors that exist in the provided DOM (prefer id, aria-label, or data-testid).
- If the selector is wrong, update it to a valid one from the DOM facts.
- If the expected value is wrong, and the actual value is provided, update the assertion if it makes sense.
- Add appropriate waits or retries for dynamic content, but avoid excessive waiting.
- Only make changes that a qualified QA would approve in a code review, following Playwright and QA best practices.
- Return ONLY the updated Playwright test script, ready to run. Do not include explanations or markdown.

Test Script:
{script}
"""
    messages = [
        {"role": "system", "content": "You are an expert Playwright test engineer. You fix broken tests."},
        {"role": "user", "content": prompt},
    ]
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemma2-9b-it",
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 0.2
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code != 200:
        return script  # fallback: return original script
    result = response.json()
    try:
        content = result["choices"][0]["message"]["content"].strip()
        # Remove Markdown code block if present
        match = re.search(r"```(?:[a-zA-Z]+)?\s*(.*?)\s*```", content, re.DOTALL)
        if match:
            fixed_script = match.group(1).strip()
        else:
            fixed_script = content
        return fixed_script
    except Exception:
        return script

def inject_save_html(script: str, html_path: str) -> str:
    injection = f"""
import fs from 'fs';
import path from 'path';
test.afterEach(async ({{ page }}, testInfo) => {{
  const html = await page.content();
  fs.writeFileSync(path.resolve('{html_path}'), html);
}});
"""
    lines = script.splitlines()
    import_indices = [i for i, line in enumerate(lines) if line.strip().startswith("import")]
    if import_indices:
        last_import_idx = max(import_indices)
        new_lines = lines[:last_import_idx+1] + [injection] + lines[last_import_idx+1:]
    else:
        # No import found, prepend the injection
        new_lines = [injection] + lines
    return "\n".join(new_lines)

def log_to_logger_agent(test_name, status, logs=None, error=None, screenshots=None):
    payload = {
        "test_name": test_name,
        "status": status,
        "logs": logs,
        "error": error,
        "screenshots": screenshots or []
    }
    try:
        resp = requests.post(LOGGER_AGENT_URL, json=payload, timeout=3)
        if resp.status_code != 200:
            print(f"[Logger Agent] Failed to log: {resp.text}")
    except Exception as e:
        print(f"[Logger Agent] Exception: {e}")

def execute_test_script(input: TestScriptInput) -> dict:
    filepath = os.path.join(TEST_DIR, input.filename)
    html_path = os.path.join(TEST_DIR, f"{input.filename.replace('.js', '')}.html")

    def run_and_collect(script: str, filename: str):
        # Inject HTML save code
        script_with_html = inject_save_html(script, html_path)
        with open(filepath, "w") as f:
            f.write(script_with_html)
        existing_videos = set(glob.glob(os.path.join(BASE_DIR, "test-results", "**", "*.webm"), recursive=True))
        try:
            command = ["npx", "playwright", "test", filepath, "--reporter=line"]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=BASE_DIR
            )
            passed = result.returncode == 0
            all_videos = set(glob.glob(os.path.join(BASE_DIR, "test-results", "**", "*.webm"), recursive=True))
            new_videos = list(all_videos - existing_videos)
            # Read DOM snapshot if available
            dom_snapshot = ""
            if os.path.exists(html_path):
                with open(html_path) as f_html:
                    dom_snapshot = f_html.read()
            return TestRunResult(
                status="passed" if passed else "failed",
                logs=result.stdout,
                error=result.stderr if not passed else None,
                screenshots=new_videos
            ), dom_snapshot
        except subprocess.TimeoutExpired:
            all_videos = set(glob.glob(os.path.join(BASE_DIR, "test-results", "**", "*.webm"), recursive=True))
            new_videos = list(all_videos - existing_videos)
            dom_snapshot = ""
            if os.path.exists(html_path):
                with open(html_path) as f_html:
                    dom_snapshot = f_html.read()
            return TestRunResult(
                status="failed",
                error="Test execution timed out.",
                screenshots=new_videos
            ), dom_snapshot

    # First attempt
    first_result, dom_snapshot = run_and_collect(input.script, input.filename)
    log_to_logger_agent(
        test_name=input.filename,
        status=first_result.status,
        logs=first_result.logs,
        error=first_result.error,
        screenshots=first_result.screenshots
    )
    # If failed, use Eye LLM to extract facts, then Brain LLM to fix and retry
    if first_result.status == "failed":
        facts = call_groq_llm_eye(input.script, first_result.logs or first_result.error or "", dom_snapshot)
        fixed_script = call_groq_llm_brain(input.script, facts)
        if fixed_script.strip() != input.script.strip():
            second_result, _ = run_and_collect(fixed_script, input.filename)
            log_to_logger_agent(
                test_name=input.filename + "_fixed",
                status=second_result.status,
                logs=second_result.logs,
                error=second_result.error,
                screenshots=second_result.screenshots
            )
            return {
                "first_attempt": first_result,
                "second_attempt": second_result,
                "fixed_script": fixed_script,
                "facts": facts
            }
    return {"first_attempt": first_result} 