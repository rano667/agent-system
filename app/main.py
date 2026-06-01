from app.graph import graph

result = graph.invoke(
    {
        "query": "What is Nvidia's market cap and what would it be after 20 percent growth?"
    }
)

print(result["final_answer"])