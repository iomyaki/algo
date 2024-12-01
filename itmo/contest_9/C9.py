import sys


def main() -> None:
    n = int(sys.stdin.readline())
    segments = []
    for _ in range(n):
        segments.append(tuple(map(int, sys.stdin.readline().split())))

    segments.sort(key=lambda x: x[1])
    points = []
    current = -1
    for segment in segments:
        start, end = segment
        if current < start:
            current = end
            points.append(current)

    print(len(points))
    print(*points)


if __name__ == "__main__":
    main()
