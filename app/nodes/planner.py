from app.llm import get_llm
from app.schemas.router import RouteDecision

llm = get_llm()

def planner_node(state):

    query = state["query"]

    prompt = f"""
You are a routing agent.

Choose ONE route:

research
calculator
rag

Rules:

- Use rag for invoices, products, buyers, totals.
- Use calculator for math.
- Use research for current events, companies, technologies.

Query:
{query}

Return ONLY the route.
"""

    structured_llm = llm.with_structured_output(
        RouteDecision
    )

    decision = structured_llm.invoke(prompt)
    
    # Temp Debuggning logs
    print("\n🧠 ROUTE DECISION")
    print(decision.route)

    return {
        "route": decision.route
    }