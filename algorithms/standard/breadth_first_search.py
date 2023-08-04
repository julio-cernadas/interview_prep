def bfs(graph, start, target):
    queue = [(start, [])]
    visited = set()

    while queue:
        current_node, path = queue.pop(0)

        if current_node == target:
            return path + [current_node]

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [current_node]))

    return None


data = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
    "G": ["C"],
}
output = bfs(data, "A", "G")
print(output)
