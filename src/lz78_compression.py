"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
The LZ78 algorithm builds a dictionary of previously seen substrings 
during compression and uses index references to encode repeated patterns.
"""

class LZ78Compressor:
    """
    LZ78 compression and decompression utility class.
    
    The compression generates a list of (index, character) tuples,
    where index 0 indicates a new dictionary entry.
    """
    
    @staticmethod
    def compress(input_string):
        """
        Compress the input string using LZ78 algorithm.
        
        Args:
            input_string (str): The string to be compressed
        
        Returns:
            list: Compressed representation as [(index, character)] tuples
        
        Raises:
            TypeError: If input is not a string
            ValueError: If input is an empty string
        """
        # Validate input
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string")
        
        if not input_string:
            raise ValueError("Input string cannot be empty")
        
        # Initialize dictionary and compressed output
        dictionary = {'' : 0}
        compressed = []
        current_string = ''
        next_index = 1
        
        # Iterate through input characters
        for char in input_string:
            # Attempt to extend current string
            test_string = current_string + char
            
            # If test string is in dictionary, update current string
            if test_string in dictionary:
                current_string = test_string
            else:
                # Find index of current string in dictionary
                current_index = dictionary.get(current_string, 0)
                
                # Add compressed tuple and update dictionary
                compressed.append((current_index, char))
                dictionary[test_string] = next_index
                next_index += 1
                
                # Reset current string
                current_string = ''
        
        # Handle remaining string if not empty
        if current_string:
            current_index = dictionary.get(current_string, 0)
            compressed.append((current_index, ''))
        
        return compressed
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress LZ78 compressed data.
        
        Args:
            compressed_data (list): Compressed data as [(index, character)] tuples
        
        Returns:
            str: Decompressed original string
        
        Raises:
            TypeError: If input is not a list of tuples
            ValueError: If input contains invalid compression data
        """
        # Validate input
        if not isinstance(compressed_data, list):
            raise TypeError("Input must be a list of (index, character) tuples")
        
        # Initialize dictionary and output
        dictionary = {0: ''}
        output = []
        next_index = 1
        
        # Process each compressed tuple
        for index, char in compressed_data:
            # Validate compressed data
            if not isinstance(index, int) or not isinstance(char, str):
                raise ValueError("Invalid compression data")
            
            # Retrieve previous string from dictionary
            try:
                previous_string = dictionary[index]
            except KeyError:
                raise ValueError(f"Invalid dictionary index: {index}")
            
            # Construct current string
            current_string = previous_string + char
            output.append(current_string)
            
            # Add to dictionary
            dictionary[next_index] = current_string
            next_index += 1
        
        # Join and return decompressed string
        return ''.join(output)