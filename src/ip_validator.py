def validate_ip_address(ip_string: str) -> bool:
    """
    Validate if a given string is a valid IP address in the format A.B.C.D,
    where A, B, C, and D are single-digit numeric characters between 0 and 9.

    Args:
        ip_string (str): The IP address string to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the string by dots
    parts = ip_string.split('.')
    
    # Check if exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Validate each part
    for part in parts:
        # Check if part is exactly 1 character long
        if len(part) != 1:
            return False
        
        # Check if the character is a digit
        if not part.isdigit():
            return False
        
        # Convert to integer and check range
        num = int(part)
        if num < 0 or num > 9:
            return False
    
    return True