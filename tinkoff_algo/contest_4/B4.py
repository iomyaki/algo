n, m, k = map(int, input().split())

prefix_matrix = []

row = tuple(map(int, input().split()))

prefix_sum = [row[0]]
for i in range(1, m):
    prefix_sum.append(prefix_sum[i - 1] + row[i])
prefix_matrix.append(prefix_sum)

for j in range(1, n):
    row = tuple(map(int, input().split()))

    prefix_sum = [row[0]]
    for i in range(1, m):
        prefix_sum.append(prefix_sum[i - 1] + row[i])

    resulting_pref = []
    for i in range(m):
        resulting_pref.append(prefix_sum[i] + prefix_matrix[j - 1][i])
    prefix_matrix.append(resulting_pref)

print(*prefix_matrix, sep=' ')

for _ in range(k):
    x_1, y_1, x_2, y_2 = map(lambda x: x - 1, map(int, input().split()))
    if x_1 - 1 == -1 and y_1 - 1 == -1:
        print(prefix_matrix[x_2][y_2])
    elif x_1 - 1 == -1:
        print(prefix_matrix[x_2][y_2] - prefix_matrix[x_2][y_1 - 1])
    elif y_1 - 1 == -1:
        print(prefix_matrix[x_2][y_2] - prefix_matrix[x_1 - 1][y_2])
    else:
        print(prefix_matrix[x_2][y_2] - prefix_matrix[x_2][y_1 - 1] - prefix_matrix[x_1 - 1][y_2] + prefix_matrix[x_1 - 1][y_1 - 1])
