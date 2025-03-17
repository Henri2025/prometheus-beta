import re
import ipaddress

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
    - Domain must have at least one dot, or be a valid IP address
    - Total length should not exceed 254 characters
    """
    # Check overall length
    if not email or len(email) > 254:
        return False
    
    # Split email into username and domain
    try:
        username, domain = email.rsplit('@', 1)
    except ValueError:
        return False
    
    # Validate username
    if not username or len(username) > 64:
        return False
    
    # Validate domain
    # Check for consecutive dots or starting with a dot
    if '..' in domain or domain.startswith('.'):
        return False
    
    # Option 1: Check against valid IP addresses
    try:
        ipaddress.ip_address(domain)
        return True
    except ValueError:
        pass
    
    # Option 2: Regular domain validation
    # Matches domain with at least one dot and valid top-level domain
    domain_regex = r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(domain_regex, domain))