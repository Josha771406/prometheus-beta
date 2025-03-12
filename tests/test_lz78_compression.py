"""
Test suite for LZ78 Compression Algorithm
"""

import pytest
from src.lz78_compression import LZ78Compressor

class TestLZ78Compression:
    def test_basic_compression(self):
        """Test basic string compression and decompression"""
        original = "TOBEORNOTTOBEORTOBEORNOT"
        compressed = LZ78Compressor.compress(original)
        decompressed = LZ78Compressor.decompress(compressed)
        assert decompressed == original
    
    def test_empty_string_compression(self):
        """Test compression of an empty string raises ValueError"""
        with pytest.raises(ValueError):
            LZ78Compressor.compress("")
    
    def test_single_character_compression(self):
        """Test compression of a single character"""
        original = "A"
        compressed = LZ78Compressor.compress(original)
        decompressed = LZ78Compressor.decompress(compressed)
        assert decompressed == original
    
    def test_repeated_pattern_compression(self):
        """Test compression of a string with repeated patterns"""
        original = "ABABABABABABABAB"
        compressed = LZ78Compressor.compress(original)
        decompressed = LZ78Compressor.decompress(compressed)
        assert decompressed == original
    
    def test_unicode_compression(self):
        """Test compression of Unicode characters"""
        original = "こんにちは世界"
        compressed = LZ78Compressor.compress(original)
        decompressed = LZ78Compressor.decompress(compressed)
        assert decompressed == original
    
    def test_invalid_input_types(self):
        """Test compression with invalid input types"""
        with pytest.raises(TypeError):
            LZ78Compressor.compress(123)
        
        with pytest.raises(TypeError):
            LZ78Compressor.compress(None)
        
        with pytest.raises(TypeError):
            LZ78Compressor.decompress("not a list")
        
        with pytest.raises(TypeError):
            LZ78Compressor.decompress(123)
    
    def test_invalid_compressed_data(self):
        """Test decompression with invalid compressed data"""
        with pytest.raises(ValueError):
            LZ78Compressor.decompress([(1, 'a'), (999, 'x')])
        
        with pytest.raises(ValueError):
            LZ78Compressor.decompress([(1, 123)])
    
    def test_compression_roundtrip(self):
        """Test multiple different strings for compression roundtrip"""
        test_strings = [
            "hello world",
            "banana banana bo bana",
            "Mississippi",
            "   spaces   ",
            "!@#$%^&*()"
        ]
        
        for original in test_strings:
            compressed = LZ78Compressor.compress(original)
            decompressed = LZ78Compressor.decompress(compressed)
            assert decompressed == original, f"Failed for string: {original}"