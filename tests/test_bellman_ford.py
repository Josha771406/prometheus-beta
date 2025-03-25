import pytest
from src.bellman_ford import bellman_ford

def test_basic_shortest_path():
    """Test a simple graph with known shortest paths"""
    graph = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 5)
    ]
    result = bellman_ford(graph, 0, 4)
    assert result == {
        0: 0,  # source vertex
        1: 4,  # path from 0 to 1 
        2: 3,  # direct path from 0 to 2
        3: 6   # path from 0 to 1 to 3 = 4 + 2
    }

def test_graph_with_negative_edges():
    """Test a graph with negative edge weights"""
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (3, 2, 5)
    ]
    result = bellman_ford(graph, 0, 4)
    assert result == {
        0: 0,  # source vertex
        1: -1,  # path from 0 to 1
        2: 2,  # path from 0 to 1 to 2
        3: 1   # path from 0 to 1 to 3
    }

def test_negative_cycle_detection():
    """Test detection of negative weight cycle"""
    graph = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, -2)
    ]
    result = bellman_ford(graph, 0, 3)
    assert result is None

def test_disconnected_vertex():
    """Test a graph with a vertex not reachable from source"""
    graph = [
        (0, 1, 4),
        (0, 2, 3),
        (3, 4, 5)  # separate component
    ]
    result = bellman_ford(graph, 0, 5)
    assert result == {
        0: 0,
        1: 4,
        2: 3
    }

def test_invalid_source_vertex():
    """Test handling of invalid source vertex"""
    graph = [(0, 1, 4), (1, 2, 3)]
    
    with pytest.raises(ValueError, match="Invalid source vertex"):
        bellman_ford(graph, -1, 3)
    
    with pytest.raises(ValueError, match="Invalid source vertex"):
        bellman_ford(graph, 3, 3)

def test_empty_graph():
    """Test handling of empty graph"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        bellman_ford([], 0, 0)

def test_single_vertex_graph():
    """Test a graph with only one vertex"""
    graph = []  # No edges
    result = bellman_ford(graph, 0, 1)
    assert result == {0: 0}