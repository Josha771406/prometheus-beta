from typing import List, Tuple, Dict, Optional, Union

def bellman_ford(graph: List[Tuple[int, int, int]], source: int, num_vertices: int) -> Union[Dict[int, int], None]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a source vertex.

    Args:
        graph (List[Tuple[int, int, int]]): List of edges, where each edge is (from_vertex, to_vertex, weight)
        source (int): The starting vertex
        num_vertices (int): Total number of vertices in the graph

    Returns:
        Dict[int, int]: Dictionary of shortest distances from source to each vertex, 
        or None if negative cycle is detected

    Raises:
        ValueError: If source vertex is invalid or graph is improperly formatted
    """
    # Input validation
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")

    if source < 0 or source >= num_vertices:
        raise ValueError(f"Invalid source vertex. Must be between 0 and {num_vertices - 1}")
    
    # Special case for single vertex graph (with no edges)
    if not graph:
        return {source: 0} if source == 0 else {}

    # Initialize distances
    distances = [float('inf')] * num_vertices
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        
        # Early stopping if no updates
        if not updated:
            break

    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    return {i: dist for i, dist in enumerate(distances) if dist != float('inf')}