def three_sum(nums):
    if len(nums) == 3 and sum(nums) == 0:
        return [nums]

    nums.sort()
    res = []

    n = len(nums)
    x = 0
    while x < n - 2 and nums[x] <= 0:
        if x > 0 and nums[x - 1] == nums[x]:
            x += 1
            continue

        l = x + 1
        r = n - 1
        while l < r:
            if l > x + 1 and nums[l - 1] == nums[l]:
                l += 1
                continue

            if r < n - 1 and nums[r + 1] == nums[r]:
                r -= 1
                continue

            three = [nums[x], nums[l], nums[r]]
            sum_of_three = sum(three)
            if sum_of_three < 0:
                l += 1
            elif sum_of_three > 0:
                r -= 1
            else:
                res.append(three)
                l += 1

        x += 1

    return res


data = [-1, 0, 1, 2, -1, -4, -10, 10, -5, 5]
output = three_sum(data)
print(output)
