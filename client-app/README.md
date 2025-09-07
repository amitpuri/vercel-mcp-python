# MCP Client for Vercel MCP Python Server

A rich, interactive client application to test and interact with your deployed MCP server.

## Features

- 🔌 **Connection Testing**: Verify server connectivity
- 🔧 **Tool Discovery**: List and explore available MCP tools
- 🎯 **Interactive Tool Calls**: Call tools with custom parameters
- 📚 **Resource Management**: List and read MCP resources
- 🧪 **Automated Testing**: Test all tools with predefined parameters
- 🎨 **Rich UI**: Beautiful console interface with colors and tables

## Quick Start

### 1. Setup

```bash
# Navigate to client directory
cd client-app

# Install dependencies
python setup.py

# Or manually:
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)

The client uses environment variables for configuration. Copy the example file and customize:

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file to customize settings
# MCP_SERVER_URL=https://your-deployed-server.vercel.app
# MCP_TIMEOUT=10
# MCP_DEBUG=false
```

### 3. Run the Client

```bash
python mcp_client.py
```

## Usage

The client provides an interactive menu with the following options:

### 1. List Tools
Shows all available MCP tools with their descriptions and parameters.

### 2. Call Tool
Interactively call any tool by:
- Selecting the tool name
- Providing required parameters
- Viewing the results

### 3. List Resources
Display all available MCP resources.

### 4. Read Resource
Read the content of a specific resource.

### 5. Test All Tools
Automatically test all tools with predefined parameters:
- **Echo**: "Hello from MCP Client!"
- **Get Time**: Current server time
- **Add Numbers**: 15 + 25 = 40
- **Weather Info**: San Francisco weather

### 6. Exit
Close the client application.

## Available Tools

Your MCP server provides these tools:

| Tool | Description | Parameters |
|------|-------------|------------|
| `echo` | Echo back a message | `message` (string) |
| `get_time` | Get current server time | None |
| `add_numbers` | Add two numbers | `a` (integer), `b` (integer) |
| `get_weather_info` | Get weather info (mock) | `location` (string) |

## Available Resources

| Resource | Description |
|----------|-------------|
| `config://server` | Server configuration information |

## Example Output

```
🤖 MCP Client
┌─────────────────────────────────────────────────────────────┐
│ MCP Client for Vercel MCP Python Server                    │
│ Connecting to: https://your-deployed-server.vercel.app │
└─────────────────────────────────────────────────────────────┘

✅ Server Status: running
📊 Available Tools: 4
📚 Available Resources: 1

🔌 Initializing MCP connection...
✅ Connected to: Vercel MCP Server
📋 Version: 1.0.0
🔧 Protocol: 2024-11-05

==================================================
MCP Client Menu
1. List Tools
2. Call Tool
3. List Resources
4. Read Resource
5. Test All Tools
6. Exit
```

## Configuration

The client can be configured using environment variables in a `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_SERVER_URL` | URL of the MCP server | `https://your-deployed-server.vercel.app` |
| `MCP_TIMEOUT` | Request timeout in seconds | `10` |
| `MCP_DEBUG` | Enable debug mode | `false` |

## Dependencies

- `requests`: HTTP client for API calls
- `colorama`: Cross-platform colored terminal output
- `rich`: Rich text and beautiful formatting
- `python-dotenv`: Environment variable management

## Server URL

The client is configured to connect to:
`https://your-deployed-server.vercel.app`

To change the server URL, edit the `server_url` variable in `mcp_client.py`.
