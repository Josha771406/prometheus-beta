import pytest
from src.palindrome_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("hello racecar world") == True
    assert contains_palindrome_word("level up") == True
    assert contains_palindrome_word("A man a plan a canal Panama") == True
    
    # Test cases without palindrome words
    assert contains_palindrome_word("python is awesome") == False
    assert contains_palindrome_word("") == False
    
    # Test cases with special characters and mixed case
    assert contains_palindrome_word("hello, Madam!") == True
    assert contains_palindrome_word("test 123 test") == False
    
    # Edge cases
    assert contains_palindrome_word("a") == True
    assert contains_palindrome_word("ab") == False
    
    # Complex cases
    assert contains_palindrome_word("wow-wow test") == True
    assert contains_palindrome_word("12321 is a number") == True
    
    # Ensure non-letter characters don't break palindrome detection
    assert contains_palindrome_word("test @ racecar % test") == True