n, m = map(int, input().split())

d = [[0 for _ in range(m + 3)] for _ in range(n + 3)]
d[2][2] = 1

for k in range(3, n + m + 1):
    x = min(m + 1, k)
    y = k - x + 2
    while x != 1 and y != n + 2:
        d[y][x] = d[y - 1][x - 2] + d[y - 2][x - 1] + d[y + 1][x - 2] + d[y - 2][x + 1]
        x -= 1
        y += 1

print(d[-2][-2])
