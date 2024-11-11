def trap(height: list):
    n = len(height)
    left, right = [0 for _ in range(n)], [0 for _ in range(n)]
    left[0], right[-1] = height[0], height[-1]

    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    for j in range(n - 2, -1, -1):
        right[j] = max(right[j + 1], height[j])

    volume = 0
    for i in range(n):
        volume += min(left[i], right[i]) - height[i]

    return volume


height = [4, 2, 0, 3, 2, 5]
print(trap(height))
