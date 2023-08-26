# BIG O:
# O(n * log n)

# EXPLANATION:
# Uses a frequency dictionary and a min-heap to efficiently find the k most frequent elements in a list.

import heapq
from collections import defaultdict


def top_k_frequent_elements(nums, k):
    freq_dict = defaultdict(int)
    for num in nums:
        freq_dict[num] += 1

    max_heap = [(-freq, num) for num, freq in freq_dict.items()]
    heapq.heapify(max_heap)

    result = []
    for _ in range(k):
        freq, num = heapq.heappop(max_heap)
        result.append(num)

    return result


data = [1, 1, 1, 2, 2, 3]
target = 2
output = top_k_frequent_elements(data, target)
print(output)
