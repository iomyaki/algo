n = int(input())

d = [0 for _ in range(n + 1)]
d[0], d[1] = 1, 3

for i in range(2, n + 1):
    d[i] = 2 * (d[i - 1] + d[i - 2])

print(d[n])