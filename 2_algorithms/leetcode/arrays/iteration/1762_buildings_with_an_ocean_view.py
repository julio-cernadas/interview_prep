# EXPLANATION:
# Tackled using a reverse iteration approach. Start iterating from the end of the array and maintain a running maximum
# height encountered so far. If the current building's height is greater than the running maximum, mark it as visible
# from the ocean, and update the running maximum. Finally, return the indices of the buildings marked as visible.


def find_buildings(heights):
    n = len(heights)
    ocean_view_buildings = []

    max_height = 0  # Step 1: Traverse the heights from right to left
    for i in range(n - 1, -1, -1):
        if heights[i] > max_height:
            ocean_view_buildings.append(i)
            max_height = heights[i]

    return ocean_view_buildings[::-1]  # Step 2: Return the ocean view buildings in left to right order


data = [4, 2, 3, 1]
output = find_buildings(data)
print(output)
