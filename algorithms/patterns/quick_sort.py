def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
output = quick_sort(data)
print(output)
