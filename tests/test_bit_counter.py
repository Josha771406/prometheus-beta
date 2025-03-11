import pytest
from src.bit_counter import count_set_bits

def test_positive_integers():
    """Test counting set bits for positive integers."""
    assert count_set_bits(5) == 2  # Binary: 101
    assert count_set_bits(15) == 4  # Binary: 1111
    assert count_set_bits(0) == 0  # Binary: 0
    assert count_set_bits(1) == 1  # Binary: 1
    assert count_set_bits(255) == 8  # Binary: 11111111

def test_negative_integers():
    """Test counting set bits for negative integers."""
    assert count_set_bits(-5) == 2  # Two's complement representation
    assert count_set_bits(-15) == 4 
    assert count_set_bits(-1) == 64  # All bits set in two's complement

def test_large_integers():
    """Test counting set bits for large integers."""
    assert count_set_bits(2**32 - 1) == 32  # All 32-bit integers set
    assert count_set_bits(2**64 - 1) == 64  # All 64-bit integers set

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    
    with pytest.raises(TypeError):
        count_set_bits(None)