import sys


class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.set = {i: [i, 1] for i in range(n)}

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


def main() -> None:
    t = int(sys.stdin.readline())
    max_nums = []
    for _ in range(t):
        n = int(sys.stdin.readline())
        ancestors = dict(enumerate((map(int, sys.stdin.readline().split())), start=1))
        merges = tuple(map(int, sys.stdin.readline().split()))

        dis_set = DisjointSet(n)
        max_num = 0
        for city in merges:
            ancestor = ancestors[city]
            dis_set.union(city, ancestor)
            max_num = max(max_num, dis_set.set[dis_set.leader(city)][1])
            max_nums.append(max_num)

        print(*max_nums)
        del max_nums[:]


if __name__ == "__main__":
    main()
