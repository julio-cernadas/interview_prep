# BIG O:
# O(v + e)

# EXPLANATION:
# Uses a DFS approach to check if you can finish all the given courses with their prerequisites without encountering
# any cycles. It creates a graph where courses are nodes and prerequisites are edges, then traverses through the graph
# using DFS, marking courses as visited and checking for cycles. If a cycle is detected, it means you cannot finish
# all the courses.


def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for crs, prereq in prerequisites:
        graph[crs].append(prereq)

    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == -1:
            return True

        visited[course] = 1
        for pr in graph[course]:
            if not dfs(pr):
                return False
        visited[course] = -1
        return True

    visited = [0] * num_courses
    for i in range(num_courses):
        if not dfs(i):
            return False

    return True


target_num = 2
data = [[1, 0]]
output = can_finish(target_num, data)
print(output)
