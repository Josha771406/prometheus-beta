import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

def create_log_capture(level=logging.INFO):
    """Create a log capture stream and configure logging."""
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    
    # Get the root logger and configure it
    logger = logging.getLogger()
    logger.setLevel(level)
    
    # Remove any existing handlers
    for existing_handler in logger.handlers[:]:
        logger.removeHandler(existing_handler)
    
    logger.addHandler(handler)
    return logger, log_capture

def test_readline_logger_basic_functionality():
    """Test basic logging of input prompt."""
    # Create log capture
    logger, log_capture = create_log_capture()
    
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
    logger, _ = create_log_capture()
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
    logger, _ = create_log_capture()
    readline_logger = ReadlineLogger(logger)
    
    # Simulate empty input
    with patch('builtins.input', return_value=''):
        with pytest.raises(ValueError, match="Input cannot be empty"):
            readline_logger.log_prompt("Enter something: ")

def test_readline_logger_custom_log_level():
    """Test logging with custom log level."""
    logger, log_capture = create_log_capture(level=logging.DEBUG)
    
    readline_logger = ReadlineLogger(logger)
    
    # Simulate user input with DEBUG level
    with patch('builtins.input', return_value='debug test'):
        result = readline_logger.log_prompt("Enter something: ", log_level=logging.DEBUG)
    
    log_output = log_capture.getvalue()
    assert "Prompt: Enter something: " in log_output
    assert "Input received: debug test" in log_output
    assert result == "debug test"

def test_readline_logger_keyboard_interrupt():
    """Test handling of keyboard interrupt."""
    logger, _ = create_log_capture()
    readline_logger = ReadlineLogger(logger)
    
    # Simulate keyboard interrupt
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            readline_logger.log_prompt("Enter something: ")

def test_readline_logger_eof_error():
    """Test handling of EOF error."""
    logger, _ = create_log_capture()
    readline_logger = ReadlineLogger(logger)
    
    # Simulate EOF error
    with patch('builtins.input', side_effect=EOFError):
        with pytest.raises(EOFError):
            readline_logger.log_prompt("Enter something: ")