import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz77_compression import LZ77Compressor

def test_lz77_compress_empty_input():
    """Test compression of empty input"""
    compressor = LZ77Compressor()
    assert compressor.compress("") == []
    assert compressor.compress(b"") == []

def test_lz77_decompress_empty_input():
    """Test decompression of empty input"""
    compressor = LZ77Compressor()
    assert compressor.decompress([]) == b""

def test_lz77_compress_decompress_simple_string():
    """Test compression and decompression of a simple string"""
    compressor = LZ77Compressor()
    original = "HELLO WORLD"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_compress_decompress_repeated_pattern():
    """Test compression and decompression with repeated patterns"""
    compressor = LZ77Compressor()
    original = "ABCABCABCABC"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_compress_decompress_binary_data():
    """Test compression and decompression of binary data"""
    compressor = LZ77Compressor()
    original = b'\x00\x01\x02\x03\x00\x01\x02\x03'
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    assert decompressed == original

def test_lz77_compress_long_input():
    """Test compression of a longer input with repeated patterns"""
    compressor = LZ77Compressor()
    original = "This is a test string with some repeated content " * 10
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_edge_cases():
    """Test various edge cases"""
    compressor = LZ77Compressor()
    
    # Single character
    original = "A"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == original
    
    # Repeated character
    original = "AAAAAAAA"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_type_handling():
    """Test different input types"""
    compressor = LZ77Compressor()
    
    # String input
    string_input = "Hello, world!"
    str_compressed = compressor.compress(string_input)
    str_decompressed = compressor.decompress(str_compressed)
    assert str_decompressed.decode('utf-8') == string_input
    
    # Bytes input
    bytes_input = b"Hello, world!"
    bytes_compressed = compressor.compress(bytes_input)
    bytes_decompressed = compressor.decompress(bytes_compressed)
    assert bytes_decompressed == bytes_input