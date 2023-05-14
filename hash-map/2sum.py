"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
    frequency_map = {}

    for i in range(len(nums)):
        if target - nums[i] in frequency_map:
            return [i, frequency_map[target - nums[i]]]
        else:
            frequency_map[nums[i]] = i

    return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))     # expected [0,1]
    print(twoSum([3, 2, 4], 6))          # expected [1,2]
    print(twoSum([3, 3], 6))             # expected [0,1]

"""
idea:

- loop through array
- calculate the complement (i.e. target - current number)
- if we've seen this complement before, we have a match
  - return the match
- if we haven't seen the complement before, store this number in the hash map
  - it is okay to completely overwrite the value in the hash map because there is only one solution by the constraint
  - idea is that if we encounter this number's complement, we have a match and can return

runtime complexity:

- looping through array is O(n)
- hash map lookup is O(1) amortized
- total runtime: O(n)
"""
