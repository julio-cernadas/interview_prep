# BIG O:
# O(n)

# EXPLANATION:
# Uses a sliding window approach to find the longest substring with the same characters by allowing at most 'k'
# replacements. It maintains a window where it tracks the character frequencies and adjusts the window based on the
# allowed replacements. The goal is to maximize the substring length with the same characters.


from collections import defaultdict


def character_replacement(s, k):
    char_count = defaultdict(int)  # Initialize a dictionary to store character counts
    max_freq = 0  # Initialize maximum character frequency in a substring
    left = 0  # Initialize left pointer of the window

    for right in range(len(s)):  # Iterate through the string using the right pointer
        char_count[s[right]] += 1  # Increment the count of the current character
        max_freq = max(max_freq, char_count[s[right]])  # Update max frequency

        if (right - left + 1 - max_freq) > k:  # Calculate the length of the current substring and check if it's valid
            char_count[s[left]] -= 1  # Move the left pointer and update counts
            left += 1

    return len(s) - left


data = "ABAB"
target = 2
output = character_replacement(data, target)
print(output)
