# CHAPTER 6: PERMUTATIONS & COMBINATIONS

# EXPLANATION:
# What is the base case?
# The first base case is a k argument of 0, meaning that a 0-combination is requested, which is always an array of the
# blank string no matter what chars is. The second case occurs if chars is the blank string, which is an empty array
# since no possible combinations can be made from a blank string.

# What argument is passed to the recursive function call?
# For the first recursive call, the tail of chars and k - 1 are passed. For the second recursive call,
# the tail of chars and k are passed.

# How does this argument become closer to the base case?
# Since the recursive calls decrement k and remove the heads from the chars arguments, eventually the k argument
# decrements to 0 or the chars argument becomes the blank string.


def get_combos(chars, k):
    # BASE CASE
    if k == 0:
        return [""]
    # BASE CASE
    elif chars == "":
        return []

    # RECURSIVE CASE
    combinations = []
    head = chars[:1]
    tail = chars[1:]
    tail_combos = get_combos(tail, k - 1)
    for tailCombo in tail_combos:
        combinations.append(head + tailCombo)

    combinations.extend(get_combos(tail, k))
    return combinations


print(get_combos("ABC", 2))
