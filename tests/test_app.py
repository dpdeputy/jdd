import pytest
from fastapi.testclient import TestClient

from src.app import app, server

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.asyncio
async def test_mcp_tool_creation():
    """
    Tests that the FastMCP server has created a tool for the root endpoint.
    """
    # The from_fastapi method automatically creates tools from the endpoints.
    # The tool name is created from the method and path.
    tools = await server.get_tools()
    tool_names = [tool.name for tool in tools.values()]
    assert "read_root" in tool_names
