def largest_rectangle_area(arr):
    ans = 0
    arr = [-1] + arr
    arr.append(-1)
    n = len(arr)
    stack = [0]

    for i in range(n):
        while arr[i] < arr[stack[-1]]:
            h = arr[stack.pop()]
            area = h * (i - stack[-1] - 1)
            ans = max(ans, area)
        stack.append(i)
    return ans


data = [2, 1, 5, 6, 2, 3]
output = largest_rectangle_area(data)
print(output)
