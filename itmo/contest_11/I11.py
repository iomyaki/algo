import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    edges = {}
    for i in range(m):
        v, u = map(int, sys.stdin.readline().split())

        graph[v].append(u)
        graph[u].append(v)
        edges[(v, u)] = i + 1
        edges[(u, v)] = i + 1

    discovery = [-1 for _ in range(n + 1)]
    lowest = [-1 for _ in range(n + 1)]
    bridges = []
    time = 0
    for root in range(1, n + 1):
        if discovery[root] == -1:
            # DFS starts
            stack_1 = [(root, None)]
            stack_2 = []

            while stack_1:
                v, parent = stack_1.pop()

                if discovery[v] == -1:
                    discovery[v] = lowest[v] = time
                    time += 1
                    stack_2.append((v, parent))

                    for u in graph[v]:
                        if discovery[u] == -1:
                            stack_1.append((u, v))
                        elif u != parent:
                            lowest[v] = min(lowest[v], discovery[u])

            while stack_2:
                v, parent = stack_2.pop()

                if parent is not None:
                    lowest[parent] = min(lowest[parent], lowest[v])

                    if lowest[v] > discovery[parent]:
                        bridges.append(edges[(parent, v)])
            # DFS ends

    bridges = sorted(set(bridges))
    print(len(bridges))
    print(*bridges)


if __name__ == "__main__":
    main()
