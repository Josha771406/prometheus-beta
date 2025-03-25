def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers in ascending order.
    
    Returns:
        list: A list of missing numbers between the smallest and largest numbers in the input array.
    
    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input array is not sorted.
    """
    # Validate input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Check if array is sorted
    if arr != sorted(arr):
        raise ValueError("Input array must be sorted in ascending order")
    
    # If array has only one element, return an empty list
    if len(arr) == 1:
        return []
    
    # Find the missing numbers
    missing_numbers = []
    for i in range(arr[0], arr[-1]):
        if i not in arr:
            missing_numbers.append(i)
    
    return missing_numbers