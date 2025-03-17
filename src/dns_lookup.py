import socket
from typing import List, Union, Optional

def perform_dns_lookup(hostname: str) -> Optional[Union[str, List[str]]]:
    """
    Perform a DNS lookup for a given hostname.

    Args:
        hostname (str): The domain name to look up.

    Returns:
        Optional[Union[str, List[str]]]: 
        - If successful, returns a single IP address (str) for A record,
        - Or a list of IP addresses for multiple records,
        - Returns None if no records are found or an error occurs.

    Raises:
        ValueError: If the hostname is empty or invalid.
        socket.gaierror: For network-related lookup errors.
    """
    # Validate input
    if not hostname or not isinstance(hostname, str):
        raise ValueError("Invalid hostname provided")

    try:
        # Perform DNS lookup
        # getaddrinfo returns a list of tuples, each containing address info
        addr_info = socket.getaddrinfo(hostname, None)

        # Extract unique IP addresses
        ip_addresses = list(set(
            addr[4][0] for addr in addr_info 
            if len(addr[4]) > 0
        ))

        # Return single IP if only one, otherwise return list
        return ip_addresses[0] if len(ip_addresses) == 1 else ip_addresses

    except socket.gaierror:
        # Return None if no records found
        return None
    except Exception as e:
        # Log or handle unexpected errors
        print(f"Unexpected error during DNS lookup: {e}")
        return None