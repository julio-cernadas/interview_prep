# BIG O:
# O(k * log n)

# EXPLANATION:
# Finds the kth largest element in a list using a max-heap, we pop k times until we get the k-th largest element.


import heapq


def find_kth_largest(nums, k):
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    for _ in range(k - 1):
        heapq.heappop(max_heap)

    return -max_heap[0]


data = [3, 2, 1, 5, 6, 4]
target = 2
output = find_kth_largest(data, target)
print(output)
