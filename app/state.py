from typing import TypedDict


class AgentState(TypedDict):
    query: str
    research: str
    summary: str