def top_k_frequent_elements(nums, k):
    # Step 1: Create a dictionary to store the frequency of each number
    num_freq = {}
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    # Step 2: Create a list of lists to represent buckets of elements by frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in num_freq.items():
        buckets[freq].append(num)

    # Step 3: Extract the top k frequent elements from the buckets
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) == k:
            return result


data = [1, 1, 1, 2, 2, 3]
target = 2
output = top_k_frequent_elements(data, target)
print(output)
