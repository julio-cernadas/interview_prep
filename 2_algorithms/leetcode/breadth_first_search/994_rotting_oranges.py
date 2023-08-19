def oranges_rotting(grid):
    queue = []
    time_cnt, fresh_cnt = 0, 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                fresh_cnt += 1
            if grid[row][col] == 2:
                queue.append([row, col])

    neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while queue and fresh_cnt > 0:
        for i in range(len(queue)):
            row, col = queue.pop(0)

            for n_row, n_col in neighbors:
                n_row += row
                n_col += col
                if n_row < 0 or n_col < 0 or n_row >= len(grid) or n_col >= len(grid[0]) or grid[n_row][n_col] != 1:
                    continue
                grid[n_row][n_col] = 2
                queue.append([n_row, n_col])
                fresh_cnt -= 1

        time_cnt += 1

    return time_cnt if fresh_cnt == 0 else -1


data = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]
output = oranges_rotting(data)
print(output)
