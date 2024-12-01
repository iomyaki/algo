import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    events = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if a < b:
            events.append((a, 0))
            events.append((b, 2))
        else:
            events.append((b, 0))
            events.append((a, 2))
    dots = tuple(map(int, sys.stdin.readline().split()))

    for i in range(m):
        events.append((dots[i], 1, i))
    del dots

    events.sort(key=lambda x: (x[0], x[1]))

    coverage = [0 for _ in range(m)]
    cnt = 0
    for i in range(len(events)):
        if events[i][1] == 0:
            cnt += 1
        elif events[i][1] == 2:
            cnt -= 1
        else:
            coverage[events[i][2]] = cnt

    print(*coverage)


if __name__ == "__main__":
    main()
