def is_valid(s):
    mapping = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for i in s:
        if i in mapping:
            stack.append(i)
        elif not stack or mapping[stack.pop()] != i:
            return False

    return len(stack) == 0


data = "(({}))"
output = is_valid(data)
print(output)
