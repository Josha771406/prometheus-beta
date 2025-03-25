def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.

    Args:
        file_path (str): Path to the file to search in.
        search_string (str): String to search for in the file.

    Returns:
        list: A list of line numbers (1-indexed) where the string is found.
        
    Raises:
        TypeError: If file_path or search_string is not a string.
        ValueError: If file_path is empty.
        FileNotFoundError: If the specified file does not exist.
    """
    # Validate input parameters
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")
    
    # Check for empty file path
    if not file_path:
        raise ValueError("file_path cannot be empty")
    
    # Try to open and search the file
    try:
        with open(file_path, 'r') as file:
            # Use list comprehension to find line numbers
            matching_lines = [
                line_num + 1  # 1-indexed line numbers
                for line_num, line in enumerate(file)
                if search_string.lower() in line.lower()
            ]
        
        return matching_lines
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")