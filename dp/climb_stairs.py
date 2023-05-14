"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(n):
    dp = [0 for _ in range(n)]

    for step in range(n):
        if step == 0:
            dp[step] = 1
        elif step == 2:
            dp[step] = 2
        else:
            dp[step] = dp[step - 2] + dp[step - 1]

    return dp[-1]


"""
idea:

- use dynamic programming to keep a running total of the total number of ways to get to step n
    - there is only one way of getting to the first step (i.e. taking 1 step)
    - there are two ways of getting to step two (i.e. taking 1 step or taking 2 steps at once)
    - for step n:
        - # of ways to get to step - 1 + 1 step
        - # of ways to get to step - 2 + 2 steps

- this problem is technically the fibonnaci sequence
    - using recursion will result in a stack overflow (stack space is 2^n for generic recursion)
    - using memoization optimizes the space to O(n)
        - every fibonacci number is only calculated once so the stack is O(n) where `n` is the number of steps

time complexity:

- only need to iterate `n` times where `n` is the number of steps
- thus, the time complexity is O(n)

space complexity:

- O(n) to create a dp array
    - where `n` is the number of total steps
- this can be optimized to O(1) by only keeping track of n - 1 and n - 2 steps
"""
