# EXPLANATION:
# In this case the recursive approach is better since the iterative will run in O(n) but recursive will do O(log n)
# Here we are leveraging the divide and conquer approach, specifically the properties of exponentations.


def exponent_by_iteration(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


def exponent_by_recursion(a, n):
    # BASE CASE
    if n == 1:
        return a

    # RECURSIVE CASE (When n is even)
    elif n % 2 == 0:
        result = exponent_by_recursion(a, n // 2)
        return result * result

    # RECURSIVE CASE (When n is odd)
    elif n % 2 == 1:
        result = exponent_by_recursion(a, n // 2)
        return result * result * a


print(exponent_by_iteration(10, 3))

print(exponent_by_recursion(3, 6))
print(exponent_by_recursion(10, 3))
print(exponent_by_recursion(17, 10))
