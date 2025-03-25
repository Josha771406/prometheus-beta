from typing import List, Optional, Tuple
from collections import deque

def find_shortest_path(maze: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from the start cell (2) to the end cell (3) in a maze.
    
    Args:
        maze (List[List[int]]): 2D grid representing the maze
            0: Empty cell
            1: Wall
            2: Start cell
            3: End cell
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path from start to end, 
        or None if no path exists
    
    Raises:
        ValueError: If start or end cell is missing, or maze is invalid
    """
    # Find start and end cells
    start = end = None
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == 2:
                start = (r, c)
            elif maze[r][c] == 3:
                end = (r, c)
    
    if start is None or end is None:
        raise ValueError("Maze must contain exactly one start (2) and one end (3) cell")
    
    # BFS to find shortest path
    queue = deque([(start, [start])])
    visited = set([start])
    
    def get_neighbors(cell: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Get valid neighboring cells that are not walls.
        
        Args:
            cell (Tuple[int, int]): Current cell coordinates
        
        Returns:
            List[Tuple[int, int]]: List of valid neighboring cells
        """
        r, c = cell
        neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        return [
            (nr, nc) for nr, nc in neighbors 
            if (0 <= nr < len(maze) and 
                0 <= nc < len(maze[0]) and 
                maze[nr][nc] != 1)
    
    def is_valid(cell: Tuple[int, int]) -> bool:
        """
        Check if a cell is a valid, empty cell in the maze.
        
        Args:
            cell (Tuple[int, int]): Cell coordinates to check
        
        Returns:
            bool: True if cell is empty, False otherwise
        """
        r, c = cell
        return (0 <= r < len(maze) and 
                0 <= c < len(maze[0]) and 
                maze[r][c] != 1)
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Explore neighbors
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None