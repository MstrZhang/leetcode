from node import Node
from collections import deque


def clone_graph_bfs(node):
    if not node:
        return node

    # initialize the queue and the hash map with the first node
    queue, clones = deque([node]), {node.val: Node(node.val, [])}

    while queue:
        current = queue.popleft()
        current_clone = clones[current.val]

        for neighbor in current.neighbors:
            # if we have never seen this node before
            if neighbor.val not in clones:
                # add it to the hash map (i.e. the seen list)
                clones[neighbor.val] = Node(neighbor.val, [])
                # append the node to the queue to be processed
                queue.append(neighbor)

            # otherwise, append the previously-made clone to the current clone's neighbors
            current_clone.neighbors.append(clones[neighbor.val])

    return clones[node.val]


def clone_graph_dfs(node):
    old_to_new = {}

    def clone_node(node):
        # if we have seen this node before, return the previously made clone
        if node in old_to_new:
            return old_to_new[node]

        # otherwise, clone the current node and add it to the seen list
        clone = Node(node.val)
        old_to_new[node] = clone

        # loop through the current node's neighbours
        for neighbor in node.neighbors:
            # recursively call clone_node on all of its neighbours
            clone.neighbors.append(clone_node(neighbor))
        return clone

    return clone_node(node) if node else None


"""
bfs:

- use a queue to keep track of the current "level"
- start the queue with the first node
- on each iteration:
    - pop the first node
    - add the node to the "seen" hash map
    - for every neighbor it has:
        - if the neighbor has never been seen before:
            - add it to the hash map
            - append this neighbor to the queue to be processed in a future iteration
        - if the neighbor has been seen before:
            - append the previously-made clone to the current clone's neighbours
- return the clones on the first node

time complexity:

- bfs needs to iterate through every node in the graph once and each edge twice
    - thus, the total time complexity is O(V + E) where
    - `V` and `E` are vertices (nodes) and edges respectively

space complexity:

- the hash map has to keep track of every node in the graph
    - total space: O(V) where `V` is number of vertices (nodes)

---

dfs:

- use a hash map to keep track of "seen" nodes
- starting on the first node:
    - if we have seen this node before:
        - return the clone reference we have in the hash map
    - if we haven't seen this node before:
        - clone the current node and add it to the hash map
        - loop through the neighbours (on the original node)
        - call clone() on all of its neighbours and add them to the neighbours list of the clone
        - return the clone
- recursively call clone() on the first node

time complexity:

- same reasoning as bfs, dfs also takes O(V + E) time

space complexity:

- same as bfs:
    - the hash map will contain all nodes so it will be O(V)

"""
