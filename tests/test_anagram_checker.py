import pytest
from src.anagram_checker import anagram_checker

def test_simple_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("hello", "olleh") == True

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("Astronomer", "Moon starer") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("python", "java") == False
    assert anagram_checker("test", "text") == False

def test_different_lengths():
    """Test words of different lengths"""
    assert anagram_checker("short", "shorter") == False
    assert anagram_checker("a", "aa") == False

def test_whitespace_handling():
    """Test anagrams with whitespace"""
    assert anagram_checker("rail safety", "fairy tales") == True
    assert anagram_checker(" listen ", "silent") == True

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-string inputs
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    
    with pytest.raises(TypeError):
        anagram_checker("test", [1, 2, 3])
    
    # Test empty string inputs
    with pytest.raises(ValueError):
        anagram_checker("", "test")
    
    with pytest.raises(ValueError):
        anagram_checker("test", "")
    
    with pytest.raises(ValueError):
        anagram_checker("  ", "test")

def test_empty_string_anagrams():
    """Ensure empty strings are not considered anagrams"""
    assert anagram_checker("a", "a") == True
    assert anagram_checker("", "") == False  # Handled by input validation