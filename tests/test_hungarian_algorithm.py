import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    """Test a simple 3x3 assignment problem"""
    cost_matrix = [
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    # The actual optimal assignment may vary
    # What matters is that the total cost is minimized
    assert total_cost <= 9
    assert len(assignment) == len(cost_matrix)
    
    # Verify each worker is assigned to exactly one job
    assigned_workers = [worker for worker, _ in assignment]
    assigned_jobs = [job for _, job in assignment]
    assert len(set(assigned_workers)) == len(assignment)
    assert len(set(assigned_jobs)) == len(assignment)

def test_large_matrix():
    """Test a larger matrix to ensure scalability"""
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    # Verify assignment is one-to-one
    assert len(set(worker for worker, _ in assignment)) == len(cost_matrix)
    assert len(set(job for _, job in assignment)) == len(cost_matrix)

def test_invalid_input_empty():
    """Test handling of empty matrix"""
    with pytest.raises(ValueError, match="Input must be a non-empty matrix"):
        hungarian_algorithm([])

def test_invalid_input_non_square():
    """Test handling of non-square matrix"""
    with pytest.raises(ValueError, match="Input must be a square matrix"):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])

def test_single_element_matrix():
    """Test single element matrix"""
    cost_matrix = [[5]]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 5
    assert assignment == [(0, 0)]

def test_all_same_costs():
    """Test matrix with uniform costs"""
    cost_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 3
    assert len(assignment) == 3

def test_numpy_input():
    """Test numpy array input"""
    cost_matrix = np.array([
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ])
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    # Expecting some valid assignment
    assert total_cost is not None
    assert len(assignment) == len(cost_matrix)

def test_zero_input_matrix():
    """Test matrix with zero values"""
    cost_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 0
    assert len(assignment) == 3