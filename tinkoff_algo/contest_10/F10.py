import sys
from queue import PriorityQueue


def Dijkstra(n: int, cups: int, graph: dict):
    time = {i: float('inf') for i in range(1, n + 1)}
    time[1] = 0
    weight = 3000000 + cups * 100

    q = PriorityQueue()
    q.put((0, 1))

    while not q.empty():
        current_t, v = q.get()

        # speedup
        if current_t > time[v]:
            continue

        for u, t, w in graph[v]:
            if weight <= w and time[u] > time[v] + t:
                time[u] = time[v] + t
                q.put((time[u], u))

    return time


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        v, u, t, w = map(int, sys.stdin.readline().split())
        graph[v].append((u, t, w))
        graph[u].append((v, t, w))

    left = 0
    right = 10000000
    while right - left > 1:
        mid = (left + right) // 2
        time = Dijkstra(n, mid, graph)
        if time[n] <= 1440:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == '__main__':
    main()
