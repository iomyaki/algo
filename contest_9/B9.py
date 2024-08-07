import sys
from math import log2, ceil, floor


class SegTree:
    def __init__(self, n):
        self.levels = ceil(log2(n))
        self.n = 2 ** self.levels
        self.range = range(self.levels, 0, -1)
        self.tree_len = 2 * self.n
        self.tree = [0 for _ in range(self.tree_len)]
        self.prom_set = [-1 for _ in range(self.tree_len)]
        self.prom_add = [0 for _ in range(self.tree_len)]

    def update(self, pos, val):
        self.tree[pos] = val
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
            pos //= 2

    def push(self, pos):
        for i in self.range:
            parent = pos // 2 ** i

            if parent != 0 and self.prom_set[parent] != -1:
                promise = self.prom_set[parent]
                self.prom_set[parent] = -1

                j = self.levels - floor(log2(parent))
                ch_theor = 2 ** (j - 1)

                left_parent = parent * 2
                children = max(0, min(ch_theor, ch_theor - ((left_parent * 2 ** (j - 1) + ch_theor - 1) - (n + self.n - 1))))
                self.tree[left_parent] = promise * children
                self.prom_set[left_parent] = promise
                self.prom_add[left_parent] = 0

                right_parent = parent * 2 + 1
                children = max(0, min(ch_theor, ch_theor - ((right_parent * 2 ** (j - 1) + ch_theor - 1) - (n + self.n - 1))))
                self.tree[right_parent] = promise * children
                self.prom_set[right_parent] = promise
                self.prom_add[right_parent] = 0

            if parent != 0 and self.prom_add[parent] != 0:
                promise = self.prom_add[parent]
                self.prom_add[parent] = 0

                j = self.levels - floor(log2(parent))
                ch_theor = 2 ** (j - 1)

                left_parent = parent * 2
                children = max(0, min(ch_theor, ch_theor - ((left_parent * 2 ** (j - 1) + ch_theor - 1) - (n + self.n - 1))))
                self.tree[left_parent] += promise * children
                self.prom_add[left_parent] += promise

                right_parent = parent * 2 + 1
                children = max(0, min(ch_theor, ch_theor - ((right_parent * 2 ** (j - 1) + ch_theor - 1) - (n + self.n - 1))))
                self.tree[right_parent] += promise * children
                self.prom_add[right_parent] += promise

    def set(self, left, right, val):
        left = left + self.n
        right = right + self.n

        while left <= right:
            if left % 2 == 1:
                level = self.levels - floor(log2(left))
                ch_theor = 2 ** level
                children = max(0, min(ch_theor, ch_theor - ((left * 2 ** level + ch_theor - 1) - (n + self.n - 1))))

                self.push(left)
                self.prom_set[left] = val
                self.prom_add[left] = 0
                self.update(left, val * children)
                left += 1

            if right % 2 == 0:
                level = self.levels - floor(log2(right))
                ch_theor = 2 ** level
                children = max(0, min(ch_theor, ch_theor - ((left * 2 ** level + ch_theor - 1) - (n + self.n - 1))))

                self.push(right)
                self.prom_set[right] = val
                self.prom_add[right] = 0
                self.update(right, val * children)
                right -= 1

            left //= 2
            right //= 2

    def add(self, left, right, val):
        left = left + self.n
        right = right + self.n

        while left <= right:
            if left % 2 == 1:
                level = self.levels - floor(log2(left))
                ch_theor = 2 ** level
                children = max(0, min(ch_theor, ch_theor - ((left * 2 ** level + ch_theor - 1) - (n + self.n - 1))))

                self.push(left)
                self.prom_add[left] += val
                self.update(left, self.tree[left] + val * children)
                left += 1

            if right % 2 == 0:
                level = self.levels - floor(log2(right))
                ch_theor = 2 ** level
                children = max(0, min(ch_theor, ch_theor - ((left * 2 ** level + ch_theor - 1) - (n + self.n - 1))))

                self.push(right)
                self.prom_add[right] += val
                self.update(right, self.tree[right] + val * children)
                right -= 1

            left //= 2
            right //= 2

    def query(self, left, right):
        left = left + self.n
        right = right + self.n

        summ = 0
        while left <= right:
            if left % 2 == 1:
                self.push(left)
                summ += self.tree[left]
                left += 1

            if right % 2 == 0:
                self.push(right)
                summ += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        print(summ)


n, m = map(int, sys.stdin.readline().split())
tree = SegTree(n)
for qq in range(m):
    q = tuple(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        tree.set(q[1], q[2] - 1, q[3])
    elif q[0] == 2:
        tree.add(q[1], q[2] - 1, q[3])
    else:
        tree.query(q[1], q[2] - 1)
