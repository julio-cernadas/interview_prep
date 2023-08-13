def min_jumps(jumps):
    if len(jumps) <= 1:
        return 0

    counter = 1
    i = 0
    while i < len(jumps) and i + jumps[i] < len(jumps) - 1:
        k = i + jumps[i]
        j = i + 1

        while j < len(jumps) and j <= i + jumps[i]:
            if j + jumps[j] > k + jumps[k]:
                k = j
            j += 1

        i = k
        counter += 1

    return counter


# data = [4, 3, 4, 2, 6, 1, 2, 1]
# data = [6, 1, 1, 1, 1, 1, 3]
# data = [2, 1]
# data = [2, 3, 0, 1, 4]
data = [1, 1, 1, 1]
output = min_jumps(data)
print(output)
