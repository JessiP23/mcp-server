from typing import List, Dict, Any
from pydantic import BaseModel
import logging

logger = logging.getLogger("mcp_server.resources")

class UserProfile(BaseModel):
    """Data model for user profiles."""
    name: str
    role: str
    department: str = "General"
    years_experience: int = 0

# Global in-memory user profile database
USER_PROFILES_DB: List[UserProfile] = [
    UserProfile(name="Alice", role="Engineer", department="Engineering", years_experience=5),
    UserProfile(name="Bob", role="Product Manager", department="Product", years_experience=3),
    UserProfile(name="Charlie", role="Designer", department="Design", years_experience=7)
]

def fetch_user_profiles() -> List[Dict[str, Any]]:
    """
    Fetch user profiles from the in-memory database.
    Returns:
        List[Dict[str, Any]]: A list of user profile dictionaries.
    """
    try:
        logger.info(f"Successfully fetched {len(USER_PROFILES_DB)} user profiles")
        return [user.model_dump() for user in USER_PROFILES_DB]
    except Exception as e:
        logger.error(f"Error fetching user profiles: {e}")
        return []