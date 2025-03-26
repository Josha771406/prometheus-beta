import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    """Test pairs of valid anagrams"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True
    assert is_anagram("python", "typhon") == True

def test_non_anagrams():
    """Test pairs of non-anagram strings"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False
    assert is_anagram("abc", "abd") == False

def test_same_string():
    """Test that a string is an anagram of itself"""
    assert is_anagram("hello", "hello") == True

def test_empty_strings():
    """Test empty string edge case"""
    assert is_anagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("abc", "abcd") == False

def test_invalid_input():
    """Test input validation for non-lowercase letters"""
    with pytest.raises(ValueError):
        is_anagram("Hello", "hello")
    
    with pytest.raises(ValueError):
        is_anagram("hello", "Hello")
    
    with pytest.raises(ValueError):
        is_anagram("hello123", "olleh")

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert is_anagram("aabbcc", "abcabc") == True
    assert is_anagram("aabbcc", "abcabd") == False