import os
import requests

def download_file(url, save_path=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download
        save_path (str, optional): The local path to save the downloaded file. 
                                   If None, uses the filename from the URL.

    Returns:
        str: The full path where the file was saved

    Raises:
        ValueError: If the URL is invalid or empty
        requests.RequestException: For network-related errors
        IOError: For file writing errors
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        
        # Raise an exception for bad HTTP responses
        response.raise_for_status()

        # Determine save path
        if save_path is None:
            # Extract filename from URL if no save path provided
            save_path = os.path.basename(url.split('?')[0])

        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path) or '.', exist_ok=True)

        # Write the file
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return os.path.abspath(save_path)

    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")
    except IOError as e:
        raise IOError(f"Error saving file to {save_path}: {str(e)}")