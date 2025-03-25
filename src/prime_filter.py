def filter_primes(numbers):
    """
    Filter a list of numbers to return only prime numbers.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A list of prime numbers from the input list.
    
    Handles both positive and negative numbers:
    - Negative numbers and 1 are not considered prime
    - 2 is the smallest prime number
    """
    def is_prime(n):
        # Handle non-prime cases first
        if n < 2:
            return False
        
        # Check for divisibility up to the square root of the number
        for i in range(2, int(abs(n)**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]