def dfs(graph, start, target):
    stack = [(start, [])]

    while stack:
        current_node, path = stack.pop()

        if current_node == target:
            return path + [current_node]

        for neighbor in graph[current_node]:
            if neighbor not in path:
                stack.append((neighbor, path + [current_node]))

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
output = dfs(data, "A", "G")
print(output)
