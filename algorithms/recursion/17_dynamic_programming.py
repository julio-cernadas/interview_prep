fibonacciCache = {}


def fibonacci(n):
    global fibonacciCache

    if n in fibonacciCache:
        return fibonacciCache[n]

    # BASE CASE
    if n == 1 or n == 2:
        fibonacciCache[n] = 1
        return 1

    # RECURSIVE CASE
    result = fibonacci(n - 1)
    result = result + fibonacci(n - 2)
    fibonacciCache[n] = result
    return result


print(fibonacci(10))
print(fibonacci(10))
