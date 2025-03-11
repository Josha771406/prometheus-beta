import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories_basic():
    """Test listing subdirectories in a typical scenario."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create some files to ensure they are not included
        open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'w').close()
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Assert correct subdirectories are returned
        assert set(subdirs) == {'subdir1', 'subdir2', 'subdir3'}
        assert len(subdirs) == 3

def test_list_subdirectories_empty():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        subdirs = list_subdirectories(temp_dir)
        assert subdirs == []

def test_list_subdirectories_only_files():
    """Test listing subdirectories when only files exist."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files
        open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'file2.txt'), 'w').close()
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        assert subdirs == []

def test_list_subdirectories_nested():
    """Test that only immediate subdirectories are returned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some nested subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1', 'nested1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Assert only immediate subdirectories are returned
        assert set(subdirs) == {'subdir1', 'subdir2'}
        assert 'nested1' not in subdirs

def test_list_subdirectories_nonexistent():
    """Test that FileNotFoundError is raised for non-existent directory."""
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_list_subdirectories_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)