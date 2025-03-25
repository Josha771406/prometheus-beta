import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test valid IP address formats."""
    assert validate_ip_address('1.2.3.4') == True
    assert validate_ip_address('0.0.0.0') == True
    assert validate_ip_address('9.9.9.9') == True

def test_invalid_ip_addresses():
    """Test invalid IP address formats."""
    # Too few or too many parts
    assert validate_ip_address('1.2.3') == False
    assert validate_ip_address('1.2.3.4.5') == False
    
    # Non-digit characters
    assert validate_ip_address('a.b.c.d') == False
    assert validate_ip_address('1.2.3.x') == False
    
    # Out of range digits
    assert validate_ip_address('10.2.3.4') == False
    assert validate_ip_address('1.2.3.10') == False
    
    # Empty string
    assert validate_ip_address('') == False

def test_edge_cases():
    """Test edge cases for IP address validation."""
    # Non-string input
    assert validate_ip_address(None) == False
    assert validate_ip_address(123) == False
    
    # Spaces and special characters
    assert validate_ip_address(' 1.2.3.4 ') == False
    assert validate_ip_address('1.2.3.4.') == False
    assert validate_ip_address('.1.2.3.4') == False