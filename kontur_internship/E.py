import sys


class DisjointSet:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.dct = {}
        self.build()

    def build(self):
        for i in range(self.n):
            for j in range(self.m):
                self.dct[(i, j)] = [(i, j), 1]

    def leader(self, v: tuple):
        if self.dct[v][0] == v:
            return v
        else:
            self.dct[v][0] = self.leader(self.dct[v][0])
            return self.dct[v][0]

    def union(self, a: tuple, b: tuple):
        a, b = self.leader(a), self.leader(b)

        if a == b:
            return

        if self.dct[a][1] > self.dct[b][1]:
            a, b = b, a

        self.dct[a][0] = b
        self.dct[b][1] += self.dct[a][1]


def main() -> None:
    n, m, q = map(int, sys.stdin.readline().split())
    field = []
    for _ in range(n):
        row = []
        for c in sys.stdin.readline().rstrip():
            row.append(c)
        field.append(row)

    dis_set = DisjointSet(n, m)
    for row in range(n):
        for col in range(m):
            if field[row][col] == "X":
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < n and 0 <= new_col < m and field[new_row][new_col] == "X":
                        dis_set.union((row, col), (new_row, new_col))

    for _ in range(q):
        row, col = map(int, sys.stdin.readline().split())
        row -= 1
        col -= 1

        if field[row][col] == ".":
            print("MISS")
        else:
            leader = dis_set.leader((row, col))
            dis_set.dct[leader][1] -= 1
            if dis_set.dct[leader][1] == 0:
                print("DESTROY")
            else:
                print("HIT")


if __name__ == "__main__":
    main()
