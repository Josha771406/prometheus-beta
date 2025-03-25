import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_basic():
    """Test finding missing numbers in a typical scenario."""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_missing_numbers_no_missing():
    """Test an array with no missing numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_missing_numbers_single_element():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == []

def test_missing_numbers_larger_range():
    """Test finding missing numbers in a larger range."""
    assert find_missing_numbers([10, 12, 15, 18]) == [11, 13, 14, 16, 17]

def test_missing_numbers_negative():
    """Test finding missing numbers with negative integers."""
    assert find_missing_numbers([-3, -1, 2, 4]) == [-2, 0, 1, 3]

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_non_integer_array_raises_error():
    """Test that a non-integer array raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([1, 2, '3', 4])

def test_non_sorted_array():
    """Test a non-sorted array (Note: function assumes sorted input)."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([5, 1, 3, 2, 4])