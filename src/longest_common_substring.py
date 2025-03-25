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

    # Create dynamic programming matrix
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Tracking variables
    max_length = 0
    end_index = 0

    # Populate dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Exact character match
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length only if continuous substring
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    # Extract and validate substring
    if max_length == 0:
        return ""

    # Key constraint: Length must exactly match the continuous substring
    substring = str1[end_index - max_length + 1 : end_index + 1]

    # Verify the substring is exactly in the second string with same continuity
    if substring in str2 and str2.index(substring) + len(substring) <= len(str2):
        return substring

    return ""