# BIG O:
# O(n + k * log n)

# EXPLANATION:
# Uses a min-heap to efficiently find the k closest points to the origin from a list of points, based on their
# squared Euclidean distances.


import heapq


def k_closest_points(points, k):
    min_heap = []
    for x, y in points:
        dist = (x**2) + (y**2)
        min_heap.append((dist, x, y))
    heapq.heapify(min_heap)

    res = []
    for _ in range(k):
        dist, x, y = heapq.heappop(min_heap)
        res.append([x, y])

    return res


matrix = [[1, 3], [-2, 2]]
k_points = 1
output = k_closest_points(matrix, k_points)
print(output)
