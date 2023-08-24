# BIG O:
# O(n^k)

# EXPLANATION:
# The code's backtracking approach effectively explores the space of possible combinations of candidates to find those
# that sum up to the target k. This approach is only considering candidates that can contribute to valid combinations,
# and by using recursive calls and backtracking to explore all possible paths through the combination space.


def combination_sum(candidates, k):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    backtrack(0, k, [])
    return result


data = [2, 3, 6, 7]
output = combination_sum(data, 7)
print(output)
