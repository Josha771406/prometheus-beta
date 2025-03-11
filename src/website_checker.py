import requests
import socket
import urllib.parse
import re

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
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL format")
    
    # If no scheme is present, prepend https://
    if not url.startswith(('http://', 'https://')):
        url = f"https://{url}"
    
    # Additional validation using regex
    url_regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if not url_regex.match(url):
        raise ValueError("Invalid URL format")
    
    try:
        # Try to make a HEAD request with a timeout
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        # Check if the response status code is successful (200-399)
        return 200 <= response.status_code < 400
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        return False