import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from strand_sort import strand_sort, merge

def test_strand_sort_empty_list():
    """Test sorting an empty list"""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element"""
    assert strand_sort([5]) == [5]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_random_order():
    """Test sorting a list in random order"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert strand_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert strand_sort(input_list) == [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 9]

def test_strand_sort_raises_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        strand_sort("not a list")
    with pytest.raises(TypeError):
        strand_sort(123)

def test_merge_function():
    """Test the merge helper function"""
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([], [1, 2, 3]) == [1, 2, 3]
    assert merge([1, 2, 3], []) == [1, 2, 3]
    assert merge([], []) == []

def test_strand_sort_float_numbers():
    """Test sorting list of float numbers"""
    input_list = [3.14, 1.41, 2.71, 0.58, 1.73]
    assert strand_sort(input_list) == [0.58, 1.41, 1.73, 2.71, 3.14]

def test_strand_sort_negative_numbers():
    """Test sorting list with negative numbers"""
    input_list = [-3, 1, -5, 2, 0, -1]
    assert strand_sort(input_list) == [-5, -3, -1, 0, 1, 2]