import sys

WHITE, GREY, BLACK = 0, 1, 2


def dfs(v: int, graph: list, colors: list, answer: list) -> None:
    stack = [(v, 0)]

    while stack:
        current, state = stack.pop()

        if state == 0:
            colors[current] = GREY
            for u in graph[current]:
                if colors[u] == WHITE:
                    stack.append((current, 0))
                    stack.append((u, 0))
                    break
                elif colors[u] == BLACK:
                    continue
                else:
                    return
            else:
                stack.append((current, 1))
        else:
            colors[current] = BLACK
            answer.append(current)


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    graph = [set() for _ in range(n + 1)]
    colors = [WHITE for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].add(v)

    answer = []
    for v in range(1, n + 1):
        if colors[v] == 0:
            dfs(v, graph, colors, answer)

    if len(answer) == n:
        print(*answer[::-1])
    else:
        print(-1)


if __name__ == "__main__":
    main()
