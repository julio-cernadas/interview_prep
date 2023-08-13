# EXPLANATION:
# Since the associative property of addition means that adding:
# 1 + 2 + 3 + 4 is the same as adding the sums of 1 + 2 and 3 + 4,
# we can divide a large array of numbers to sum into two smaller arrays of numbers to sum.

# The benefit is that for larger sets of data to process, we could farm out the subproblems to different computers
# and have them all work together in parallel. There’s no need to wait for the first half of the array to be summed
# before another computer can start summing the second half. This is a large advantage of the
# divide-and-conquer technique, as CPUs aren’t getting much faster but we can have multiple CPUs work simultaneously

# What is the base case?
# Either an array containing zero numbers (return 0) or an array containing one number (return the number).

# What argument is passed to the recursive function call?
# Either the left half or the right half of the array of numbers.

# How does this argument become closer to the base case?
# The size of the array of numbers is halved each time, eventually becoming an array containing zero or one number.


def sum_div_conq(numbers):
    # BASE CASE
    if len(numbers) == 0:
        return 0
    # BASE CASE
    elif len(numbers) == 1:
        return numbers[0]

    # RECURSIVE CASE
    mid = len(numbers) // 2
    left_half_sum = sum_div_conq(numbers[0:mid])
    right_half_sum = sum_div_conq(numbers[mid : len(numbers) + 1])
    return left_half_sum + right_half_sum


nums = [1, 2, 3, 4, 5]
print(sum_div_conq(nums))
