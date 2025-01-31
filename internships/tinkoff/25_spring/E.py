import sys


def get_range_sum(l: int, r: int, prefix: list[int]) -> int:
    return prefix[r] - prefix[l - 1] if l else prefix[r]


def main() -> None:
    n, s = map(int, sys.stdin.readline().split())
    bar = tuple(map(int, sys.stdin.readline().split()))

    prefix = [0 for _ in range(n)]
    prefix[0] = bar[0]
    for i in range(1, n):
        prefix[i] = bar[i] + prefix[i - 1]

    dp = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if get_range_sum(i, n - 1, prefix) <= s:
            dp[i] = n - i
            continue

        l, r = i, n - 1
        while r > l:
            mid = l + (r - l) // 2
            if get_range_sum(i, mid, prefix) <= s:
                l = mid + 1
            else:
                r = mid

        dp[i] = dp[l] + n - i

    print(sum(dp))


if __name__ == "__main__":
    main()
