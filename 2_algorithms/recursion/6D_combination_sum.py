def combination_sum(nums, k):
    def dfs(start, target, path):
        # BASE CASE
        if target == 0:
            result.append(path)
            return

        # RECURSIVE CASE
        for i in range(start, len(nums)):
            if nums[i] <= target:
                dfs(i + 1, target - nums[i], path + [nums[i]])

    result = []
    dfs(0, k, [])
    return result


data = [2, 3, 5, 7, 8]
output = combination_sum(data, 10)
print(output)
