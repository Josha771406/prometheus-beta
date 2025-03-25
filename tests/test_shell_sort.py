import pytest
from src.shell_sort import shell_sort

def test_shell_sort_normal_list():
    """Test shell sort with a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert shell_sort(input_list) == expected

def test_shell_sort_already_sorted():
    """Test shell sort with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert shell_sort(input_list) == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test shell sort with a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert shell_sort(input_list) == expected

def test_shell_sort_empty_list():
    """Test shell sort with an empty list"""
    assert shell_sort([]) == []

def test_shell_sort_single_element():
    """Test shell sort with a single element"""
    assert shell_sort([42]) == [42]

def test_shell_sort_with_duplicates():
    """Test shell sort with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert shell_sort(input_list) == expected

def test_shell_sort_with_floats():
    """Test shell sort with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert shell_sort(input_list) == expected

def test_shell_sort_invalid_input():
    """Test shell sort with invalid input type"""
    with pytest.raises(TypeError):
        shell_sort("not a list")

def test_shell_sort_with_mixed_types():
    """Test shell sort with elements that cannot be compared"""
    with pytest.raises(TypeError):
        shell_sort([1, 'a', 2, 'b'])