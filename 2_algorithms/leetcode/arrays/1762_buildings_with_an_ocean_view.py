def find_buildings(heights):
    n = len(heights)
    ocean_view_buildings = []

    # Step 1: Traverse the heights from right to left
    max_height = 0
    for i in range(n - 1, -1, -1):
        if heights[i] > max_height:
            ocean_view_buildings.append(i)
            max_height = heights[i]

    # Step 2: Return the ocean view buildings in left to right order
    return ocean_view_buildings[::-1]


data = [4, 2, 3, 1]
output = find_buildings(data)
print(output)
