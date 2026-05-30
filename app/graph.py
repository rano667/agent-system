from langgraph.graph import StateGraph, START, END

from app.state import AgentState

from app.nodes.researcher import researcher_node
from app.nodes.summarizer import summarizer_node


builder = StateGraph(AgentState)

# Add nodes
builder.add_node("researcher", researcher_node)
builder.add_node("summarizer", summarizer_node)

# Add edges
builder.add_edge(START, "researcher")
builder.add_edge("researcher", "summarizer")
builder.add_edge("summarizer", END)

graph = builder.compile()