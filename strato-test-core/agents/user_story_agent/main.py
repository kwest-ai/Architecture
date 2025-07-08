from fastapi import FastAPI
from .models import IntentInput, UserStoryResponse
from .agent import generate_user_story

app = FastAPI()

@app.post("/v1/story", response_model=UserStoryResponse)
def story_route(intent: IntentInput):
    return generate_user_story(intent) 