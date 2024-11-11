import sys
from math import floor


class Solution:
    def __init__(self):
        self.dp = {}

    def f(self, x):
        if x <= 2:
            if x not in self.dp:
                self.dp[x] = 1
            return self.dp[x]
        else:
            if x % 2 == 1:
                a, b = floor(6 * x / 7), floor(2 * x / 3)
            else:
                a, b = x - 1, x - 3

            if a not in self.dp:
                self.dp[a] = self.f(a)
            if b not in self.dp:
                self.dp[b] = self.f(b)
            return self.dp[a] + self.dp[b]


def main() -> None:
    print(Solution().f(int(sys.stdin.readline())) % 2 ** 32)


if __name__ == "__main__":
    main()
