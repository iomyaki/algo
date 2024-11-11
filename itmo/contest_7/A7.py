import sys


def main() -> None:
    n = int(sys.stdin.readline())
    stairs = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(n + 1)]
    dp[1] = stairs[1]

    for i in range(2, n + 1):
        dp[i] = stairs[i] + max(dp[i - 1], dp[i - 2])

    print(dp[-1])


if __name__ == "__main__":
    main()
