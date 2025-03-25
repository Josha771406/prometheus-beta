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
    
    # Initialize dictionary with unique characters from input
    dictionary = {c: i for i, c in enumerate(set(input_data))}
    next_code = len(dictionary)
    
    # Compression process
    result = []
    current_sequence = input_data[0]
    
    for char in input_data[1:]:
        # Try to extend the current sequence
        potential_sequence = current_sequence + char
        
        # If the sequence is in the dictionary, extend it
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output the code for the current sequence
            result.append(dictionary[current_sequence])
            
            # Add the new sequence to the dictionary
            dictionary[potential_sequence] = next_code
            next_code += 1
            
            # Reset current sequence to the current character
            current_sequence = char
    
    # Output the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
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
    
    # Initialize dictionary with a sorted list of unique codes
    unique_codes = sorted(set(compressed_data))
    dictionary = {code: chr(code) for code in unique_codes}
    next_code = max(unique_codes) + 1
    
    # Decompression process
    result = []
    current_code = compressed_data[0]
    current_string = dictionary[current_code]
    result.append(current_string)
    
    for code in compressed_data[1:]:
        # Determine the current entry
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_string + current_string[0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.append(entry)
        
        # Add new sequence to dictionary
        dictionary[next_code] = current_string + entry[0]
        next_code += 1
        
        # Update current string
        current_string = entry
    
    return ''.join(result)