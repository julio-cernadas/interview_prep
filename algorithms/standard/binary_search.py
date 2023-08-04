def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == arr[mid]:
            return mid
        if item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


data = [1, 3, 5, 6, 9]
output = binary_search(data, 3)
print(output)

output = binary_search(data, -1)
print(output)
