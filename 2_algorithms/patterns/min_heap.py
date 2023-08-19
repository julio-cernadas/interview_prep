def min_heapify(arr, k):
    smallest = k
    left = 2 * k + 1
    right = 2 * k + 2
    if left < len(arr) and arr[left] < arr[k]:
        smallest = left

    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right

    if smallest != k:
        arr[k], arr[smallest] = arr[smallest], arr[k]
        min_heapify(arr, smallest)


def build_min_heap(arr):
    n = int((len(arr) // 2) - 1)
    for k in range(n, -1, -1):
        min_heapify(arr, k)
    return arr


data = [3, 9, 2, 1, 4, 5]
output = build_min_heap(data)
print(output)
