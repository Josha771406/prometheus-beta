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
    return sorted(list(set(list1) & set(list2)))