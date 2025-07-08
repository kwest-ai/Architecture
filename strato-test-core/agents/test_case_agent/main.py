from fastapi import FastAPI
from .agent import generate_test_script

app = FastAPI()

@app.post("/v1/generate_tests")
def generate_tests(user_story_input: dict):
    return generate_test_script(user_story_input["user_story"]) 