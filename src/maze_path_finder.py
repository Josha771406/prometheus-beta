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
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Get possible neighboring cells
        r, c = current
        potential_neighbors = [
            (r+1, c), 
            (r-1, c), 
            (r, c+1), 
            (r, c-1)
        ]
        
        # Filter valid and unvisited neighbors
        valid_neighbors = []
        for neighbor in potential_neighbors:
            nr, nc = neighbor
            if (
                0 <= nr < len(maze) and 
                0 <= nc < len(maze[0]) and 
                (maze[nr][nc] == 0 or maze[nr][nc] == 3) and
                neighbor not in visited
            ):
                valid_neighbors.append(neighbor)
        
        # Add valid neighbors to queue
        for neighbor in valid_neighbors:
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None