import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    jewelry = []
    for i in range(n):
        v, w = map(int, sys.stdin.readline().split())
        jewelry.append((v, w, i + 1))
    jewelry.sort(key=lambda x: (-x[0], x[1]))
    for j in range(k):
        print(jewelry[j][2], end=" ")


if __name__ == "__main__":
    main()

# WA test 3