def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: The longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        [10, 22, 33, 50, 60, 80]
        >>> find_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])
        [7]
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Length of the input array
    n = len(arr)
    
    # Store the length of the longest increasing subsequence ending at each index
    dp = [1] * n
    
    # Store the previous index in the longest subsequence to reconstruct the sequence
    prev_index = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev_index[i] = j
    
    # Find the index of the maximum length subsequence
    max_length_index = dp.index(max(dp))
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev_index[current]
    
    return subsequence