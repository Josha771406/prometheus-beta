"""
Test suite for Lempel-Ziv-Welch compression and decompression functions.
"""

import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_single_character_string():
    """Test compression and decompression of a single character string."""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_repeated_characters():
    """Test compression and decompression of repeated characters."""
    original = "AAAAAAAAAA"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_mixed_characters():
    """Test compression and decompression of mixed character strings."""
    original = "Hello, World!"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_unicode_characters():
    """Test compression and decompression of unicode characters."""
    original = "こんにちは世界"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_compress_invalid_input_type():
    """Test that TypeError is raised for non-string input to compress."""
    with pytest.raises(TypeError):
        lzw_compress(123)
    with pytest.raises(TypeError):
        lzw_compress(["test"])

def test_compress_empty_string():
    """Test that ValueError is raised for empty string input to compress."""
    with pytest.raises(ValueError):
        lzw_compress("")

def test_decompress_invalid_input_type():
    """Test that TypeError is raised for non-list or non-integer input to decompress."""
    with pytest.raises(TypeError):
        lzw_decompress("test")
    with pytest.raises(TypeError):
        lzw_decompress([1, 2, "3"])

def test_decompress_empty_list():
    """Test that ValueError is raised for empty list input to decompress."""
    with pytest.raises(ValueError):
        lzw_decompress([])

def test_compression_and_decompression_complexity():
    """Test a more complex string with various patterns."""
    original = "ABRACADABRA" * 10
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original