from pydantic import BaseModel
from typing import List

class ParsePromptRequest(BaseModel):
    prompt: str

class ParsePromptResponse(BaseModel):
    goal: str
    entities: List[str]
    constraints: List[str] 