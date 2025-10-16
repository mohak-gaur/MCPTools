import asyncio
from mcp import ClientSession , StdioServerParameters
from mcp.client.stdio import stdio_client


def input_from_user(): #input from user
    tool_name = input("Enter tool name to call: ")
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    return tool_name, first , second

async def main():
    
    server_params = StdioServerParameters(command="python", args =[r"C:\MCPTools\calculator.py"])
    
    async with stdio_client(server_params) as (stdio,write):
        async with ClientSession(stdio, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"Tool: {tool.name}, Description: {tool.description}")
                # print("Parameters:", tool.parameters)

            toolname, a, b = input_from_user()
            response = await session.call_tool(toolname, {"a": a, "b": b})
            print(f"Result of {toolname}({a}, {b}):", response.structuredContent.get("result"))

asyncio.run(main())