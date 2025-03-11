import pytest
from src.vowel_counter import count_vowels_consonants

def test_basic_string():
    """Test counting vowels and consonants in a basic string."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case_string():
    """Test that the function is case-insensitive."""
    result = count_vowels_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_empty_string():
    """Test counting in an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_string_with_spaces_and_punctuation():
    """Test string with non-alphabetic characters."""
    result = count_vowels_consonants("Hello, World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_only_vowels():
    """Test a string containing only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string containing only consonants."""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)

def test_unicode_characters():
    """Test handling of unicode characters."""
    result = count_vowels_consonants("Héllô")
    assert result == {'vowels': 2, 'consonants': 3}

def test_numeric_and_special_characters():
    """Test string with numbers and special characters."""
    result = count_vowels_consonants("Hello123!")
    assert result == {'vowels': 2, 'consonants': 3}