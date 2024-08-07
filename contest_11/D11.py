L, n = map(int, input().split())
cuts = [0] + list(map(int, input().split())) + [L]
length = n + 2

dp = [[0 for _ in range(length)] for _ in range(length)]
for k in range(2, length):
    l, r = 0, k
    while r < length:
        dp[l][r] = cuts[r] - cuts[l] + min([dp[l][i] + dp[i][r] for i in range(l + 1, r)])
        l += 1
        r += 1

print(dp[0][-1])
