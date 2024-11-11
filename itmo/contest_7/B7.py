import sys


def main() -> None:
    n = int(sys.stdin.readline())

    # prepare dp array
    dp = [0 for _ in range(3 * n + 1)]
    dp[n] = 0
    for i in range(n + 1, 3 * n + 1):
        dp[i] = float("inf")

    # count the minimal number of actions
    for x in range(n - 1, -1, -1):
        dp[x] = min(dp[x + 1], dp[2 * x], dp[3 * x]) + 1
    print(dp[1])

    # restore the answer
    pos = 1
    while pos <= n:
        print(pos, end=" ")
        minimum = min(dp[pos + 1], dp[2 * pos], dp[3 * pos])
        if dp[pos + 1] == minimum:
            pos += 1
        elif dp[2 * pos] == minimum:
            pos *= 2
        else:
            pos *= 3


if __name__ == "__main__":
    main()
