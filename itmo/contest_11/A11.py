import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [set() for _ in range(n + 1)]
    edges = set()
    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        if u > v:
            v, u = u, v

        edges.add((u, v))
        graph[v].add(u)
        graph[u].add(v)

    cnt = 0
    for v, u in edges:
        for w in range(1, n + 1):
            if w != v and w != u and w in graph[v] and w in graph[u]:
                cnt += 1

    print(cnt // 3)


if __name__ == "__main__":
    main()
