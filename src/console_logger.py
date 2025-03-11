import logging
from enum import Enum, auto
from typing import Optional, Any

class UserPermissionLevel(Enum):
    """Enum representing different user permission levels."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class ConsoleLogger:
    """
    A logging utility that logs messages based on user permission levels.
    
    Attributes:
        _logger (logging.Logger): Internal logger instance
        _min_permission_level (UserPermissionLevel): Minimum permission level 
            required to log messages
    """
    
    def __init__(self, min_permission_level: UserPermissionLevel = UserPermissionLevel.USER):
        """
        Initialize the ConsoleLogger.
        
        Args:
            min_permission_level (UserPermissionLevel, optional): 
                Minimum permission level required to log messages. 
                Defaults to UserPermissionLevel.USER.
        """
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        
        # Create console handler if not already exists
        if not self._logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(levelname)s: %(message)s')
            console_handler.setFormatter(formatter)
            self._logger.addHandler(console_handler)
        
        self._min_permission_level = min_permission_level
    
    def log(self, message: str, user_permission: UserPermissionLevel, 
            log_level: int = logging.INFO) -> bool:
        """
        Log a message if the user has sufficient permissions.
        
        Args:
            message (str): The message to log
            user_permission (UserPermissionLevel): Current user's permission level
            log_level (int, optional): Logging level. Defaults to logging.INFO.
        
        Returns:
            bool: True if message was logged, False otherwise
        
        Raises:
            ValueError: If message is empty or None
            TypeError: If arguments are of incorrect type
        """
        # Validate inputs
        if message is None or message.strip() == "":
            raise ValueError("Message cannot be empty or None")
        
        if not isinstance(user_permission, UserPermissionLevel):
            raise TypeError("user_permission must be a UserPermissionLevel")
        
        # Check if user has sufficient permissions to log
        if user_permission.value >= self._min_permission_level.value:
            # Log the message
            if log_level == logging.INFO:
                self._logger.info(message)
            elif log_level == logging.WARNING:
                self._logger.warning(message)
            elif log_level == logging.ERROR:
                self._logger.error(message)
            elif log_level == logging.DEBUG:
                self._logger.debug(message)
            else:
                self._logger.log(log_level, message)
            
            return True
        
        return False