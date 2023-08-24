# BIG O:
# O(log n)

# EXPLANATION:
# Supports setting values with timestamps and retrieving values based on timestamps using a binary search approach.
# This is useful for maintaining a time-based key-value store and efficiently retrieving historical values.

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(arr, tmstamp):
            res = ""
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][1] <= tmstamp:
                    res = arr[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1

            return res

        values = self.store.get(key, [])
        return binary_search(values, timestamp)
