import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test max subarray sum with a normal input"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test with a single element array"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(arr, 2) == -3  # -1 + -2

def test_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, 4) is None

def test_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, 0) is None

def test_k_negative():
    """Test when k is negative"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, -1) is None

def test_empty_array():
    """Test with an empty array"""
    arr = []
    assert max_subarray_sum(arr, 2) is None

def test_invalid_input_type():
    """Test with invalid input types"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list", 2)
    
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], "not an int")