from collections import deque


def bfs(root):
    depths = {substance: -1 for substance in substances}
    depths[root] = 0

    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if depths[w] == -1:
                queue.append(w)
                depths[w] = depths[v] + 1

                if w == finish:
                    return depths[w]

    return -1


m = int(input())

graph = {}
substances = set()
for _ in range(m):
    a, b = input().split(' -> ')
    if a not in substances:
        graph[a] = []
        substances.add(a)
    if b not in substances:
        graph[b] = []
        substances.add(b)
    graph[a].append(b)

start = input()
finish = input()

if start not in substances or finish not in substances:
    print(-1)
elif start == finish:
    print(0)
else:
    print(bfs(start))
