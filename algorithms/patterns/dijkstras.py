def dijkstra(graph, start):
    infinity = float("inf")
    distances = {node: infinity for node in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda n: distances[n])
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


data = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "D": 2, "E": 7},
    "C": {"A": 4, "F": 5},
    "D": {"B": 2},
    "E": {"B": 7},
    "F": {"C": 5},
}

output = dijkstra(data, "F")
print(output)
