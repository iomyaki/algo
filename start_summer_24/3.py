def dfs(root):
    used.add(root)
    print(' ' * 2 * root[1] + root[0])
    for node in graph[root]:
        if node not in used:
            dfs(node)


n = int(input())
graph = {}
for j in range(n):
    names = input().split('/')

    if j == 0:
        root = (names[0], 0)
        graph[root] = set()

    for i in range(1, len(names)):
        if (names[i - 1], i - 1) not in graph:
            graph[(names[i - 1], i - 1)] = set()
        if (names[i], i) not in graph:
            graph[(names[i], i)] = set()
        graph[(names[i - 1], i - 1)].add((names[i], i))

for key in graph:
    graph[key] = sorted(graph[key])

used = set()
dfs(root)
