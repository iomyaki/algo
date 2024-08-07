def ternary(q):
    nums = []
    while q:
        q, r = divmod(q, 3)
        nums.append(str(r))

    return '0' * (m - len(nums)) + ''.join(reversed(nums))


n, m = map(int, input().split())
coins = tuple(sorted(map(int, input().split())))

greater = False
for i in range(1, 3 ** m + 1):
    mask = ternary(i)
    count = []
    for j in range(m):
        mask_j = mask[j]
        if mask_j == '1':
            count.append(coins[j])
        elif mask_j == '2':
            count.extend([coins[j], coins[j]])

    summ = sum(count)
    if summ > n:
        greater = True
    elif summ == n:
        print(len(count))
        print(*count)
        break
else:
    if greater:
        print(0)
    else:
        print(-1)
