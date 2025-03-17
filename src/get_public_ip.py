import requests

def get_public_ip() -> str:
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address as a string.
    
    Raises:
        ConnectionError: If unable to connect to IP lookup service
        ValueError: If no valid IP address can be retrieved
    """
    try:
        # Use a reliable IP lookup service
        response = requests.get('https://api.ipify.org', timeout=10)
        
        # Check if the response was successful
        response.raise_for_status()
        
        # Validate the IP address format
        ip_address = response.text.strip()
        
        # Basic IP address validation 
        if not _validate_ip_address(ip_address):
            raise ValueError("Retrieved IP address is not valid")
        
        return ip_address
    
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to retrieve public IP: {str(e)}") from e

def _validate_ip_address(ip: str) -> bool:
    """
    Validate the format of an IP address.
    
    Args:
        ip (str): IP address to validate
    
    Returns:
        bool: True if IP address is valid, False otherwise
    """
    # Simple validation for IPv4 address
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    
    try:
        # Check if each part is a valid integer between 0 and 255
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False