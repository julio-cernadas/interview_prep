# EXPLANATION:
# What is the base case?
# A zero or one-character string, which returns True because it is always a palindrome.

# What argument is passed to the recursive function call?
# The middle characters of the string argument.

# How does this argument become closer to the base case?
# The string argument shrinks by two characters for each recursive call until it becomes a zero or one-character string.


def is_palindrome(the_string):
    # BASE CASE
    if len(the_string) == 0 or len(the_string) == 1:
        return True

    # RECURSIVE CASE
    head = the_string[0]
    middle = the_string[1:-1]
    last = the_string[-1]
    return head == last and is_palindrome(middle)


text = "racecar"
print(is_palindrome(text))
