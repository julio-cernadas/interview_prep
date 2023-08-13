# EXPLANATION:
# What is the base case?
# Searching a range of items that is only one item in length or zero items (because left > right.)

# What argument is passed to the recursive function call?
# The indices of the left and right ends of the range in the list we are searching.

# How does this argument become closer to the base case?
# The range roughly halves in size for each recursive call, so it eventually becomes one item long.


def binary_search(item, arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    # BASE CASE
    # The item is not in array
    if left > right:
        return None

    mid = (left + right) // 2
    # BASE CASE
    if item == arr[mid]:
        return mid
    # RECURSIVE CASE
    elif item < arr[mid]:
        return binary_search(item, arr, left, mid - 1)
    elif item > arr[mid]:
        return binary_search(item, arr, mid + 1, right)


print(binary_search(13, [1, 4, 8, 11, 13, 16, 19, 19]))
