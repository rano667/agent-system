from app.state import AgentState


def summarizer_node(state: AgentState):

    research = state["research"]

    summary = f"Summary: {research}"

    return {
        "summary": summary
    }