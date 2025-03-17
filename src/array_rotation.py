def rotate_array_right(arr, k):
    """
    Rotate an array to the right by k positions.
    
    Args:
        arr (list): The input array to be rotated
        k (int): Number of positions to rotate right
    
    Returns:
        list: A new array rotated to the right by k positions
    
    Raises:
        TypeError: If input is not a list or k is not an integer
        ValueError: If k is negative
    
    Examples:
        >>> rotate_array_right([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate_array_right([1, 2, 3], 0)
        [1, 2, 3]
    """
    # Validate inputs
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("Rotation amount must be an integer")
    
    if k < 0:
        raise ValueError("Rotation amount cannot be negative")
    
    # Handle empty or single-element arrays
    if len(arr) <= 1:
        return arr.copy()
    
    # Normalize k to be within array length
    k = k % len(arr)
    
    # Perform rotation
    return arr[-k:] + arr[:-k]