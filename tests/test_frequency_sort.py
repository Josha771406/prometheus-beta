import pytest
from src.frequency_sort import sort_by_frequency

def test_sort_by_frequency_basic():
    """Test basic frequency sorting"""
    assert sort_by_frequency([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]

def test_sort_by_frequency_empty_list():
    """Test empty list input"""
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    """Test list with a single element"""
    assert sort_by_frequency([5]) == [5]

def test_sort_by_frequency_all_unique():
    """Test list with all unique elements"""
    assert sort_by_frequency([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_by_frequency_complex_case():
    """Test more complex frequency sorting"""
    assert sort_by_frequency([5, 5, 4, 4, 4, 3, 3, 3, 3]) == [5, 5, 4, 4, 4, 3, 3, 3, 3]

def test_sort_by_frequency_negative_numbers():
    """Test sorting with negative numbers"""
    assert sort_by_frequency([-1, -1, 2, 2, 2, 3]) == [3, -1, -1, 2, 2, 2]

def test_sort_by_frequency_preserve_original_order():
    """Test that original order is preserved for elements with same frequency"""
    input_list = [1, 2, 1, 3, 2]
    result = sort_by_frequency(input_list)
    # Check that within same frequency group, original order is maintained
    assert result.index(3) < result.index(1) < result.index(2)