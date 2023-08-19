import heapq


def find_kth_largest(nums, k):
    # Convert the input list into a min-heap with k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Convert the list into a heap in O(k) time

    # Traverse the remaining elements in the input list
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)  # Remove the smallest element
            heapq.heappush(min_heap, num)  # Push the larger element into the heap

    # The root of the min-heap will be the kth largest element
    return min_heap[0]


data = [3, 2, 1, 5, 6, 4]
target = 2
output = find_kth_largest(data, target)
print(output)
