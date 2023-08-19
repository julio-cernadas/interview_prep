# EXPLANATION:
# By iterating through the array, this maintains both the maximum and minimum products ending at each position, allowing
# it to handle negative numbers and changing signs effectively. The result is continuously updated with the maximum
# product encountered during the iteration, providing the solution.


def max_continuous_product(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product  # Swap max and min due to negative number

        max_product = max(nums[i], max_product * nums[i])  # Choose: start a new subarray or extend the current one
        min_product = min(nums[i], min_product * nums[i])  # Choose: start a new subarray or extend the current one

        result = max(result, max_product)  # Update result with the maximum of result and max_product

    return result


data = [2, 3, -2, -4]
output = max_continuous_product(data)
print(output)
