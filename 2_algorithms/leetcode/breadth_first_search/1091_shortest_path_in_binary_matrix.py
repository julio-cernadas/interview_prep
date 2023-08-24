# BIG O:
# O(n)

# EXPLANATION:
# Utilizes BFS to calculate the shortest path from the top-left corner to the bottom-right corner of a binary matrix.
# It efficiently explores neighboring cells and tracks visited cells to find the optimal path while considering
# obstacles and boundaries.


def shortest_path_binary_matrix(matrix):
    if matrix[0][0] == 1 or matrix[-1][-1] == 1:
        return -1

    queue = [(0, 0, 1)]
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    while queue:
        row, col, distance = queue.pop(0)
        if (row, col) == (len(matrix) - 1, len(matrix) - 1):
            return distance

        for n_row, n_col in neighbors:
            n_row += row
            n_col += col
            is_out_of_bound = n_row < 0 or n_row >= len(matrix) or n_col < 0 or n_col >= len(matrix[0])
            if is_out_of_bound or matrix[n_row][n_col] != 0:
                continue

            matrix[n_row][n_col] = -1
            queue.append((n_row, n_col, distance + 1))

    return -1


data = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
output = shortest_path_binary_matrix(data)
print(output)
