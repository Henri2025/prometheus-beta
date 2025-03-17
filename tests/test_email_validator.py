import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email formats."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@domain.org",
        "first.last@domain.net",
        "user+tag@example.com",
        "user-name@domain.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # No @ symbol
        "@missing-username.com",  # Missing username
        "user@.com",  # Missing domain name
        "user@domain",  # Missing top-level domain
        "user@domain..com",  # Double dot in domain
        "user@domain@com",  # Multiple @ symbols
        "a" * 255 + "@example.com",  # Too long email
        "user@example",  # Missing top-level domain
        "user@.example.com"  # Invalid domain start
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email formats."""
    edge_cases = [
        "user.name+tag@example.com",  # Dots and plus sign
        "user-name@sub.domain.com",  # Subdomain
        "user@123.123.123.123"  # IP address domain
    ]
    for email in edge_cases:
        assert validate_email(email) is True, f"{email} should be valid"