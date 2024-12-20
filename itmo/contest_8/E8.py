import sys

CLOSING = {")", "]", "}"}
PAIRS = {"()", "[]", "{}"}


def main() -> None:
    s = sys.stdin.readline().rstrip()
    n = len(s)
    dp = [["" for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            for l in range(i, i + length):
                if s[l] in CLOSING:
                    continue
                for r in range(l + 1, i + length):
                    if s[l] + s[r] in PAIRS:
                        new_s = dp[i][max(i, l - 1)] + s[l] + dp[l + 1][r - 1] + s[r] + dp[min(j, r + 1)][j]
                        if len(new_s) > len(dp[i][j]):
                            dp[i][j] = new_s

    print(dp[0][-1])


if __name__ == "__main__":
    main()
