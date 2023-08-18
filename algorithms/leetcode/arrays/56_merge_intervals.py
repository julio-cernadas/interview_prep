def merge(intervals):
    # Step 1: Sort intervals based on their start values.
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize an empty result list to store merged intervals.
    merged = [intervals.pop(0)]

    # Step 3: Iterate through each interval and merge overlapping ones.
    for start, end in intervals:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


data = [[1, 3], [2, 6], [8, 10], [15, 18]]
output = merge(data)
print(output)
