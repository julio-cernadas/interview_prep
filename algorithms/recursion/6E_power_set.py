# CHAPTER 6: PERMUTATIONS & COMBINATIONS

# What is the base case?
# If chars is the blank string (the empty set), the function returns an array with just a blank
# string, since the empty set is the only subset of the empty set.

# What argument is passed to the recursive function call?
# The tail of chars is passed.

# How does this argument become closer to the base case?
# Since the recursive calls remove the heads from the chars arguments, eventually the chars
# argument becomes the blank string.


def get_power_set(chars, indent=0):
    # BASE CASE
    if chars == "":
        return [""]

    # RECURSIVE CASE
    power_set = []
    head = chars[0]
    tail = chars[1:]

    tail_power_set = get_power_set(tail, indent + 1)

    for tailSet in tail_power_set:
        power_set.append(head + tailSet)

    power_set = power_set + tail_power_set
    return power_set


print(get_power_set("ABC"))
