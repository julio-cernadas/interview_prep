# code pulled from brilliant example


def permutation(list, start, end):
    if start == end:
        return []

    for i in range(start, end + 1):
        list[start], list[i] = list[i], list[start]  # The swapping
        permutation(list, start + 1, end)
        list[start], list[i] = list[i], list[start]  # Backtracking


permutation([1, 2, 3], 0, 2)  # The first index of a list is zero
