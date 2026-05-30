from app.state import AgentState

def planner_node(state: AgentState):

    query = state["query"]

    plan = f"""
    1. Research topic: {query}
    2. Gather information
    3. Summarize findings
    """

    return {
        "plan": plan
    }