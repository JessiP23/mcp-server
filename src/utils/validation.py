from typing import Dict, Any, List, Optional, Type
from pydantic import BaseModel, ValidationError
import logging

logger = logging.getLogger("mcp_server.validation")

def validate_request(
    data: Dict[str, Any],
    model_class: Type[BaseModel]
) -> tuple[Optional[BaseModel], Optional[Dict[str, Any]]]:

    """
    Validate the incoming request data against the specified Pydantic model.

    Args:
        data: input data to validation
        model_class: pydantic model to use for validation

    Return:
        tuple: (validated_model, error_dict)
            - if valid: (model instance, None)
            - if invalid: (None, error dictionary)
    """

    try:
        validated_data = model_class(**data)
        return validated_data, None
    except ValidationError as e:
        errors = e.errors()
        error_dict = {
            "status": "error",
            "message": "Validation failed",
            "errors": errors
        }

        logger.error(f"Validation error: {errors}")

        return None, error_dict