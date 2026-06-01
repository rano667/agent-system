from app.tools.search_tool import search_tool
from app.tools.calculator_tool import calculator_tool
from app.tools.rag_tool import rag_tool


TOOLS = {
    "search": search_tool,
    "calculator": calculator_tool,
    "rag": rag_tool
}

# TOOLS = {
#     "search": search_tool,
#     "calculator": calculator_tool,
#     "rag": rag_tool,
#     "memory": memory_tool
# }

# Tomorrow:

# SQL Database
# GitHub
# Jira
# AWS
# Slack
# Email

# will also be tools.