import pytest
import json
from src.json_parser import parse_api_response

def test_parse_valid_json():
    """Test parsing a valid JSON response."""
    response = '{"name": "John", "age": 30}'
    result = parse_api_response(response)
    assert result == {"name": "John", "age": 30}

def test_parse_nested_json():
    """Test parsing a nested JSON response."""
    response = '{"user": {"name": "Jane", "details": {"age": 25, "city": "New York"}}}'
    result = parse_api_response(response)
    assert result == {"user": {"name": "Jane", "details": {"age": 25, "city": "New York"}}}

def test_parse_empty_input():
    """Test parsing an empty input raises ValueError."""
    with pytest.raises(ValueError, match="API response cannot be None or empty"):
        parse_api_response("")

def test_parse_none_input():
    """Test parsing None input raises ValueError."""
    with pytest.raises(ValueError, match="API response cannot be None or empty"):
        parse_api_response(None)  # type: ignore

def test_parse_invalid_json():
    """Test parsing an invalid JSON string raises ValueError."""
    invalid_json = '{"name": "John", "age": }'
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_api_response(invalid_json)

def test_parse_json_with_complex_types():
    """Test parsing JSON with various complex types."""
    response = '{"numbers": [1, 2, 3], "is_active": true, "null_value": null}'
    result = parse_api_response(response)
    assert result == {"numbers": [1, 2, 3], "is_active": True, "null_value": None}