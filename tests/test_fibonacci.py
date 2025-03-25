import pytest
from src.fibonacci import generate_fibonacci_subsequence

def test_fibonacci_subsequence_zero_length():
    """Test generating a Fibonacci subsequence of length 0."""
    assert generate_fibonacci_subsequence(0) == []

def test_fibonacci_subsequence_one_element():
    """Test generating a Fibonacci subsequence of length 1."""
    assert generate_fibonacci_subsequence(1) == [0]

def test_fibonacci_subsequence_two_elements():
    """Test generating a Fibonacci subsequence of length 2."""
    assert generate_fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_longer():
    """Test generating a Fibonacci subsequence of length 5."""
    assert generate_fibonacci_subsequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_subsequence_larger():
    """Test generating a Fibonacci subsequence of length 7."""
    assert generate_fibonacci_subsequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_invalid_input_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Length of subsequence must be non-negative"):
        generate_fibonacci_subsequence(-1)

def test_invalid_input_type():
    """Test that a non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence("3")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence(3.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence(None)