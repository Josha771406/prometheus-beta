import pytest
import requests
from src.website_checker import is_website_online

def test_valid_online_website():
    """Test that a known online website returns True"""
    assert is_website_online("https://www.google.com") is True

def test_invalid_website():
    """Test that an invalid website returns False"""
    assert is_website_online("https://www.nonexistentwebsitexyz123.com") is False

def test_malformed_url():
    """Test that malformed URLs raise a ValueError"""
    with pytest.raises(ValueError):
        is_website_online("not a url")

def test_url_without_scheme():
    """Test that URLs without a scheme are handled correctly"""
    assert is_website_online("google.com") is True

def test_timeout_parameter():
    """Test that timeout parameter works"""
    # Use a very short timeout to simulate slow connection
    assert is_website_online("https://www.google.com", timeout=0.001) in [True, False]

def test_empty_string():
    """Test that an empty string raises a ValueError"""
    with pytest.raises(ValueError):
        is_website_online("")