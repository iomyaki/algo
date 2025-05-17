import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    lines = [(-1, -1)]
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        lines.append((a, b))
    q = int(sys.stdin.readline().rstrip())
    for _ in range(q):
        t, d = map(int, sys.stdin.readline().split())
        start, interval = lines[t]
        normalized = d - start
        factor = normalized // interval
        if normalized % interval != 0:
            factor += 1

        print(start + factor * interval)


if __name__ == '__main__':
    main()
