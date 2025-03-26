def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. This function assumes both input
    strings contain only lowercase letters.

    Args:
        str1 (str): The first input string (lowercase letters only)
        str2 (str): The second input string (lowercase letters only)

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        ValueError: If either input contains characters other than lowercase letters
    """
    # Special case for empty strings
    if str1 == "" and str2 == "":
        return True

    # Validate input contains only lowercase letters
    if not all(c.islower() for c in str1 + str2):
        raise ValueError("Inputs must contain only lowercase letters")

    # Quick length check
    if len(str1) != len(str2):
        return False

    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}

    # Count character frequencies for both strings
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequency dictionaries
    return char_count1 == char_count2