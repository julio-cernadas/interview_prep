from collections import defaultdict


def valid_path(n, edges, start, end):
    # Step 1: Create an adjacency list to represent the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Perform a depth-first search (DFS) to find a path from 'start' to 'end'
    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    visited = set()
    return dfs(start)


vertices = 3
data = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
output = valid_path(vertices, data, source, destination)
print(output)
