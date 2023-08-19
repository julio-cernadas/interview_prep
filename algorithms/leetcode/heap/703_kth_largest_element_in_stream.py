import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
