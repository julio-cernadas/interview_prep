# BIG O:
# O(v * e)

# EXPLANATION:
# This code simulates the process of oranges rotting in a matrix and calculates the time it takes for all fresh oranges
# to become rotten. It utilizes a queue-based BFS approach to track and process the rottening of oranges while keeping
# track of the time taken.


def oranges_rotting(matrix):
    queue = []
    time_cnt, fresh_cnt = 0, 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                fresh_cnt += 1
            if matrix[row][col] == 2:
                queue.append((row, col))

    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue and fresh_cnt > 0:
        for i in range(len(queue)):
            row, col = queue.pop(0)
            for n_row, n_col in neighbors:
                n_row += row
                n_col += col

                is_out_of_bound = n_row < 0 or n_row >= len(matrix) or n_col < 0 or n_col >= len(matrix[0])
                if is_out_of_bound or matrix[n_row][n_col] != 1:
                    continue

                matrix[n_row][n_col] = 2
                queue.append((n_row, n_col))
                fresh_cnt -= 1
        time_cnt += 1

    if fresh_cnt > 0:
        return -1
    return time_cnt


data = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]
output = oranges_rotting(data)
print(output)
