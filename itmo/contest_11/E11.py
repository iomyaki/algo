import sys

WHITE, GREY, BLACK = 0, 1, 2


def dfs(v: int, graph: list, colors: list) -> int | None:
    stack = [(v, 0)]

    while stack:
        current, state = stack.pop()

        if state == 0:
            colors[current] = GREY
            for u in graph[current][0]:
                graph[u][1] = current
                if colors[u] == WHITE:
                    stack.append((current, 0))
                    stack.append((u, 0))
                    break
                elif colors[u] == BLACK:
                    continue
                else:
                    return u
            else:
                stack.append((current, 1))
        else:
            colors[current] = BLACK


def traceback(v: int, graph: list):
    path = []
    curr = graph[v][1]
    while curr != v:
        path.append(curr)
        curr = graph[curr][1]

    path.reverse()
    return [v] + path


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [[set(), -1] for _ in range(n + 1)]
    colors = [WHITE for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u][0].add(v)

    answer = None
    for v in range(1, n + 1):
        if colors[v] == 0:
            answer = dfs(v, graph, colors)
            if answer is not None:
                break

    if answer is not None:
        print("YES")
        print(*traceback(answer, graph))
    else:
        print("NO")


if __name__ == "__main__":
    main()
