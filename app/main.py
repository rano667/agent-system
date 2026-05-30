from app.graph import graph

result = graph.invoke(
    {
        "query": "Latest Nvidia AI initiatives"
    }
)

print(result["final_answer"])

# # Testing tool directly:
# from app.tools.search_tool import search_tool

# result = search_tool(
#     "Latest Nvidia AI initiatives"
# )

# print(result)