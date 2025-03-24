import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

def test_readline_logger_basic_functionality():
    """Test basic logging of input prompt."""
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    logger = logging.getLogger()
    
    # Create ReadlineLogger
    readline_logger = ReadlineLogger(logger)
    
    # Simulate user input
    with patch('builtins.input', return_value='test input'):
        result = readline_logger.log_prompt("Enter something: ")
    
    # Check log output
    log_output = log_capture.getvalue()
    assert "Prompt: Enter something: " in log_output
    assert "Input received: test input" in log_output
    assert result == "test input"

def test_readline_logger_input_processor():
    """Test input processing functionality."""
    logger = logging.getLogger(__name__)
    readline_logger = ReadlineLogger(logger)
    
    # Define a processor that converts input to uppercase
    def uppercase_processor(input_str):
        return input_str.upper()
    
    readline_logger.set_input_processor(uppercase_processor)
    
    # Simulate user input
    with patch('builtins.input', return_value='hello'):
        result = readline_logger.log_prompt("Enter something: ")
    
    assert result == "HELLO"

def test_readline_logger_empty_input():
    """Test handling of empty input."""
    logger = logging.getLogger(__name__)
    readline_logger = ReadlineLogger(logger)
    
    # Simulate empty input
    with patch('builtins.input', return_value=''):
        with pytest.raises(ValueError, match="Input cannot be empty"):
            readline_logger.log_prompt("Enter something: ")

def test_readline_logger_custom_log_level():
    """Test logging with custom log level."""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.DEBUG)
    logger = logging.getLogger()
    
    readline_logger = ReadlineLogger(logger)
    
    # Simulate user input with DEBUG level
    with patch('builtins.input', return_value='debug test'):
        result = readline_logger.log_prompt("Enter something: ", log_level=logging.DEBUG)
    
    log_output = log_capture.getvalue()
    assert "Input received: debug test" in log_output
    assert result == "debug test"

def test_readline_logger_keyboard_interrupt():
    """Test handling of keyboard interrupt."""
    logger = logging.getLogger(__name__)
    readline_logger = ReadlineLogger(logger)
    
    # Simulate keyboard interrupt
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            readline_logger.log_prompt("Enter something: ")

def test_readline_logger_eof_error():
    """Test handling of EOF error."""
    logger = logging.getLogger(__name__)
    readline_logger = ReadlineLogger(logger)
    
    # Simulate EOF error
    with patch('builtins.input', side_effect=EOFError):
        with pytest.raises(EOFError):
            readline_logger.log_prompt("Enter something: ")