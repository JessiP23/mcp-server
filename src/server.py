from mcp.server.fastmcp import FastMCP
import logging
from src.resources.user_profiles import fetch_user_profiles
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
        mcp = FastMCP(
            name="MyMCPServer",
            version="0.1.0",
            description="A simple MCP server example"
        )

        # SOLUTION 1: Use a standard HTTP URL format
        @mcp.resource(
            uri="http://localhost/user_profiles/list",
            name="user_profiles",
            description="List of the user profiles from the company"
        )
        def user_profiles() -> list[dict]:
            return fetch_user_profiles()

        # Alternative solutions you can try instead:
        
        # SOLUTION 2: Use a file-like URI
        # @mcp.resource(
        #     uri="file:///user_profiles/list",
        #     name="user_profiles", 
        #     description="List of the user profiles from the company"
        # )
        # def user_profiles() -> list[dict]:
        #     return fetch_user_profiles()

        # SOLUTION 3: Use a data URI
        # @mcp.resource(
        #     uri="data:application/json,user_profiles_list",
        #     name="user_profiles",
        #     description="List of the user profiles from the company" 
        # )
        # def user_profiles() -> list[dict]:
        #     return fetch_user_profiles()

        @mcp.tool(
            name="create_user_profile",
            description="Create a new user profile in the database"
        )
        def create_user(
            name: str,
            role: str,
            department: str = "",
            years_experience: int = 0
        ) -> dict:
            """Create a new user profile in the database.

            Args:
                name: Name of the user
                role: Role of the user
                department: Department of the user (optional)
                years_experience: Years of experience of the user
            """
            return create_user_profile(name, role, department, years_experience)

        logger.info("Starting MCP server...")
        mcp.run()

    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        raise

if __name__ == "__main__":
    logger.info(f"Server running? Try http://localhost:8000 or check FastMCP for host/port setup")

    main()