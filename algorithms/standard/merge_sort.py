# Input -   [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
# Output -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    return merge(left_half, right_half)


data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
output = merge_sort(data)
print(output)
