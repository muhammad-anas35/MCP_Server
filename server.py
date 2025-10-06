from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

mcp = FastMCP(name="mcp_app", stateless_http=True)


@mcp.tool(
    name="get_date",
    description="Get the current date and time in YYYY-MM-DD HH:MM:SS format",
)
def get_date() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool(
    name="get_weather",
    description="Get the current weather for a given city"
)
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny with a high of 25°C."

mcp_app = mcp.streamable_http_app()

