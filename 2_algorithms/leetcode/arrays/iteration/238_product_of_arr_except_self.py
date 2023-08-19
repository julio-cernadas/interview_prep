# EXPLANATION:
# Solved using a two-pass approach. In the first pass, calculate the product of all elements to the left of each
# element and store it in an output array. In the second pass, calculate the product of all elements to the right of
# each element and multiply it with the corresponding left product from the output array. This way, you'll get the
# product of the array except the element at the current index.


def product_except_self(nums):
    n = len(nums)
    res = [1] * len(nums)

    for i in range(n - 1):
        res[i + 1] = nums[i] * res[i]

    multiplier = 1
    for i in range(n - 1, 0, -1):
        multiplier *= nums[i]
        res[i - 1] *= multiplier

    return res


data = [1, 2, 3, 4]
output = product_except_self(data)
print(output)
