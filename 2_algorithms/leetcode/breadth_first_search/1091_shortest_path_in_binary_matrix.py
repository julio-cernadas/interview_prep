# EXPLANATION:
# Utilizes BFS to calculate the shortest path from the top-left corner to the bottom-right corner of a binary matrix.
# It efficiently explores neighboring cells and tracks visited cells to find the optimal path while considering
# obstacles and boundaries.


def shortest_path_binary_matrix(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    n = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    queue = [(0, 0, 1)]
    visited = {(0, 0)}

    while queue:
        row, col, distance = queue.pop(0)
        if (row, col) == (n - 1, n - 1):
            return distance
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            within_matrix = 0 <= new_row < n and 0 <= new_col < n
            if within_matrix and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))

    return -1


data = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
output = shortest_path_binary_matrix(data)
print(output)
