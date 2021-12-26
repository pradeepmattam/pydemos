import sys


def mincoins(coins, amount):
    dp = [sys.maxsize for i in range(0, amount+1)]
    dp[0] = 0

    for i in range(1, amount+1):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], 1 + dp[i-j])

    return dp[amount] if dp[amount] != sys.maxsize else -1


coin_list = [9, 6, 5, 1]
m = len(coin_list)
V = 30
print("for given amount {} and coin_list {} "
      "Minimum coins required is {}".format(V, coin_list, mincoins(coin_list, V)))
