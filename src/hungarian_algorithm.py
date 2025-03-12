import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
    """
    Implement the Hungarian algorithm (Munkres algorithm) for solving the assignment problem.
    
    The function finds the optimal assignment that minimizes the total cost.
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A square matrix of costs for assignments.
                    Each element represents the cost of assigning a worker to a job.
    
    Returns:
        tuple: A tuple containing:
            - The optimal total cost of the assignment
            - A list of (worker, job) pairs representing the optimal assignment
    
    Raises:
        ValueError: If the input is not a valid square matrix or is empty
    """
    # Input validation
    if not isinstance(cost_matrix, (list, np.ndarray)) or len(cost_matrix) == 0:
        raise ValueError("Input must be a non-empty matrix")
    
    # Convert to numpy array for easier manipulation
    cost_matrix = np.array(cost_matrix, dtype=float)
    
    # Ensure square matrix
    if cost_matrix.ndim != 2 or cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    # Use scipy's linear_sum_assignment for robust solution
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Generate full assignment list
    assignment = list(zip(row_ind, col_ind))
    
    # Calculate total cost
    total_cost = cost_matrix[row_ind, col_ind].sum()
    
    return total_cost, assignment