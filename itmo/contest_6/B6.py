import sys


class Solution:
    def __init__(self, n: int, W: float, goods: list[tuple[float, float]]):
        self.n = n
        self.W = W + 1e-8
        self.goods = goods
        self.ans = 0

    def go(self, i, sum_w, sum_cost):
        if i == self.n:
            if sum_w <= self.W:
                self.ans = max(self.ans, sum_cost)
            return
        self.go(i + 1, sum_w, sum_cost)
        self.go(i + 1, sum_w + self.goods[i][0], sum_cost + self.goods[i][1])

    def answer(self):
        print(f"{self.ans:.9f}")


def main():
    n, W = map(float, sys.stdin.readline().split())
    n = int(n)
    goods = []
    for _ in range(n):
        w, cost = map(float, sys.stdin.readline().split())
        goods.append((w, cost))

    solution = Solution(n, W, goods)
    solution.go(0, 0, 0)
    solution.answer()


if __name__ == "__main__":
    main()
