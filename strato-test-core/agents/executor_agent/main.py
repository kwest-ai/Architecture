from fastapi import FastAPI
from .models import TestScriptInput
from .agent import execute_test_script

app = FastAPI()

@app.post("/v1/execute")
def execute(input: TestScriptInput):
    return execute_test_script(input) 