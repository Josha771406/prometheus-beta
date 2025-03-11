def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1's) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits for.
    
    Returns:
        int: The number of set bits in the integer.
    
    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> count_set_bits(5)  # Binary: 101 
        2
        >>> count_set_bits(0)
        0
        >>> count_set_bits(15)  # Binary: 1111
        4
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to unsigned representation
    if n < 0:
        n = abs(n)
    
    # Count set bits
    count = 0
    while n:
        # Bitwise AND with 1 checks the least significant bit
        count += n & 1
        # Right shift to check next bit
        n >>= 1
    
    return count