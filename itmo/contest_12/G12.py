import sys
from collections import defaultdict
from heapq import heappush, heappop
from math import sqrt


def dist(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    return sqrt(sum((z1 - z2) * (z1 - z2) for z1, z2 in zip(p1, p2)))


def a_star(graph: defaultdict, start: tuple[int, int], finish: tuple[int, int]) -> int | float:
    if start == finish:
        return .0

    costs = {start: .0}

    heap = []
    heappush(heap, (.0, .0, start))

    while heap:
        _, current_cost, v = heappop(heap)

        if current_cost > costs[v]:
            continue

        if v == finish:
            return costs[v]

        for u in graph[v]:
            cost = costs[v] + dist(v, u)
            if u not in costs or costs[u] > cost:
                costs[u] = cost
                heappush(heap, (cost + dist(u, finish), cost, u))

    return -1


def main() -> None:
    n, d = map(int, sys.stdin.readline().split())
    points = [None] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    graph = defaultdict(set)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if points[i] != points[j] and dist(points[i], points[j]) <= d:
                graph[points[i]].add(points[j])
                graph[points[j]].add(points[i])

    for _ in range(int(sys.stdin.readline().strip())):
        a, b = map(int, sys.stdin.readline().split())
        print(a_star(graph, points[a], points[b]))


if __name__ == "__main__":
    main()
