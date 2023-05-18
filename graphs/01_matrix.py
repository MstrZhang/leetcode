import math

"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""


def update_matrix(mat):
    m, n = len(mat), len(mat[0])
    queue = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                # number is arbitrary
                # any number / character to indicate this cell hasn't been processed yet
                mat[i][j] = -1

    while queue:
        row, col = queue.pop(0)
        for d1, d2 in directions:
            new_row, new_col = row + d1, col + d2

            if new_row < 0 or new_row == m or new_col < 0 or new_col == n or mat[new_row][new_col] != -1:
                continue

            mat[new_row][new_col] = mat[row][col] + 1
            # add this value to the end of the queue
            queue.append((new_row, new_col))

    return mat


def update_matrix_dp(mat):
    m, n = len(mat), len(mat[0])

    for row in range(m):
        for col in range(n):
            if mat[row][col] > 0:
                top = mat[row - 1][col] if row > 0 else math.inf
                left = mat[row][col - 1] if col > 0 else math.inf
                mat[row][col] = min(top, left) + 1

    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if mat[row][col] > 0:
                bottom = mat[row + 1][col] if row < m - 1 else math.inf
                right = mat[row][col + 1] if col < n - 1 else math.inf
                mat[row][col] = min(mat[row][col], bottom + 1, right + 1)

    return mat


"""
idea:

bfs:

- add all the 0s to a queue and process them first
- process all the neighbours of each 0
    - if the neighbour has been processed (i.e. is not -1) then skip it
    - if the neighbour isn't processed
        - set the neighbour to be the current distance + 1 (cells that are 0 are defined to have distance 0)
        - add this new neighbour to the end of the queue (in case it needs to be processed again)
- time complexity:
    - O(m * n) to iterate through the matrix
    - O(n) worst case to sort through the queue
        - total: O(m * n)
- space complexity:
    - in the worst case, the entire matrix is added to the queue
        - total: O(m * n)

---

dynamic programming:

- idea behind dynamic programming is to reuse previously calculated values through memoization
- the issue is that we have 4 directions to take into account so we run into the issue of overcalculating values
    - we can cross the same path multiple times
    - instead we only count directions one at a time to not overcount
- instead of processing 0s, process 1s and their distance from 0s

process:

- pass 1:
    - start from the top left
    - only consider values on the top and the left of the current cell
    - if the cell is not 0:
        - set the current cell to be the min of the top and left cell + 1
- pass 2:
    - start from the bottom right
    - only consider values on the bottom and right of the current cell
    - if the cell is not 0:
        - set the current cell to be the min of the current cell, the bottom cell + 1, or the right cell + 1

- time complexity:
    - O(n * m) to traverse through the matrix
        - this is done twice
- space complexity:
    - O(1) since everything is done in place
"""
