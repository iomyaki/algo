import sys


def main() -> None:
    n = int(sys.stdin.readline().rstrip())
    dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    max_collinear = 0
    for i in range(n):
        for j in range(i + 1, n):
            collinear = 0
            for k in range(n):
                if (dots[k][0] - dots[i][0]) * (dots[j][1] - dots[i][1]) == (dots[k][1] - dots[i][1]) * (dots[j][0] - dots[i][0]):
                    collinear += 1
            max_collinear = max(max_collinear, collinear)

    if max_collinear <= (2 * n) // 3:
        print(n // 3)
    else:
        print(n - max_collinear)


if __name__ == "__main__":
    main()
