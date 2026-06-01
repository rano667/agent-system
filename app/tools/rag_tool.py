
import requests
import os

from dotenv import load_dotenv

load_dotenv()

RAG_API_URL = os.getenv("RAG_API_URL")


def rag_tool(query: str):

    response = requests.post(
        RAG_API_URL,
        json={"query": query},
        timeout=60
    )

    data = response.json()

    return data["answer"]