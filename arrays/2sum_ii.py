"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1

    while numbers[left] + numbers[right] != target:
        # case 1: sum is too big
        if numbers[left] + numbers[right] > target:
            right -= 1
        # case 2: sum is too small
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            break

    # indices are 1-indexed for some reason
    return [left + 1, right + 1]


"""
idea:

- consider the outer most numbers and move inwards
- because the list is sorted:
    - if the pair of numbers is too big, the right number can never be used as a sum to get target
    - if the pair of numbers is too small, the left number can never be used as a sum to get target
- with this logic, we can use 2 pointers to close the window to find the sum

time complexity:

- every number is considered once so the time complexity is O(n)
    - having this sorted doesn't actually impact the time complexity at all

space complexity:

- everything is done in place so the space complexity is O(1)
    - this does improve the space complexity by not having to need a hash map
"""
