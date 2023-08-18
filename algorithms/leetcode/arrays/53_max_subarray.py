def max_sub_array(nums):
    # Initialize both max_sum and current_sum with the first element
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        # Choose between starting a new subarray or extending the current one
        current_sum = max(nums[i], current_sum + nums[i])

        # Update max_sum with the maximum of max_sum and current_sum
        max_sum = max(max_sum, current_sum)

    return max_sum


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_sub_array(data)
print(output)
