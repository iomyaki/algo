class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree_size = 2 * self.n
        self.tree = [None] * self.tree_size
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = [arr[i], 1]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.compose(self.tree[i * 2], self.tree[i * 2 + 1])

    def compose(self, left, right):
        if left[0] < right[0]:
            return left
        elif left[0] > right[0]:
            return right
        else:
            return [left[0], left[1] + right[1]]

    def update(self, pos, new_val):
        pos += self.n
        self.tree[pos] = [new_val, 1]
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.compose(self.tree[pos * 2], self.tree[pos * 2 + 1])
            pos //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        answer = [float('inf'), 0]
        while left <= right:
            if left % 2 == 1:
                answer = self.compose(answer, self.tree[left])
                left += 1

            if right % 2 == 0:
                answer = self.compose(answer, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return answer


n, m = map(int, input().split())
values = list(map(int, input().split()))
tree = SegTree(values)
for _ in range(m):
    tp, a, b = map(int, input().split())
    if tp == 1:
        tree.update(a, b)
    else:
        print(*tree.query(a, b - 1))
