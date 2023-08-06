# Input -   [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
# Output -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
output = bubble_sort(data)
print(output)
