import json
from typing import Any, Dict, Optional

def parse_api_response(response: str) -> Dict[str, Any]:
    """
    Parse a JSON response from an API.

    Args:
        response (str): A JSON-formatted string from an API response.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed JSON data.

    Raises:
        ValueError: If the input is None, empty, or not a valid JSON string.
        json.JSONDecodeError: If the JSON is malformed.
    """
    # Check for None or empty input
    if not response:
        raise ValueError("API response cannot be None or empty")

    try:
        # Attempt to parse the JSON string
        return json.loads(response)
    except json.JSONDecodeError as e:
        # Provide a more informative error message
        raise ValueError(f"Invalid JSON format: {str(e)}")