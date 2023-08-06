def length_of_longest_sub_string(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    left_idx = 0
    right_idx = 1
    longest_sub_string = 1

    while right_idx < n:
        sub_string = s[left_idx:right_idx]

        if s[right_idx] not in sub_string:
            curr_length = len(sub_string) + 1
            if curr_length > longest_sub_string:
                longest_sub_string = curr_length
        else:
            left_idx = right_idx

        right_idx += 1

    return longest_sub_string


data = "abcabcbb"
output = length_of_longest_sub_string(data)
print(output)
