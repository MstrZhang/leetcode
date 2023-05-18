"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


def level_order(root):
    result = []
    # more correct to use python collections.deque() since list.pop() is O(n)
    queue = [root] if root else []

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.pop(0)

            if node:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        if level:
            result.append(level)

    return result


"""
idea:

- perform a BFS and use a queue to keep track of each level
- start by adding the root node to the queue
- while the queue has items:
    - get the current length of the queue
    - loop through the queue
        - pop the first node from the queue
        - if the node is non-null, add it's value to the current sublevel list
        - add its children to the queue
    - if the sublevel list is non-empty, add it to the result
- return the result

time complexity:

- every node enters the queue once so the overall time complexity is O(n)

space complexity:

- in the worst case, the queue contains every node in the tree so the worst case is O(n)
    - the worst case, the queue has 1 node and that node is the entire tree
    - at any other given point, a given sub-level could have up to n/2 nodes which is still O(n)
"""
