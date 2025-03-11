import random

def generate_random_integer(min_value: int, max_value: int) -> int:
    """
    Generate a random integer within the given range (inclusive).

    Args:
        min_value (int): The lower bound of the range (inclusive).
        max_value (int): The upper bound of the range (inclusive).

    Returns:
        int: A random integer between min_value and max_value.

    Raises:
        ValueError: If min_value is greater than max_value.
    """
    # Validate input range
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise TypeError("Both min_value and max_value must be integers")
    
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    
    # Generate and return random integer using random.randint
    return random.randint(min_value, max_value)