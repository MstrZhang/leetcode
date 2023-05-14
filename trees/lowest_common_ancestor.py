"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


def lowest_common_ancestor(root, p, q):
    current_val = root.val

    # case 1: p and q are < root; recurse through left subtree
    if p.val < current_val and q.val < current_val:
        return lowest_common_ancestor(root.left, p, q)
    # case 2: p and q are > root; recurse through right subtree
    elif p.val > current_val and q.val > current_val:
        return lowest_common_ancestor(root.right, p, q)
    # case 3: root is LCA and p and q are ancestors of root
    else:
        return root


"""
idea:

- BSTs work in the following way:
    - all numbers less than the root are in the left subtree
    - all numbers greater than the root are in the right subtree
    - recurse this logic through all subtrees
- given p, q, the LCA must be:
    - in the left subtree if p and q < root
    - in the right sutree if p and q > root
    - the root itself otherwise
        - this is due to the constraints given in the question (p != q, p and q exist in the BST)
        - if the above two cases are not true, the only other case is that the root itself is the LCA

recursion:

- perform a BFS
    - check left subtree if p and q < root
    - check right subtree if p and q > root
    - return root otherwise

time complexity:

- O(n) where `n` is the number of nodes in the tree
    - every node needs to be checked in the worst case
    - in a large tree, one of the subtrees (i.e. half the tree) is checked resulting in O(1/2 * n) => O(n)

space complexity:

- O(n) where `n` is the number of nodes in the tree
    - recursion stack needs to keep track of every node in the tree in the worst case (similar logic to time complexity)
"""
