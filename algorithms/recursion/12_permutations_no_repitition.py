# EXPLANATION:

# What is the base case?
# An argument of a single character string or empty string, which returns an array of just that string.

# What argument is passed to the recursive function call?
# The string argument missing one character. A separate recursive call is made for each character missing.

# How does this argument become closer to the base case?
# The size of the string shrinks and eventually becomes a single-character string.


def get_perms(chars):
    # BASE CASE
    if len(chars) == 1:
        return [chars]

    # RECURSIVE CASE
    permutations = []
    head = chars[0]
    tail = chars[1:]

    tail_permutations = get_perms(tail)
    for tailPerm in tail_permutations:
        for i in range(len(tailPerm) + 1):
            new_perm = tailPerm[0:i] + head + tailPerm[i:]
            permutations.append(new_perm)

    return permutations


print(get_perms("ABCD"))
