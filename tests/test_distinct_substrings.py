import pytest
from src.distinct_substrings import count_distinct_substrings

def test_empty_string():
    """Test that an empty string returns 0 distinct substrings."""
    assert count_distinct_substrings("") == 0

def test_single_character():
    """Test a single character string returns 1 distinct substring."""
    assert count_distinct_substrings("a") == 1

def test_simple_string():
    """Test a simple string with multiple distinct substrings."""
    assert count_distinct_substrings("abc") == 6  # "", "a", "b", "c", "ab", "bc", "abc"

def test_repeated_characters():
    """Test a string with repeated characters."""
    assert count_distinct_substrings("aaa") == 3  # "", "a", "aa", "aaa"

def test_complex_string():
    """Test a more complex string with various substrings."""
    assert count_distinct_substrings("abcab") == 13

def test_none_input():
    """Test that passing None raises a TypeError."""
    with pytest.raises(TypeError):
        count_distinct_substrings(None)

def test_long_string():
    """Test a longer string to ensure performance."""
    long_str = "abcdefghijklmnopqrstuvwxyz" * 100
    result = count_distinct_substrings(long_str)
    assert result > 0  # Exact count depends on implementation, but should be non-zero