import os
import pytest
from src.file_string_search import search_string_in_file

# Helper function to create a test file
def create_test_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# Fixture to help clean up test files
@pytest.fixture
def cleanup_test_files():
    yield
    # Clean up test files after tests
    test_files = ['test_search.txt', 'empty_file.txt']
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)

def test_search_string_found(cleanup_test_files):
    # Create a test file
    create_test_file('test_search.txt', 
        "Hello world\n"
        "This is a test file\n"
        "Multiple lines here\n"
        "Test string is here\n"
    )
    
    # Search for an existing string
    result = search_string_in_file('test_search.txt', 'test')
    assert result == [2, 4], "Should find 'test' in lines 2 and 4"

def test_search_string_not_found(cleanup_test_files):
    # Create a test file
    create_test_file('test_search.txt', 
        "Hello world\n"
        "This is a test file\n"
    )
    
    # Search for a non-existing string
    result = search_string_in_file('test_search.txt', 'unicorn')
    assert result == [], "Should return empty list when string not found"

def test_empty_file(cleanup_test_files):
    # Create an empty file
    create_test_file('empty_file.txt', '')
    
    # Search in empty file
    result = search_string_in_file('empty_file.txt', 'anything')
    assert result == [], "Should return empty list for empty file"

def test_file_not_found():
    # Try to search in a non-existent file
    with pytest.raises(FileNotFoundError):
        search_string_in_file('nonexistent_file.txt', 'test')

def test_invalid_input_types():
    # Test invalid file path type
    with pytest.raises(TypeError):
        search_string_in_file(123, 'test')
    
    # Test invalid search string type
    with pytest.raises(TypeError):
        search_string_in_file('test.txt', 123)

def test_empty_file_path():
    # Test empty file path
    with pytest.raises(ValueError):
        search_string_in_file('', 'test')

def test_case_sensitive_search(cleanup_test_files):
    # Create a test file
    create_test_file('test_search.txt', 
        "Hello World\n"
        "hello world\n"
    )
    
    # Search should be case-sensitive
    result = search_string_in_file('test_search.txt', 'Hello')
    assert result == [1], "Should be case-sensitive"
    
    result = search_string_in_file('test_search.txt', 'hello')
    assert result == [2], "Should be case-sensitive"