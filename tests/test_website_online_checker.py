import pytest
import requests
from src.website_online_checker import is_website_online

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_valid_online_website(mocker):
    """Test that a valid online website returns True."""
    mocker.patch('requests.get', return_value=MockResponse(200))
    assert is_website_online('https://www.google.com') is True

def test_valid_online_website_without_scheme(mocker):
    """Test that a website without scheme still works."""
    mocker.patch('requests.get', return_value=MockResponse(200))
    assert is_website_online('www.google.com') is True

def test_website_with_error_status(mocker):
    """Test that a website with error status returns False."""
    mocker.patch('requests.get', return_value=MockResponse(404))
    assert is_website_online('https://www.example.com') is False

def test_connection_error(mocker):
    """Test that a connection error returns False."""
    mocker.patch('requests.get', side_effect=requests.ConnectionError())
    assert is_website_online('https://nonexistent.website') is False

def test_timeout_error(mocker):
    """Test that a timeout error returns False."""
    mocker.patch('requests.get', side_effect=requests.Timeout())
    assert is_website_online('https://slowwebsite.com') is False

def test_invalid_url():
    """Test that invalid URLs raise a ValueError."""
    with pytest.raises(ValueError):
        is_website_online('')
    
    with pytest.raises(ValueError):
        is_website_online('not a url')

def test_custom_timeout(mocker):
    """Test that custom timeout works."""
    mock_get = mocker.patch('requests.get', return_value=MockResponse(200))
    is_website_online('https://www.example.com', timeout=3.0)
    
    # Check that the mocked get was called with the correct timeout
    mock_get.assert_called_once_with('https://www.example.com', timeout=3.0)