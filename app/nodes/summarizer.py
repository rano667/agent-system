from app.state import AgentState
from app.llm import get_llm

llm = get_llm()


def summarizer_node(state: AgentState):

    query = state["query"]
    observations = state["observations"]

    prompt = f"""
User Query:
{query}

Tool Results:
{observations}

Answer the user.
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }