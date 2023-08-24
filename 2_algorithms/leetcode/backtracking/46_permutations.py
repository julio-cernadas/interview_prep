# BIG O:
# O(n!)

# EXPLANATION:
# This generates all possible permutations of the given nums list using a backtracking approach. The backtrack function
# recursively swaps elements and explores different positions to construct permutations. By restoring the original order
# through backtracking, it generates all valid permutations, which are collected in the permutations list.


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


data = [1, 2, 3, 4]
output = permute(data)
print(output)
