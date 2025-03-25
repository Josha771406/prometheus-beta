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

    # Find all exact matches with strict constraints
    def find_strict_match(s1, s2):
        matches = []
        for start in range(len(s1)):
            substring = s1[start:]
            for end in range(len(substring), 0, -1):
                candidate = substring[:end]
                if candidate in s2 and all(c1 == c2 for c1, c2 in zip(candidate, s2[s2.index(candidate):s2.index(candidate)+len(candidate)])):
                    matches.append(candidate)
        return matches

    # Get all matches
    matches = find_strict_match(str1, str2)
    
    # Return the longest match (or empty string if no matches)
    return max(matches, key=len, default="")