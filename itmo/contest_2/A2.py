def main():
    n = int(input())
    dx = [-10 ** 9, 10 ** 9]
    dy = [-10 ** 9, 10 ** 9]
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 < dx[1] and x2 > dx[0] and y1 < dy[1] and y2 > dy[0]:
            dx[0] = max(dx[0], x1)
            dx[1] = min(dx[1], x2)
            dy[0] = max(dy[0], y1)
            dy[1] = min(dy[1], y2)
        else:
            print(0)
            return
    area = (dx[1] - dx[0]) * (dy[1] - dy[0])
    if area > 0:
        print(area)
    else:
        print(0)


if __name__ == "__main__":
    main()
