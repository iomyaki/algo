import sys


def main() -> None:
    n = int(sys.stdin.readline())
    seq_1 = tuple(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    seq_2 = tuple(map(int, sys.stdin.readline().split()))
    l = int(sys.stdin.readline())
    seq_3 = tuple(map(int, sys.stdin.readline().split()))

    dp = [[[float("-inf") for _ in range(l + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(m):
            for k in range(l):
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
                dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k])
                if seq_1[i] == seq_2[j]:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k])
                if seq_1[i] == seq_3[k]:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k])
                if seq_2[j] == seq_3[k]:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k])
                if seq_1[i] == seq_2[j] == seq_3[k]:
                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k + 1], dp[i][j][k] + 1)

    max_len = 0
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(l + 1):
                max_len = max(max_len, dp[i][j][k])

    print(max_len)


if __name__ == "__main__":
    main()
