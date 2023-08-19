def min_remove_to_make_valid(s):
    stack = []
    to_remove = set()

    # Step 1: Mark unmatched open and close parentheses
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                to_remove.add(i)

    # Add remaining unmatched open parentheses to the set
    to_remove.update(stack)

    # Step 2: Construct the valid string without removed characters
    result = []
    for i, char in enumerate(s):
        if i not in to_remove:
            result.append(char)

    return "".join(result)


data = "lee(t(c)o)de)"
output = min_remove_to_make_valid(data)
print(output)
