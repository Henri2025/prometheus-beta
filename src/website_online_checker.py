import requests
import socket
import urllib.parse

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online by attempting to establish a connection.

    Args:
        url (str): The URL of the website to check.
        timeout (float, optional): Connection timeout in seconds. Defaults to 5.0.

    Returns:
        bool: True if the website is online, False otherwise.

    Raises:
        ValueError: If the provided URL is invalid.
    """
    # Validate and repair URL
    try:
        parsed_url = urllib.parse.urlparse(url)
        
        # If no scheme, add https
        if not parsed_url.scheme:
            url = f"https://{url}"
            parsed_url = urllib.parse.urlparse(url)
        
        # Check if netloc exists
        if not parsed_url.netloc:
            raise ValueError("Invalid URL format")
    except Exception:
        raise ValueError("Invalid URL format")

    try:
        # Attempt to get the website with a timeout
        response = requests.get(url, timeout=timeout)
        
        # Check if the request was successful
        return response.status_code < 400
    except (requests.ConnectionError, requests.Timeout, socket.error):
        # Connection failed
        return False