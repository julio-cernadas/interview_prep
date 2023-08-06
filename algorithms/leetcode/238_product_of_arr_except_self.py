def product_except_self(nums):
    n = len(nums)
    res = [1] * len(nums)

    idx = 0
    multiplier = 1
    while idx < n - 1:
        multiplier *= nums[idx]
        res[idx + 1] *= multiplier
        idx += 1

    idx = n - 1
    multiplier = 1
    while idx > 0:
        multiplier *= nums[idx]
        res[idx - 1] *= multiplier
        idx -= 1

    return res


data = [1, 2, 3, 4]
output = product_except_self(data)
print(output)
