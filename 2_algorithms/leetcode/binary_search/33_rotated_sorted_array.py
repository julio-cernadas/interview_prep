# BIG O:
# O(log n)

# EXPLANATION:
# Performs a binary search in a rotated sorted array to find the index of the target value. It handles cases where one
# half of the array is sorted, making adjustments to the search range based on comparisons with the target value. This
# approach enables the algorithm to efficiently locate the target index or determine its absence in the array.


def binary_search(nums, target: int) -> int:
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid

        # if the left half is sorted
        if nums[low] <= nums[mid]:
            if (target < nums[mid]) and (target >= nums[low]):
                high = mid - 1
            else:
                low = mid + 1

        # if the right half is sorted
        else:
            if (target > nums[mid]) and (target <= nums[high]):
                low = mid + 1
            else:
                high = mid - 1

    return -1


data = [4, 5, 6, 7, 0, 1, 2]
output = binary_search(data, 0)
print(output)
