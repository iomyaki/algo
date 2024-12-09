import sys


def dfs(v: int, graph: list, visited: set, components: list, cnt: int) -> None:
    stack = [(v, 0)]

    while stack:
        current, state = stack.pop()

        if state == 0:
            visited.add(current)
            components[current] = cnt

        for u in graph[current]:
            if u not in visited:
                stack.append((current, 1))
                stack.append((u, 0))
                break


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        graph[v].add(u)
        graph[u].add(v)

    visited = set()
    components = [0 for _ in range(n + 1)]
    cnt = 1
    for v in range(1, n + 1):
        if v not in visited:
            dfs(v, graph, visited, components, cnt)
            cnt += 1

    print(cnt - 1)
    print(*components[1:])


if __name__ == "__main__":
    main()
