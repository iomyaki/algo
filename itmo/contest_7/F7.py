import sys


def main() -> None:
    m, n = map(int, sys.stdin.readline().split())
    f = [[float("inf") for _ in range(m + 1)]]
    for _ in range(n):
        f.append([float("inf")] + list(map(int, sys.stdin.readline().split())))

    dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) != (1, 1):
                dp[i][j] = min(
                    abs(f[i][j] - f[i][j - 1]) + dp[i][j - 1],
                    abs(f[i][j] - f[i - 1][j]) + dp[i - 1][j],
                )

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
