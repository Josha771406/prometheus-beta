import os
import bz2
import pytest
import tempfile
import stat
from src.bzip2_decompressor import decompress_bzip2_file

@pytest.fixture
def sample_bzip2_file():
    """Create a sample bzip2 compressed file for testing."""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bz2') as temp_compressed:
        original_content = b"This is a test file for bzip2 decompression."
        compressed_content = bz2.compress(original_content)
        temp_compressed.write(compressed_content)
        temp_compressed.close()
        yield temp_compressed.name
    
    # Cleanup
    os.unlink(temp_compressed.name)

def test_decompress_valid_bzip2_file(sample_bzip2_file):
    """Test decompressing a valid bzip2 file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'decompressed.txt')
        result_path = decompress_bzip2_file(sample_bzip2_file, output_path)
        
        assert os.path.exists(result_path)
        with open(result_path, 'rb') as f:
            content = f.read()
        assert content == b"This is a test file for bzip2 decompression."

def test_decompress_default_output_path(sample_bzip2_file):
    """Test decompression with default output path."""
    result_path = decompress_bzip2_file(sample_bzip2_file)
    
    assert os.path.exists(result_path)
    with open(result_path, 'rb') as f:
        content = f.read()
    assert content == b"This is a test file for bzip2 decompression."
    
    # Cleanup
    os.unlink(result_path)

def test_nonexistent_file():
    """Test handling of nonexistent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file('/path/to/nonexistent/file.bz2')

def test_invalid_bzip2_file():
    """Test handling of invalid bzip2 file."""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bz2') as invalid_file:
        invalid_file.write(b"This is not a valid bzip2 file")
        invalid_file.close()
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(invalid_file.name)
    
    # Cleanup
    os.unlink(invalid_file.name)

def test_permission_error(tmp_path):
    """Test handling of permission errors."""
    # Create a temp file with read+write permissions
    temp_file_path = tmp_path / 'test.bz2'
    
    # Compress some test data with bzip2
    test_data = b"Test content for bzip2 decompression"
    compressed_data = bz2.compress(test_data)
    
    with open(temp_file_path, 'wb') as f:
        f.write(compressed_data)
    
    # Multiple test cases for permission testing
    permission_test_cases = [
        # Scenario 1: Try to write to a read-only directory
        lambda: (
            str(temp_file_path),
            str(tmp_path / 'no_write_dir' / 'result.txt'),
            lambda output_path: os.makedirs(os.path.dirname(output_path), mode=0o555)
        ),
        # Scenario 2: Try to write to a read-only file
        lambda: (
            str(temp_file_path),
            str(tmp_path / 'read_only_file'),
            lambda output_path: (
                open(output_path, 'w').close(),  # Create file
                os.chmod(output_path, 0o400)  # Make read-only
            )
        )
    ]

    # Test each permission scenario
    for test_case in permission_test_cases:
        input_path, output_path, permission_setter = test_case()
        
        # Set restrictive permissions
        permission_setter(output_path)
        
        # Attempt to decompress and ensure permission error is raised
        try:
            decompress_bzip2_file(input_path, output_path)
            pytest.fail(f"Expected PermissionError for input {input_path}, output {output_path}")
        except (PermissionError, OSError):
            pass  # Expected behavior