import os
import pytest
import shutil
import tempfile

from src.file_renamer import rename_file

@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing file operations."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname

def test_rename_file_success(temp_dir):
    """Test successful file renaming."""
    # Create a source file
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('test content')
    
    # Rename the file
    result = rename_file(source_path, dest_path)
    
    # Verify
    assert result is True
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_rename_file_to_different_directory(temp_dir):
    """Test renaming a file to a different directory."""
    # Create source directory and file
    os.makedirs(os.path.join(temp_dir, 'sourcedir'))
    os.makedirs(os.path.join(temp_dir, 'destdir'))
    source_path = os.path.join(temp_dir, 'sourcedir', 'source.txt')
    dest_path = os.path.join(temp_dir, 'destdir', 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('test content')
    
    # Rename the file
    result = rename_file(source_path, dest_path)
    
    # Verify
    assert result is True
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_rename_nonexistent_file(temp_dir):
    """Test renaming a file that doesn't exist."""
    source_path = os.path.join(temp_dir, 'nonexistent.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with pytest.raises(FileNotFoundError):
        rename_file(source_path, dest_path)

def test_rename_to_existing_file(temp_dir):
    """Test renaming to a file that already exists."""
    # Create source and destination files
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('source content')
    
    with open(dest_path, 'w') as f:
        f.write('destination content')
    
    # Attempt to rename
    with pytest.raises(FileExistsError):
        rename_file(source_path, dest_path)

def test_rename_directory(temp_dir):
    """Test attempting to rename a directory."""
    source_dir = os.path.join(temp_dir, 'sourcedir')
    dest_dir = os.path.join(temp_dir, 'destdir')
    
    os.makedirs(source_dir)
    
    with pytest.raises(IsADirectoryError):
        rename_file(source_dir, dest_dir)

def test_invalid_input_types():
    """Test passing invalid input types."""
    with pytest.raises(TypeError):
        rename_file(123, 'dest')
    
    with pytest.raises(TypeError):
        rename_file('source', 456)