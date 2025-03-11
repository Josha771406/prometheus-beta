import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test basic list intersection"""
    result = find_list_intersection([1, 2, 3], [3, 4, 5])
    assert result == [3]

def test_duplicate_intersection():
    """Test intersection with duplicate elements"""
    result = find_list_intersection([1, 2, 2, 3], [2, 3, 3, 4])
    assert set(result) == {2, 3}

def test_no_intersection():
    """Test lists with no common elements"""
    result = find_list_intersection([1, 2], [3, 4])
    assert result == []

def test_empty_lists():
    """Test intersection with empty lists"""
    result = find_list_intersection([], [1, 2, 3])
    assert result == []

def test_type_error_first_argument():
    """Test type error when first argument is not a list"""
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        find_list_intersection("not a list", [1, 2, 3])

def test_type_error_second_argument():
    """Test type error when second argument is not a list"""
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        find_list_intersection([1, 2, 3], "not a list")

def test_mixed_type_intersection():
    """Test intersection with mixed type elements"""
    result = find_list_intersection([1, 'a', 2], [2, 'a', 3])
    assert set(result) == {2, 'a'}

def test_large_lists():
    """Test intersection with large lists"""
    list1 = list(range(1000)) + [1001]
    list2 = list(range(500, 1500))
    expected_result = list(range(500, 1000))
    result = find_list_intersection(list1, list2)
    assert set(result) == set(expected_result)