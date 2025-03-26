def get_unique_sorted_chars(input_string):
    """
    Extract unique characters from a string and return them in case-sensitive alphabetical order.

    Args:
        input_string (str): The input string to process.

    Returns:
        list: A sorted list of unique characters from the input string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a dictionary to maintain order and uniqueness (Python 3.7+)
    unique_chars = dict.fromkeys(input_string)
    
    # Sort the unique characters and return as a list
    return sorted(unique_chars)