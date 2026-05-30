from app.state import AgentState
from app.llm import get_llm

llm = get_llm()


def summarizer_node(state: AgentState):

    query = state["query"]
    research = state["research"]

    prompt = f"""
You are a research analyst.

User Question:
{query}

Research Data:
{research}

Generate:

1. Key Findings
2. Important Technologies
3. Business Impact

Keep answer concise.
"""

    response = llm.invoke(prompt)

    return {
        "summary": response.content,
        "final_answer": response.content
    }