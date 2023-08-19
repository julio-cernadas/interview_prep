# EXPLANATION:
# Two-pointer technique to find unique triplets in a sorted list that sum up to zero.
# It handles duplicates and outputs the found triplets.
# We iterate through a sorted arrray (excluding last two elements) with inner while loop
# adjusting the left or right pointer based on distance from target sum. When we find a triplet that works
# record result, then adjust left / right pointer to skip duplicates in both directions.


def three_sum(nums):
    nums.sort()  # Step 1: Sort the input array in ascending order
    result = []  # This list will store the triplets that satisfy the condition

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements to avoid duplicate triplets

        left, right = i + 1, len(nums) - 1  # Initialize two pointers (one next to it, the other at the end)

        while left < right:
            total = nums[i] + nums[left] + nums[right]  # Calculate the sum of three elements

            if total < 0:
                left += 1  # Move the left pointer to increase the sum
            elif total > 0:
                right -= 1  # Move the right pointer to decrease the sum
            else:
                result.append([nums[i], nums[left], nums[right]])  # Found a valid triplet
                # Skip duplicates in both directions
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1  # Move the left pointer to the next unique element
                right -= 1  # Move the right pointer to the next unique element

    return result


data = [-1, 0, 1, 2, -1, -4, -10, 10, -5, 5]
output = three_sum(data)
print(output)
