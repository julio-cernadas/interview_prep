# BIG O:
# O(n^2)

# EXPLANATION:
# Use the center expansion technique to count palindromic substrings. We iterate through the string, treating each
# character as the center of both odd and even length palindromes, and expand around them to find palindromic
# substrings. The count of palindromic substrings is returned as the result.


def count_substrings(s: str) -> int:
    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    count = 0
    for i in range(len(s)):
        # For odd-length palindromes
        expand_around_center(i, i)

        # For even-length palindromes
        expand_around_center(i, i + 1)

    return count


data = "abccc"
output = count_substrings(data)
print(output)
