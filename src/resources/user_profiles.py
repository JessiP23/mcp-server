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

def fetch_user_profiles() -> List[Dict[str, Any]]:
    """
    Fetch user profiles from the database.
    
    Returns:
        List[Dict[str, Any]]: A list of user profile dictionaries.
    """
    try:
        # In a real implementation, this would query a database
        # For this example, we'll return mock data
        users = [
            UserProfile(name="Alice", role="Engineer", department="Engineering", years_experience=5),
            UserProfile(name="Bob", role="Product Manager", department="Product", years_experience=3),
            UserProfile(name="Charlie", role="Designer", department="Design", years_experience=7)
        ]
        
        logger.info(f"Successfully fetched {len(users)} user profiles")
        return [user.model_dump() for user in users]
    except Exception as e:
        logger.error(f"Error fetching user profiles: {e}")
        # In production, you might want to return an empty list or raise
        # a specific exception depending on your error handling strategy
        return []