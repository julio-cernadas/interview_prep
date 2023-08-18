def find_kth_largest(nums, k):
    pivot = nums[len(nums) // 2]
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]

    n = len(nums) - len(left)
    if k > n:
        return find_kth_largest(left, k - n)
    if k <= len(right):
        return find_kth_largest(right, k)
    else:
        return pivot


data = [3, 2, 1, 5, 6, 4]
target = 2
output = find_kth_largest(data, target)
print(output)
