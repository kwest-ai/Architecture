from pydantic import BaseModel
from typing import List

class IntentInput(BaseModel):
    goal: str
    entities: List[str]
    constraints: List[str]

class UserStoryResponse(BaseModel):
    user_story: str 