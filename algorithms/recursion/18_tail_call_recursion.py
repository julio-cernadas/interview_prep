def factorial(number, accum=1):
    # BASE CASE
    if number == 1:
        return accum

    # RECURSIVE CASE
    return factorial(number - 1, accum * number)


print(factorial(5))
