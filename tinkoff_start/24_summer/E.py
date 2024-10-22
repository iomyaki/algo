n = int(input())
forest = [[0 for _ in range(5)]]
dec = {'W': -1, '.': 0, 'C': 1}
impassible = n
for k in range(n):
    inp = input()

    if inp == 'WWW':
        impassible = k

    forest.append([-1, dec[inp[0]], dec[inp[1]], dec[inp[2]], -1])

d = [[0 for _ in range(5)]] + [[-1, 0, 0, 0, -1] for _ in range(n)]

#current_max = -1
for i in range(1, n + 1):
    for j in range(1, 4):
        if forest[i][j] == -1:
            d[i][j] = -1
        else:
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j], d[i - 1][j + 1]) + forest[i][j]
            #current_max = max(current_max, d[i][r])

possible = max(d[impassible])
if possible >= 0:
    print(possible)
else:
    print(0)
