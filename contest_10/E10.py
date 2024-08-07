import sys
from queue import PriorityQueue


def Dijkstra(n: int, graph: dict):
    d = {i: float('inf') for i in range(1, n + 1)}
    d[1] = 0

    q = PriorityQueue()
    q.put((0, 1))

    while not q.empty():
        current_d, v = q.get()

        # speedup
        if current_d > d[v]:
            continue

        for u, w in graph[v]:
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                q.put((d[u], u))

    return d.values()


n, m = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v].append((u, w))
    graph[u].append((v, w))

print(*Dijkstra(n, graph))
