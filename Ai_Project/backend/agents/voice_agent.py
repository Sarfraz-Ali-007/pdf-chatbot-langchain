def voice_agent(state):
    audio = state["input"]

    response = "Voice received. (Whisper STT will be added in Phase 3)"

    state["output"] = response
    return state