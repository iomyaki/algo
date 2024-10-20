def main():
    n, m = map(int, input().split())
    arr = [[['.', None] for _ in range(m + 1)]]
    for _ in range(n):
        row = [['.', None]]
        for square in input():
            row.append([square, None])
        arr.append(row)

    for i in range(n):
        for j in range(m):
            x = arr[i][j]
            if x == '-':
                arr[i][j] = 0
            elif x == 'S':
                arr[i][j] = 1
            elif x == 'X':
                arr[i][j] = 2

    used = [[False] * m for _ in range(n)]
    vec = []
    ships = [0, 0, 0]

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not used[i][j]:
                used[i][j] = True
                vec.append((i, j))
                nS, nX = 0, 0
                while vec:
                    tmp = vec.pop()
                    if arr[tmp[0]][tmp[1]] == 1:
                        nS += 1
                    else:
                        nX += 1
                    for x_ in range(-1, 2):
                        for y_ in range(-1, 2):
                            if abs(x_) + abs(y_) == 1:
                                xt = tmp[0] + x_
                                yt = tmp[1] + y_
                                if 0 <= xt < n and 0 <= yt < m:
                                    if not used[xt][yt] and arr[xt][yt]:
                                        used[xt][yt] = True
                                        vec.append((xt, yt))
                if nX == 0:
                    ships[0] += 1
                elif nS == 0:
                    ships[2] += 1
                else:
                    ships[1] += 1

    for i in ships:
        print(i, end=" ")


if __name__ == "__main__":
    main()
