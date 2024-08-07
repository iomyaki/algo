n = int(input())
costs = tuple(map(int, input().split()))

if n == 1:
    print(costs[0])
else:
    d = [0 for _ in range(n)]
    d[0], d[1] = costs[0], costs[1]

    for i in range(2, n):
        d[i] = min(d[i - 1], d[i - 2]) + costs[i]

    print(d[-1])
