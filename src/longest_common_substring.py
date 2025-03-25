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
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Track the length and ending position of longest common substring
    max_length = 0
    end_index = 0

    # Fill the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Strictly match exact characters (case-sensitive)
            if str1[i-1] == str2[j-1]:
                # Only continue substring if previous characters matched
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and ending position
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    # Return the exact longest common substring
    # Ensure the substring is a continuous match from the beginning
    return str1[end_index - max_length + 1 : end_index + 1] if max_length > 0 else ""