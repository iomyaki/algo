import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    ropes = []
    max_len = -1
    for _ in range(n):
        rope = int(sys.stdin.readline())
        max_len = max(max_len, rope)
        ropes.append(rope)

    l, r = 0, 10 ** 7 + 1  # upper bound from the task plus one
    while r - l > 1:
        m = (l + r) // 2
        if sum(map(lambda x: x // m, ropes)) >= k:
            l = m
        else:
            r = m

    print(l)


if __name__ == "__main__":
    main()
