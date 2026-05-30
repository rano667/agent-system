def search_tool(query: str):

    mock_results = {
        "nvidia":
            "Nvidia is investing heavily in AI chips, robotics and agentic AI.",
    }

    query_lower = query.lower()

    for key in mock_results:
        if key in query_lower:
            return mock_results[key]

    return "No results found."

# Why Mock Tool First?

# Because we want to understand:

# Agent
# ↓
# Tool
# ↓
# Result

# before introducing:

# Tavily
# Serper
# Web APIs