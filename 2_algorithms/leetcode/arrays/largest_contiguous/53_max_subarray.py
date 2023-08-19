# EXPLANATION:
# This is also known as "Largest Sum Contiguous Subarray", the solution employs the Kadane's algorithm to find the
# maximum sum of a subarray within the given array. By iterating through the array, it continuously updates both the
# current subarray sum and the maximum sum encountered so far, effectively finding the maximum subarray sum.


def max_sub_array(nums):
    max_sum = float("-inf")
    current_sum = float("-inf")

    for i in range(len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])  # Choose: start a new subarray or extend the current one
        max_sum = max(max_sum, current_sum)  # Update max_sum with the maximum of max_sum and current_sum

    return max_sum


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_sub_array(data)
print(output)
