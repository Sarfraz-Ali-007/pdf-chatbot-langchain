def router(state):
    text = state.get("input", "")

    # decide type
    if isinstance(text, dict) and text.get("image"):
        return {"route": "vision"}

    if isinstance(text, dict) and text.get("audio"):
        return {"route": "voice"}

    return {"route": "text"}