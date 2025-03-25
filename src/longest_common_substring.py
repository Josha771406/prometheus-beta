def find_longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string.

    Time Complexity: O(m*n), where m and n are lengths of input strings
    Space Complexity: O(m*n)

    Examples:
        >>> find_longest_common_substring("hello", "world")
        ''
        >>> find_longest_common_substring("programming", "programmer")
        'program'
        >>> find_longest_common_substring("", "test")
        ''
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""

    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    
    # Track the maximum length and substring
    max_length = 0
    longest_substring = ""

    # Iterate through all possible starting positions
    for i in range(m):
        for j in range(n):
            # If characters match, check the continuous substring
            k = 0
            while (i + k < m and j + k < n and 
                   str1[i + k] == str2[j + k]):
                k += 1
            
            # Update longest substring if current is longer
            if k > max_length:
                max_length = k
                longest_substring = str1[i:i+k]
    
    return longest_substring