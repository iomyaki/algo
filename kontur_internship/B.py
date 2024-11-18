import sys


def main() -> None:
    n = int(sys.stdin.readline())
    expectation, reality = [], []
    for _ in range(n):
        expectation.append(tuple(map(int, sys.stdin.readline().split())))
    for _ in range(n):
        reality.append(tuple(map(int, sys.stdin.readline().split())))

    expectation.sort()
    reality.sort()

    dx, dy = reality[0][0] - expectation[0][0], reality[0][1] - expectation[0][1]
    print(dx, dy)


if __name__ == "__main__":
    main()
