import sys


def main() -> None:
    n = int(sys.stdin.readline())
    w = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        w.append([0] + list(map(int, sys.stdin.readline().split())))

    dp = [[[float("inf"), -1] for _ in range(n + 1)] for _ in range(1 << (n + 1))]
    dp[0][0][0] = 0

    for mask in range(1 << (n + 1)):
        for v in range(n + 1):
            for u in range(n + 1):
                if u != v and (1 << u) & mask == 0 and dp[mask][v][0] + w[v][u] < dp[mask ^ (1 << u)][u][0]:
                    dp[mask ^ (1 << u)][u][0] = dp[mask][v][0] + w[v][u]
                    dp[mask ^ (1 << u)][u][1] = v

    print(dp[(1 << (n + 1)) - 1][0][0])

    mask = (1 << (n + 1)) - 1
    curr = 0
    prev = dp[mask][curr][1]
    while prev != 0:
        print(prev, end=" ")

        mask = mask ^ (1 << curr)
        curr = prev
        prev = dp[mask][curr][1]


if __name__ == "__main__":
    main()
