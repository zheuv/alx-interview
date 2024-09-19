#!/usr/bin/python3
""" Module doc """


def makeChange(coins, total):
    """ function doc """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make a total of 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
