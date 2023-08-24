# EXPLANATION:
# This code effectively uses BFS to compute the shortest distances from each cell to the nearest zero cell in the given
# matrix. It initializes a queue with zero cells, explores neighboring cells, and updates distances accordingly,
# ultimately producing the desired result.


from collections import deque


def update_matrix(mat):
    m, n, q, visited = len(mat), len(mat[0]), deque(), set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
                visited.add((r, c))
            else:
                mat[r][c] = -1

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
                visited.add((nr, nc))

    return mat


matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
output = update_matrix(matrix)
print(output)
