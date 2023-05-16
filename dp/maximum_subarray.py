"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


def max_subarray(nums):
    dp = [0 for _ in nums]

    for i, num in enumerate(nums):
        dp[i] = max(num, num + dp[i - 1])

    return max(dp)


"""
idea:

dynamic programming:

- initialize a dp array
    - each element of the dp array represents the maximum subarray sum up to this point
    - i.e. the maximum subarray A[0:i]
- iterate through nums
    - two options:
        - the greatest subarray starts here using this number
        - the greatest subarray is this number plus the greatest subarray up to this point
    - populate dp array
- return the max from the dp array
    - important to see what the dp array represents
        - in this case the end of the dp array does not necessarily represent the max subarray
        - the max subarray could be in the middle of the array
- time complexity:
    - O(n) to traverse through the nums
- space complexity:
    - O(n) to create the dp array
    - to save space, this can be done with a variable instead which would be O(1)
"""
