import pytest
import socket
from src.dns_lookup import perform_dns_lookup

def test_valid_hostname():
    """Test lookup for a known valid hostname."""
    result = perform_dns_lookup('google.com')
    assert result is not None
    assert isinstance(result, (str, list))
    # Check it's a valid IP address
    if isinstance(result, str):
        assert _is_valid_ip(result)
    else:
        assert all(_is_valid_ip(ip) for ip in result)

def test_localhost():
    """Test lookup for localhost."""
    result = perform_dns_lookup('localhost')
    assert result is not None
    assert result in ['127.0.0.1', ['127.0.0.1']]

def test_invalid_hostname():
    """Test lookup for an invalid hostname."""
    result = perform_dns_lookup('not.a.valid.hostname.xyz')
    assert result is None

def test_empty_hostname():
    """Test that empty hostname raises ValueError."""
    with pytest.raises(ValueError):
        perform_dns_lookup('')

def test_none_hostname():
    """Test that None hostname raises ValueError."""
    with pytest.raises(ValueError):
        perform_dns_lookup(None)

def _is_valid_ip(ip: str) -> bool:
    """
    Validate if a string is a valid IP address.
    Supports both IPv4 and IPv6.
    """
    try:
        socket.inet_pton(socket.AF_INET, ip)  # IPv4
        return True
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, ip)  # IPv6
            return True
        except socket.error:
            return False