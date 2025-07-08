from fastapi import FastAPI
from .models import ParsePromptRequest, ParsePromptResponse
from .agent import parse_prompt

app = FastAPI()

@app.post("/v1/parse", response_model=ParsePromptResponse)
def parse_route(request: ParsePromptRequest):
    return parse_prompt(request.prompt) 