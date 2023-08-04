def max_sub_array(nums) -> int:
    greatest_sum = nums[0]

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr_sum = sum(nums[i : j + 1])
            if curr_sum > greatest_sum:
                greatest_sum = curr_sum

    return greatest_sum


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_sub_array(data)
print(output)
