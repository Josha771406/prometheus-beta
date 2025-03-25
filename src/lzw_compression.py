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
    
    # Initialize dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    
    # Compression process
    w = input_data[0]
    for c in input_data[1:]:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c
    
    # Output the last sequence
    if w:
        result.append(dictionary[w])
    
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
    
    # Initialize dictionary with single characters
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # Decompression process
    result = []
    w = dictionary[compressed_data[0]]
    result.append(w)
    
    for code in compressed_data[1:]:
        # Retrieve the current entry
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = w + w[0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.append(entry)
        
        # Add new sequence to dictionary
        dictionary[next_code] = w + entry[0]
        next_code += 1
        
        # Update current entry
        w = entry
    
    return ''.join(result)