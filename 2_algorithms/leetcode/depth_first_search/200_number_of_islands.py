# BIG O:
# O(v * e)

# EXPLANATION:
# The provided code counts the number of islands (groups of connected '1' cells) in a given matrix using a depth-first
# search (DFS) algorithm. It iterates through each cell in the matrix and, when encountering a '1', marks the entire
# island using DFS traversal.


def num_of_islands(matrix) -> int:
    def dfs(row, col):
        is_out_of_bounds = row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0])
        if is_out_of_bounds or matrix[row][col] != "1":
            return

        matrix[row][col] = "#"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "1":
                dfs(r, c)
                count += 1
    return count


data = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
output = num_of_islands(data)
print(output)
