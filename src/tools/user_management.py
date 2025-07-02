from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, ValidationError
import logging

logger = logging.getLogger("mcp_server.tools")

class CreateUserRequest(BaseModel):
    """Request model for creating a new user."""
    name: str = Field(..., min_length=2, description="Name of the user")
    role: str = Field(..., min_length=2, description="Role of the user")
    department: Optional[str] = Field("General", description="Department of the user")
    years_experience: int = Field(0, description="Years of experience of the user")

def create_user_profile(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a new user profile in the database.
    Args:
        request_data (Dict[str, Any]): Data for the new user containing name, role, etc.

    Return:
        Dict[str, Any]: Response with status and user info
    """

    try:
        # validate data
        user_data = CreateUserRequest(**request_data)

        logger.info(f"Creating new user: {user_data.name} - {user_data.role} in {user_data.department}")

        return {
            "status": "success",
            "message": f"User {user_data.name} created successfully",
            "user": user_data.model_dump()
        }
    except ValidationError as e:
        logger.error(f"Validation error: {e}")

        return {
            "status": "error",
            "message": "Invalid input data",
            "details": str(e)
        }
    except Exception as e:
        # Other specific exceptions
        logger.error(f"Error creating user: {e}")
        return {
            "status": "error",
            "message": "Failed to create user profile",
            "details": str(e)
        }