def planner_node(state):

    query = state["query"].lower()

    if any(word in query for word in [
        "invoice",
        "product",
        "buyer",
        "total due"
    ]):
        route = "rag"

    elif any(word in query for word in [
        "calculate",
        "+",
        "-",
        "*",
        "/"
    ]):
        route = "calculator"

    else:
        route = "research"

    return {
        "route": route
    }