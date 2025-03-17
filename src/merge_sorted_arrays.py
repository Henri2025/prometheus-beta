def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.

    Args:
        arr1 (list): First sorted input array
        arr2 (list): Second sorted input array

    Returns:
        list: A new sorted array containing all elements from arr1 and arr2

    Raises:
        TypeError: If input is not a list
        ValueError: If input arrays are not sorted
    """
    # Validate input types
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Inputs must be lists")
    
    # Validate that input arrays are sorted
    if not (is_sorted(arr1) and is_sorted(arr2)):
        raise ValueError("Input arrays must be sorted")
    
    # Merge arrays
    merged = []
    i, j = 0, 0
    
    # Compare and add elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1, if any
    merged.extend(arr1[i:])
    
    # Add remaining elements from arr2, if any
    merged.extend(arr2[j:])
    
    return merged

def is_sorted(arr):
    """
    Check if an array is sorted in non-decreasing order.

    Args:
        arr (list): Input array to check

    Returns:
        bool: True if array is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) if arr else True