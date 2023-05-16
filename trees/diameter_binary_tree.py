"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


class Solution:
    def __init__(self):
        # store the current max diameter
        self.diameter = 0

    def depth(self, root):
        # calculate the depth of both subtrees
        left = self.depth(root.left) if root.left else 0
        right = self.depth(root.right) if root.right else 0

        # check if the diameter around this node is the max; update if it is
        self.diameter = max(left + right, self.diameter)

        # return the depth of the subtree
        return 1 + max(left, right)

    def diameter_of_binary_tree(self, root):
        self.depth(root)
        return self.diameter


"""
idea:

naively, the diameter of a binary tree is the height of the left subtree + the height of the right subtree
this however is not true because the diameter does not necessarily have to include the root (i.e. the diameter can be a subtree)

consider the following binary tree:

                   1
                  /  \
                 2    3
                    /   \
                   4     5
                  /       \
                 6         7
                /           \
               8             9

using the root, the diameter would be 5 but the subtree on 3 has a diameter of 6

instead of assuming the diameter is at the root, we need to calculate the diameter at every node and take the max

---

recursion:

- at every node:
    - calculate the depth of the left subtree
    - calculate the depth of the right subtree
    - the diameter is the sum of the left and right subtree
        - if the diameter around this node is greater than the max, update the max
    - return 1 + the depth of the greater of the two subtrees
        - this is the height of the given subtree

time complexity:

- in the worst case, this algorithm needs to traverse through every node once
- thus, the time complexity is O(n)

space complexity:

- the worst case is a binary tree that is similar to a linked list (i.e. one really long string)
    - in this case, the worst case space complexity would be O(n) as every node would have to be kept in the stack
- in an average case of a balanced binary tree, the call stack is cleared after the height of each subtree is calculated
    - e.g. once one subtree has its value return, the call stack is cleared
    - thus, the call stack will only ever have at most O(h) nodes in memory where `h` is the height of the tree
    - average case: O(h)

note:

- this question is similar to max path sum which is considered a leetcode hard problem (this is leetcode easy)
    - the difference is that max path sum requires you to calculate the sum of the path as well
"""
