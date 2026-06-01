from app.graph import graph

result = graph.invoke(
    {
        "query": "What products are in invoice 1213?"
    }
)

print(result["final_answer"])