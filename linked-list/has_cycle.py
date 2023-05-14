"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


def has_cycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


"""
two-pointers:

- initialize 2 pointers
    - fast and slow pointer
    - slow pointer moves 1 node at a time, fast pointer moves 2 nodes at a time
- move the pointers
    - if the one of the pointers ever hits the end there is no cycle
    - if the fast pointer and the slow pointer meet, there is a cycle

time complexity:

- any given list will have `n` nodes
- if a list has a cycle, the cycle will have `m` nodes where m <= n
    - the slow and fast pointers will meet one another at some point in the cycle at some multiple of `m` iterations
    - once the slow pointer gets into the cycle:
        - the distance between the fast pointer and the slow pointer decreases by 1 each iteration
        - the distance the fast pointer needs to catch up with the slow pointer is at most the length of the cycle `m` which will be within n - m steps
        - thus, the upper bound time complexity is O(n - m) => O(n)

space complexity:

- since everything is done in place, the space complexity is O(1)

why does this work?

you can reason that this will work through intuition:

- imagine that you are running a race around a circular track
    - your opponent runs at double your speed
    - you run infinite laps
- because your opponent runs faster than you, you expect at some point (i.e. at some rotation) that they lap you
    - the point at which they lap you is the "meeting point"
    - the "meeting point" must exist because the track is a circle (i.e. a linked list cycle)
        - thus, there must be some point where the two pointers meet one another

---

hash map:

- traverse through the linked list
- if we haven't seen this particular node before, add it to the dictionary
- if we reach the end of the list, return False
- if we've seen this node before, return True

time complexity:

- O(n) to traverse through the linked list
    - O(1) for hash map operations

space complexity:

- in the worst case, we traverse through every node in the list so the maximum space for the array is O(n)
"""
