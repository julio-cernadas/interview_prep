# EXPLANATION:
# This code takes a list of non-overlapping intervals and a new interval. It iterates through the existing intervals,
# considering cases where the new interval needs to be inserted before, after, or in between existing intervals. If
# there's an overlap, the new interval's start and end values are updated to encompass the overlapping range.
# Finally, if the new interval hasn't been inserted at this point, it's added to the end.


def insert(intervals, new_interval):
    res = []
    for i in range(len(intervals)):
        if new_interval[1] < intervals[i][0]:
            res.append(new_interval)
            return res + intervals[i:]
        elif new_interval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]

    res.append(new_interval)
    return res


data = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
output = insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
print(output)
