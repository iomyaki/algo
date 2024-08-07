n, m = map(int, input().split())

graph = [set() for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].add(b)

guess = list(map(int, input().split()))[::-1]

used = set()
for node in guess:
    if graph[node - 1] <= used:
        used.add(node)
    else:
        print('NO')
        break
else:
    print('YES')
