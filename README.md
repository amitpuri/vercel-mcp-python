![AI Generated](https://img.shields.io/badge/AI-Generated-blueviolet?style=for-the-badge&logo=openai&logoColor=white)

# Vercel MCP Python Server

A Model Context Protocol (MCP) server built with Python and FastMCP, designed to run on Vercel's serverless platform.

## Project Structure

```
vercel-mcp-python/
├── api/
│   └── index.py          # Main Vercel function
├── src/
│   └── mcp_server.py     # Your MCP server logic
├── client-app/           # Interactive MCP client
│   ├── mcp_client.py     # Rich client application
│   ├── requirements.txt  # Client dependencies
│   ├── setup.py          # Setup script
│   ├── README.md         # Client documentation
│   └── run_client.bat    # Windows launcher
├── requirements.txt       # Server dependencies
├── vercel.json           # Vercel configuration
└── README.md
```

## Features

This MCP server provides the following tools:

- **echo**: Echo back a provided message
- **get_time**: Get the current server time
- **add_numbers**: Add two numbers together
- **get_weather_info**: Get mock weather information for a location

And the following resources:

- **config://server**: Server configuration information

## Prerequisites

Before setting up the project, you'll need to install the Vercel CLI:

### Installing Vercel CLI

**For Git Bash on Windows:**

1. **Install Node.js** (if not already installed):
   - Download from [nodejs.org](https://nodejs.org/)

2. **Install Vercel CLI globally**:
   ```bash
   npm install -g vercel
   ```

3. **Verify installation**:
   ```bash
   vercel --version
   ```

**If you encounter PATH issues:**
```bash
# Find npm global directory
npm config get prefix

# Add to PATH (add this to your ~/.bashrc)
export PATH=$PATH:$(npm bin -g)
source ~/.bashrc
```

**Alternative methods:**
```bash
# Using npx (no global installation)
npx vercel

# Using yarn
yarn global add vercel
```

## Setup

1. **Create and activate virtual environment** (Recommended):
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   
   # On Windows Git Bash:
   source venv/Scripts/activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Login to Vercel**:
   ```bash
   vercel login
   ```

4. **Deploy to Vercel**:
   ```bash
   vercel --prod
   ```

## Local Development

To test locally, you can use Vercel's development server:

```bash
vercel dev
```

### Troubleshooting Windows Issues

**Note**: Local development with `vercel dev` may have issues on Windows due to runtime initialization errors. This is a known limitation and doesn't affect production deployment.

**If you encounter issues with `vercel dev`:**

**Solution 1: Deploy directly (Recommended)**
```bash
vercel --prod
```
Your server will be available at the provided Vercel URL and works perfectly in production.

**Solution 2: Test locally with Python (in virtual environment)**
```bash
# Activate virtual environment first
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source venv/Scripts/activate  # Windows Git Bash

# Test MCP server functionality
python -c "
import sys, os
sys.path.append('src')
from mcp_server import mcp
import json

# Test echo tool
request = {
    'jsonrpc': '2.0',
    'id': 1,
    'method': 'tools/call',
    'params': {'name': 'echo', 'arguments': {'message': 'Hello from venv!'}}
}
response = mcp.handle_request(request)
print(json.dumps(response, indent=2))
"
```

**Solution 3: Use the deployed version**
Your server will be available at your Vercel domain after deployment.

You can test it by:
1. Opening the URL in your browser
2. Using a tool like Postman or curl
3. Connecting with an MCP client

**Solution 4: Run as Administrator (if needed)**
1. Close your terminal
2. Right-click on Git Bash/PowerShell and select "Run as administrator"
3. Navigate back to your project: `cd /d/repos/vercel-mcp-python`
4. Try `vercel dev` again

## API Endpoints

- `GET /`: Returns server information and status
- `POST /`: Handles MCP protocol requests
- `OPTIONS /`: Handles CORS preflight requests

## Dependencies

- `fastmcp>=0.15.0`: FastMCP framework for building MCP servers
- `uvicorn>=0.24.0`: ASGI server for Python web applications
- `python-json-logger>=2.0.0`: JSON logging for Python applications

## Configuration

The server is configured through `vercel.json` with:
- Python runtime using `@vercel/python`
- 30-second maximum execution time
- CORS enabled for cross-origin requests
- Automatic routing to the main handler

## Usage

Once deployed, your MCP server will be available at your Vercel domain. You can connect to it using any MCP-compatible client.

### Using the Included Client App

A rich, interactive client application is included in the `client-app/` directory:

```bash
# Navigate to client directory
cd client-app

# Setup (first time only)
python setup.py

# Configure environment (optional)
cp .env.example .env
# Edit .env to customize server URL and settings

# Run the client
python mcp_client.py
```

The client provides:
- 🔌 Connection testing
- 🔧 Interactive tool calling
- 📚 Resource management
- 🧪 Automated testing of all tools
- 🎨 Beautiful console interface

See `client-app/README.md` for detailed usage instructions.

## Additional Resources

- [Vercel MCP Documentation](https://vercel.com/docs/mcp) - Official Vercel documentation for Model Context Protocol
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers) - Explore available MCP servers
- [AI SDK Documentation](https://sdk.vercel.ai/) - Use the AI SDK to initialize MCP clients

## License

MIT
