from tree_node import TreeNode

"""
Given a binary tree, determine if it is height-balanced

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""


def is_balanced(root):
    def height(root):
        if not root:
            return 0
        else:
            return max(height(root.left), height(root.right)) + 1

    if not root:
        return True
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def is_balanced_dfs(root):
    def dfs_height(root):
        if not root:
            return 0

        left_height = dfs_height(root.left)
        right_height = dfs_height(root.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            # return some value to indicate the tree at this point is not balanced
            return -1
        return max(left_height, right_height) + 1

    return dfs_height(root) != -1


if __name__ == '__main__':
    tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tree2 = TreeNode(1, TreeNode(2, TreeNode(
        3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    tree3 = TreeNode(1, TreeNode(2), TreeNode(
        2, TreeNode(3), TreeNode(4, TreeNode(4))))
    tree4 = TreeNode(1)
    tree5 = TreeNode(1, TreeNode(2))

    print(is_balanced_dfs(tree1))
    print(is_balanced_dfs(tree2))
    print(is_balanced_dfs(tree3))
    print(is_balanced_dfs(tree4))
    print(is_balanced_dfs(tree5))

"""
idea:

use the definition of a height balanced binary tree and apply recursion to solve

recursive (top-down / bfs):

- if tree is empty, it is height balanced by definition
- otherwise:
    - calculate height of left subtree and right subtree
    - return true if abs(height(left) - height(right)) <= 1 and subtrees are height balanced
- time complexity:
    - height() access every node in the tree so its runtime is O(n) where `n` is the number of nodes in the tree
    - height() gets called `n` times for every node in the tree
        - thus, the overall time complexity is O(n^2)
- space complexity:
    - same idea as the time complexity, this will also be O(n^2)

recursive (bottom-up / dfs):

- for each node:
    - check if i am balanced?
    - if i am balanced:
        - give my height to the parent so they can check if they are balanced or not
- time complexity:
    - DFS keeps a running track of the height instead of having to recalculate it each time using all the nodes
        - every node only needs to be accessed once
        - thus, overall time complexity must be O(n) where `n` is the number of nodes
- space complexity:
    - O(n) for the same reasoning as above
        - in the worst-case (a perfectly balanced tree) every node needs to be kept in the call stack
"""
