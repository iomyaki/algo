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
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        b, e = map(int, sys.stdin.readline().split())
        graph[b].append(e)
        graph[e].append(b)

    total_sum = 0
    for v in range(1, n + 1):
        total_sum += sum(bfs(graph, v)[1:])

    print(total_sum // 2)


if __name__ == "__main__":
    main()
