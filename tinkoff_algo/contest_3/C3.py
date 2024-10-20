from collections import deque


def create_adjacency_list(ancestors):
    n = len(ancestors)
    adj_list = {i: [] for i in range(n)}

    for i in range(n):
        parent = ancestors[i]
        if parent is not None:
            adj_list[parent].append(i)
            adj_list[i].append(parent)

    return list(adj_list.values())


def bfs(adj_list, s):
    level = [-1] * len(adj_list)

    level[s] = 0
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for w in adj_list[v]:
            if level[w] == -1:
                queue.append(w)
                level[w] = level[v] + 1

    return level


def lca(u, v):
    global ancestors, depths

    h_1 = depths[u]
    h_2 = depths[v]

    while h_1 != h_2:
        if h_1 > h_2:
            u = ancestors[u]
            h_1 -= 1
        else:
            v = ancestors[v]
            h_2 -= 1

    while u != v:
        u = ancestors[u]
        v = ancestors[v]

    return u


_ = input()
ancestors = [None] + list(map(int, input().split()))
adj_list = create_adjacency_list(ancestors)
depths = bfs(adj_list, 0)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v))
