import numpy as np

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
    
    n = cost_matrix.shape[0]
    
    # Step 1: Reduce rows
    reduced_matrix = cost_matrix.copy()
    for i in range(n):
        reduced_matrix[i] -= reduced_matrix[i].min()
    
    # Step 2: Reduce columns
    for j in range(n):
        reduced_matrix[:, j] -= reduced_matrix[:, j].min()
    
    # Step 3: Find optimal assignment using Hungarian matching
    def kuhn_munkres_matching(matrix):
        # Adapted from Kuhn-Munkres (Hungarian) algorithm
        match_x = [-1] * n
        match_y = [-1] * n
        used = [False] * n
        
        def dfs(v):
            used[v] = True
            for u in range(n):
                if matrix[v][u] == 0 and match_y[u] == -1:
                    match_x[v] = u
                    match_y[u] = v
                    return True
            
            for u in range(n):
                if matrix[v][u] == 0 and not used[match_y[u]]:
                    if dfs(match_y[u]):
                        match_x[v] = u
                        match_y[u] = v
                        return True
            
            return False
        
        # Try to match each worker
        for v in range(n):
            used = [False] * n
            dfs(v)
        
        return match_x
    
    # Find matching
    assignment_indices = kuhn_munkres_matching(reduced_matrix)
    
    # Prepare full assignment list
    full_assignment = []
    for worker, job in enumerate(assignment_indices):
        if job != -1:
            full_assignment.append((worker, job))
    
    # Calculate total cost
    total_cost = sum(cost_matrix[worker, job] for worker, job in full_assignment)
    
    return total_cost, full_assignment