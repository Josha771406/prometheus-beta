def gravity_sort(arr):
    """
    Implement the gravity sort algorithm (Bead Sort / Gravity Sort).
    
    This algorithm works by simulating gravity acting on a set of beads,
    where each number is represented by a column of beads. When gravity
    is applied, the beads fall down, effectively sorting the numbers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # If list is empty or has only one element, return as-is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr) if arr else 0
    
    # Create a 2D representation of beads
    beads = [[1 if num > j else 0 for j in range(max_num)] for num in arr]
    
    # Apply gravity (drop beads)
    for col in range(max_num):
        # Count beads in each column
        col_sum = sum(row[col] for row in beads)
        
        # Adjust rows to reflect gravity
        for row in range(len(beads)):
            beads[row][col] = 1 if row >= len(beads) - col_sum else 0
    
    # Convert back to sorted list (descending to ascending)
    return sorted(sum(row) for row in beads)