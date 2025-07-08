from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class OrchestratorInput(BaseModel):
    prompt: str

class OrchestratorResult(BaseModel):
    intent: Dict[str, Any]
    user_story: Dict[str, Any]
    tests: List[Dict[str, Any]]
    execution_results: List[Dict[str, Any]]
    log_status: List[Dict[str, Any]] 