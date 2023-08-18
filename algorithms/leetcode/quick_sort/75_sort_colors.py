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
