"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


def contains_duplicate(nums):
    frequency_map = {}

    for num in nums:
        try:
            frequency_map[num] += 1
        except:
            frequency_map[num] = 1

    return True if any(x >= 2 for x in list(frequency_map.values())) else False


def contains_duplicate_set(nums):
    frequency_set = set()

    for num in nums:
        if num in frequency_set:
            return True
        else:
            frequency_set.add(num)

    return False


"""
hash map:

- keep a hash map of frequencies
- return True if any of the values is >= 2
- time complexity:
    - O(n) to traverse through nums
    - O(n) to check for duplicate in values
    - O(n) total
- space complexity:
    - in the worst case, there are no duplicates and the space is O(n)

set:

- keep set of values
- traverse through nums
    - if this number is in the set, return True
    - if this number is not in the set, add it
- return False if we have reached the end of nums
- time complexity:
    - O(n) to traverse through nums
    - in python, sets are implemented as hash maps so add and lookup operations are O(1)
    - O(n) total
- space complexity:
    - same as hash map O(n)

optimize space:

- if we really care about O(n) space we can save space by performing operations in place
- first sort the array
    - time complexity: O(n * log(n)) by lower bound of comparison-based sort algorithms
- iterate through the array
    - if we find 2 numbers next to each other that are the same, return True
    - if we reach the end of the array, return False
"""
