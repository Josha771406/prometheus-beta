import logging
import pytest
import time
from unittest.mock import patch
from src.function_logger import log_execution_time

# Capture logging output
def test_log_execution_time_basic():
    @log_execution_time
    def sample_function(x, y):
        return x + y
    
    with patch('logging.Logger.info') as mock_log_info:
        result = sample_function(3, 4)
        
        # Check the function returns correct result
        assert result == 7
        
        # Check logging calls
        assert mock_log_info.call_count == 2
        
        # Verify start logging
        start_log = mock_log_info.call_args_list[0][0][0]
        assert "Starting execution of sample_function" in start_log
        assert "(3, 4)" in start_log
        
        # Verify end logging
        end_log = mock_log_info.call_args_list[1][0][0]
        assert "Completed execution of sample_function" in end_log
        assert "Execution time:" in end_log

def test_log_execution_time_with_kwargs():
    @log_execution_time
    def sample_function_kwargs(x, y=0):
        return x + y
    
    with patch('logging.Logger.info') as mock_log_info:
        result = sample_function_kwargs(3, y=5)
        
        # Check the function returns correct result
        assert result == 8
        
        # Check logging calls
        assert mock_log_info.call_count == 2
        
        # Verify start logging
        start_log = mock_log_info.call_args_list[0][0][0]
        assert "Starting execution of sample_function_kwargs" in start_log
        assert "x=3, y=5" in start_log

def test_log_execution_time_exception():
    @log_execution_time
    def sample_function_exception():
        raise ValueError("Test exception")
    
    with patch('logging.Logger.info') as mock_log_info, \
         patch('logging.Logger.error') as mock_log_error:
        
        with pytest.raises(ValueError, match="Test exception"):
            sample_function_exception()
        
        # Check logging calls
        mock_log_info.assert_called_once()
        mock_log_error.assert_called_once()
        
        # Verify error logging
        error_log = mock_log_error.call_args[0][0]
        assert "Exception in sample_function_exception" in error_log
        assert "Test exception" in error_log

def test_log_execution_time_performance():
    @log_execution_time
    def slow_function():
        time.sleep(0.1)  # Simulate a slow function
    
    with patch('logging.Logger.info') as mock_log_info:
        slow_function()
        
        # Check logging calls
        assert mock_log_info.call_count == 2
        
        # Verify end log includes execution time
        end_log = mock_log_info.call_args_list[1][0][0]
        assert "Execution time:" in end_log
        
        # Extract execution time
        import re
        match = re.search(r'Execution time: (\d+\.\d+)', end_log)
        assert match is not None
        execution_time = float(match.group(1))
        
        # Check execution time is around 0.1 seconds (with some tolerance)
        assert 0.09 <= execution_time <= 0.11