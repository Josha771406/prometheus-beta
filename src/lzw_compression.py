"""
Lempel-Ziv-Welch (LZW) Compression Algorithm Implementation

This module provides functions for LZW compression and decompression.
"""

def lzw_compress(input_data):
    """
    Compress the input data using the Lempel-Ziv-Welch algorithm.
    
    Args:
        input_data (str): The input string to be compressed.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(input_data, str):
        raise TypeError("Input must be a string")
    
    if not input_data:
        raise ValueError("Input cannot be an empty string")
    
    # Initialize dictionary with mappings
    compressed_mapping = {}
    reverse_mapping = {}
    next_code = 0
    
    def get_code(key):
        """Get or add a code for a sequence."""
        nonlocal next_code
        if key not in compressed_mapping:
            compressed_mapping[key] = next_code
            reverse_mapping[next_code] = key
            next_code += 1
        return compressed_mapping[key]
    
    # Initial codes for all characters in the input
    for char in input_data:
        if char not in compressed_mapping:
            get_code(char)
    
    # Compression process
    result = []
    current_sequence = input_data[0]
    
    for char in input_data[1:]:
        # Try to extend the current sequence
        potential_sequence = current_sequence + char
        
        # If the sequence exists, extend it
        if potential_sequence in compressed_mapping:
            current_sequence = potential_sequence
        else:
            # Output the code for the current sequence
            result.append(get_code(current_sequence))
            
            # Add the new sequence 
            get_code(potential_sequence)
            
            # Reset current sequence to the current character
            current_sequence = char
    
    # Output the last sequence
    if current_sequence:
        result.append(get_code(current_sequence))
    
    return result

def lzw_decompress(compressed_data):
    """
    Decompress data that was compressed using the LZW algorithm.
    
    Args:
        compressed_data (list): A list of integer codes to decompress.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input is an empty list.
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integers")
    
    if not compressed_data:
        raise ValueError("Input cannot be an empty list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in compressed_data):
        raise TypeError("All elements must be integers")
    
    # Decompression process
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    result = []
    previous = chr(compressed_data[0])
    result.append(previous)
    
    for code in compressed_data[1:]:
        # Determine the current entry
        if code in dictionary:
            current = dictionary[code]
        elif code == next_code:
            current = previous + previous[0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.append(current)
        
        # Add new sequence to dictionary
        dictionary[next_code] = previous + current[0]
        next_code += 1
        
        previous = current
    
    return ''.join(result)