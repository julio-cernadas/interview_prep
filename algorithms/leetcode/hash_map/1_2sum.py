def two_sum(nums, target):
    hash_map = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_map:
            return [hash_map[diff], i]

        hash_map[nums[i]] = i


data = [2, 7, 11, 15]
target_sum = 9
output = two_sum(data, target_sum)
print(output)
