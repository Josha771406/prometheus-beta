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
        neighbors = [
            (r+1, c), (r-1, c), 
            (r, c+1), (r, c-1)
        ]
        
        # Filter valid and unvisited neighbors
        valid_neighbors = [
            neighbor for neighbor in neighbors
            if (0 <= neighbor[0] < len(maze) and 
                0 <= neighbor[1] < len(maze[0]) and 
                (maze[neighbor[0]][neighbor[1]] == 0 or 
                 maze[neighbor[0]][neighbor[1]] == 3) and
                neighbor not in visited
        ]
        
        # Add valid neighbors to queue
        for neighbor in valid_neighbors:
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None