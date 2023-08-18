# CHAPTER 6: PERMUTATIONS & COMBINATIONS

# EXPLANATION:

# What is the base case?
# The base case in this recursive function is when the start parameter becomes equal to the length of the string.
# In the code, this is represented by the condition if start == len(string). At this point, the function adds the
# current permutation of the string to the list of permutations and returns.

# What argument is passed to the recursive function call?
# The backtrack function is called recursively with the argument start + 1. This means that the recursive call
# processes the next index in the string, effectively moving towards the end of the string.

# How does this argument become closer to the base case?
# The argument start becomes closer to the base case by incrementing it in each recursive call. At each level of
# recursion, the start index is moved one step forward, which means that the substring being considered becomes shorter
# by one character. This process continues until the base case is reached, at which point the permutations for the
# entire string have been generated and the recursion starts to unwind.


def generate_permutations(string):
    def backtrack(start):
        if start == len(string):
            permutations.append("".join(string))
            return

        for i in range(start, len(string)):
            string[start], string[i] = string[i], string[start]
            backtrack(start + 1)
            string[start], string[i] = string[i], string[start]

    permutations = []
    string = list(string)
    backtrack(0)
    return permutations


print(generate_permutations("ABCD"))
