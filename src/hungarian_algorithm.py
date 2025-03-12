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
    
    # Step 1: Subtract row minimums
    reduced_matrix = cost_matrix.copy()
    for i in range(n):
        reduced_matrix[i] -= reduced_matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        reduced_matrix[:, j] -= reduced_matrix[:, j].min()
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Create coverage arrays
        row_covered = np.zeros(n, dtype=bool)
        col_covered = np.zeros(n, dtype=bool)
        
        # Count zeros in each row and column
        zero_rows = [np.sum(row == 0) for row in matrix]
        zero_cols = [np.sum(matrix[:, col] == 0) for col in range(n)]
        
        # Assign lines to cover all zeros
        lines = 0
        while lines < n:
            # Find row or column with most uncovered zeros
            max_zeros_row = -1
            max_zeros_col = -1
            max_zeros = -1
            
            for i in range(n):
                if not row_covered[i] and zero_rows[i] > max_zeros:
                    max_zeros = zero_rows[i]
                    max_zeros_row = i
            
            for j in range(n):
                if not col_covered[j] and zero_cols[j] > max_zeros:
                    max_zeros = zero_cols[j]
                    max_zeros_col = j
                    max_zeros_row = -1
            
            # Cover the row or column
            if max_zeros_row != -1:
                row_covered[max_zeros_row] = True
                lines += 1
            elif max_zeros_col != -1:
                col_covered[max_zeros_col] = True
                lines += 1
            else:
                break
        
        return row_covered, col_covered, lines
    
    # Step 4: Find optimal assignment
    def find_assignment(matrix):
        assignment = []
        used_rows = set()
        used_cols = set()
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0 and i not in used_rows and j not in used_cols:
                    assignment.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
                    break
        
        return assignment
    
    # Iterations to find optimal assignment
    row_covered, col_covered, lines = cover_zeros(reduced_matrix)
    
    while lines < n:
        # Find the smallest uncovered entry
        min_uncovered = float('inf')
        for i in range(n):
            for j in range(n):
                if not row_covered[i] and not col_covered[j]:
                    min_uncovered = min(min_uncovered, reduced_matrix[i, j])
        
        # Modify matrix
        for i in range(n):
            for j in range(n):
                if row_covered[i]:
                    reduced_matrix[i, j] += min_uncovered
                if not col_covered[j]:
                    reduced_matrix[i, j] -= min_uncovered
        
        # Recheck zero coverage
        row_covered, col_covered, lines = cover_zeros(reduced_matrix)
    
    # Find optimal assignment
    assignment = find_assignment(reduced_matrix)
    
    # Calculate total cost
    total_cost = sum(cost_matrix[worker, job] for worker, job in assignment)
    
    return total_cost, assignment