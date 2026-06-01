from pydantic import BaseModel


class ToolCall(BaseModel):
    tool: str
    input: str