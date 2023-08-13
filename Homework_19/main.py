def find_deepest_lake_depth(heights):
    left = 0
    left_peak = heights[left]
    right = len(heights) - 1
    right_peak = heights[right]
    deepest = 0

    while left < right:
        if left_peak < right_peak:
            left += 1
            deepest = max(deepest, left_peak - heights[left])
            left_peak = max(left_peak, heights[left])
        else:
            right -= 1
            deepest = max(deepest, right_peak - heights[right])
            right_peak = max(right_peak, heights[right])

    return deepest


my_heights = [1, 3, 2, 4, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
deepest_lake_depth = find_deepest_lake_depth(my_heights)
print("Глибина найглибшого озера:", deepest_lake_depth)


assert(find_deepest_lake_depth([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
assert(find_deepest_lake_depth([9, 0, 9, 12, 2, 12]) == 10)
assert (find_deepest_lake_depth([1, 1, 9, 12, 9, 12]) == 3)