from typing import TypedDict


class AgentState(TypedDict):
    query: str

    tool_calls: list

    observations: list

    final_answer: str