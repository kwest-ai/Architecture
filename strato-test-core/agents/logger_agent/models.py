from pydantic import BaseModel
from typing import List, Optional

class LogInput(BaseModel):
    test_name: str
    status: str
    logs: Optional[str] = None
    error: Optional[str] = None
    screenshots: Optional[List[str]] = [] 