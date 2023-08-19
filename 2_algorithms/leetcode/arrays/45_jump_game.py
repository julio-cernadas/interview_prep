def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0  # To keep track of the number of jumps taken
    current_max = 0  # The farthest index we can reach with the current jumps
    next_max = 0  # The farthest index we can reach with one more jump

    for i in range(n - 1):
        next_max = max(next_max, i + nums[i])  # Update next_max based on the current jump
        if i == current_max:  # We've reached the farthest index we can reach with the current jumps
            jumps += 1
            current_max = next_max

            if current_max >= n - 1:  # If we can already reach the last index, no need to continue
                break

    return jumps


# data = [4, 3, 4, 2, 6, 1, 2, 1]
# data = [6, 1, 1, 1, 1, 1, 3]
# data = [2, 1]
# data = [2, 3, 0, 1, 4]
data = [1, 1, 1, 1]
output = min_jumps(data)
print(output)
