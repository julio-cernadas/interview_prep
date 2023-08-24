# BIG O:
# O(2^n)

# EXPLANATION:
# Uses a backtracking approach to generate all subsets of the given nums list. The backtrack function starts with an
# empty subset and systematically adds each element to the subset, generating subsets along the way. After appending
# each subset to the result list, the code recursively explores all possible combinations of elements. When a valid
# combination is found, the current element is removed to backtrack and explore other combinations.


def subsets(nums):
    def backtrack(start, current):
        result.append(current)

        for i in range(start, len(nums)):
            backtrack(i + 1, current + [nums[i]])

    result = []
    backtrack(0, [])
    return result


data = [1, 2, 3]
output = subsets(data)
print(output)
