import sys


def dfs(root):
    used.add(root)
    comp.append(root)
    for node in graph[root]:
        if node not in used:
            dfs(node)


sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

graph = {i + 1: [] for i in range(n)}
all_nodes = graph.keys()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

used = set()
components = []
n_comp = 0
for node in all_nodes:
    if node not in used:
        comp = []
        dfs(node)
        components.append(comp)
        n_comp += 1

print(n_comp)
for comp in components:
    print(len(comp))
    print(*sorted(comp))
