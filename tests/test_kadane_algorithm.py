import pytest
from src.kadane_algorithm import max_subarray_sum

def test_basic_positive_array():
    """Test with a standard array containing positive and negative numbers."""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_single_element_array():
    """Test with a single element array."""
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-5]) == -5

def test_all_negative_array():
    """Test an array with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_mixed_positive_negative_array():
    """Test an array with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1]) == 7

def test_zero_sum_array():
    """Test an array where the maximum sum is zero."""
    assert max_subarray_sum([-1, -1, 0, -1, -1]) == 0

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum(123)

def test_empty_array():
    """Test that ValueError is raised for an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])