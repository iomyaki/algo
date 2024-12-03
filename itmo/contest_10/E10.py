import sys
from math import dist as dst
from queue import PriorityQueue


def dijkstra(graph: dict, start: tuple[int, int]) -> dict:
    maxima = {v: float("inf") for v in graph}
    maxima[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        current_d, v = queue.get()

        if current_d > maxima[v]:
            continue

        for u, w in graph[v]:
            if maxima[u] > max(maxima[v], w):
                maxima[u] = max(maxima[v], w)
                queue.put((maxima[u], u))

    return maxima


def main() -> None:
    h, n = map(int, sys.stdin.readline().split())
    hillocks = []
    for _ in range(n):
        hillocks.append(tuple(map(int, sys.stdin.readline().split())))

    graph = {i: [] for i in hillocks}
    for i in range(n):
        hillock = hillocks[i]
        for j in range(i + 1, n):
            another = hillocks[j]

            distance = dst(hillock, another)
            graph[hillock].append((another, distance))
            graph[another].append((hillock, distance))
    del hillocks

    start, finish = (0, 0), (0, h)
    graph[start], graph[finish] = [], []
    for v in graph:
        if v != start and v != finish:
            graph[v].append((start, v[1]))
            graph[v].append((finish, h - v[1]))
            graph[start].append((v, v[1]))
            graph[finish].append((v, h - v[1]))

    print(dijkstra(graph, start)[finish])


if __name__ == "__main__":
    main()
