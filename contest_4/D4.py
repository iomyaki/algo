def check(x):
    x -= 1
    less_then_x_count = 0
    for i in range(1, n + 1):
        less_then_x_count += min(x // i, n)

    return less_then_x_count < k


n, k = map(int, input().split())

left = 1
right = n ** 2 + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
