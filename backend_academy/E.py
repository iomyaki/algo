def hamilton_path(graph, start_v):
    size = len(graph)
    to_visit = [None, start_v]
    path = []
    while to_visit:
        v = to_visit.pop()
        if v:
            path.append(v)
            if len(path) == size:
                break
            for x in graph[v] - set(path):
                to_visit.append(None)
                to_visit.append(x)
        else:
            path.pop()

    return path


def main():
    n, m = map(int, input().split())
    graph = {i + 1: set() for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            print("No")
            return
        graph[a].add(b)

    for i in range(1, n + 1):
        path = hamilton_path(graph, i)
        if path:
            print("Yes")
            print(*path)
            return
    else:
        print("No")


if __name__ == "__main__":
    main()
