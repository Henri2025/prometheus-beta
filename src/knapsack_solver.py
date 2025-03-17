def knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing:
            - Maximum total value that can be achieved
            - List of indices of items selected
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not (isinstance(weights, list) and isinstance(values, list) and isinstance(capacity, int)):
        raise ValueError("Invalid input types")
    
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")
    
    if capacity < 0:
        raise ValueError("Capacity must be non-negative")
    
    # Special case: empty input or zero capacity
    if not weights or capacity == 0:
        return 0, []
    
    # Number of items
    n = len(weights)
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Current item's weight and value
            current_weight = weights[i-1]
            current_value = values[i-1]
            
            # If current item can be included
            if current_weight <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude current item
                    dp[i-1][w-current_weight] + current_value  # Include current item
                )
            else:
                # Can't include current item
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            # This item was selected
            selected_items.append(i-1)
            w -= weights[i-1]
    
    # Return max value and list of selected item indices (in reverse order)
    return dp[n][capacity], list(reversed(selected_items))