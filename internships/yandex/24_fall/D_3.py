import sys


class Solution:
    def __init__(self, s) -> None:
        self.s = s
        self.n = len(s)
        self.dp = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        self.opening = {"(", "[", "{"}
        self.closing = {")", "]", "}"}

    def go(self, start: int, finish: int) -> int:
        if self.dp[start][finish] == -1:
            if start >= finish:
                self.dp[start][finish] = 0
            elif start + 1 == finish:
                first, second = self.s[start], self.s[finish]
                if first == second == "?":
                    self.dp[start][finish] = 3
                elif first == "?" and second in self.closing:
                    self.dp[start][finish] = 1
                elif first in self.opening and second == "?":
                    self.dp[start][finish] = 1
                elif is_matching(first, second):
                    self.dp[start][finish] = 1
                else:
                    self.dp[start][finish] = 0
            else:
                ways = 0
                for i in range(start, finish - 1):
                    first = self.s[i]
                    for j in range(start + 1, finish):
                        second = self.s[j]

                        if first == second == "?":
                            mult = 3
                        elif first == "?" and second in self.closing:
                            mult = 1
                        elif first in self.opening and second == "?":
                            mult = 1
                        elif is_matching(first, second):
                            mult = 1
                        else:
                            mult = 0

                        ways += mult * self.go(start + 1, j - 1) * self.go(j + 1, finish)
                self.dp[start][finish] = ways

        return self.dp[start][finish]


def is_matching(opn: str, cls: str) -> bool:
    return opn == "(" and cls == ")" or opn == "[" and cls == "]" or opn == "{" and cls == "}"


def main() -> None:
    s = "?{?[(?])?)"
    n = len(s)
    solution = Solution(s)
    print(solution.go(0, n - 1))
    print(*solution.dp, sep="\n")

if __name__ == "__main__":
    main()

"""assert count_valid_sequences("?{?[(?])?)") == 3
assert count_valid_sequences("[]()") == 1
assert count_valid_sequences("]??(") == 0
assert count_valid_sequences("[]??()") == 3
assert count_valid_sequences("????") == 18
assert count_valid_sequences("?[?]??") == 6
assert count_valid_sequences("{}????()") == 18"""
