# CHAPTER 2: CLASSIC RECURSION ALGORITHMS

# EXPLANATION:
# We're using the head and tail approach here, splitting head - tail...

# What is the base case?
# A zero or one-character string.

# What argument is passed to the recursive function call?
# The tail of the original string argument, which has one less character than the original string argument.

# How does this argument become closer to the base case?
# The array argument shrinks by one element for each recursive call until it becomes a one or zero-length array.


def rev(the_string):
    # BASE CASE
    if len(the_string) == 0 or len(the_string) == 1:
        return the_string

    # RECURSIVE CASE
    head = the_string[0]
    tail = the_string[1:]
    return rev(tail) + head


print(rev("Hello, world!"))
