import sys
from math import log2, ceil


def dfs(v):
    global time, depth, max_depth

    max_depth = max(depth, max_depth)

    used.add(v)
    graph[v][1][0] = time
    for u in graph[v][0]:
        if u[0] not in used:
            time += 1
            depth += 1
            dfs(u[0])
    graph[v][1][1] = time
    time += 1
    depth -= 1


def check_ancestry(a, b):
    a_in, a_out = graph[a][1][0], graph[a][1][1]
    b_in, b_out = graph[b][1][0], graph[b][1][1]

    return a_in <= b_in <= b_out <= a_out


def build_bin_up():
    max_pow_2 = ceil(log2(max_depth))
    bin_up = [[[0, float('inf')] for _ in range(max_pow_2 + 1)] for _ in range(n)]

    for j in range(1, n):
        bin_up[j][0][0], bin_up[j][0][1] = ancestors[j]

    for v in range(1, n):
        for pow in range(1, max_pow_2 + 1):
            bin_up[v][pow][0] = bin_up[bin_up[v][pow - 1][0]][pow - 1][0]
            bin_up[v][pow][1] = min(bin_up[v][pow - 1][1], bin_up[bin_up[v][pow - 1][0]][pow - 1][1])

    return max_pow_2, bin_up


sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
ancestors = [None]
graph = {i: [[], [None, None]] for i in range(n)}
for v in range(1, n):
    u, w = map(int, sys.stdin.readline().split())
    ancestors.append((u, w))
    graph[v][0].append((u, w))
    graph[u][0].append((v, w))

# get entry and exit times for each vertex during DFS; also find the depth of a tree
depth = 0
max_depth = float('-inf')
used = set()
time = 0
dfs(0)

# get bin-up matrix
max_pow_2, bin_up = build_bin_up()

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    res = float('inf')

    for pow in range(max_pow_2, -1, -1):
        ancestor_a = bin_up[a][pow][0]
        if not check_ancestry(ancestor_a, b):
            res = min(res, bin_up[a][pow][1])
            a = ancestor_a

    if not check_ancestry(a, b):
        res = min(res, bin_up[a][0][1])

    for pow in range(max_pow_2, -1, -1):
        ancestor_b = bin_up[b][pow][0]
        if not check_ancestry(ancestor_b, a):
            res = min(res, bin_up[b][pow][1])
            b = ancestor_b

    if not check_ancestry(b, a):
        res = min(res, bin_up[b][0][1])

    print(res)
