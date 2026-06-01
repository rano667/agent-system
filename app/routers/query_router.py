from app.state import AgentState


def route_query(state: AgentState):
    return state["route"]