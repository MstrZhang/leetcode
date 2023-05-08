"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_profit(prices):
    dp = [0 for _ in range(len(prices))]
    min_price = prices[0]

    for i in range(len(prices)):
        dp[i] = max(dp[i - 1], prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return dp[-1]


"""
idea:

this problem can be solved using dynamic programming

- on any given day, we can choose to sell (generating a profit)
- on any given day, we can choose to buy (creating the initial buy price)

steps:

- generate the dp array
- assume the first price is the lowest (this is the earliest we can buy)
- every day:
  - the maximum profit we can make at this point is either selling today with the min price or the previous highest profit
  - if today's price is lower than the lowest min price, reset the min price
    - the initial case is short-circuited because the [i - 1] value is 0

time complexity:

- only needs to traverse the prices array once so O(n) total time complexity
- needs O(n) space complexity to store dp array
"""

if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
