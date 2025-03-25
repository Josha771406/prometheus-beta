import os
import shutil

def rename_file(source_path, destination_path):
    """
    Rename a file from source path to destination path.

    Args:
        source_path (str): The current path of the file to be renamed.
        destination_path (str): The new path for the file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to rename the file.
        IsADirectoryError: If the source path is a directory.
        FileExistsError: If the destination file already exists.
    """
    # Validate input paths
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Paths must be strings")
    
    # Normalize paths to handle different path separators
    source_path = os.path.normpath(source_path)
    destination_path = os.path.normpath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Ensure source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")
    
    # Check if destination already exists
    if os.path.exists(destination_path):
        raise FileExistsError(f"Destination file already exists: {destination_path}")
    
    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    try:
        # Rename the file
        shutil.move(source_path, destination_path)
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied when renaming file from {source_path} to {destination_path}")