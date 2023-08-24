# EXPLANATION:
# Employs the Dutch National Flag algo to sort an array of colors represented as numbers. Three pointers: low for 0s,
# high for 2s, and current for traversing the array. The algorithm works by swapping elements to their respective
# positions based on their values. As the current pointer moves, it swaps elements with the low pointer for 0s and the
# high pointer for 2s. Elements that are already in their correct positions (1s) are simply skipped.


def sort_colors(nums):
    low, high = 0, len(nums) - 1
    current = 0

    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1
        elif nums[current] == 2:
            nums[current], nums[high] = nums[high], nums[current]
            high -= 1
            continue

        current += 1


data = [2, 0, 2, 1, 1, 0]
sort_colors(data)
print(data)
