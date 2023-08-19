def merge(intervals):
    intervals.sort(key=lambda x: x[0])  # Step 1: Sort intervals based on their start values.
    merged = [intervals.pop(0)]  # Step 2: Initialize an empty result list to store merged intervals.

    for start, end in intervals:  # Step 3: Iterate through each interval and merge overlapping ones.
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


data = [[1, 3], [2, 6], [8, 10], [15, 18]]
output = merge(data)
print(output)
