# BIG O:
# O(n)

# EXPLANATION:
# Uses a max heap to simulate the process of smashing stones together, removing the heaviest stones, and replacing them
# with new stones until only one or no stone remains. The function then returns the weight of the last remaining stone.


import heapq


def last_stone_weight(stones):
    max_heap = [-stone for stone in stones]  # Convert stone weights to negative values to create a max heap
    heapq.heapify(max_heap)  # Convert the list to a max heap

    while len(max_heap) > 1:
        heaviest1 = heapq.heappop(max_heap)  # Pop the heaviest stone
        heaviest2 = heapq.heappop(max_heap)  # Pop the second heaviest stone

        diff = heaviest1 - heaviest2
        if diff != 0:
            heapq.heappush(max_heap, diff)  # Push the new stone's weight if it's not zero

    return -max_heap[0] if max_heap else 0  # Return the last stone weight or 0 if no stones are left


data = [2, 7, 4, 1, 8, 1]
output = last_stone_weight(data)
print(output)
