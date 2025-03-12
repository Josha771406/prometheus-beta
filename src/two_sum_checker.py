def check_two_sum(nums, target):
    """
    Check if any two unique numbers in the input array sum to the target.

    Args:
        nums (list): A list of unique integers to check.
        target (int): The target sum to find.

    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise.

    Raises:
        TypeError: If nums is not a list or target is not an integer.
        ValueError: If the input list contains duplicates.
    """
    # Type checking
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check for duplicates
    if len(nums) != len(set(nums)):
        raise ValueError("Input list must contain unique integers")
    
    # Edge case: empty list or list with only one element
    if len(nums) < 2:
        return False
    
    # Use a set for O(n) time complexity
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False