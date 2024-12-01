import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    dots = list(map(int, sys.stdin.readline().split()))
    events = []
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        events.append((a, 0, i))
        events.append((b + 1, 1, i))

    dots.sort()
    events.sort()

    coverage = [0 for _ in range(m)]
    cnt = 0
    i = 0
    for coord, typ, idx in events:
        while i < n and dots[i] < coord:
            cnt += 1
            i += 1

        if typ == 0:
            coverage[idx] -= cnt
        else:
            coverage[idx] += cnt

    print(*coverage)


if __name__ == "__main__":
    main()
