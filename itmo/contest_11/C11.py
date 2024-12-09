import sys


def dfs(v: int, graph: list, lengths: list, visited: set) -> None:
    stack = [v]
    visited.add(v)

    while stack:
        current = stack.pop()

        for u in graph[current]:
            if lengths[current] + 1 > lengths[u]:
                lengths[u] = lengths[current] + 1
                stack.append(u)


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        graph[v].add(u)

    lengths = [0 for _ in range(n + 1)]
    visited = set()
    for v in range(1, n + 1):
        if v not in visited:
            dfs(v, graph, lengths, visited)

    print(max(lengths))


if __name__ == "__main__":
    main()
