# CHAPTER 2: RECURSION VS. ITERATION

# EXPLANATION:
# In this case the iterative approach is better since the recursive will cause a stack overflow when 1001 is parameter


def factorial_iterative(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product


def factorial_recursive(number):
    # BASE CASE
    if number == 1:
        return 1

    # RECURSIVE CASE
    return number * factorial_recursive(number - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))
