import functools
import logging
import time
from typing import Callable, Any

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that logs the start and end of function execution, 
    including execution time.

    Args:
        func (Callable): The function to be decorated

    Returns:
        Callable: The wrapped function with logging
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log function start with arguments
        func_args_str = ', '.join([repr(a) for a in args] + 
                                   [f"{k}={repr(v)}" for k, v in kwargs.items()])
        logger.info(f"Starting execution of {func.__name__}({func_args_str})")
        
        # Record start time
        start_time = time.time()
        
        try:
            # Execute the function
            result = func(*args, **kwargs)
            
            # Calculate and log execution time
            end_time = time.time()
            execution_time = end_time - start_time
            logger.info(f"Completed execution of {func.__name__}. "
                        f"Execution time: {execution_time:.4f} seconds")
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur
            logger.error(f"Exception in {func.__name__}: {str(e)}")
            raise
    
    return wrapper