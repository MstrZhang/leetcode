def fill(image, sr, sc, color, current):
    # if selected square is out of bounds, return
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
        return

    # if the current cursor is not equal to the previous color, return
    if current != image[sr][sc]:
        return

    # update the current square
    image[sr][sc] = color

    # recurse in all 4 directions
    fill(image, sr - 1, sc, color, current)
    fill(image, sr + 1, sc, color, current)
    fill(image, sr, sc - 1, color, current)
    fill(image, sr, sc + 1, color, current)


def flood_fill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image

    fill(image, sr, sc, color, image[sr][sc])
    return image


if __name__ == "__main__":
    print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

"""
idea:

- performs a depth first search on each node
    - worst case needs to traverse every node in the graph
    - goes as far as it can in one direction before recursing on neighbours / other directions

recursion:

- if the selected node is out of bounds, return
- if the selected square does not match the proper colour, return
- update the current square's color to the fill colour
- recurse in all 4 directions

time complexity:

- O(n * m) in the worst case has to traverse every node
    - `n` and `m` are the rows and columns of the graph

space complexity:

- O(n * m)
    - recursion stack will need to visit all the elements in a large matrix
    - in the worst case, the call stack will have a size of n * m
"""
