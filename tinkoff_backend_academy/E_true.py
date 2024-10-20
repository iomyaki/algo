def dfs(graph, colors, answer, v):
    colors[v] = "grey"
    for u in graph[v]:
        if colors[u] == "white":
            dfs(graph, colors, answer, u)
        else:
            return
    colors[v] = "black"
    answer.append(v)


def main():
    n, m = map(int, input().split())
    graph = {i: set() for i in range(1, n + 1)}
    colors = {i: "white" for i in range(1, n + 1)}
    answer = []

    # filling the graph
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)

    # topological sorting
    for i in range(1, n + 1):
        if colors[i] == "white":
            dfs(graph, colors, answer, i)

    # answering
    if len(answer) == n:
        print("Yes")
        print(*answer[::-1])
    else:
        print("No")


if __name__ == "__main__":
    main()
