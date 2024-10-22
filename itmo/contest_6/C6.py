import sys


class Solution:
    def __init__(self, n):
        self.n = n
        self.partition = [0 for _ in range(40)]

    def go(self, pos, maximal, num):
        if num == 0:
            for m in range(pos):
                print(self.partition[m], end=" ")
            print()
            return

        for m in range(1, min(maximal, num) + 1):
            self.partition[pos] = m
            self.go(pos + 1, m, num - m)


def main():
    n = int(sys.stdin.readline())
    solution = Solution(n)
    solution.go(0, n, n)


if __name__ == "__main__":
    main()
