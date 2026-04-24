from langgraph.graph import StateGraph, END
from backend.graph.state import AgentState
from backend.graph.nodes import router
from backend.agents.text_agent import text_agent
from backend.agents.vision_agent import vision_agent
from backend.agents.voice_agent import voice_agent

workflow = StateGraph(AgentState)

def router(state):
    return {"route": "text"}

# nodes
workflow.add_node("router", router)
workflow.add_node("text", text_agent)
workflow.add_node("vision", vision_agent)
workflow.add_node("voice", voice_agent)

# entry
workflow.set_entry_point("router")

# routing manually after router
workflow.add_edge("router", "text")
workflow.add_edge("router", "vision")
workflow.add_edge("router", "voice")

lambda state: state["route"]

workflow.add_conditional_edges(
    "router",
    lambda state: state["route"],   # 👈 IMPORTANT FIX
    {
        "text": "text",
        "vision": "vision",
        "voice": "voice"
    }
)

# final node
def final_node(state):
    return {
        "input": state.get("input"),
        "type": state.get("type"),
        "output": state.get("output", "No output generated")
    }

workflow.add_node("final", final_node)

workflow.add_edge("text", "final")
workflow.add_edge("vision", "final")
workflow.add_edge("voice", "final")
workflow.add_edge("final", END)

app = workflow.compile()