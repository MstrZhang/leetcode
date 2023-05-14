"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # if middle number is less than target, target is in latter half of the list
        if nums[mid] < target:
            left = mid + 1
        # if middle number is greater than target, target is in first half of the list
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


"""
idea:

- because we know the list is already sorted we can apply a binary search to cut unnecessary API calls
- consider the midpoint of the list
    - if the midpoint is good, the first bad must be in the latter half
        - cut the list to the back half
    - if the midpoint is bad, the first bad must be in the prior half
        - cut the list to the front half
    - if both pointers equal each other, we must have found the first bad
        - return result

time complexity:

- in the best case, the algorithm finds the first bad version in the very first call resulting in O(1)
- in the worst case:
    - initial length of array: n
    - first pass: n/2
    - second pass: (n / 2) / 2 = n / 2^2
    - kth pass: n / 2^k
    - after k iterations, the size of the array becomes 1:
        - n / 2^k = 1 => n = 2^k => log_2(n) = log_2(2^k) => log(n) = k * log(2) = k => k = log(n)
        - thus, the overall time complexity is O(log(n))

space complexity:

- O(1) since everything is done in place
"""
