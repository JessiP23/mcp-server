from typing import Dict, Any
from mcp_server import MCPServer, Resource, Tool
import logging
from src.resources.fetch_user_profiles import fetch_user_profiles
from src.tools.user_management import create_user_profile

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("mcp_server")

def main() -> None:
    """Initialize and start the MCP server."""
    try:
        server = MCPServer(
            name="MyMCPServer",
            version="0.1.0",
            description="A simple MCP server example"
        )

        user_profiles = Resource(
            name="user_profiles",
            description="List of user profiles from the company database",
            fetch_fn=fetch_user_profiles,
        )

        create_user = Tool(
            name="create_user_profile",
            description="Create a new user profile in the database",
            parameters={
                "name": {
                    "type": "string",
                    "description": "Name of the user",
                },
                "role": {
                    "type": "string",
                    "description": "Role of the user",
                },
                "department": {
                    "type": "string",
                    "description": "Department of the user (optional)",
                },
                "years_experience": {
                    "type": "integer",
                    "description": "Years of experience of the user",
                }
            },
            execute_fn=create_user_profile
        )

        server.add_resource(user_profiles)
        server.add_tool(create_user)
        # Resources and tools will be added here
        
        logger.info("Starting MCP server...")
        server.start()
    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        raise

if __name__ == "__main__":
    main()