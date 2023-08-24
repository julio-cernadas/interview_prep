# EXPLANATION:
# Uses binary search to locate the minimum value in a rotated sorted array. By comparing the midpoint value with the
# value at the right end of the search range, the algorithm determines whether the minimum lies in the left or right
# half, thus efficiently narrowing down the search space.


def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


data = [3, 4, 5, 1, 2]
output = find_min(data)
print(output)
