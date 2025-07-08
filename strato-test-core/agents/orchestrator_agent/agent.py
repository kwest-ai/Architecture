import requests
from .models import OrchestratorInput, OrchestratorResult

PROMPT_AGENT_URL = "http://localhost:8003/v1/parse"
USER_STORY_AGENT_URL = "http://localhost:8004/v1/story"
TEST_CASE_AGENT_URL = "http://localhost:8005/v1/generate_tests"
EXECUTOR_AGENT_URL = "http://localhost:8002/v1/execute"
LOGGER_AGENT_URL = "http://localhost:8001/v1/log"

TIMEOUT = 10

def orchestrate_full_test(data: OrchestratorInput) -> OrchestratorResult:
    # 1. Prompt Agent
    try:
        resp = requests.post(PROMPT_AGENT_URL, json={"prompt": data.prompt}, timeout=TIMEOUT)
        resp.raise_for_status()
        intent = resp.json()
    except Exception as e:
        raise RuntimeError(f"Prompt Agent failed: {e}")

    # 2. User Story Agent
    try:
        resp = requests.post(USER_STORY_AGENT_URL, json=intent, timeout=TIMEOUT)
        resp.raise_for_status()
        user_story = resp.json()
    except Exception as e:
        raise RuntimeError(f"User Story Agent failed: {e}")

    # 3. Test Case Agent
    try:
        print("Sending to Test Case Agent:", user_story)
        resp = requests.post(TEST_CASE_AGENT_URL, json=user_story, timeout=TIMEOUT)
        print("Test Case Agent response:", resp.json())
        resp.raise_for_status()
        tests = resp.json().get("tests", [])
    except Exception as e:
        raise RuntimeError(f"Test Case Agent failed: {e}")

    execution_results = []
    log_status = []
    # 4. Executor Agent & 5. Logger Agent (for each test)
    for test in tests:
        try:
            exec_resp = requests.post(EXECUTOR_AGENT_URL, json=test, timeout=60)
            exec_resp.raise_for_status()
            exec_result = exec_resp.json()
            execution_results.append(exec_result)
            # Log both first and second attempt if present
            for attempt_key in ["first_attempt", "second_attempt"]:
                if attempt_key in exec_result:
                    log_payload = {
                        "test_name": test.get("filename", "unknown") + ("_fixed" if attempt_key=="second_attempt" else ""),
                        "status": exec_result[attempt_key].get("status"),
                        "logs": exec_result[attempt_key].get("logs"),
                        "error": exec_result[attempt_key].get("error"),
                        "screenshots": exec_result[attempt_key].get("screenshots", [])
                    }
                    try:
                        log_resp = requests.post(LOGGER_AGENT_URL, json=log_payload, timeout=TIMEOUT)
                        log_status.append(log_resp.json())
                    except Exception as le:
                        log_status.append({"error": str(le), "test_name": log_payload["test_name"]})
        except Exception as e:
            execution_results.append({"error": str(e), "test_name": test.get("filename", "unknown")})
    return OrchestratorResult(
        intent=intent,
        user_story=user_story,
        tests=tests,
        execution_results=execution_results,
        log_status=log_status
    ) 