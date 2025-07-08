# Orchestrator Agent

## Overview
The Orchestrator Agent chains all other agents (Prompt, User Story, Test Case, Executor, Logger) to provide a single endpoint for end-to-end autonomous test automation.

## Endpoint
- `POST /v1/full_test`
  - **Input:** `{ "prompt": "<natural language test request>" }`
  - **Output:** Full pipeline result (intent, user story, test cases, execution results, log status)

## How to Run
1. Ensure all other agents are running on their respective ports (see agent URLs in `agent.py`).
2. Start the orchestrator agent:
   ```bash
   uvicorn orchestrator_agent.main:app --port 8000
   ```
3. Send a POST request to `http://localhost:8000/v1/full_test` with a JSON body:
   ```json
   { "prompt": "Verify login works on example.com" }
   ```

## Production Notes
- Each agent can be containerized and scaled independently.
- Add authentication, rate limiting, and monitoring as needed for SaaS.
- Update agent URLs in `agent.py` for your deployment environment. 