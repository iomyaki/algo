import sys


def dfs(s: int, t: int, graph: list, visited: set) -> int | None:
    stack = [s]

    while stack:
        current = stack.pop()

        visited.add(current)
        for u in graph[current][0]:
            if u not in visited:
                graph[u][1] = current
                if u == t:
                    return u
                stack.append(u)


def traceback(s: int, t: int, graph: list):
    path = [t]
    curr = graph[t][1]
    while curr != graph[s][1]:
        path.append(curr)
        curr = graph[curr][1]

    path.reverse()
    return path


def main() -> None:
    n, m, s, t = map(int, sys.stdin.readline().split())
    graph = [[set(), -1] for _ in range(n + 1)]
    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        graph[v][0].add(u)

    visited = set()
    if dfs(s, t, graph, visited) is not None:
        print(*traceback(s, t, graph))
    else:
        print(-1)


if __name__ == "__main__":
    main()
