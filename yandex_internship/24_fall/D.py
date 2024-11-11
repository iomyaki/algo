import sys
from copy import deepcopy


class Solution:
    def __init__(self, n: int, seq: str):
        self.n = n
        self.seq = seq
        self.mod = 10 ** 9 + 7
        self.cnt = 0
        self.closing = {")": "(", "]": "[", "}": "{"}
        self.debug = 0

    def go(self, i: int, par: str, prev_stack: list) -> None:
        #print(f"now: {i}, {par}, {prev_stack}")
        self.debug += 1
        if i == self.n:
            if len(prev_stack) == 0:
                self.cnt = (self.cnt + 1) % self.mod
            return

        stack = deepcopy(prev_stack)
        if par not in self.closing:
            stack.append(par)
        else:
            if len(stack) == 0:
                del stack
                return
            else:
                if stack[-1] != self.closing[par]:
                    del stack
                    return
                else:
                    stack.pop()

        if self.seq[i + 1] != "?":
            self.go(i + 1, self.seq[i + 1], stack)
        else:
            for p in "()[]{}":
                self.go(i + 1, p, stack)

        del stack

    def answer(self):
        print(self.cnt % self.mod)


def main() -> None:
    #sys.stdin.readline()
    #n = 8
    #seq = "?{?[(?])?)" + "_"
    #seq = "[]()" + "_"
    #seq = "]??(" + "_"
    #seq = "????????" + "_"
    seq = "??????_"
    n = len(seq) - 1

    solution = Solution(n, seq)
    stack = []
    if seq[0] != "?":
        solution.go(0, seq[0], stack)
    else:
        for p in "([{":
            solution.go(0, p, stack)

    solution.answer()
    #print(solution.debug)


if __name__ == "__main__":
    main()
