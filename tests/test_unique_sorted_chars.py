import pytest
from src.unique_sorted_chars import get_unique_sorted_chars

def test_basic_string():
    """Test with a basic mixed-case string."""
    assert get_unique_sorted_chars("hello") == ['e', 'h', 'l', 'o']

def test_empty_string():
    """Test with an empty string."""
    assert get_unique_sorted_chars("") == []

def test_case_sensitivity():
    """Test case-sensitive sorting."""
    assert get_unique_sorted_chars("Hello") == ['H', 'e', 'l', 'o']

def test_string_with_numbers_and_symbols():
    """Test string with numbers and symbols."""
    assert get_unique_sorted_chars("a1b2c3!@#") == ['!', '#', '1', '2', '3', '@', 'a', 'b', 'c']

def test_repeated_characters():
    """Test string with repeated characters."""
    assert get_unique_sorted_chars("aaaAAAbbbBBB") == ['A', 'B', 'a', 'b']

def test_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        get_unique_sorted_chars(123)
    with pytest.raises(TypeError):
        get_unique_sorted_chars(None)