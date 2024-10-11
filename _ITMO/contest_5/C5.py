import sys


def main():
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    array = []
    cur = 0
    for _ in range(n):
        cur = (cur * a + b) % 4294967296
        x = cur >> 8
        cur = (cur * a + b) % 4294967296
        y = cur >> 8
        array.append(((x << 8) ^ y) % 4294967296)
    print(array)
    print(sorted(array))


if __name__ == "__main__":
    main()
