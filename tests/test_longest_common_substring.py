import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    """Test finding a basic common substring"""
    result = find_longest_common_substring("programming", "programmer")
    print(f"Debug result: '{result}'")
    assert result == "program"

def test_no_common_substring():
    """Test when no common substring exists"""
    result = find_longest_common_substring("hello", "world")
    print(f"Debug result: '{result}'")
    assert result == ""

def test_empty_strings():
    """Test behavior with empty strings"""
    assert find_longest_common_substring("", "") == ""
    assert find_longest_common_substring("test", "") == ""
    assert find_longest_common_substring("", "test") == ""

def test_single_character_common_substring():
    """Test with single character common substring"""
    result = find_longest_common_substring("abc", "bcd")
    print(f"Debug result: '{result}'")
    assert result == "c"

def test_identical_strings():
    """Test with identical strings"""
    assert find_longest_common_substring("hello", "hello") == "hello"

def test_case_sensitivity():
    """Test case-sensitive substring matching"""
    result = find_longest_common_substring("Hello", "hello")
    print(f"Debug result: '{result}'")
    assert result == ""

def test_multiple_common_substrings():
    """Test when multiple common substrings exist"""
    assert find_longest_common_substring("abcdef", "bcdefg") == "bcdef"

def test_long_strings():
    """Test with longer strings"""
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "mnopqrstuvwxyzabcdefghijkl"
    assert find_longest_common_substring(str1, str2) == "abcdefghijkl"