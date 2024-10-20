def dfs(root):
    global cycle

    colors[root - 1] = 'grey'
    for node in graph[root]:
        if colors[node - 1] == 'white':
            dfs(node)
        elif colors[node - 1] == 'grey':
            cycle = True
            return
    colors[root - 1] = 'black'


n, m = map(int, input().split())

graph = {i + 1: [] for i in range(n)}
colors = ['white' for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

cycle = False
for i in range(n):
    if colors[i] == 'white':
        dfs(i + 1)

if cycle:
    print(1)
else:
    print(0)
