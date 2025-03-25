import pytest
from src.path_case_converter import convert_to_path_case

def test_convert_to_path_case_basic_string():
    """Test basic string conversion to path case."""
    assert convert_to_path_case("Hello World") == "hello-world"

def test_convert_to_path_case_snake_case():
    """Test conversion of snake_case to path case."""
    assert convert_to_path_case("snake_case_string") == "snake-case-string"

def test_convert_to_path_case_camel_case():
    """Test conversion of camelCase to path case."""
    assert convert_to_path_case("camelCaseString") == "camel-case-string"

def test_convert_to_path_case_mixed_case():
    """Test conversion of mixed case with special characters."""
    assert convert_to_path_case("Mixed Case String!") == "mixed-case-string"

def test_convert_to_path_case_pascal_case():
    """Test conversion of PascalCase to path case."""
    assert convert_to_path_case("PascalCaseString") == "pascal-case-string"

def test_convert_to_path_case_empty_string():
    """Test conversion of empty string."""
    assert convert_to_path_case("") == ""

def test_convert_to_path_case_multiple_spaces():
    """Test conversion of string with multiple spaces."""
    assert convert_to_path_case("Hello   World  Test") == "hello-world-test"

def test_convert_to_path_case_special_characters():
    """Test conversion of string with various special characters."""
    assert convert_to_path_case("Hello, World! Test@123") == "hello-world-test-123"

def test_convert_to_path_case_error_non_string():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_path_case(123)

def test_convert_to_path_case_numbers():
    """Test conversion of string with numbers."""
    assert convert_to_path_case("Test2Number") == "test-2-number"