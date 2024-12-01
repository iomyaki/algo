import sys


def go(v: int, graph: list[list[int]], dp: list[bool]) -> None:
    stack = [(v, 0)]
    visited = set()

    while stack:
        current, state = stack.pop()

        if state == 0:
            stack.append((current, 1))
            visited.add(current)
            for u in graph[current]:
                if u not in visited:
                    stack.append((u, 0))
        else:
            if not graph[current]:
                dp[current] = False
            else:
                dp[current] = any(not dp[child] for child in graph[current])


def main() -> None:
    n = int(sys.stdin.readline())
    parents = tuple(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n + 1)]
    dp = [False for _ in range(n + 1)]

    for i in range(n):
        graph[parents[i]].append(i + 1)

    root = graph[0][0]
    go(root, graph, dp)

    if dp[root]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
