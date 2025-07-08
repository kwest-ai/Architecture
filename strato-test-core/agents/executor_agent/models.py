from pydantic import BaseModel
from typing import List, Optional

class TestScriptInput(BaseModel):
    filename: str
    script: str  # Full JS code

class TestRunResult(BaseModel):
    status: str  # "passed" or "failed"
    logs: Optional[str] = None
    error: Optional[str] = None
    screenshots: Optional[List[str]] = [] 