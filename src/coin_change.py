def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): Available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount, 
             or -1 if the amount cannot be made up exactly
    
    Raises:
        ValueError: If input is invalid (negative amount or empty coins list)
    """
    # Input validation
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not coins:
        raise ValueError("Coins list cannot be empty")
    
    # Special case: 0 amount requires 0 coins
    if amount == 0:
        return 0
    
    # Dynamic programming solution
    # Initialize dp array with amount+1 (impossible value)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount
    
    # Build solution bottom-up
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, or -1 if no solution found
    return dp[amount] if dp[amount] != float('inf') else -1