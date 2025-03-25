import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    """Test finding a basic common substring"""
    assert find_longest_common_substring("programming", "programmer") == "program"

def test_no_common_substring():
    """Test when no common substring exists"""
    assert find_longest_common_substring("hello", "world") == ""

def test_empty_strings():
    """Test behavior with empty strings"""
    assert find_longest_common_substring("", "") == ""
    assert find_longest_common_substring("test", "") == ""
    assert find_longest_common_substring("", "test") == ""

def test_single_character_common_substring():
    """Test with single character common substring"""
    assert find_longest_common_substring("abc", "bcd") == "c"

def test_identical_strings():
    """Test with identical strings"""
    assert find_longest_common_substring("hello", "hello") == "hello"

def test_case_sensitivity():
    """Test case-sensitive substring matching"""
    assert find_longest_common_substring("Hello", "hello") == ""

def test_multiple_common_substrings():
    """Test when multiple common substrings exist"""
    assert find_longest_common_substring("abcdef", "bcdefg") == "bcdef"

def test_long_strings():
    """Test with longer strings"""
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "mnopqrstuvwxyzabcdefghijkl"
    assert find_longest_common_substring(str1, str2) == "mnopqrstuvwxyz"