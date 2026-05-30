import os

from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_tool(query: str):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    results = []

    for item in response["results"]:

        results.append(
            f"""
Title: {item['title']}
Content: {item['content']}
URL: {item['url']}
"""
        )

    return "\n\n".join(results)