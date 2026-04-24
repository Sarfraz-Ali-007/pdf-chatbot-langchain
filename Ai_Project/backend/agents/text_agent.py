from langchain_groq import ChatGroq
from backend.config import GROQ_API_KEY

llm = ChatGroq(
    api_key='GROQ_API_KEY',
    model="llama-3.3-70b-versatile"
)

from backend.tools.memory import save_memory, search_memory

def text_agent(state):
    query = state.get("input", "")

    # 🔍 fetch memory
    past = search_memory(query)

    context = "\n".join(past)

    prompt = f"""
You are an AI assistant.

Memory:
{context}

User: {query}
Answer:
"""

    response = llm.invoke(prompt)

    # 💾 save interaction
    save_memory(query + " -> " + response.content)

    state["output"] = response.content
    return state