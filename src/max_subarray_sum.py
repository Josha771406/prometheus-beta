def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a subarray with size k in the given array.
    
    Args:
        arr (list): Input list of integers
        k (int): Size of the subarray
    
    Returns:
        int: Maximum sum of a subarray of size k
             Returns None if k is larger than the array length or k <= 0
    
    Raises:
        TypeError: If input is not a list or k is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not isinstance(k, int):
        raise TypeError("Subarray size k must be an integer")
    
    # Handle edge cases
    if k <= 0:
        return None
    
    if k > len(arr):
        return None
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove first element of previous window and add next element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum