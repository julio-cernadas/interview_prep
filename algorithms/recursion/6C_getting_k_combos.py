# CHAPTER 6: PERMUTATIONS & COMBINATIONS

# EXPLANATION:
# What is the base case?
# The base case in the backtrack function is when the length of the current_combination reaches the desired length k.
# At this point, the function adds the current combination to the combinations list and returns,
# effectively terminating the recursion.

# What argument is passed to the recursive function call?
# Two arguments are passed to the recursive function call:
# start: This argument indicates the index from which the function should start considering characters
# for the next combination. It helps to avoid generating duplicate combinations.
# current_combination: This argument represents the current state of the combination being constructed. During each
# recursive call, characters from the string are added to the current_combination to build up the combination.

# How does this argument become closer to the base case?
# In each recursive call, the start index is incremented by 1. This helps to ensure that each character in the string
# is considered at least once for the current position in the combination. As the recursion progresses, characters
# from the string are added to the current_combination, and the start index moves forward. This process continues
# until the length of the current_combination reaches the base case length of k. At this point, the recursion stops,
# and the current combination is added to the combinations list.


def get_combos(string, k):
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            combinations.append(current_combination)
            return

        for i in range(start, len(string)):
            backtrack(i + 1, current_combination + string[i])

    combinations = []
    backtrack(0, "")
    return combinations


print(get_combos("ABC", 2))
