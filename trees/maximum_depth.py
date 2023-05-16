"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


def max_depth(root):
    # base case: tree has no nodes
    if not root:
        return 0
    # recursive step
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))


"""
idea:

this is basically same as the BST height function. the depth of a tree at its node is its height

recursion:

- if there are no nodes return 0
- recurse:
    - 1 node for root
    - plus maximum of (# of nodes in left subtree / # of nodes in right subtree)

time complexity:

- O(n) since every node needs to be visited
    - `n` is the number of nodes in the tree

space complexity:

- in the worst case, the space complexity is O(n) where `n` is the number of nodes in the tree
    - e.g. the tree is like a linked list with only one subtree and every node connects to that tree
- in the average case of a balanced binary tree, the space complexity is O(h) where `h` is the height of the tree
    - the call stack refreshes after it returns a value so at most it will have nodes equal to the height of the tree
    - O(h) => O(log(n)) where `n` is the nodes in the tree
"""
