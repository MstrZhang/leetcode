"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def three_sum(nums):
    nums.sort()
    result = []

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        else:
            # 2sum_ii implementation
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])

                    # it doesn't matter which pointer we increment since it will re-enter the loop
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        # increment until a new value is seen or the pointers pass one another
                        left += 1

    return result


"""
idea:

consider any given triplet as a permutation of 3 numbers a + b + c

___ + ___ + ___ = 0
 a     b     c

the duplicate problem arises because we don't know if a given triplet we've found has been found sometime in the past

to combat this, we can sort the array beforehand and follow the given logic:

- traverse through the sorted array
- choose the current number as the `a` option:
    - if this option is the same as the one before, we have seen it already so skip it
    - if this option is different from the one before:
        - consider only the elements after this one (we have already considered all the ones before it)
        - the problem can now be solved as either 2sum or 2sum_ii (since the array is sorted)

time complexity:

- it costs O(n * log(n)) to sort an array
- it costs O(n) to traverse through the array to pick the `a` value
    - for every `n` in nums, it costs O(n) to perform 2sum (or 2sum_ii)
- total complexity: O(n * log(n)) + O(n * n) => O(n * log(n)) + O(n^2) => O(n^2)

space complexity:

- depends on the sorting algorithm:
    - in some languages is O(1) and others is O(n)
    - in python this is worst case O(n) (best case is O(1))
- to perform 2sum:
    - classic 2sum costs O(n) for the hash map implementation
    - 2sum_ii costs O(1) for the two pointer implementation
- total:
    - either O(1) if both sorting and 2sum cost O(1)
    - O(n) if one of or both of sorting and 2sum cost O(n)
"""
