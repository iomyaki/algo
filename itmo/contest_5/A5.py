import sys


def main():
    n = int(sys.stdin.readline())
    array = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        array.append((a, b, i + 1))

    array.sort(key=lambda x: (x[0], x[1], x[2]))
    for elem in array:
        print(elem[2], end=" ")


if __name__ == "__main__":
    main()
