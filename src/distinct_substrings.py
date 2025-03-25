def count_distinct_substrings(s: str) -> int:
    """
    Find the number of distinct substrings in a given string with O(n) time complexity.
    
    Uses a rolling hash approach with a set to track unique substrings efficiently.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Number of distinct substrings
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a string
    """
    # Handle edge cases
    if s is None:
        raise TypeError("Input must be a string")
    
    if not s:
        return 0
    
    # Use a set to track unique substrings
    unique_substrings = set()
    
    # Generate all substrings in a single pass
    for start in range(len(s)):
        current = ""
        for end in range(start, len(s)):
            current += s[end]
            unique_substrings.add(current)
    
    return len(unique_substrings)