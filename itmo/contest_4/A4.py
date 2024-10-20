import sys
from heapq import heappush, heappop


def main():
    n = int(sys.stdin.readline())
    h = []
    for i in range(n):
        q = sys.stdin.readline().rstrip()
        if q == "GetMin":
            print(heappop(h))
        elif q == "GetMax":
            h.sort()
            print(h.pop())
        else:
            heappush(h, int(q.split("(")[1].split(")")[0]))


if __name__ == "__main__":
    main()
