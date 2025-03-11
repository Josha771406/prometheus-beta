import os
import bz2
import pytest
import tempfile
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

def test_permission_error(monkeypatch):
    """Test handling of permission errors."""
    def mock_open(*args, **kwargs):
        raise PermissionError("Mocked permission error")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bz2') as temp_file:
        temp_file.close()
        
        monkeypatch.setattr('builtins.open', mock_open)
        
        with pytest.raises(PermissionError):
            decompress_bzip2_file(temp_file.name)
    
    # Cleanup
    os.unlink(temp_file.name)