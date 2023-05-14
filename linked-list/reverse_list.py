"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


def reverse_list(head):
    prev = None
    curr = head
    next = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head


def reverse_list_rec(head):
    if not head or not head.next:
        return head

    # original list = head -> head.next -> ... -> node
    # rest = node -> ... -> head.next -> None
    # reassign head: node -> ... -> head.next -> head -> None
    rest = reverse_list_rec(head.next)
    head.next.next = head
    head.next = None
    return rest


"""
idea:

use 3 pointers:
    - curr = current position of the pointer
    - prev = previous node (initialized to None)
    - next = next node (initialized to None)

iterative:

- until curr is None:
    - set next to the next node
    - set curr.next to the previous node
        - if this is the first node, this sets the current node to point to None as desired
        - if this is not the first node, this sets the current node to the previous node in memory
    - set prev to the current node
    - set current to the next node
- time complexity:
    - runs through every node of the list once
    - thus, time complexity is O(n) where `n` is the number of nodes in the list
- space complexity:
    - everything is done in place so time is O(1)

recursive:

- if the list has 0 or 1 nodes:
    - return the head (it is reversed by definition)
- otherwise:
    - a list is reversed if we put the head to the end and the rest of the list is reversed
    - set the rest of the list to be reverse(head.next)
    - move the head to the end of the list
    - return the result
- time complexity:
    - runs through every node of the list once
    - same time complexity O(n)
- space complexity:
    - stack needs to keep track of every node in the rest of the list (minus head)
    - thus, stack is O(n)

"""
