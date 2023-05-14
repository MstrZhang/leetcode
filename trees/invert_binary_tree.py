"""
Given the root of a binary tree, invert the tree, and return its root.

(an inverted binary tree is a horizontal reflection about it's root)
"""


def invert_tree(root):
    # case 1: tree is empty or has only one node
    if not root or not root.left and not root.right:
        return root
    # case 2: tree has more than one level
    else:
        # flip the nodes and invert the children
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root


def invert_tree2(root):
    # cleaner
    if root:
        root.left, root.right = invert_tree2(
            root.right), invert_tree2(root.left)
        return root


"""
idea:

- if the tree is empty or has only one node
  - return the tree
- otherwise:
  - we need to flip every subtree by it's root
  - flip the left and right subtrees
  - recurse on all the child roots

time complexity:
  - we traverse through every node once so time complexity is O(n)
    - `n` is number of nodes

space complexity:
  - stack keeps track of the entire tree so space complexity is O(n)
    - `n` is number of nodes
"""
