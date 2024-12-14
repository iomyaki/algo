import sys
from heapq import heappush, heappop


def dijkstra(graph: list[list[tuple[int, int]]], start: int) -> list[int | float]:
    dists = [float("inf") for _ in range(len(graph))]
    dists[start] = 0

    heap = []
    heappush(heap, (0, start))

    while heap:
        current_dist, v = heappop(heap)

        if current_dist > dists[v]:
            continue

        for u, w in graph[v]:
            if dists[u] > dists[v] + w:
                dists[u] = dists[v] + w
                heappush(heap, (dists[u], u))

    return dists


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    s, t = map(int, sys.stdin.readline().split())
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        b, e, w = map(int, sys.stdin.readline().split())
        graph[b].append((e, w))
        graph[e].append((b, w))

    dists = dijkstra(graph, s)
    target = dists[t]
    if target != float("inf"):
        print(target)
    else:
        print(-1)


if __name__ == "__main__":
    main()
