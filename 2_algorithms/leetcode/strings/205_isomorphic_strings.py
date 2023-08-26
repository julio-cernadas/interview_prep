# BIG O:
# O(n)

# EXPLANATION:
# Iterates through their corresponding characters and maintaining a dictionary iso_map that stores the mapping between
# characters in s and t. It ensures that the mapping is consistent and that one character in t is not mapped to multiple
# characters in s. If all conditions are met, the function returns True, otherwise, it returns False.


def isomorphic_strings(s, t):
    iso_map = {}
    for char_s, char_t in zip(s, t):
        if char_s in iso_map and iso_map[char_s] != char_t:
            return False
        if char_s not in iso_map and char_t in iso_map.values():
            return False
        iso_map[char_s] = char_t

    return True


output = isomorphic_strings("egg", "add")
print(output)
