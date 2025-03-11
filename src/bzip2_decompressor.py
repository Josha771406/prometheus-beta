import os
import bz2
import stat

def decompress_bzip2_file(input_path, output_path=None):
    """
    Decompress a bzip2-compressed file.

    Args:
        input_path (str): Path to the bzip2-compressed input file.
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input filename 
                                     with .bz2 extension stripped.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        ValueError: If input file is not a valid bzip2 compressed file.
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Check read permissions on input file
    if not os.access(input_path, os.R_OK):
        raise PermissionError(f"No read permission for input file: {input_path}")

    # Determine output path if not provided
    if output_path is None:
        # Remove .bz2 extension if present
        output_path = input_path.removesuffix('.bz2') if input_path.endswith('.bz2') else input_path + '.decompressed'

    # Check write permissions on output path's directory
    output_dir = os.path.dirname(output_path) or '.'
    if not os.access(output_dir, os.W_OK):
        raise PermissionError(f"No write permission for output directory: {output_dir}")

    # Check if output file already exists and is writable
    if os.path.exists(output_path):
        try:
            # Check if the file is writable
            with open(output_path, 'a'):
                pass
        except PermissionError:
            raise PermissionError(f"No write permission for output file: {output_path}")

    try:
        # Open input compressed file and output decompressed file
        with bz2.open(input_path, 'rb') as compressed_file, \
             open(output_path, 'wb') as decompressed_file:
            # Read and decompress file contents
            decompressed_data = compressed_file.read()
            
            # Validate decompressed data exists
            if not decompressed_data:
                raise ValueError("Invalid or empty bzip2 compressed file")
            
            decompressed_file.write(decompressed_data)

    except OSError as e:
        # This will catch various bzip2 specific decompression errors
        if 'Permission denied' in str(e):
            raise PermissionError(f"Permission error: {e}")
        raise ValueError(f"Invalid bzip2 compressed file: {e}")
    except Exception as e:
        # Re-raise other unexpected errors
        raise

    return output_path