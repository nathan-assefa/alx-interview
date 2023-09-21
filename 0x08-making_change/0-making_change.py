def makeChange(coins, total):
    if total < 0:
        return -1

    # Initialize a table to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calculate the minimum number of coins for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
