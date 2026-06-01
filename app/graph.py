from langgraph.graph import StateGraph, START, END

from app.state import AgentState

from app.routers.query_router import route_query

from app.nodes.planner import planner_node
from app.nodes.researcher import researcher_node
from app.nodes.calculator import calculator_node
from app.nodes.rag import rag_node
from app.nodes.research_summarizer import research_summarizer_node


builder = StateGraph(AgentState)

# Add nodes
builder.add_node("planner", planner_node)
builder.add_node("calculator", calculator_node)
builder.add_node("rag", rag_node)
builder.add_node("researcher", researcher_node)
builder.add_node("research_summary", research_summarizer_node)

# Add edges
builder.add_edge(START, "planner")
builder.add_conditional_edges(
    "planner",
    route_query,
    {
        "research": "researcher",
        "calculator": "calculator",
        "rag": "rag"
    }
)
builder.add_edge("researcher", "research_summary")
builder.add_edge("calculator", END)
builder.add_edge("rag", END)
builder.add_edge("research_summary", END)

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