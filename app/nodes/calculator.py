def calculator_node(state):

    query = state["query"]

    try:

        expression = (
            query.replace("calculate", "")
            .strip()
        )

        result = eval(expression)

        return {
            "research": f"Result = {result}"
        }

    except Exception:

        return {
            "research": "Unable to calculate."
        }