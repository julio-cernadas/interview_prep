import heapq


def top_k_frequent_elements(nums, k):
    # Step 1: Create a dictionary to store the frequency of each number
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Step 2: Create a min-heap to store the k most frequent elements
    min_heap = []

    # Step 3: Iterate through the items in the frequency dictionary
    for num, freq in freq_dict.items():
        # Step 4: Push the current element and its frequency as a tuple into the min-heap
        heapq.heappush(min_heap, (freq, num))

        # Step 5: If the size of the min-heap exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 6: Extract the k most frequent elements from the min-heap
    result = [num for freq, num in min_heap]

    # Step 7: Return the result
    return result


data = [1, 1, 1, 2, 2, 3]
target = 2
output = top_k_frequent_elements(data, target)
print(output)
