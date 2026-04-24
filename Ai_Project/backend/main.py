from fastapi import FastAPI
from backend.graph.workflow import app

api = FastAPI()

@api.post("/run")
def run_agent(payload: dict):

    result = app.invoke(payload)

    return result   # ✅ now this will NOT be null

def router(state):
    user_input = state.get("input", None)

    if not user_input:
        return "text"  # default fallback

    if isinstance(user_input, dict) and user_input.get("image"):
        return "vision"

    elif isinstance(user_input, dict) and user_input.get("audio"):
        return "voice"

    return "text"

    result = app.invoke(payload)

    return result