import pytest
import logging
from src.currency_logger import format_currency_log

def test_basic_currency_formatting(caplog):
    """Test basic currency formatting and logging"""
    caplog.set_level(logging.INFO)
    
    result = format_currency_log(1234.56)
    
    assert result == '$1,234.56'
    assert 'Currency Log: $1,234.56' in caplog.text

def test_custom_currency_symbol():
    """Test formatting with a different currency symbol"""
    result = format_currency_log(1234.56, currency='€')
    
    assert result == '€1,234.56'

def test_whole_number():
    """Test formatting with a whole number"""
    result = format_currency_log(1000)
    
    assert result == '$1,000.00'

def test_negative_number():
    """Test formatting with a negative number"""
    result = format_currency_log(-1234.56)
    
    assert result == '$-1,234.56'

def test_invalid_amount_type():
    """Test raising ValueError for invalid amount type"""
    with pytest.raises(ValueError, match="Amount must be a number"):
        format_currency_log("not a number")

def test_invalid_currency_type():
    """Test raising TypeError for invalid currency type"""
    with pytest.raises(TypeError, match="Currency must be a string"):
        format_currency_log(1234.56, currency=123)

def test_zero_amount():
    """Test formatting with zero amount"""
    result = format_currency_log(0)
    
    assert result == '$0.00'