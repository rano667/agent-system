from app.state import AgentState
from app.tools.search_tool import search_tool

def researcher_node(state: AgentState):

    query = state["query"]

    research = search_tool(query)

    return {
        "research": research
    }
    
    

# Before:
# Researcher
# ↓
# Hardcoded Output

# Now:

# Researcher
# ↓
# Calls Tool
# ↓
# Gets Data
# ↓
# Updates State

# This is agent behavior.