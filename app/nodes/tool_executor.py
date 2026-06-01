from app.state import AgentState
from app.tools.tool_registry import TOOLS


def tool_executor_node(state: AgentState):

    observations = []

    for call in state["tool_calls"]:

        tool_name = call.tool
        tool_input = call.input

        tool = TOOLS.get(tool_name)

        if tool:

            result = tool(tool_input)

            observations.append(
                {
                    "tool": tool_name,
                    "result": result
                }
            )

    return {
        "observations": observations
    }