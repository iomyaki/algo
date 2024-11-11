import sys


def main() -> None:
    n = int(sys.stdin.readline())
    seq = tuple(map(int, sys.stdin.readline().split()))

    dp = [1 for _ in range(n)]
    for i in range(1, n):
        subseq_len = 0
        for j in range(i):
            if seq[i] % seq[j] == 0:
                subseq_len = max(subseq_len, dp[j])
        dp[i] = 1 + subseq_len

    print(max(dp))


if __name__ == "__main__":
    main()
