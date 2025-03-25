import pytest
from src.maze_path_finder import find_shortest_path

def test_simple_path():
    """Test a simple maze with a direct path"""
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert len(path) == 3  # Start, intermediate, and end cells
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (1, 2)  # End cell

def test_path_with_obstacles():
    """Test a maze with obstacles requiring navigation"""
    maze = [
        [0, 0, 0, 0],
        [2, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (3, 3)  # End cell
    # Check path doesn't include walls
    for r, c in path:
        assert maze[r][c] != 1, f"Path contains a wall at {(r, c)}"

def test_no_path_exists():
    """Test a maze where no path exists"""
    maze = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_missing_start_or_end():
    """Test raising an error when start or end is missing"""
    maze_no_start = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 3]
    ]
    maze_no_end = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 2]
    ]
    
    with pytest.raises(ValueError, match="Maze must contain exactly one start"):
        find_shortest_path(maze_no_start)
    
    with pytest.raises(ValueError, match="Maze must contain exactly one start"):
        find_shortest_path(maze_no_end)

def test_multiple_possible_paths():
    """Test a maze with multiple possible paths"""
    maze = [
        [0, 0, 0, 0],
        [2, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (3, 3)  # End cell
    # Verify it's the shortest path
    assert len(path) == 6

def test_large_maze():
    """Test a larger maze to ensure scalability"""
    maze = [
        [0, 0, 0, 0, 0, 0],
        [2, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path[0] == (1, 0)  # Start cell
    assert path[-1] == (4, 5)  # End cell