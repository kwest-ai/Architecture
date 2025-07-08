from fastapi import FastAPI
from .models import LogInput
from .agent import log_test_result

app = FastAPI()

@app.post("/v1/log")
def log(data: LogInput):
    return log_test_result(data) 