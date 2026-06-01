from app.graph import graph

result = graph.invoke(
    {
        "query": "Latest Google AI initiatives"
    }
)

print(result["final_answer"])