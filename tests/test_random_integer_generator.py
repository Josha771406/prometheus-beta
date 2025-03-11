import pytest
import random
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_in_range():
    """Test that the generated integer is within the specified range."""
    for _ in range(100):  # Run multiple times to ensure randomness
        min_val, max_val = 1, 10
        result = generate_random_integer(min_val, max_val)
        assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_equal_bounds():
    """Test when min and max values are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5

def test_generate_random_integer_negative_range():
    """Test random integer generation with negative numbers."""
    for _ in range(100):
        min_val, max_val = -10, 0
        result = generate_random_integer(min_val, max_val)
        assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_large_range():
    """Test random integer generation with a large range."""
    for _ in range(100):
        min_val, max_val = -1000, 1000
        result = generate_random_integer(min_val, max_val)
        assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_invalid_input_types():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError):
        generate_random_integer(1.5, 10)
    with pytest.raises(TypeError):
        generate_random_integer(1, "10")
    with pytest.raises(TypeError):
        generate_random_integer("1", 10)

def test_invalid_range():
    """Test that ValueError is raised when min_value > max_value."""
    with pytest.raises(ValueError):
        generate_random_integer(10, 1)