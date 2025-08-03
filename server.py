
from agents import Agent, Runner,AsyncOpenAI,set_default_openai_api,set_default_openai_client,set_tracing_disabled ,function_tool
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

import os

load_dotenv()

mcp = FastMCP(name="My_MCP", stateless_http=True)

set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

external_client= AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

# @function_tool
# def Fetch_weather(city:str) -> str:
#     return f"The weather of {city} is sunny"

main_agent : Agent = Agent(
    name="Order Agent",
    instructions="You are a helpful assistant that can answer questions about health.You are an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Only terminate your turn when you are sure that the problem is solved.",
    model="gemini-2.5-flash",
    # tools=[Fetch_weather],
    # tool_use_behavior="stop_on_first_tool"
)

@mcp.tool()
async def agent_tool(query:str) -> str:
    result= Runner.run_sync(
        main_agent,
        query,
    # max_turns=1
)
    return await    result.final_output

@mcp.tool()
def get_weather(city:str) -> str:
    return f"The weather in {city} is 20 degree "

@mcp.tool()
def fetch_weather(city:str) -> str:
    return f"The weather in {city} is 40 degree "

mcp_app = mcp.streamable_http_app()

