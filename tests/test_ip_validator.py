import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test a variety of valid IP addresses."""
    valid_ips = [
        "0.0.0.0",
        "255.255.255.255", 
        "192.168.0.1",
        "10.0.0.1",
        "172.16.0.1"
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP address formats."""
    invalid_ips = [
        # Out of range numbers
        "256.0.0.1",
        "0.256.0.1",
        "0.0.256.1",
        "0.0.0.256",
        
        # Negative numbers
        "-1.0.0.1",
        "0.-1.0.1",
        "0.0.-1.1",
        "0.0.0.-1",
        
        # Non-numeric
        "a.b.c.d",
        "192.168.0.abc",
        
        # Leading zeros
        "01.02.03.04",
        
        # Incorrect format
        "192.168.0",  # Too few octets
        "192.168.0.1.2",  # Too many octets
        "192.168.0.",  # Trailing dot
        ".192.168.0.1",  # Leading dot
        
        # Misc invalid inputs
        "",
        "   ",
        None,
        123,
        "192.168.0.1 ",  # Extra whitespace
        " 192.168.0.1"   # Leading whitespace
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) == False, f"{ip} should be invalid"

def test_zero_cases():
    """Specifically test zero and zero-like cases."""
    zero_cases = [
        "0.0.0.0"
    ]
    for ip in zero_cases:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_boundary_values():
    """Test boundary values for IP address octets."""
    boundary_ips = [
        "0.0.0.0",    # All zeros
        "255.255.255.255"  # All max values
    ]
    for ip in boundary_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"