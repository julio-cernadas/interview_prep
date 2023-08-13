# EXPLANATION:

# What is the base case?
# A perm_length argument of 0, meaning a permutation zero characters long,
# signals that the prefix argument now contains the complete permutation and so prefix should be returned in an array.

# What argument is passed to the recursive function call?
# The chars string of the characters to get permutations of, a perm_length argument that begins as the length of chars,
# and a prefix argument that begins as the blank string. Recursive calls decrement the perm_length argument while
# appending a character from chars to the prefix argument.

# How does this argument become closer to the base case?
# Eventually, the perm_length argument decrements to 0.


def get_perms_with_rep(chars, perm_length=None, prefix=""):
    if perm_length is None:
        perm_length = len(chars)

    # BASE CASE
    if perm_length == 0:
        return [prefix]

    # RECURSIVE CASE
    results = []
    for char in chars:
        new_prefix = prefix + char
        results.extend(get_perms_with_rep(chars, perm_length - 1, new_prefix))

    return results


print(get_perms_with_rep("JPB123", 4))
