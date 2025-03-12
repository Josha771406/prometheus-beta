import pytest
from src.pascal_case_converter import convert_to_pascal_case

def test_convert_to_pascal_case_basic():
    """Test basic string conversion to Pascal case."""
    assert convert_to_pascal_case("hello world") == "HelloWorld"
    assert convert_to_pascal_case("hello_world") == "HelloWorld"
    assert convert_to_pascal_case("hello-world") == "HelloWorld"

def test_convert_to_pascal_case_single_word():
    """Test conversion of a single word."""
    assert convert_to_pascal_case("hello") == "Hello"

def test_convert_to_pascal_case_already_pascal():
    """Test conversion of a string already in Pascal case."""
    assert convert_to_pascal_case("HelloWorld") == "HelloWorld"

def test_convert_to_pascal_case_mixed_separators():
    """Test conversion with mixed separators."""
    assert convert_to_pascal_case("hello_world-test") == "HelloWorldTest"

def test_convert_to_pascal_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_pascal_case("") == ""

def test_convert_to_pascal_case_multiple_spaces():
    """Test conversion with multiple spaces."""
    assert convert_to_pascal_case("hello   world") == "HelloWorld"

def test_convert_to_pascal_case_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_pascal_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_pascal_case(None)