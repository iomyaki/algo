import sys


def main() -> None:
    n = int(sys.stdin.readline())
    tanks = tuple(map(int, sys.stdin.readline().split()))
    for i in range(1, n):
        if tanks[i - 1] > tanks[i]:
            print(-1)
            break
    else:
        print(tanks[-1] - tanks[0])


if __name__ == "__main__":
    main()
