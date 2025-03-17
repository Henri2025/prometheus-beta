def rotate_array_right(arr, n):
    """
    Rotate an array to the right by a specified number of positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate to the right
    
    Returns:
        list: A new array rotated to the right
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(n, int):
        raise TypeError("Rotation positions must be an integer")
    
    if n < 0:
        raise ValueError("Rotation positions cannot be negative")
    
    # Handle empty array or zero rotation
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation to array length to handle large rotations
    n = n % len(arr) if arr else 0
    
    # Perform rotation
    return arr[-n:] + arr[:-n]