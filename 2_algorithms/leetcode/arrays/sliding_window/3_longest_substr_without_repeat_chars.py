# EXPLANATION:
# Here we use the sliding window approach. It initializes a dictionary to track the last seen index of each character
# and maintains pointers for the current substring's start and maximum length. While iterating through the string,
# if a character is encountered that was previously seen within the current substring, the start pointer is adjusted
# to exclude the repeating character and maintain a unique substring. The code efficiently calculates the length of
# each non-repeating substring and updates the maximum length accordingly. The final solution returns the length of
# the longest substring without repeating characters.


def length_of_longest_sub_string(s: str) -> int:
    char_index = {}  # Create a dictionary to store the last seen index of each character
    start = 0  # Initialize variables for the start of the substring and the maximum length
    max_length = 0

    for i in range(len(s)):
        if s[i] in char_index:
            start = max(start, char_index[s[i]] + 1)  # Increment the start if we've seen char before

        char_index[s[i]] = i  # Update the last seen index of the current character
        max_length = max(max_length, i - start + 1)  # Update the maximum length if the current substring is longer

    return max_length


data = "abcabcbb"
output = length_of_longest_sub_string(data)
print(output)
