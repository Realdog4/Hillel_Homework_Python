def find_deepest_lake_depth(heights):
    stack = []
    deepest_lake = 0

    for i, h in enumerate(heights):
        while stack and h >= stack[-1][1]:
            idx, prev_h = stack.pop()
            if stack:
                distance = i - stack[-1][0] - 1
                deepest_lake = max(deepest_lake, (min(h, stack[-1][1]) - prev_h) * distance)

        stack.append((i, h))

    return deepest_lake


my_heights = [1, 3, 2, 4, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
deepest_lake_depth = find_deepest_lake_depth(my_heights)
print("Глибина найглибшого озера:", deepest_lake_depth)