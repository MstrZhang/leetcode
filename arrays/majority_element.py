"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


def majority_element(nums):
    counter = 0
    majority = None

    for element in nums:
        if counter == 0:
            majority = element
            counter = 1
        elif element == majority:
            counter += 1
        else:
            counter -= 1

    return majority


"""
idea:

naive solution:

- use a hash map to count frequencies
- return the character that has the highest frequency
- time complexity:
    - O(n) to populate hash map
    - O(n) to check for majority element in hash map
    - total time: O(n)
- space complexity:
    - hash map is O(n) where `n` is the number of elements in the array

moore's voting algorithm

- initialize a counter to 0 and a variable to track the majority element
- iterate through nums:
    - if the counter is 0, set the current value to be the new majority
    - if the element is the same as the majority element, increase the counter
    - if the element is not the same as the majority element, decrease the counter
- return the majority
- time complexity:
    - O(n) only does a single pass through the array
- space complexity:
    - O(1) only a static counter and a memory variable for the majority is required

---

voting algorithm correctness:

the proof for this is quite verbose; i find it hard to believe you will have to prove this during an interview

the boyer-moore algorithm only works if there is a guaranteed majority element

at any given iteration `k`, if counter reaches 0 there are two cases:

[   k iterations   ][     n - k iterations     ]

1. we have the majority element
    - by definition, we must have consumed k / 2 elements that have the majority element
    - the remaining subsequence of n - k elements must have the majority too (we can use induction with the same logic)
2. we do not have the majority element
    - either there were at least k / 2 elements that cancelled out the candidate from being the majority element
    - or k / 2 elements are a part of the "actual majority" and the remaining elements have the "actual majority"
        - so we can kind of "ignore" the first k elements of the array
    - thus, the remaining n - k elements must contain the majority element
        - n - k must be non-zero since we have the assumption that there must be a majority element
        - this subsequence must contain the majority element by the pigeonhole principle
            - this subsequence must have the majority element if the first k elements cancelled everything out
            - if this sequence doesn't contain a majority element we have a contradiction (i.e. there is no majority element)
    - we can use induction on the remaining n - k elements to get the majority
"""
