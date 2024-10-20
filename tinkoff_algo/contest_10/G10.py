import sys
from queue import PriorityQueue


def Dijkstra(n: int, s: int, graph: dict):
    d = {i: float('inf') for i in range(1, n + 1)}
    d[s] = 0

    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        current_d, v = q.get()

        # speedup
        if current_d > d[v]:
            continue

        for u, w in graph[v]:
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                q.put((d[u], u))

    return d


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        v, u, w = map(int, sys.stdin.readline().split())
        graph[v].append((u, w))
        graph[u].append((v, w))
    a, b, c = map(int, sys.stdin.readline().split())

    d_a, d_b, d_c = Dijkstra(n, a, graph), Dijkstra(n, b, graph), Dijkstra(n, c, graph)

    answer = float('inf')
    for x in range(1, n + 1):
        a_x, b_x, c_x = d_a[x], d_b[x], d_c[x]
        if a_x != float('inf') or b_x != float('inf') or c_x != float('inf'):
            answer = min(answer, 2 * a_x + b_x + c_x, 2 * b_x + a_x + c_x, 2 * c_x + a_x + b_x)

    if answer != float('inf'):
        print(answer)
    else:
        print(-1)


if __name__ == '__main__':
    main()
