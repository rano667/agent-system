from typing import TypedDict

class AgentState(TypedDict):
    query: str
    route: str

    plan: str
    research: str

    summary: str
    final_answer: str