from app.state import AgentState


def researcher_node(state: AgentState):

    query = state["query"]

    research_result = f"Research completed for: {query}"

    return {
        "research": research_result # LangGraph merges automatically.
    }