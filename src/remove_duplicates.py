def remove_duplicates(arr):
    """
    Remove duplicate values from an array while preserving the original order.
    
    Args:
        arr (list): Input list that may contain duplicate values
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence
    
    Raises:
        TypeError: If the input is not a list
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1])
        [1, 2, 3, 4]
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen values while maintaining order
    seen = set()
    result = []
    
    for item in arr:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result