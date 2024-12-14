import sys
from heapq import heappush, heappop


def dijkstra(graph: list, start: int) -> list[int | float]:
    dists = [float("inf") for _ in range(len(graph))]
    dists[start] = 0

    heap = []
    heappush(heap, (0, start))

    while heap:
        current_dist, v = heappop(heap)

        if current_dist > dists[v]:
            continue

        for u, w in graph[v][0]:
            if dists[u] > dists[v] + w:
                dists[u] = dists[v] + w
                graph[u][1] = v
                heappush(heap, (dists[u], u))

    return dists


def traceback(s: int, f: int, graph: list) -> list:
    path = [f]
    curr = graph[f][1]
    while curr != graph[s][1]:
        path.append(curr)
        curr = graph[curr][1]

    path.reverse()
    return path


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    s, f = map(int, sys.stdin.readline().split())
    graph = [[[], None] for _ in range(n + 1)]
    for _ in range(m):
        b, e, w = map(int, sys.stdin.readline().split())
        graph[b][0].append((e, w))
        graph[e][0].append((b, w))

    dists = dijkstra(graph, s)
    target = dists[f]
    if target != float("inf"):
        print(target)
        print(*traceback(s, f, graph))
    else:
        print(-1)


if __name__ == "__main__":
    main()
