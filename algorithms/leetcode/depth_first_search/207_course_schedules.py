def can_finish(num_courses, prerequisites):
    # Step 1: Create a graph to represent courses and their dependencies.
    graph = {i: [] for i in range(num_courses)}
    for crs, prereq in prerequisites:
        graph[crs].append(prereq)

    # Step 2: Create a function to perform depth-first search (DFS) on the graph.
    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == -1:
            return True

        visited[course] = 1
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        visited[course] = -1
        return True

    # Step 3: Initialize a visited array to keep track of course status.
    visited = [0] * num_courses

    # Step 4: Iterate through each course and check if it's possible to complete all courses.
    for i in range(num_courses):
        if not dfs(i):
            return False

    return True


target_num = 2
data = [[1, 0]]
output = can_finish(target_num, data)
print(output)
