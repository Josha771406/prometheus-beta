import readline
import logging
from typing import Optional, Callable, Any

class ReadlineLogger:
    """
    A utility class for logging interactive readline prompts with advanced features.
    
    This class provides methods to log user inputs captured through readline,
    with configurable logging levels and optional custom processing.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): A custom logger. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
        self._input_processor: Optional[Callable[[str], Any]] = None
    
    def set_input_processor(self, processor: Optional[Callable[[str], Any]] = None):
        """
        Set an optional input processor function to transform or validate input.
        
        Args:
            processor (Optional[Callable[[str], Any]]): A function to process input.
        """
        self._input_processor = processor
    
    def log_prompt(self, prompt: str, log_level: int = logging.INFO) -> str:
        """
        Log an interactive prompt and capture user input.
        
        Args:
            prompt (str): The prompt text to display.
            log_level (int, optional): Logging level. Defaults to logging.INFO.
        
        Returns:
            str: The user's input.
        
        Raises:
            ValueError: If the input is empty after processing.
        """
        # Log the prompt
        self.logger.log(log_level, f"Prompt: {prompt}")
        
        try:
            # Capture user input
            user_input = input(prompt)
            
            # Apply optional input processor
            if self._input_processor:
                processed_input = self._input_processor(user_input)
            else:
                processed_input = user_input
            
            # Validate non-empty input
            if processed_input is None or (isinstance(processed_input, str) and not processed_input.strip()):
                raise ValueError("Input cannot be empty")
            
            # Log the input
            self.logger.log(log_level, f"Input received: {processed_input}")
            
            return str(processed_input)
        
        except (KeyboardInterrupt, EOFError) as e:
            # Log and re-raise interruption
            self.logger.error(f"Input interrupted: {e}")
            raise
        except Exception as e:
            # Log any unexpected errors
            self.logger.error(f"Error in prompt: {e}")
            raise