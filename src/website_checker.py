import requests
import socket
import urllib.parse

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online by attempting to connect to it.

    Args:
        url (str): The URL of the website to check
        timeout (float, optional): Connection timeout in seconds. Defaults to 5.0.

    Returns:
        bool: True if the website is online, False otherwise

    Raises:
        ValueError: If the provided URL is invalid
    """
    # Validate URL
    try:
        # If no scheme is present, prepend https://
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"
        
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL format")
    except Exception:
        raise ValueError("Invalid URL format")
    
    try:
        # Try to make a HEAD request with a timeout
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        # Check if the response status code is successful (200-399)
        return 200 <= response.status_code < 400
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        return False