import pytest
import requests
from unittest.mock import patch
from src.get_public_ip import get_public_ip, _validate_ip_address

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")

def test_get_public_ip_successful():
    """Test successful retrieval of public IP address."""
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse('8.8.8.8')
        assert get_public_ip() == '8.8.8.8'

def test_get_public_ip_connection_error():
    """Test handling of connection errors."""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.ConnectionError("Connection failed")
        with pytest.raises(ConnectionError):
            get_public_ip()

def test_get_public_ip_invalid_response():
    """Test handling of invalid IP address response."""
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse('invalid.ip')
        with pytest.raises(ValueError):
            get_public_ip()

def test_ip_address_validation():
    """Test IP address validation function."""
    # Valid IP addresses
    assert _validate_ip_address('192.168.1.1') == True
    assert _validate_ip_address('0.0.0.0') == True
    assert _validate_ip_address('255.255.255.255') == True
    
    # Invalid IP addresses
    assert _validate_ip_address('256.0.0.1') == False
    assert _validate_ip_address('1.2.3.4.5') == False
    assert _validate_ip_address('abc.def.ghi.jkl') == False
    assert _validate_ip_address('') == False
    assert _validate_ip_address('192.168.1') == False