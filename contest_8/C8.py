import math


class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.pow = 2 ** math.ceil(math.log2(self.n))
        self.tree_size = 2 * self.pow
        self.tree = [0 for _ in range(self.tree_size)]
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.pow + i] = arr[i]

        for i in range(self.pow - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos):
        pos += self.pow

        if self.tree[pos] == 1:
            diff = -1
        else:
            diff = 1

        while pos > 1:
            self.tree[pos] += diff
            pos //= 2

    def query(self, k):
        k += 1
        i = 1
        diff = 0
        while i < self.pow:
            i_left = i * 2
            val_left = self.tree[i_left]
            if k <= val_left + diff:
                i = i_left
            else:
                diff += val_left
                i = i_left + 1

        print(i - self.pow)


n, m = map(int, input().split())
arr = tuple(map(int, input().split()))
tree = SegTree(arr)
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        tree.update(b)
    else:
        tree.query(b)
