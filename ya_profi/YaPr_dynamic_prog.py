"""
Move from top left to the bottom right cell in a matrix, collecting the largest sum possible.
You allowed to move only to the right or diagonally to the right-down.
"""

n = int(input())
m = int(input())
matrix = []

for i in range(n):
    line = list(map(int, input().replace(',', '').split()))
    matrix.append(line)

summ = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, m + 1):
        if x >= y:
            summ[y][x] = max(summ[y][x - 1], summ[y - 1][x - 1]) + matrix[y - 1][x - 1]
        else:
            summ[y][x] = 0

print(summ[n][m])
