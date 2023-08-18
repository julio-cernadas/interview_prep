from math import sqrt


def k_closest_points(points, k):
    res = []

    for i in range(len(points)):
        dist = sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
        res.append((i, dist))

    sorted_res = sorted(res, key=lambda x: x[1])

    k_closest = [points[i] for i, dist in sorted_res[:k]]
    return k_closest


matrix = [[1, 3], [-2, 2]]
k_points = 1
output = k_closest_points(matrix, k_points)
print(output)
