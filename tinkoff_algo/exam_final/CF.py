n, m = map(int, input().split())
field = [[['.', None] for _ in range(m + 1)]]
for _ in range(n):
    row = [['.', None]]
    for square in input():
        row.append([square, None])
    field.append(row)

ship_count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if field[i][j][0] == '.':
            continue
        elif field[i][j - 1][0] == '.' and field[i - 1][j][0] == '.':
            field[i][j][1] = ship_count
            ship_count += 1
        else:
            if field[i - 1][j][0] != '.':
                field[i][j][1] = field[i - 1][j][1]
                k = j - 1
                while field[i][k][0] != '.':
                    field[i][k][1] = field[i - 1][j][1]
                    k -= 1
            else:
                field[i][j][1] = field[i][j - 1][1]

ships = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if field[i][j][0] != '.':
            if field[i][j][1] in ships:
                ships[field[i][j][1]].add(field[i][j][0])
            else:
                ships[field[i][j][1]] = set(field[i][j][0])

act, wia, kia = 0, 0, 0
for key in ships.keys():
    if len(ships[key]) == 2:
        wia += 1
    elif ships[key] == {'#'}:
        act += 1
    else:
        kia += 1

print(act, wia, kia)
