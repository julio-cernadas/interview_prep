def sub_array_sum(nums, k):
    res = 0
    cur_sum = 0
    prefix_sums = {0: 1}

    for n in nums:
        cur_sum += n
        diff = cur_sum - k

        res += prefix_sums.get(diff, 0)
        prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

    return res


data = [1, 1, 1]
target = 2
output = sub_array_sum(data, target)
print(output)
