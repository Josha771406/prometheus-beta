import pytest
from src.smallest_positive_to_multiple import find_smallest_positive_to_multiple

def test_basic_cases():
    """Test basic scenarios with different arrays"""
    assert find_smallest_positive_to_multiple([1, 2, 3]) == 4
    assert find_smallest_positive_to_multiple([3, 1, 2]) == 4
    assert find_smallest_positive_to_multiple([7, 8]) == 5

def test_zero_sum():
    """Test case where array sum is zero"""
    assert find_smallest_positive_to_multiple([0, 0, 0]) == 5

def test_sum_already_multiple_of_five():
    """Test case where sum is already a multiple of 5"""
    assert find_smallest_positive_to_multiple([5, 10, 15]) == 5

def test_negative_numbers():
    """Test case with negative numbers"""
    assert find_smallest_positive_to_multiple([-1, -2, -3]) == 4

def test_mixed_positive_negative():
    """Test case with mixed positive and negative numbers"""
    assert find_smallest_positive_to_multiple([-10, 3, 4]) == 2

def test_error_non_list_input():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        find_smallest_positive_to_multiple("not a list")

def test_error_non_integer_list():
    """Test that list with non-integer elements raises ValueError"""
    with pytest.raises(ValueError):
        find_smallest_positive_to_multiple([1, 2, "3"])

def test_empty_list():
    """Test behavior with an empty list"""
    assert find_smallest_positive_to_multiple([]) == 5