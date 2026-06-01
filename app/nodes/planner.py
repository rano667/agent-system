from app.llm import get_llm

from app.schemas.router import RouteDecision
from app.schemas.tool_call import ToolCall

from pydantic import BaseModel
    
llm = get_llm()

class PlannerOutput(BaseModel):
    tool_calls: list[ToolCall]

def planner_node(state):

    query = state["query"]

    prompt = f"""
You are an AI planning agent.

Available tools:
- search
- calculator
- rag

Generate the tool calls required
to answer the user's query.

Query:
{query}
"""

    structured_llm = llm.with_structured_output(
        PlannerOutput
    )

    decision = structured_llm.invoke(prompt)
    
    # Temp Debuggning logs
    print("\n🧠 RAW DECISION:")
    print(decision)
    print(type(decision))

    return {
        "tool_calls": decision.tool_calls
    }