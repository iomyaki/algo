import math


class SegTree:
    def __init__(self, arr):
        self.n = 2 ** math.ceil(math.log2(len(arr)))
        self.tree_size = 2 * self.n
        self.tree = [float('-inf') for _ in range(self.tree_size)]
        self.build(arr)

    def build(self, arr):
        for i in range(n):
            self.tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, pos, val):
        pos += self.n
        self.tree[pos] = val
        pos //= 2
        while pos > 0:
            self.tree[pos] = max(self.tree[pos * 2], self.tree[pos * 2 + 1])
            pos //= 2

    def descend(self, idx, x):
        i = idx
        while i < self.n:
            if self.tree[i * 2] >= x:
                i *= 2
            else:
                i = i * 2 + 1

        return i

    def query(self, x, l):
        left = self.n + l
        right = self.n + n - 1

        min_i = float('inf')

        while left < right:
            if left % 2 == 1:
                if self.tree[left] >= x:
                    min_i = min(min_i, self.descend(left, x))
                left += 1

            if right % 2 == 0:
                if self.tree[right] >= x:
                    min_i = min(min_i, self.descend(right, x))
                right -= 1

            left //= 2
            right //= 2

            if left == right - 1:
                if self.tree[left] >= x:
                    min_i = min(min_i, self.descend(left, x))
                elif self.tree[right] >= x:
                    min_i = min(min_i, self.descend(right, x))
                break

        if left == right and self.tree[left] >= x:
            min_i = min(min_i, self.descend(left, x))

        if min_i == float('inf'):
            print(-1)
        else:
            print(min_i - self.n)


n, m = map(int, input().split())
arr = tuple(map(int, input().split()))
tree = SegTree(arr)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(b, c)
    else:
        tree.query(b, c)
