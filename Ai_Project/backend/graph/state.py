from typing import TypedDict, Optional

class AgentState(TypedDict):
    input: str
    type: str   # "text", "image", "voice"
    output: Optional[str]