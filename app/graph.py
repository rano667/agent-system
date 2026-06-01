from langgraph.graph import StateGraph, START, END

from app.state import AgentState

from app.routers.query_router import route_query

from app.nodes.tool_executor import tool_executor_node
from app.nodes.planner import planner_node
from app.nodes.researcher import researcher_node
from app.nodes.calculator import calculator_node
from app.nodes.rag import rag_node
from app.nodes.summarizer import summarizer_node


builder = StateGraph(AgentState)

# Add nodes
builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "tool_executor",
    tool_executor_node
)

builder.add_node(
    "summarizer",
    summarizer_node
)

builder.add_edge(
    START,
    "planner"
)

builder.add_edge(
    "planner",
    "tool_executor"
)

builder.add_edge(
    "tool_executor",
    "summarizer"
)

builder.add_edge(
    "summarizer",
    END
)

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