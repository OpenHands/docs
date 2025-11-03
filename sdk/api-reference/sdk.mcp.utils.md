---
title: openhands.sdk.mcp.utils
description: API reference for openhands.sdk.mcp.utils
---

# openhands.sdk.mcp.utils module

<a id="module-openhands.sdk.mcp.utils"></a>

Utility functions for MCP integration.

### *async* openhands.sdk.mcp.utils.log_handler(message: LoggingMessageNotificationParams)

Handles incoming logs from the MCP server and forwards them
to the standard Python logging system.

### openhands.sdk.mcp.utils.create_mcp_tools(config: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | MCPConfig, timeout: [float](https://docs.python.org/3/library/functions.html#float) = 30.0) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[MCPToolDefinition](https://github.com/OpenHands/software-agent-sdk/sdk.mcp.tool.md#openhands.sdk.mcp.tool.MCPToolDefinition)]

Create MCP tools from MCP configuration.
