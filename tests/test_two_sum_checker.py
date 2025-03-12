import pytest
from src.two_sum_checker import check_two_sum

def test_two_sum_basic_true():
    """Test basic case where two numbers sum to target."""
    assert check_two_sum([1, 2, 3, 4], 7) == True

def test_two_sum_basic_false():
    """Test case where no two numbers sum to target."""
    assert check_two_sum([1, 2, 3, 4], 10) == False

def test_two_sum_first_and_last():
    """Test when first and last elements sum to target."""
    assert check_two_sum([1, 2, 3, 4, 5], 6) == True

def test_two_sum_empty_list():
    """Test empty list returns False."""
    assert check_two_sum([], 5) == False

def test_two_sum_single_element():
    """Test list with single element returns False."""
    assert check_two_sum([5], 10) == False

def test_two_sum_negative_numbers():
    """Test with negative numbers."""
    assert check_two_sum([-1, -2, 3, 4], 2) == True

def test_two_sum_zero_target():
    """Test with zero as target."""
    assert check_two_sum([-1, 0, 1], 0) == True

def test_two_sum_type_error_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        check_two_sum("not a list", 5)

def test_two_sum_type_error_non_integer_target():
    """Test raising TypeError for non-integer target."""
    with pytest.raises(TypeError, match="Target must be an integer"):
        check_two_sum([1, 2, 3], "not an int")

def test_two_sum_value_error_duplicates():
    """Test raising ValueError for list with duplicates."""
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        check_two_sum([1, 2, 2, 3], 4)