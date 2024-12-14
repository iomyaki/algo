import sys
from collections import deque


def bfs(graph: list, start: int) -> list[int]:
    depths = [-1 for _ in range(len(graph))]
    depths[start] = 0

    queue = deque([start])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if depths[u] == -1:
                depths[u] = depths[v] + 1
                queue.append(u)

    return depths


def main() -> None:
    n, s, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[b].append(a)

    print(*bfs(graph, s)[1:])


if __name__ == "__main__":
    main()
