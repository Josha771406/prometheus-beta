import pytest
from src.alternating_case import to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert to_alternating_path_case("hello world") == "hello-World"
    assert to_alternating_path_case("PYTHON PROGRAMMING") == "python-Programming"

def test_snake_case_conversion():
    """Test conversion of snake_case strings."""
    assert to_alternating_path_case("snake_case example") == "snake-Case-Example"

def test_mixed_case_conversion():
    """Test conversion of mixed case strings."""
    assert to_alternating_path_case("MixED cASe ExAMPle") == "mixed-Case-Example"

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_path_case("hello") == "hello"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_path_case("") == ""

def test_multiple_spaces():
    """Test conversion with multiple spaces."""
    assert to_alternating_path_case("multiple   spaces") == "multiple-Spaces"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_path_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_path_case(None)

def test_special_characters():
    """Test conversion with special characters."""
    assert to_alternating_path_case("hello! world@") == "hello-World"