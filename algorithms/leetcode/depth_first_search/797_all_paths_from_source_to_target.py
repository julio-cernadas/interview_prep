def all_paths_source_target(graph):
    def dfs(node, path):
        if node == target:
            result.append(path)
            return
        for neighbor in graph[node]:
            dfs(neighbor, path + [neighbor])

    target = len(graph) - 1
    result = []
    dfs(0, [0])
    return result


data = [[1, 2], [3], [3], []]
output = all_paths_source_target(data)
print(output)
