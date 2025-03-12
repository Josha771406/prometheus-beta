import pytest
from src.lcs_length import longest_common_subsequence_length

def test_basic_subsequence():
    """Test basic common subsequence scenarios"""
    assert longest_common_subsequence_length("abcde", "ace") == 3
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    """Test edge cases with empty strings"""
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("abc", "") == 0
    assert longest_common_subsequence_length("", "xyz") == 0

def test_partial_subsequence():
    """Test scenarios with partial subsequences"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_case_sensitive():
    """Test case sensitivity"""
    assert longest_common_subsequence_length("ABC", "abc") == 0
    assert longest_common_subsequence_length("AbC", "aBc") == 1

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence_length(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence_length("abc", ["a", "b", "c"])
    with pytest.raises(TypeError):
        longest_common_subsequence_length(None, "abc")

def test_repeated_characters():
    """Test with repeated characters"""
    assert longest_common_subsequence_length("AAAA", "AA") == 2
    assert longest_common_subsequence_length("ABABABAB", "BABA") == 4