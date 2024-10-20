n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [[0 for _ in range(m)] for _ in range(n)]

for j in range(m):
    d[0][j] = arr[0][j]
for i in range(n):
    d[i][0] = arr[i][0]

max_val = 1
i_max = 0
j_max = 0
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + arr[i][j]
        else:
            d[i][j] = 0

        if d[i][j] >= max_val:
            max_val = d[i][j]
            i_max = i
            j_max = j

print(max_val)
print(i_max - max_val + 2, j_max - max_val + 2)
