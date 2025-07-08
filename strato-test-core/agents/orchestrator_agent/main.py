from fastapi import FastAPI, HTTPException
from .models import OrchestratorInput, OrchestratorResult
from .agent import orchestrate_full_test

app = FastAPI()

@app.post("/v1/full_test", response_model=OrchestratorResult)
def full_test(data: OrchestratorInput):
    try:
        return orchestrate_full_test(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 