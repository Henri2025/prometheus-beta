import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation rules:
    - Must have a username part before the @
    - Must have a domain name after the @
    - Username can contain letters, numbers, and some special characters
    - Domain must have at least one dot
    - Total length should not exceed 254 characters
    """
    # Check overall length
    if not email or len(email) > 254:
        return False
    
    # Regular expression for email validation
    # Breakdown of the regex:
    # ^[a-zA-Z0-9._%+-]+    : Username can have letters, numbers, and some special chars
    # @                     : Must have @ symbol
    # [a-zA-Z0-9.-]+        : Domain name
    # \.[a-zA-Z]{2,}$       : Top-level domain with at least 2 characters
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the pattern
    return bool(re.match(email_regex, email))