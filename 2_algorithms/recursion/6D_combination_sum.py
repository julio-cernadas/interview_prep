def combination_sum(nums, k):
    def dfs(start, path):
        # BASE CASE
        if sum(path) == k:
            result.append(path)
            return

        # RECURSIVE CASE
        for i in range(start, len(nums)):
            curr_sum = sum(path) + nums[i]
            if curr_sum > k:
                continue

            dfs(i + 1, path + [nums[i]])

    result = []
    dfs(0, [])
    return result


data = [2, 3, 5, 7, 8]
target = 10
print(combination_sum(data, target))
