# CHAPTER 6: PERMUTATIONS & COMBINATIONS

# EXPLANATION:

# What is the base case?
# The base case in the backtrack function is when the length of the current_permutation reaches the desired length k.
# At this point, the function adds the current permutation to the permutations list and returns,
# effectively terminating the recursion.

# What argument is passed to the recursive function call?
# The argument passed to the recursive function call is the current_permutation. This argument represents the current
# state of the permutation being constructed. During each recursive call, a character from the given string is added
# to the current_permutation to build up the permutation.

# How does this argument become closer to the base case?
# In each recursive call, the current_permutation is extended by adding a character from the string.
# This action brings the permutation one step closer to the desired length k. As the recursive calls progress,
# the length of the current_permutation gradually increases until it reaches the base case length of k.
# Once the base case is reached, the recursion stops, and the current permutation is added to the permutations list.


def get_perms_with_rep(string, k):
    def backtrack(current_permutation):
        if len(current_permutation) == k:
            permutations.append(current_permutation)
            return
        for char in string:
            backtrack(current_permutation + char)

    permutations = []
    backtrack("")
    return permutations


print(get_perms_with_rep("JPB123", 2))
