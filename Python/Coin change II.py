def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in coins:
        j = i
        while j <= amount:
            dp[j] += dp[j - i]
            j += 1
    return dp[amount]

print(change(5, [1, 2, 5]))