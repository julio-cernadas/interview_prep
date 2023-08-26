# BIG O:
# O(n)

# EXPLANATION:
# Uses two defaultdict objects to create frequency maps of characters in the input strings s and t. It then compares
# these maps to determine if the strings are valid anagrams. If the maps are equal, the function returns True,
# indicating valid anagrams; otherwise, it returns False.

from collections import defaultdict


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    s_map = defaultdict(int)
    t_map = defaultdict(int)
    for i in range(len(s)):
        s_map[s[i]] += 1
        t_map[t[i]] += 1

    return s_map == t_map


output = valid_anagram("anagram", "nagaram")
print(output)
