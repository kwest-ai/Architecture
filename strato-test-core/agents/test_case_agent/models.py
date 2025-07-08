from pydantic import BaseModel
from typing import List

class UserStoryInput(BaseModel):
    user_story: str

class TestCase(BaseModel):
    title: str
    script: str  # The Playwright JS test block

class MultiTestScriptResponse(BaseModel):
    test_cases: List[TestCase] 