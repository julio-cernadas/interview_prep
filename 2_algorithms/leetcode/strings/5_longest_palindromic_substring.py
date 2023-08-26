# BIG O:
# O(n^2)

# EXPLANATION:
# Utilizes the concept of expanding around centers to find both odd & even length palindromes. The expand_around_center
# function is used to expand the palindrome around a specific center, and the main function iterates through each
# character to find the longest palindrome.


def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        # Check for odd length palindromes
        palindrome_odd = expand_around_center(i, i)
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd

        # Check for even length palindromes
        palindrome_even = expand_around_center(i, i + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest


data = "babad"
output = longest_palindrome(data)
print(output)
