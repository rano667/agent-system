def calculator_node(state):

    query = state["query"]

    try:

        expression = (
            query.replace("calculate", "")
            .strip()
        )

        result = eval(expression)

        return {
            "final_answer":
                f"{expression} = {result}"
        }

    except Exception:

        return {
            "final_answer":
                "Unable to calculate."
        }