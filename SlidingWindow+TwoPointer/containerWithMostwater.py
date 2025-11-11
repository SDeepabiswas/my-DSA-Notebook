def max_water(heights):
    left_index = 0
    right_index = len(heights) - 1
    max_area = 0
    while left_index < right_index:
        if heights[left_index] < heights[right_index]:
            current_area = heights[left_index] * (right_index - left_index)
            left_index += 1
        else:
            current_area = heights[right_index] * (right_index - left_index)
            right_index -= 1
        if current_area > max_area:
            max_area = current_area
    return max_area
# Example usage:
heights = [3, 9, 4, 8, 2, 6, 1]
print(max_water(heights))  # Output: 24