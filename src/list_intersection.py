def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists, returning unique common elements.

    Args:
        list1 (list): First input list
        list2 (list): Second input list

    Returns:
        list: A list of unique elements common to both input lists

    Raises:
        TypeError: If either input is not a list
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")
    
    # Use set intersection for efficient unique common elements
    # Convert to set first to handle mixed types and ensure efficiency
    common_elements = set(list1) & set(list2)
    
    # Attempt to sort if possible, otherwise return unsorted
    try:
        return sorted(common_elements)
    except TypeError:
        return list(common_elements)