import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gravity_sort import gravity_sort

def test_gravity_sort_basic():
    """Test basic sorting functionality"""
    assert gravity_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_gravity_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert gravity_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_gravity_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert gravity_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_gravity_sort_with_duplicates():
    """Test sorting list with duplicate values"""
    assert gravity_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_gravity_sort_empty_list():
    """Test sorting an empty list"""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test sorting a list with a single element"""
    assert gravity_sort([42]) == [42]

def test_gravity_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        gravity_sort("not a list")

def test_gravity_sort_negative_numbers():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        gravity_sort([-1, 2, 3])

def test_gravity_sort_non_integer():
    """Test that ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        gravity_sort([1, 2.5, 3])

def test_gravity_sort_large_numbers():
    """Test sorting with large numbers"""
    large_list = [1000, 10, 100, 1, 10000]
    assert gravity_sort(large_list) == [1, 10, 100, 1000, 10000]