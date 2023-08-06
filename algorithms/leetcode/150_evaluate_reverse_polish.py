def eval_rpn(tokens) -> int:
    if len(tokens) < 3:
        return int(tokens[0])

    operations = ["+", "-", "*", "/"]
    stack = []
    res = None
    while tokens:
        token = tokens.pop(0)

        if token in operations:
            right = stack.pop(-1)
            left = stack.pop(-1)
            res = int(eval(f"{left}{token}{right}"))
            stack.append(res)
        else:
            stack.append(token)

    return res


data = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
output = eval_rpn(data)
print(output)
