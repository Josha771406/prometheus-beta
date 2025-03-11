import pytest
import logging
import io

from src.console_logger import ConsoleLogger, UserPermissionLevel

class TestConsoleLogger:
    def setup_method(self):
        """Set up a new logger and capture log output for each test."""
        # Capture log output
        self.log_capture = io.StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        
        # Create a logger to capture output
        self.test_logger = logging.getLogger()
        self.test_logger.setLevel(logging.INFO)
        self.test_logger.addHandler(self.log_handler)
    
    def teardown_method(self):
        """Remove the log handler after each test."""
        self.test_logger.removeHandler(self.log_handler)
        self.log_capture.close()
    
    def test_log_with_sufficient_permissions(self):
        """Test logging with sufficient permissions."""
        logger = ConsoleLogger(min_permission_level=UserPermissionLevel.USER)
        result = logger.log("Test message", UserPermissionLevel.ADMIN)
        
        assert result is True
        assert "Test message" in self.log_capture.getvalue()
    
    def test_log_with_insufficient_permissions(self):
        """Test logging with insufficient permissions."""
        logger = ConsoleLogger(min_permission_level=UserPermissionLevel.ADMIN)
        result = logger.log("Test message", UserPermissionLevel.USER)
        
        assert result is False
        assert "Test message" not in self.log_capture.getvalue()
    
    def test_log_at_minimum_permission(self):
        """Test logging at the minimum permission level."""
        logger = ConsoleLogger(min_permission_level=UserPermissionLevel.USER)
        result = logger.log("Test message", UserPermissionLevel.USER)
        
        assert result is True
        assert "Test message" in self.log_capture.getvalue()
    
    def test_log_empty_message_raises_error(self):
        """Test that empty message raises ValueError."""
        logger = ConsoleLogger()
        
        with pytest.raises(ValueError, match="Message cannot be empty or None"):
            logger.log("", UserPermissionLevel.USER)
        
        with pytest.raises(ValueError, match="Message cannot be empty or None"):
            logger.log(None, UserPermissionLevel.USER)
    
    def test_log_invalid_permission_type(self):
        """Test that invalid permission type raises TypeError."""
        logger = ConsoleLogger()
        
        with pytest.raises(TypeError, match="user_permission must be a UserPermissionLevel"):
            logger.log("Test message", "ADMIN")
    
    def test_different_log_levels(self):
        """Test logging at different log levels."""
        logger = ConsoleLogger()
        
        # Test various log levels
        assert logger.log("Info message", UserPermissionLevel.USER, logging.INFO) is True
        assert logger.log("Warning message", UserPermissionLevel.USER, logging.WARNING) is True
        assert logger.log("Error message", UserPermissionLevel.USER, logging.ERROR) is True
        assert logger.log("Debug message", UserPermissionLevel.USER, logging.DEBUG) is True
    
    def test_custom_log_level(self):
        """Test logging with a custom log level."""
        logger = ConsoleLogger()
        
        # Use a custom log level
        custom_level = 25  # between INFO and WARNING
        assert logger.log("Custom level message", UserPermissionLevel.USER, custom_level) is True