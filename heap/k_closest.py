import heapq

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""


def k_closest(points, k):
    heap = []

    for (x, y) in points:
        # python heapq is implemented as a min heap
        # we want a max heap so when we pop we remove the largest value
        # also sqrt is not necessary since it doesn't affect the ratio between distances
        distance = -(x ** 2 + y ** 2)

        if len(heap) == k:
            heapq.heappushpop(heap, (distance, x, y))
        else:
            heapq.heappush(heap, (distance, x, y))

    return [[x, y] for (_, x, y) in heap]


"""
idea:

- maintain a heap to store the points
- for each item:
    - if inserting an element makes the heap size larger than k, immediately pop
    - otherwise, just push the element to the heap

time complexity:

- inserting an item into the heap takes O(log(k)) time
    - we do this n times where `n` is the number of points
    - total: O(n * log(k))

space complexity:

- O(k) since the heap is defined to be at most size `k`

why does this improve the runtime?

- the naive solution calculates all the distances, sorts it, and returns the result
    - in the worst case, this is O(n * log(n)) where `n` is the number of points
- the heap solution has the same runtime complexity if k = n
    - however, it doesn't scale based on `n` instead scaling based on `k`
    - in instances where k < n the heap solution outperforms
        - this is advantageous in streaming data situations where we don't know how many total `n` there are
        - we can calculate min `k` with just the current amount of data
"""
