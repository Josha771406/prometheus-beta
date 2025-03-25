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
    
    # Initialize dictionary with unique characters
    dictionary = {c: i for i, c in enumerate(set(input_data))}
    next_code = len(dictionary)
    
    # Compression process
    result = []
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
    
    # Reverse mapping to get the dictionary keys
    reverse_dictionary = {v: k for k, v in lzw_decompress._global_dict.items()}
    next_code = len(reverse_dictionary)
    
    # Decompression process
    result = []
    current = reverse_dictionary[compressed_data[0]]
    result.append(current)
    
    for code in compressed_data[1:]:
        # Determine the entry for this code
        if code in reverse_dictionary:
            # Existing code in the dictionary
            entry = reverse_dictionary[code]
        elif code == next_code:
            # Special case: the new sequence is the previous + its first character
            entry = current + current[0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.append(entry)
        
        # Add new sequence to dictionary
        reverse_dictionary[next_code] = current + entry[0]
        next_code += 1
        
        current = entry
    
    return ''.join(result)

# Initialize a global dictionary for optimization
lzw_decompress._global_dict = {c: i for i, c in enumerate(set(chr(x) for x in range(65536)))}