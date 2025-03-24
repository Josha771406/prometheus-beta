import logging

def configure_logging():
    """
    Configure basic logging for the application.
    
    Sets up a basic logging configuration with INFO level 
    and a simple format.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )