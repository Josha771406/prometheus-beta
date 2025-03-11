import os
from typing import List

def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in a given directory.

    Args:
        directory_path (str): The path to the directory to search for subdirectories.

    Returns:
        List[str]: A list of subdirectory names (not full paths).

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Validate input
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")
    
    try:
        # List all entries in the directory
        all_entries = os.listdir(directory_path)
        
        # Filter for subdirectories
        subdirs = [
            entry for entry in all_entries 
            if os.path.isdir(os.path.join(directory_path, entry))
        ]
        
        return subdirs
    
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to access directory '{directory_path}'.")