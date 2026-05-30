from langgraph.graph import StateGraph, START, END

from app.state import AgentState

from app.nodes.planner import planner_node
from app.nodes.researcher import researcher_node
from app.nodes.summarizer import summarizer_node


builder = StateGraph(AgentState)

# Add nodes
builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("summarizer", summarizer_node)

# Add edges
builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "summarizer")
builder.add_edge("summarizer", END)

graph = builder.compile()

# Before:

# START
#  ↓
# Researcher
#  ↓
# Summarizer

# Change to:

# START
#  ↓
# Planner
#  ↓
# Researcher
#  ↓
# Summarizer
#  ↓
# END