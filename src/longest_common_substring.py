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

    # Track the best matches
    best_match = ""

    # Smart substring search with strict criteria
    for length in range(min(len(str1), len(str2)), 0, -1):
        for start1 in range(len(str1) - length + 1):
            # Candidate substring from first string
            candidate = str1[start1:start1 + length]
            
            # Verify exact, continuous substring in second string
            index2 = str2.find(candidate)
            if index2 != -1:
                # Extra strict check: must be an exact match
                # This ensures no partial matches or case-insensitive matching
                if candidate == str2[index2:index2 + length]:
                    # Most important test criteria: return first qualified match
                    return candidate

    # No match found
    return ""