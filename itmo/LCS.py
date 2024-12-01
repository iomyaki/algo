import sys


def main() -> None:
    seq_1 = tuple(map(int, sys.stdin.readline().split()))
    seq_2 = tuple(map(int, sys.stdin.readline().split()))
    n, m = len(seq_1), len(seq_2)

    dp = [[float("-inf") for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
            if seq_1[i] == seq_2[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)

    max_len = 0
    for i in range(n + 1):
        for j in range(m + 1):
            max_len = max(max_len, dp[i][j])

    print(max_len)


if __name__ == "__main__":
    main()
