# BIG O:
# O(v * e)

# EXPLANATION:
# This code effectively uses BFS to compute the shortest distances from each cell to the nearest zero cell in the given
# matrix. It initializes a queue with zero cells, explores neighboring cells, and updates distances accordingly,
# ultimately producing the desired result.


def update_matrix(matrix):
    queue = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                queue.append((row, col))
            else:
                matrix[row][col] = -1

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        row, col = queue.pop(0)
        for n_row, n_col in neighbors:
            n_row += row
            n_col += col

            is_out_of_bound = n_row < 0 or n_row >= len(matrix) or n_col < 0 or n_col >= len(matrix[0])
            if is_out_of_bound or matrix[n_row][n_col] != -1:
                continue

            matrix[n_row][n_col] = matrix[row][col] + 1
            queue.append((n_row, n_col))

    return matrix


data = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
output = update_matrix(data)
print(output)
