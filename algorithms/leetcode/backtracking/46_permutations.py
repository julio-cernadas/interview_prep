def permute(nums):
    def backtrack(start):
        if start == len(nums):
            permutations.append(nums.copy())
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    permutations = []
    backtrack(0)
    return permutations


data = [1, 2, 3]
output = permute(data)
print(output)
