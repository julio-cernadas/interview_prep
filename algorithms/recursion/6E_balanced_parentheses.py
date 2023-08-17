# CHAPTER 6: PERMUTATIONS & COMBINATIONS

# What is the base case?
# When the number of opening and closing parentheses remaining to be added to the string being built has reached 0.
# A second base case always occurs after the recursive cases have finished.

# What argument is passed to the recursive function call?
# The total number of pairs of parentheses (pairs), the remaining number of opening and closing
# parentheses to add (openRem and closeRem), and the string currently being built (current).

# How does this argument become closer to the base case? As we add more opening and closing
# parentheses to current, we decrement the openRem and closeRem arguments until they become 0.


def get_balanced_parens(pairs, open_rem=None, close_rem=None, current="", indent=0):
    if open_rem is None:
        open_rem = pairs

    if close_rem is None:
        close_rem = pairs

    # BASE CASE
    if open_rem == 0 and close_rem == 0:
        return [current]

    # RECURSIVE CASE
    results = []
    if open_rem > 0:
        balanced_parens = get_balanced_parens(pairs, open_rem - 1, close_rem, current + "(", indent + 1)
        results.extend(balanced_parens)

    if close_rem > open_rem:
        balanced_parens = get_balanced_parens(pairs, open_rem, close_rem - 1, current + ")", indent + 1)
        results.extend(balanced_parens)

    # BASE CASE
    return results


print(get_balanced_parens(2))
