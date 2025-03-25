class LZ77Compressor:
    """
    LZ77 compression algorithm implementation.
    
    The LZ77 algorithm works by replacing repeated occurrences of data 
    with references to a single copy of that data existing earlier in the input stream.
    """
    
    def compress(self, input_data):
        """
        Compress the input data using LZ77 compression algorithm.
        
        Args:
            input_data (str or bytes): The data to be compressed
        
        Returns:
            list: A list of tuples representing compressed data 
                  Each tuple is (offset, length, next_character)
        """
        # Convert input to bytes if it's a string
        if isinstance(input_data, str):
            input_data = input_data.encode('utf-8')
        
        # Validate input
        if not input_data:
            return []
        
        compressed = []
        window_size = 4096  # Typical sliding window size
        look_ahead_buffer_size = 16  # Look-ahead buffer size
        
        current_pos = 0
        while current_pos < len(input_data):
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Determine search window start and end
            window_start = max(0, current_pos - window_size)
            window_end = current_pos
            
            # Look for the longest match in the window
            for offset in range(window_start, window_end):
                # Calculate maximum possible match length
                max_length = min(look_ahead_buffer_size, 
                                 len(input_data) - current_pos)
                
                # Find match length
                match_length = 0
                while (match_length < max_length and 
                       input_data[offset + match_length] == 
                       input_data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_pos - offset
            
            # If no match found, output single character
            if best_length == 0:
                compressed.append((0, 0, input_data[current_pos]))
                current_pos += 1
            else:
                # Output match with next character
                next_char = (input_data[current_pos + best_length] 
                             if current_pos + best_length < len(input_data) 
                             else None)
                compressed.append((best_offset, best_length, 
                                   next_char if next_char is not None else 0))
                current_pos += best_length + 1
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZ77 algorithm.
        
        Args:
            compressed_data (list): Compressed data as list of tuples
        
        Returns:
            bytes: Decompressed data
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        
        for offset, length, next_char in compressed_data:
            # If no match (offset and length are 0)
            if offset == 0 and length == 0:
                decompressed.append(next_char)
            else:
                # Copy from previous matches
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Add next character if it exists
                if next_char != 0:
                    decompressed.append(next_char)
        
        return bytes(decompressed)