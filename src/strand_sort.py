def strand_sort(arr):
    """
    Implement the strand sort algorithm to sort a list in ascending order.
    
    Strand sort works by repeatedly extracting a sorted sublist from the input list
    and merging it with the result list.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a working copy of the input list
    working = arr.copy()
    result = []
    
    while working:
        # Extract a sorted sublist
        sublist = [working.pop(0)]
        
        # Iterate through remaining elements
        i = 0
        while i < len(working):
            # If current element is greater than the last element in sublist, 
            # add it to the sublist and remove from working
            if working[i] >= sublist[-1]:
                sublist.append(working.pop(i))
            else:
                i += 1
        
        # Merge the sublist with the result
        result = merge(result, sublist)
    
    return result

def merge(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    
    Returns:
        list: A merged sorted list
    """
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements from list1, if any
    merged.extend(list1[i:])
    
    # Add remaining elements from list2, if any
    merged.extend(list2[j:])
    
    return merged