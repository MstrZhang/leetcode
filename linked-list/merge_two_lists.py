"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


def merge_two_lists(list1, list2):
    # case 1: both lists are empty
    if not list1 and not list2:
        # can return either one it doesn't matter
        return list1
    # case 2: one list is empty
    elif not list1 and list2 or not list2 and list1:
        return list1 if list1 else list2
    # case 3: both lists are non-empty
    else:
        # if list1's head is lower, use it as the new next (rest becomes new list2)
        if list1.val < list2.val:
            return ListNode(list1.val, merge_two_lists(list1.next, list2))
        # if list2's head is lower, use it as the new next (rest becomes new list1)
        elif list2.val < list1.val:
            return ListNode(list2.val, merge_two_lists(list2.next, list1))
        # if both are the same size, it doesn't matter (rest becomes new list2)
        else:
            return ListNode(list1.val, merge_two_lists(list1.next, list2))


"""
idea:

- solve using recursion
- base cases:
    1. both lists are empty
        - return an empty list
    2. only one list is empty
        - return the non-empty list
    3. both lists are non-empty
        - if list1 is lower, use it as the new head and recurse on the remaining lists
        - if list2 is lower, use it as the new head and recurse on the remaining lists
        - if both are equal, choose one or the other (it doesn't matter)
            - this case can be consolidated with the other cases

runtime complexity:

- on average, this will short-circuit on the shorter list
    - average complexity is O(m) where `m` is length of shorter list
- worst case = both lists are exactly the same
    - we need to recurse the full extent of both lists
    - runtime complexity is O(n + m) where `n` and `m` are the lengths of each list
        - simplifies to O(n)
"""
