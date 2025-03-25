def max_subarray_sum(arr):
    """
    Implement Kadane's algorithm to find the maximum sum of a contiguous subarray.
    
    This function uses Kadane's algorithm to find the maximum sum of a contiguous 
    subarray within a one-dimensional array of integers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum subarray sum.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check for invalid input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_so_far = float('-inf')  # Maximum sum found so far
    max_ending_here = 0  # Maximum sum ending at current position
    
    # Iterate through the array
    for num in arr:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the maximum sum found so far
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far