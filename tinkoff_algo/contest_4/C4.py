def check(distance):
    cows = 1
    last_cow_coord = coords[0]
    for coord in coords:
        if coord - last_cow_coord >= distance:
            cows += 1
            last_cow_coord = coord

    return cows >= k


n, k = map(int, input().split())
coords = list(map(int, input().split()))

left = 0
right = coords[-1] - coords[0] + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
