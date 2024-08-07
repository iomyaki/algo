import sys


class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.set = {i: [i, 1] for i in range(1, n + 1)}

    def leader(self, v: int):
        if self.set[v][0] == v:
            return v
        else:
            self.set[v][0] = self.leader(self.set[v][0])
            return self.set[v][0]

    def union(self, a: int, b: int):
        a, b = self.leader(a), self.leader(b)

        if a == b:
            return

        if self.set[a][1] > self.set[b][1]:
            a, b = b, a

        self.set[a][0] = b
        self.set[b][1] += self.set[a][1]


def Kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    dis_set = DisjointSet(n)
    mst_weight = 0  # minimum spanning tree weight

    for edge in edges:
        a, b = edge[0], edge[1]

        if dis_set.leader(a) != dis_set.leader(b):
            dis_set.union(a, b)
            mst_weight += edge[2]

    return mst_weight


sys.setrecursionlimit(10 ** 9)
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    edges.append(tuple(map(int, sys.stdin.readline().split())))

print(Kruskal(n, edges))
