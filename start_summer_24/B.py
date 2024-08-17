n, m = map(int, input().split())
image = []
for _ in range(n):
    image.append(list(map(int, input().split())))

rotated = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):  # rows in image
    for j in range(m):  # columns in image
        rotated[j][n - 1 - i] = image[i][j]

for row in rotated:
    print(*row)
