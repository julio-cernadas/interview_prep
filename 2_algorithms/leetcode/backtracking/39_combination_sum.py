def combination_sum(candidates, k):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

    result = []
    backtrack(0, k, [])
    return result


data = [2, 3, 6, 7]
output = combination_sum(data, 7)
print(output)
