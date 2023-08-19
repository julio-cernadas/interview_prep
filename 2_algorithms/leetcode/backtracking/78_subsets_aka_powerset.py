def subsets(nums):
    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    result = []
    backtrack(0, [])
    return result


data = [1, 2, 3]
output = subsets(data)
print(output)
