"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""


def middle_node(head):
    nodes = []

    while head is not None:
        nodes.append(head)
        head = head.next

    return nodes[len(nodes) // 2]


def middle_node_pointers(head):
    slow, fast = head, head

    while fast:
        fast = fast.next

        if fast:
            fast = fast.next
        else:
            # fast has reached the end of the list
            # slow is at the midpoint
            break

        slow = slow.next

    return slow


"""
idea:

naive approach:

- traverse through the list and store every node in an array
- return the node at the midpoint of the array
- time complexity:
    - O(n) to pass through the list
    - O(n) to calculate the midpoint of the array
    - overall O(n)
- space complexity:
    - O(n) to store the secondary array

2 pointers:

- use a slow and a fast pointer
    - the slow pointer moves 1 node at a time
    - the fast pointer moves 2 nodes at a time (double the speed)
- logically, when the fast pointer reaches the end, the slow pointer must have moved half the distance
    - this must be the midpoint of the list
- time complexity:
    - only one pass O(n)
- space complexity:
    - everything is done in place so the space complexity is O(1)
"""
