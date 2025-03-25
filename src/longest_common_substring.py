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

    # Create a matrix to store potential common substrings
    m, n = len(str1), len(str2)
    
    # Track the maximum length of substring
    max_length = 0
    best_substring = ""

    # Systematic check for common substrings
    for length in range(1, min(m, n) + 1):
        for start1 in range(m - length + 1):
            # Current substring from first string
            substring = str1[start1:start1 + length]
            
            # Find exact index in second string
            if substring in str2:
                # Verify continuous substring
                index2 = str2.index(substring)
                if substring == str2[index2:index2 + length]:
                    # Update if longer or more precisely matching substring
                    if length > max_length:
                        max_length = length
                        best_substring = substring

    return best_substring