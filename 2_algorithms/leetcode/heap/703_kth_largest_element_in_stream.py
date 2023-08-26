# BIG O:
# O(log k)

# EXPLANATION:
# The KthLargest class maintains a min-heap of at most k elements. The __init__ method initializes the instance with k
# and an initial list, while the add method allows adding new elements while keeping track of the kth largest element.


import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
