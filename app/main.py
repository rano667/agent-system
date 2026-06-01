from app.graph import graph

result = graph.invoke(
    {
        "query": "What is the latest trend in the US Market?"
    }
)

print(result["final_answer"])