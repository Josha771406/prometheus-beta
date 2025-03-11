def count_vowels_consonants(input_string):
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' count.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase for consistent counting
    input_string = input_string.lower()
    
    # Define vowels
    vowels = set('aeiou')
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in input_string:
        # Only count alphabetic characters
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    # Return results as a dictionary
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }